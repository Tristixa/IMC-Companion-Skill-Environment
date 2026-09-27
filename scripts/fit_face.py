"""Fit cropped artwork to one spec face; run mask_faces.py afterwards."""
import argparse
import json
from pathlib import Path

import numpy as np
from PIL import Image


def resample_nodes(image, size, nodes):
    """Original pixel-centre bilinear horizontal registration; linear vertical fit."""
    w, h = size
    nodes = sorted(nodes)
    if any(b[0] <= a[0] or b[1] <= a[1] for a, b in zip(nodes, nodes[1:])):
        raise ValueError('Door bounds must be strictly inside source and target widths')
    sx = np.interp(np.arange(w) + .5, [n[0] for n in nodes], [n[1] for n in nodes]) - .5
    sy = (np.arange(h) + .5) * image.height / h - .5
    a = np.array(image).astype(float)
    sx, sy = sx.clip(0, image.width - 1), sy.clip(0, image.height - 1)
    x0, y0 = np.floor(sx).astype(int), np.floor(sy).astype(int)
    x1, y1 = np.minimum(x0 + 1, image.width - 1), np.minimum(y0 + 1, image.height - 1)
    fx, fy = (sx - x0)[None, :, None], (sy - y0)[:, None, None]
    top = a[y0[:, None], x0[None, :]] * (1 - fx) + a[y0[:, None], x1[None, :]] * fx
    bottom = a[y1[:, None], x0[None, :]] * (1 - fx) + a[y1[:, None], x1[None, :]] * fx
    return Image.fromarray(np.rint(top * (1 - fy) + bottom * fy).clip(0, 255).astype('uint8'))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--spec', required=True, type=Path, help='Facade spec JSON.')
    parser.add_argument('--face', required=True, help='Exact face.file selector, e.g. tavern/n.png.')
    parser.add_argument('--source', required=True, type=Path, help='Already cropped source image; all landmarks are relative to this crop.')
    parser.add_argument('--output', required=True, type=Path, help='Destination PNG (source must be a different path).')
    parser.add_argument('--door-bounds', nargs=2, type=float, metavar=('LEFT', 'RIGHT'), help='Source door-leaf horizontal edge coordinates; register to spec door centre and width. Does not infer door height.')
    parser.add_argument('--storey-repeat', action='store_true', help='Assemble explicit vertical source bands; repeat an upper-storey band in --source-spans to add storeys.')
    parser.add_argument('--source-spans', nargs='+', help='With --storey-repeat: TOP:BOTTOM crop-relative pixel spans, in output order; spans may repeat.')
    parser.add_argument('--target-heights-m', nargs='+', type=float, help='With --storey-repeat: descending band boundaries in metres above ground, from total face height to 0; one more boundary than spans.')
    args = parser.parse_args()
    try:
        spec = json.loads(args.spec.read_text(encoding='utf-8-sig'))
        matches = [f for f in spec['faces'] if f['file'] == args.face]
        if len(matches) != 1:
            raise ValueError(f'Expected one spec face matching {args.face!r}')
        face = matches[0]
        w, h = face['px']
        if args.source.resolve() == args.output.resolve():
            raise ValueError('Output must differ from source')
        with Image.open(args.source) as source:
            rgb = source.convert('RGB')
        nodes = [(0, 0), (w, rgb.width)]
        if args.door_bounds:
            if not face.get('door'):
                raise ValueError('Selected face has no door specification')
            door = face['door']
            left, right = args.door_bounds
            if not np.isfinite([left, right]).all() or not 0 < left < right < rgb.width:
                raise ValueError('Source door bounds must satisfy 0 < LEFT < RIGHT < source width')
            scale = w / face['width_m']
            nodes += [((door['centre_x_m'] - door['width_m'] / 2) * scale, left),
                      ((door['centre_x_m'] + door['width_m'] / 2) * scale, right)]
        if args.storey_repeat:
            if not args.source_spans or not args.target_heights_m:
                raise ValueError('--storey-repeat requires --source-spans and --target-heights-m')
            spans = [tuple(map(int, s.split(':'))) for s in args.source_spans]
            heights = args.target_heights_m
            total = face['wall_height_m'] + face['gable_height_m']
            if len(heights) != len(spans) + 1 or not np.isfinite(heights).all() or not np.isclose(heights[0], total) or heights[-1] != 0:
                raise ValueError('Target boundaries must cover total face height to 0, with one more boundary than spans')
            if any(a <= b for a, b in zip(heights, heights[1:])):
                raise ValueError('Target heights must strictly descend')
            boundaries = [round(h * (1 - y / total)) for y in heights]
            out = Image.new('RGB', (w, h))
            for span, top, bottom in zip(spans, boundaries, boundaries[1:]):
                if len(span) != 2 or not 0 <= span[0] < span[1] <= rgb.height or bottom <= top:
                    raise ValueError('Invalid source span or target band rounds to zero pixels')
                strip = rgb.crop((0, span[0], rgb.width, span[1]))
                fitted = resample_nodes(strip, (w, bottom - top), nodes) if args.door_bounds else strip.resize((w, bottom - top), Image.Resampling.LANCZOS)
                out.paste(fitted, (0, top))
        else:
            if args.source_spans or args.target_heights_m:
                raise ValueError('Band options require --storey-repeat')
            out = resample_nodes(rgb, (w, h), nodes) if args.door_bounds else rgb.resize((w, h), Image.Resampling.LANCZOS)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        out.convert('RGBA').save(args.output)
        print(f'PASS: fitted {args.face} to {w}x{h}: {args.output}')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(1, f'FAIL: {exc}\n')


if __name__ == '__main__':
    main()
