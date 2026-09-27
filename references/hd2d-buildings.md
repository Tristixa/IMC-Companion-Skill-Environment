# HD-2D buildings: painted facades for 3D volumes

The user approved this workflow on 2026-09-27, after reviewing the Eurydica explorable-town proof (`D:/Storyboards/Isekai Mercenary Company/HD-2D Proof`, published proof https://claude.ai/artifact/N7VYKQzNWXJWwfDhYrUtRb). The approved result is `Environment Assets/Eurydica/Approved Facades v1/` in the storyboard project. Use this reference whenever an HD-2D (Octopath-like) town, district or building needs painted buildings. It replaces a baked town backdrop or modular top-down sheets for that job.

## Why this path

- **The HD-2D town is a real 3D scene:**
  - buildings are box volumes with curved roof geometry;
  - pixel sprites stand in the scene;
  - the engine lights everything (sun, shadows, lamp light, water).
- **What the art supplies:** painted surfaces for those volumes. Each face of a building is one straight-on **orthographic elevation** texture, UV-mapped flat onto that face. The runtime camera and perspective come from the engine, never from the paint.
- **The approved camera:** straight north, perspective, about 40° down (the owner chose the straight heading on 2026-09-27):
  - offset (0, 18.4, 21.8) m from the player, FOV 30°, following without rotation;
  - at that distance, a 1.68 m character sprite is about 93 px on a 1280×800 view, its native pixel size;
  - buildings between the camera and the player (or nearby people) fade out, Octopath-style cutaway.

This camera applies to the HD-2D town only. The top-down front-facing camera in [playable-camera.md](playable-camera.md) still governs painted 2D playable environments. The skill's scene-camera lock therefore applies here only to the **props sheet**, which is painted for the gameplay camera. Facades are elevations.

## Roles

- **Claude (proof author):**
  - owns the geometry and writes the face spec from it;
  - integrates the approved faces into the 3D scene;
  - reviews the result in the proof.
- **Codex (with this skill):** paints and processes the faces to the spec, runs the checks and records the run.
- **The user:** approves in the proof. Candidates stay outside the project until then.

## 1. Spec: one contract per pass

Write `facades-spec.json` with `scripts/facade_spec.mjs` from a small buildings file (the script's header documents the input). The approved Eurydica spec is the worked example. Fixed values:

- **Density:** 64 px per metre on every face, tile and prop.
- **Face naming:** each building gets `n`, `e`, `s`, `w` faces, painted as seen from outside, standing in front of that face.
- **Wall faces:** width × wall height `H`.
- **Gable faces:** width W × (H + G), where G = min(5, 0.55 × W).
  - Opaque below H.
  - Above H, the opaque top edge follows the concave sweep `y = H + G·(1 − u)^1.4`, with `u = |x − W/2| / (W/2)`.
  - Above the curve is alpha 0.
  - The 3D roof uses the same curve, so paint and roof meet.
- **Wall height:** about 3.1 m per storey (tavern 9.3 m for 3 storeys, shops and houses 6.2 m, a small house 4.4 m). A broad low working building may use about 4.8 m.
- **Doors:** centred on the door face, 1.4 × 2.3 m by default; wide work or stable doors 3.0 m wide (2.8 m high for the repair shop); sheds 1.2 m wide. The spec records every door. Collision and NPC placement depend on it.
- **Arches:** a walk-through gate is a transparent opening, straight to 3.0 m then a semicircle (Eurydica's gate is 4.6 m wide with its apex at 5.3 m).
- **Roof tiles:** 512×512, covering 8×8 m, seamless in both axes, broad courses running parallel to the ridge.
- **Wall tiles:** seamless horizontally (city wall 256×218 = 4 × 3.4 m).
- **Attachments:** awnings, banners and signs as straight-on cutouts at exact metre sizes.
- **Props:** painted at the gameplay camera and extracted by chroma, with `props/anchors.json` giving each prop's size, its bottom-centre ground-contact anchor and height_m.
- **Generic houses:** a few per district (Eurydica has `house_violet` and `house_green`). The integration rotates their faces with the building's door face and stretches them to other footprints. Keep them plainer than named buildings.

## 2. Painting (Codex)

- **Design identity:** the approved location concepts; name the source concept for every building. Concepts are oblique, so design the unseen faces plainly and consistently with the visible ones, and record which faces were invented.
- **Finish:**
  - the approved simplified game appearance ([game-appearance.md](game-appearance.md));
  - compatible with the clean painted Mosswood set, since those trees stand in the same streets;
  - no pixel grid, no palette quantization, `fit.pixel_unfake: false`.
- **Lighting:** near-albedo paint with soft ambient occlusion only (under eaves, in window and door recesses, at the base). No directional sun, cast shadows or light-implying highlights. Windows are dark and unlit, and no fixture glows. Treat all faces alike: the engine lights them.
- **One sheet per building:**
  - Generate each building's four elevations together on one sheet (2×2), so corners, floor bands and materials match.
  - Attach, with explicit roles: the building's layout guide (from `scripts/`, drawn from the spec), its concept (identity), a Mosswood clean object (finish), and the accepted anchor sheet ("finish and detail level of this set").
  - The first building of a pass becomes the anchor once it's right. The built-in tool takes at most five references.
- **No text on production assets:** no lettering, labels, people or props baked into faces (pictogram signs only). Labels belong on the separate review sheet.

## 3. Processing (Codex, scripts in `scripts/`)

- **`fit_face.py`:** crops a face from its source sheet and resamples it to the spec's exact `px`.
  - Optional door registration moves the painted door onto the spec door (piecewise horizontal resample).
  - Optional storey repeat covers a sheet with fewer painted storeys than the spec, repeating an existing painted storey rather than repainting.
- **`mask_faces.py`:** applies the analytic gable and arch silhouettes with binary alpha, and scrubs RGB under alpha 0. It never repaints.
- **Records:** keep the untouched sources, exact prompts and reference provenance, source crops and door registration in the run.
- **`check_facades.py --spec --run`:** must pass before review. It checks:
  - exact sizes;
  - binary alpha and silhouette correctness;
  - opaque wall rectangles;
  - tile seams;
  - attachment sizes;
  - prop anchors, margins and chroma residue.

  The Eurydica pass scored 422/422.
- **Review sheet:** a labeled overview of all faces, tiles in repeat, attachments and props, plus paper assemblies (faces side by side at one scale and ground line) for the two most important buildings.

## 4. Integration (proof author)

The reference implementation is `HD-2D Proof/src/town.html` (the `building()`, `roofMesh()`, `prop()` and `cutaway()` code) with `tools/build-town.mjs`, which inlines the approved folder as webp.

- **Walls:** a plaster-coloured core box (solid, casts shadows) plus one alpha-tested plane per face, 2 cm proud of the box, with a matching depth material so gable paint casts correct shadows.
- **Roofs:** two parametric curved slopes following the same profile, 0.1 m above the wall top.
  - Overhang is 0.45 m all round, with eaves flaring up about 0.2 m.
  - The roof tile is UV-mapped in 8 m units along the ridge and down the slope.
  - A ridge cap runs along the top.
- **Generic reuse:** the facade id's door face rotates onto the building's door face; the ridge swaps axis on a 90° turn, so gable and wall faces keep their types. Faces stretch to the footprint and G is recomputed from the actual span.
- **Gatehouse:** two solid piers, a lintel and a barrel vault; the passage stays walkable.
- **Awnings:** planes hinged at the wall top (about 3.1 m), sloping out and down about 60°.
- **Props:** billboards at 1/64 m per px, anchored at their ground contact and tilted like the character sprites (60% of the camera pitch). Small solid props get a small collision block.
- **Cutaway:** every building's meshes fade together to 22% opacity while a ray from the camera to the Commander, or to a person within 9 m, passes through them.
- **Fallback:** a face with no painting yet gets a plain drawn face with the same silhouette, so geometry work never waits on art.

## 5. Approval and storage

- **Candidates:** run folders under `D:/Codex/IMC/runs/`, marked candidate, never in the project.
- **Review:** in the running proof at gameplay size, not only on the review sheet.
- **After approval:** copy the run into `Environment Assets/<Location>/Approved Facades vN/` with the spec, records, review sheet and an approval README (date, proof link, what was approved). The build reads from that folder.
- **Repairs:** fix a malformed face in its own file and re-run the mask and checks. Don't regenerate an approved building to fix one face.
