---
name: imc-environment-art-direction
description: Create, revise, brief or review IMC (Isekai Mercenary Company) environments, hunting and battle backgrounds, playable rooms such as the Adventurer Office, scenery and maps with consistent crisp Japanese illustrated fantasy art direction. Apply when the project or conversation establishes IMC. Character portraits, sprites, creature designs and character animations belong to imc-art-direction.
---

# IMC Environment Art Direction

This companion supplies IMC's environment creative and integration requirements. The installed `sprite-gen` skill supplies image production workflows where needed; keep upstream tooling and provider defaults separate from this art brief. Use `$imc-art-direction` for character and creature deliverables in a mixed request.

## Establish the task

Identify the location, requested output and whether the request concerns a brief/review, concept candidate, production background or game integration. Carry forward the user's choices. Do not generate images during documentation-only work. A candidate request does not itself authorize replacing live textures or changing runtime geometry.

Read [references/project-contract.md](references/project-contract.md) for current project sources, asset bindings and the location brief. Resolve project paths against the actual IMC checkout, including worktrees; the original local checkout is `D:/Godot Projects/IMC-godot`. Read current sources rather than treating historical production prompts as current approval.

Choose the relevant environment use:

- **Hunting and battle backgrounds:** Establish the region/biome, encounter mood, intended camera, party/enemy staging, shared ground plane and HUD space from the actual scene. Design clear combat space and readable silhouettes at gameplay size. Do not assume the background is traversable or that a battle reference's camera applies to every hunting scene.
- **Playable environments and rooms:** For the Adventurer Office and other HQ departments or exploration locations, design around the location's activity, furnishing, entrances, connections, movement space, interaction points and foreground occlusion. Preserve department ownership. Record geometry changes needed by a redesigned layout.
- **HQ and region maps:** Read the current map documents and UI placement. Preserve meaningful connections, navigation landmarks and clickable areas when required by the task. Keep labels and controls in the runtime UI; a map request does not imply new locations or gameplay rules.

Proceed with reasonable recorded choices when context resolves the brief. Ask only when a missing reference, conflicting design source or unspecified purpose would materially change the result.

## Rendering and references

Before visual briefing, production or review, read [references/rendering-contract.md](references/rendering-contract.md) and inspect its retained PawPop 2 image. Use crisp Japanese 2D-HD/chibi JRPG environments with clean anime contours, simplified material planes, controlled cel-shading, medium-detail ground surfaces and graphic foliage. Keep painterly texture minimal and atmospheric softness in distant layers. This supersedes earlier broadly painterly environment guidance.

Apply that rendering approach to the actual location, camera, palette and time of day. PawPop 2's shrine architecture, blossoms, night lighting and pasted sprites are examples, not universal content requirements. Avoid photorealism, gritty Western game-art styling, glossy 3D rendering and pixel-grid styling unless explicitly requested.

For uploaded references, record which image supplies rendering, location identity, composition, layout, lighting or mood. Preserve requested design locks without copying unrelated reference content. Inspect approved images directly; an existing file or historical audit alone does not establish current visual approval.

## Composition and integration

For a new or redesigned environment, develop an original composition appropriate to its function. Existing room art supplies context and is not a mandatory image-generation reference. Lock existing image coordinates only for a layout-preserving replacement. Read runtime geometry to distinguish functional constraints from an old crop or furnishing arrangement.

Match intended aspect ratio, camera perspective and actual display scale. Keep a usable actor ground plane, natural staging and space for runtime UI. Keep characters and their contact shadows separate from empty backgrounds; static scenery shadows may remain. Review representative approved sprites at gameplay size without changing their identity or proportions. Do not bake extra people, monsters, labels, controls, unrequested text, pseudo-writing, signatures or watermarks into the environment. An explicitly requested inscription is its own intentional element.

Follow the rendering contract for foreground occlusion, foot contact and separate runtime shadows. Export layers only when requested and supported; do not assume unimplemented parallax, movement or occlusion systems. For a redesign, record required walkable-area, entrance, interaction, actor-position and occlusion adjustments before an authorized integration.

## Production and delivery

For image production, read the installed `sprite-gen` skill and only the route documents needed for the operation; on this installation use its absolute `run-sprite-gen.cmd` launcher. Follow active image generation/editing tool instructions and preserve the user's provider choices. Keep illustrated rendering free of palette quantization and pixel-unfake (`fit.pixel_unfake: false`) unless the user requests pixel art. Character-specific frame counts, blinking and Officer animation rules do not define environment deliverables; scope any requested ambient animation separately.

Keep runs and candidate revisions separate from live game assets. Save the location brief and reference provenance with the run, retain source references during authorized production, and mark candidate versus approved output explicitly. Export the selected result through the applicable pipeline. State runtime compatibility only after checking the actual bindings.

Review rendering against the retained reference, useful ground space, camera/scale, sprite separation across expected movement, UI clearance, lighting, floor contact and foreground occlusion. Check both native resolution and actual gameplay size. Diagnose rendering/import issues before regenerating approved artwork. A technically valid file or prompt style label does not establish visual quality.

Deliver the requested candidate/export with relevant paths, checks actually performed and any remaining integration work. For documentation/skill edits, list authored files and their purpose. Do not silently update project documents, production artwork or game code while maintaining this companion.
