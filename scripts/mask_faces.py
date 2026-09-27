"""Apply the fixed 1.4-power gable/semicircular-arch facade contract."""
import argparse
import json
from pathlib import Path

import numpy as np
from PIL import Image


def silhouette(face):
    w, h = face['px']
    W, H, G = (face[k] for k in ('width_m', 'wall_height_m', 'gable_height_m'))
    x = (np.arange(w) + .5) * W / w
    y = (h - np.arange(h) - .5) * (H + G) / h
    mask = y[:, None] <= (H + G * (1 - np.abs(x - W / 2) / (W / 2)) ** 1.4)[None, :]
    if face.get('arch'):
        arc = face['arch']
        dx, radius = x - arc['centre_x_m'], arc['half_width_m']
        top = arc['straight_to_m'] + np.sqrt(np.maximum(0, radius * radius - dx * dx))
        mask &= ~((np.abs(dx)[None, :] <= radius) & (y[:, None] <= top[None, :]))
    return mask


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--spec', required=True, type=Path, help='Facade spec JSON; uses its fixed y=H+G*(1-u)^1.4 profile.')
    parser.add_argument('--faces', required=True, type=Path, help='Root containing each face.file; PNGs are masked in place, without resampling.')
    args = parser.parse_args()
    try:
        faces = json.loads(args.spec.read_text(encoding='utf-8-sig'))['faces']
        # Preflight the whole batch before modifying any image.
        for face in faces:
            path = args.faces / face['file']
            if not path.is_file():
                raise ValueError(f'Missing face: {path}')
            with Image.open(path) as im:
                if list(im.size) != face['px']:
                    raise ValueError(f'{path}: expected {face["px"]}, got {list(im.size)}')
        for face in faces:
            path = args.faces / face['file']
            with Image.open(path) as im:
                pixels = np.array(im.convert('RGBA'))
            mask = silhouette(face)
            pixels[:, :, 3] = mask.astype('uint8') * 255
            pixels[~mask, :3] = 0
            Image.fromarray(pixels).save(path)
        print(f'PASS: masked {len(faces)} faces; binary alpha and transparent RGB scrubbed.')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(1, f'FAIL: {exc}\n')


if __name__ == '__main__':
    main()
