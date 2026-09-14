# IMC environment sources and production briefs

All project paths below are relative to the active IMC repository root. Check newer active versions and repository instructions before editing. Current user decisions take precedence over historical prompts; project evidence does not authorize expanding the task.

## Sources to read

| Work | Project sources |
|---|---|
| All environment rendering | Companion [rendering contract](rendering-contract.md); inspect [PawPop 2](media/pawpop-2-background-style.png) |
| Rooms, hunting and battle backgrounds | `docs/visual/environment-production.md`; `assets/visual/environments.json`; relevant location/floor plan and HUD; relevant sections of `IMC_Visual_Design_Document_v1.1.md` |
| Gameplay purpose and staging | Relevant sections of `IMC_Reworked_GDD_HUD_Aligned_v1.1.md`; current scene data and runtime usage |
| HQ and region maps | `docs/visual/map-art-production.md`; current map assets, navigation bindings and UI placement |
| Sprite scale and compositing | `docs/visual/gameplay-sprite-style.md`; approved gameplay images and actual runtime display sizes; `presentation/animated_actor.gd` and relevant actor manifests |
| Runtime integration | `presentation/art.gd`; `presentation/hq.gd` and `presentation/app.gd` where relevant; trace the requested location's environment ID to its actual texture, staging, walkable areas, entrances and foreground occlusion |

The user's PawPop 2 direction supersedes broadly painterly prompts in older environment production documents. Inspect the retained image before visual work. Existing artwork is context, not a required design reference for an original composition; lock old coordinates only when retaining the layout is requested. Do not infer that changing a texture implements new navigation, parallax or occlusion behavior.

For playable rooms, retain the department's purpose and ownership. The Adventurer Office is Elsie's department; changing its environment does not redesign her character. Verify current room and actor bindings from project sources rather than relying on this example as a permanent implementation snapshot.

## Persistent location brief

Store the brief with the run or in an explicitly requested project documentation location. Record relevant fields:

- Stable location/environment ID, name, purpose and current asset revision.
- Output type: hunting/battle backdrop, playable environment, map or requested layer/animation.
- Reference paths/revisions, their roles, and candidate/selection/approval status. Retain source copies during authorized production; include hashes when publishing final provenance.
- Location features and gameplay constraints to preserve; requested changes and unresolved details.
- Rendering, materials, biome or department, palette, light sources, time of day, camera and intended display scale/aspect ratio.
- Actor and enemy staging as applicable, movement/interaction areas, entrances/connections, UI clearance and foreground occlusion.
- Whether this is a layout-preserving replacement or a redesign, with required runtime changes for the latter.
- Requested deliverables, selected export, visual/compositing review and integration status.

Keep stable game IDs separate from artwork revisions. A missing source or unverified binding must remain recorded as unresolved; do not replace it with invented geometry or silently approve a candidate.
