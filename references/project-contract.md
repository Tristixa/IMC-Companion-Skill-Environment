# IMC environment sources and production briefs

All project paths below are relative to the active IMC repository root. Check newer active versions and repository instructions before editing. Current user decisions take precedence over historical prompts; project evidence does not authorize expanding the task.

## Sources to read

| Work | Project sources |
|---|---|
| All environment rendering | Default [approved game appearance](game-appearance.md) and its retained images; companion [rendering contract](rendering-contract.md). Only load alternative style families when explicitly requested. Keep camera and location references separately labeled. |
| Playable interior/exterior camera | [Playable-camera reference guide](playable-camera.md); substantial downward ground view with readable front faces, independent of rendering style and fixed/scrolling coverage |
| Rooms, hunting and battle backgrounds | `docs/visual/environment-production.md`; `assets/visual/environments.json`; relevant location/floor plan and HUD; relevant sections of `IMC_Visual_Design_Document_v1.1.md` |
| Gameplay purpose and staging | Relevant sections of `IMC_Reworked_GDD_HUD_Aligned_v1.1.md`; current scene data and runtime usage |
| HQ and region maps | `docs/visual/map-art-production.md`; current map assets, navigation bindings and UI placement |
| Sprite scale and compositing | `docs/visual/gameplay-sprite-style.md`; approved gameplay images and actual runtime display sizes; `presentation/animated_actor.gd` and relevant actor manifests |
| Runtime integration | `presentation/art.gd`; `presentation/hq.gd`, `presentation/exploration_view.gd`, `presentation/illustrated_terrain.gd`, `presentation/daylight.gd` and `presentation/app.gd` where relevant; trace the requested location's environment ID to its actual texture, camera, staging, walkable areas, entrances, foreground occlusion, runtime lights and water implementation |

On 2026-09-20 the user approved Eurydica v0.3 and asked to preserve its simple game appearance for every new location. This supersedes the 2026-09-18 per-run illustration-style choice. Use the [approved reference pair](game-appearance.md) by default; the old portrait/hall examples, Unicorn Overlord and PawPop 2 remain explicit alternatives only. Transfer broad surfaces, curved forms and restrained detail, while giving each new place its own layout, materials and colors. Existing artwork supplies only its assigned reference role; lock coordinates only when retaining a layout is requested. Do not infer that a generated image or changed texture implements runtime geometry, navigation, parallax or occlusion.

Current user-specified folders: concepts and approval records belong in `D:/Storyboards/Isekai Mercenary Company`; the game is `D:/Godot Projects/imc-playground`. Historical paths and binding examples below must be verified in the actual game project before implementation. Keep concept work in the storyboard until final and integration is requested.

The 2026-09-17 [open-space and modular asset direction](rendering-contract.md#open-space-and-modular-environment-assets) supersedes older dense or fully baked playable-environment briefs: use approximately 80% open usable ground, wide routes and a sparse base plus separate object sheets. The 2026-09-18 direction adds visible ownership and accumulated use without filling that open space, along with water-free bases and unlit light fixtures so Godot retains control of water and lighting effects. Preserve editable sources even if the current runtime consumes a flattened texture. Maintaining this skill does not authorize retrofitting existing environments.

For playable rooms, retain the department's purpose and ownership. The Adventurer Office is Elsie's department; changing its environment does not redesign her character. Verify current room and actor bindings from project sources rather than relying on this example as a permanent implementation snapshot.

## Persistent location brief

Store the brief with the run or in an explicitly requested project documentation location. Record relevant fields:

- Stable location/environment ID, name, purpose and current asset revision.
- Output type: playable interior, playable exterior, expedition backdrop, map or requested layer/animation. `Playable environment` is the parent term for interiors and exteriors; an expedition scene where the player actually traverses the ground is a playable exterior rather than a backdrop.
- Reference paths/revisions, their roles, and candidate/selection/approval status. Retain source copies during authorized production; include hashes when publishing final provenance.
- Location features and gameplay constraints to preserve; requested changes and unresolved details.
- Rendering choice and representative images actually passed to generation, separate camera reference, materials, biome or department, dominant/secondary/accent palette, intended runtime light sources and time of day. Record coherent fantasy design traits without imposing a historical era, plus visible past/repair, current ownership and daily-use evidence for inhabited locations.
- The user's selected camera label, with top-down front-facing offered as the default before generation; record projection, elevation, horizontal viewing angle, front/facing axis, horizon or vanishing behavior, ground-plane angle, intended display scale/aspect ratio and the selected base revision used as the camera reference for modular assets.
- For playable environments, the user's explicit camera-movement answer. Record fixed single-screen or scrolling large area, verified runtime viewport, world extent, closest camera view, provider output dimensions, final production-master dimensions and target source pixel density. Default fixed production master: 1920×1080. Current city-scale scrolling minimum: 3072×2048, increased proportionally for a larger area or closer view.
- Actor and enemy staging as applicable, movement/interaction areas, entrances/connections, UI clearance and foreground occlusion.
- For playable scenes, the reserved open ground and route widths, limited landscape features, separate object inventory and a review of the approximate 80/20 balance after composition.
- Base, object-sheet and extracted-object paths; object scale, source pixel density, ground anchors, placements, stacking/occlusion and separately editable shadows. Record any flattened runtime export alongside its editable sources.
- Runtime-effect separation: unlit light fixtures; Godot-owned emissions, light pools, bloom, godrays and volumetric effects; water-free base terrain; and any runtime water mask or separate illustrated water layer with its placement and occlusion information.
- Whether this is a layout-preserving replacement or a redesign, with required runtime changes for the latter.
- Requested deliverables, selected export, visual/compositing review and integration status.

Keep stable game IDs separate from artwork revisions. A missing source or unverified binding must remain recorded as unresolved; do not replace it with invented geometry or silently approve a candidate.
