# HD-2D building scripts

See `../references/hd2d-buildings.md` for the workflow. Python scripts need Pillow and numpy (the sprite-gen environment has both).

## Spec

`node facade_spec.mjs buildings.json facades-spec.json` writes the painting contract (the input format is documented in the script header).


Requires Python, Pillow and numpy. Paths in the spec are relative to the asset root.

Mask already fitted faces in place (all spec faces must exist at their exact size):
```sh
python mask_faces.py --spec facades-spec.json --faces output
```

Fit a cropped source and optionally register its door leaf horizontally:
```sh
python fit_face.py --spec facades-spec.json --face provisions/e.png --source cropped.png --output output/provisions/e.png --door-bounds 80 168
```

Check the complete run without writing to it:
```sh
python check_facades.py --spec facades-spec.json --run output
```

Run each script with `--help` for options. Fit produces opaque RGB artwork in RGBA format; input should be cropped, edge-extended paint with any chroma already removed. Apply masking afterwards. Fit does not automatically identify storeys, paint missing artwork, or register door height.

For storey assembly add `--storey-repeat --source-spans 0:243 243:420 243:420 420:597 597:662 --target-heights-m 14.25 9.3 6.2 3.1 0.9 0` to a fit invocation for the original tavern/n crop. Coordinates are crop-relative, bottom-exclusive; repeat any band as needed. Explicit target heights determine the storey count because the existing spec has no storey-count field. Bands use Lanczos, or the original bilinear mapping when combined with door registration.

The supported gable profile is the spec's fixed exponent 1.4; free-form prose is not evaluated. Arch fields define a semicircle above straight sides. Checks compare every silhouette pixel (including every edge) plus a 7px grid. Faces require binary alpha and scrubbed transparent RGB; antialiased attachments and props remain valid. Tiles allow opposite-edge differences up to 2/255. Props follow `props_sheet.items`, `props/<name>.png` and `props/anchors.json`; margins require at least one fully transparent outer row/column. Optional door-registration metadata verifies recorded transforms, not painted door recognition. Scene-specific review images, identical gatehouse artwork and art approval are outside this reusable geometric check.

`python self_test.py --spec facades-spec.json --run approved-run` runs the checker, tests the three approved sample faces on temporary copies beneath this directory, exercises fitting and failure cases, and confirms the approved run's file hashes did not change.
