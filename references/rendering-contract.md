# IMC environment rendering and compositing

Current rendering default: the user-approved simplified IMC game appearance, established 2026-09-20. It supersedes the earlier per-run style-selection requirement. Camera, open-space, modular asset and runtime-effect rules remain applicable to their respective deliverables. These requirements do not authorize editing production artwork or game code during skill maintenance.

## Reference roles

- [Approved game appearance and retained references](game-appearance.md): default for IMC locations. The approved Eurydica v0.3 image governs simplified rendering; the retained actual game screenshot governs environment complexity. Inspect and attach both. Its dialogue portrait and UI are excluded from the environment style.
- The three illustration families below are retained alternatives only when the user explicitly requests them. They are not default references and must not compete with the approved game appearance in ordinary generation calls.
- [3D-anime JRPG reference](media/3d-anime-jrpg-reference.jpg) and the [full 3D-to-2D example set](3d-to-2d.md): the **3D-anime-rendered 2D JRPG** option. Study modeled volumes, broad shading, material contrast and warm/cool color relationships across the set, rather than reducing the style to one timber-hall portrait. These are rendering references, not playable-camera references.
- [Unicorn Overlord battle scene](media/uo-battle-composition.jpg): the **Unicorn Overlord background style** option. Use its hand-painted storybook surface treatment, softened natural edges, grouped organic shapes, restrained detail, muted value transitions and atmospheric depth without copying its characters, ruins, side-on battle camera or outdoor subject matter.
- [PawPop 2](media/pawpop-2-background-style.png): the **PawPop 2 background style** option. Use its crisp illustrated shapes, clear anime color grouping, simplified materials, readable ground, strong silhouette separation and controlled decorative detail without copying its shrine, blossoms, night palette, characters, water or exact camera.

These images define environment rendering and compositing context. Approved character identities and gameplay proportions remain under the character skill and current IMC project references.

## Default and explicit alternatives

Use [simplified IMC game appearance](game-appearance.md) without asking the user to choose again. The user's 2026-09-20 request makes it the persistent default for new places. Keep attractive modeled curves, broad plain material areas, restrained shadows and grouped foliage at the complexity of the actual game world. Do not call the old portrait-based 3D-to-2D illustration option by default: its application to Eurydica produced rejected, overly detailed images. Explicit requests for another style override this default for that task. For an expressly requested style comparison, generate candidates independently from a shared location brief and the selected rendering references; keep camera, furnishing method and approximate density comparable.

### 3D-anime-rendered 2D JRPG

Create a drawn 2D game environment that preserves the appealing modeled volumes, material response and color organization of the retained 3D-anime-to-2D examples. Combine clear shadow boundaries with gentle shading across broad forms; use selective edge accents and warm/cool relationships to distinguish wood, stone, metal, plaster and cloth. Preserve coherent thickness, support and attachment. Clean rendering describes how well the image is resolved, not whether every object is new or pristine. Follow [3d-to-2d.md](3d-to-2d.md) for the full example analysis and transfer it to the separately selected playable camera. Avoid reducing this mode to uniform brown surfaces, identical object outlines, flat modular tokens or an evenly shaded room shell.

### Unicorn Overlord background style

Create a hand-painted 2D fantasy JRPG environment with storybook softness and convincing spatial depth. Use broad painterly color masses, gently softened edges, restrained linework, natural material variation, atmospheric layering and selective detail at important forms. Keep playable ground and interactable silhouettes readable. Preserve controlled imperfection and lived-in wear without turning the scene muddy, noisy, photorealistic or densely distressed.

### PawPop 2 background style

Create a crisp, polished 2D anime game environment with clean graphic silhouettes, simplified but distinct materials, confident color grouping, controlled cel-like shading and sharp readable gameplay ground. Use decorative accents selectively around boundaries and focal points. Preserve natural depth and construction without raw 3D rendering, plastic gloss, uniform outlines, dense texture or copying the reference's night shrine subject matter.

### Shared IMC construction rules

- **Construction, contours and depth:** Show believable planes, thickness, support, attachment and ground contact. Let the selected rendering option control edge treatment: subdued drawn edges, softer painterly edges or crisp graphic shapes. Do not force one uniform outline treatment across styles or objects. Reduce fine detail with distance while keeping playable ground and object footprints readable; short room distances do not need cinematic haze.
- **Materials and shading:** Organize shading into broad value groups, expressed through the selected style. The restriction on micro-gradients does not prohibit gentle shading across large forms. Sparse deliberate highlights may distinguish metal or glazed ceramics; avoid tiny reflected lights scattered over everything. Wood reads through construction and restrained grain, stone through planes and limited joints, cloth through a few broad folds. Avoid uniform PBR gloss, blanket scratches, tiny cracks, speckles and exhaustive texture. Keep contact shading at credible joins without heavy dark rims around every object.
- **Foliage:** Build leaves and flowers into graphic clusters with a readable outer silhouette and grouped light/shadow colors. A few distinct leaves or petals can accent the cluster; every leaf need not compete for attention. The reference's pink blossoms are optional subject matter, not IMC's default vegetation.
- **Composition:** Carry forward the clear shared ground plane and readable depth. For playable environments, the open-space and modular asset rules below supersede the reference's prop density and baked scenery arrangement. Keep floor detail restrained, paths broad and scenery sparse; do not copy rich prop clusters simply because they appear in the style reference.
- **Color and light:** Group hue, value and saturation into clear environmental families with deliberate accents. Use neutral form shading in authored art while leaving emissive fixtures, local light pools, bloom, godrays and volumetric effects to Godot. Avoid cinematic depth-of-field across playable ground, scattered glints and a universal blue-night or golden-palace treatment.

Choose silhouette separation using the whole cast's hair, clothes and expected movement. Keep useful environmental detail and a sense of place; do not solve readability by placing a blank dark rectangle or character-shaped halo behind every Officer. Preserve credible lighting rather than making all characters uniformly brighter than their surroundings. The reference's shadow also helps grounding, so do not attribute the entire improvement to background style alone.

### Fantasy identity and ownership

IMC is an other-world fantasy setting; do not infer a fixed historical medieval or industrial era from the word tavern or from Steambot-inspired nostalgia. Read current location sources and describe a small coherent set of fantasy design traits in the brief: for example distinctive architectural curves, painted joinery, colored local stone or ceramics, regional motifs, or a useful magical fitting when supported by the setting. These are design possibilities, not mandatory props or new lore. Scale ambition to the location: an everyday tavern need not become a monumental palace or magical showroom.

Give the location an intentional palette with dominant, secondary and accent colors. Warmth and familiarity can come from relationships among colors; they do not require every surface to be brown, beige or desaturated. Timber and plaster remain valid materials, but a default stack of timber, cream plaster, barrels and a rustic hearth does not establish distinctive fantasy identity by itself. Avoid solving fantasy identity through indiscriminate saturation, glowing crystals or extra clutter.

Steambot-inspired ownership governs how things are used, repaired and adapted. It does not supply a historical period, sepia filter or requirement for machinery. Preserve regional design and color through repairs and daily use. Polished rendering and visibly old objects are compatible.

### Owned and lived-in construction

An inhabited location must visibly have a past, a present owner and a daily routine:

- **Past:** show a restrained repaired section, reused structure, replaced board or tile, faded finish, practical extension or older material layer where it makes sense.
- **Owner:** show how the current household, company, department or trade has organized and adapted the place. Prefer recognizable practical decisions over generic decoration.
- **Daily routine:** show broad circulation wear, swept and unswept zones, work contact, loading or cart paths, training scuffs and storage at the point of use.

Controlled imperfection must remain structurally correct and easy to read. Do not substitute random dirt, broken anatomy, warped architecture, procedural distress, dozens of tiny stains or dense prop clutter. Nostalgia does not require a brown filter, universal decay or an old-fashioned industrial theme. For remote wilderness, express age, weather and ecology; show human use only when the location brief establishes a trail, camp, crossing or occupation.

The lived-in rule does not weaken the open-space target. Quiet ground can carry history through broad wear and repair patterns while remaining traversable. Use a few purposeful modular clusters around the edges rather than filling the center with evidence of life.

### Camera contract

Before any environment image generation, ask the user to choose the camera angle. Offer **top-down front-facing** as the default, with relevant alternatives such as three-quarter/oblique, side-view or reference-matched/custom. Do not infer or silently apply the default, and do not begin generation until the user answers. Record the choice before briefing the base or any modular asset.

For a playable environment, also ask whether the camera moves through the area. Do not infer the answer from the current game or the requested location name. Record **no** as a fixed single-screen environment and **yes** as a scrolling large environment such as a whole city, district or broad exploration ground. Both answers must be settled before generating its base or object sheets.

For playable environments, **top-down front-facing** means looking substantially downward onto the movement plane while keeping front faces readable. Front-facing describes the scene's horizontal orientation, not a low camera facing a rear wall. Inspect and use the relevant retained [playable-camera examples](playable-camera.md). Roofs/tabletops/wall tops, footprints, routes behind furniture and steps must read clearly. Avoid tall rear elevations dominating a shallow stage, thin tabletop slivers and strongly shrinking distant furniture. Orthographic-like or mild illustrated perspective may fit; match the selected reference rather than assigning an unsupported exact angle. A room can have abundant empty floor and still fail this camera requirement.

The shared front axis need not force every prop into an identical frontal orientation; rotated objects are valid when constructed under the same camera. Do not change a correct downward gameplay camera to escape a tabletop-like rendering problem. Keep rendering, world design and camera as separate decisions. Expedition backdrops follow their own staging camera and do not define playable projection.

Treat the selected camera as one shared construction rule. The base and modular objects must share projection, camera elevation, horizontal camera angle, horizon/vanishing behavior, ground-plane angle and character-relative scale; individual objects may rotate within that scene. Once the base is selected, use it as the direct camera reference for later object sheets whenever possible. An object rendered from a different camera fails even if both assets are individually well drawn. Correct the mismatched object locally rather than regenerating an accepted base.

### Production dimensions and source density

- **Fixed playable environment:** use a 1920×1080 final production master by default, matching IMC's current internal viewport. Inspect and record another verified runtime size when the target differs.
- **Scrolling playable environment:** for the current 64×48 IMC city-scale projection and present closest camera, use at least a 3072×2048 final production master. This replaces the undersized 1536×1024 city source, whose closest gameplay crop is enlarged by roughly 1.66×.
- **Larger scrolling area or closer camera:** scale the production master upward in proportion to the projected world span and closest permitted camera view. Do not treat 3072×2048 as enough for every possible whole-city map.
- **Object sheets:** their canvas dimensions may vary, but their objects must retain the base's source pixel density, character-relative scale and locked camera. Include recorded placement scale so Krita assembly does not depend on resizing by eye.

Provider generation dimensions and the final production-master dimensions are separate facts. Record both. A deterministic upscale can avoid runtime enlargement softness but does not create new authored detail; registered sections can add real detail but require seam and perspective review. Never describe an undersized provider result as a native-resolution final master.

### Open space and modular environment assets

For new or redesigned playable environments, target roughly **80% open negative space and 20% landscape/scenery occupancy**. Negative space is connected, unobstructed ground for movement, staging and encounters. It can contain quiet paving, grass, dirt, floor joints and broad shading; it need not be a blank fill. Judge the ratio as a practical composition target at the intended camera and gameplay scale, not an exact pixel calculation. Sky, inaccessible terrain, hidden floor behind buildings and UI margins do not substitute for usable ground. Check the assembled scene as well as the base: separate props must not fill the reserved space afterward.

Use broad roads, plazas, courtyards and room circulation. Do not squeeze a city road into a narrow corridor between buildings or decorations. Outdoor bases may include limited major terrain such as a mountain, cliff, dry channel, basin or riverbank while leaving a broad connected ground plane. Planned water barriers must not divide the remaining space into unusable strips. Preserve required entrances and interaction access. This target governs playable scenes; apply the actual staging needs to non-traversable battle backdrops and the actual navigation purpose to overview maps, rather than forcing every illustration into the same ratio.

Produce these independently editable assets by default:

- **Base environment:** ground/floor, broad surface treatment and the limited major terrain needed to establish the location. Exclude placeable scenery, decorative clutter, water surfaces and runtime lighting effects.
- **Transparent object sheets and extracted objects:** buildings or building sections, walls, trees, unlit lamp fixtures, stages, flags, banners, crates, fences, signs, planters and furniture. Give each independently correctable object clear separation, a complete silhouette and sufficient margins. A lamp and a crate remain separate objects unless their combination is intentionally requested. Do not invent supporting boxes, fused props or extra decorations.
- **Composition information:** retain each object's identity, source sheet/crop, intended scale, placement and ground-contact anchor, stacking/occlusion order and shadow relationship. Split foreground portions when needed for characters to pass behind them. A composed preview demonstrates the arrangement but does not replace the editable sources.

For an explicitly requested rendering-style comparison or early composition test, a furnished environment with objects baked into the candidate is allowed. Mark it as a comparison candidate rather than a modular production base. Generate every style candidate independently from the shared location brief and its own selected style reference; do not use one candidate as the source or reference for another. Return to the modular base-and-object workflow when the user selects a direction for production.

Match object sheets to the locked camera contract and the base's character-relative scale, palette, linework and light direction. Do not size each object independently to fill a sheet cell. Group compatible objects into sheets when useful; object separation does not require one generation call per object. Keep object contact/cast shadows on an associated editable layer or separately placeable asset, so moving or replacing a lamp does not leave its old shadow painted on the ground. Keep terrain shading in the base.

Review object construction and placement as well as visual style. Check support, attachment, scale, ground contact, plausible layering and unobstructed circulation. The user's Serena screenshot (`C:/Users/Tristixa-/Pictures/Screenshots/Temp/Serena Ingame.png`) is a failure example for clutter and an unintended lamp/box association, not an approved composition or a new rendering reference; these written rules remain usable without that temporary file.

When a prop is malformed, edit or regenerate only that object's asset, preserve accepted neighboring objects and the base, then recompose and inspect its joins/shadow. If objects share a sheet, replace only the affected object and retain the accepted cutouts. Do not regenerate an accepted whole background for a local prop correction. Retain modular source assets even if an authorized integration needs a flattened texture; separating files alone does not implement collision, depth sorting or runtime occlusion.

### Runtime lighting and water separation

Lamp posts, lanterns, braziers, magical sconces and similar light-bearing objects must be illustrated **unlit**. Preserve their readable construction and neutral form shading, but paint no emissive flame, glowing glass, light pool, halo, bloom or lens flare. Do not bake godrays, sun shafts, volumetric beams or comparable effects into a base or object sheet. Godot supplies those emissions and effects so intensity, color, time of day and placement remain adjustable.

Keep rivers, ponds, canals, pools, waterfalls and other water surfaces out of the base. The base may contain banks, basins, channels, riverbeds, waterfall cliffs and receiving terrain, but no painted water surface, foam, spray, reflection or caustics. Prefer Godot runtime water. When illustrated water is explicitly required, provide it as a separate transparent object/layer with a placement guide or mask, locked camera and scale, occlusion order and independent correction path. A composed preview may show the water layer, but the retained base remains water-free.

### Original layouts and integration

For new or redesigned rooms, create a composition around the department's work, furnishing, circulation and atmosphere. The user prefers original designs over repainting the current Adventurer Office. Use existing floor plans and game data to understand connections and functional needs; do not attach the current room texture as a layout lock unless the task asks to retain it. Rendering style does not prescribe shrine architecture, a side-on battle camera or one universal room arrangement.

Distinguish an exact replacement from a redesign. An exact replacement must fit existing camera, staging and occlusion coordinates. A redesign may change those coordinates while retaining the location's gameplay purpose; record the needed walkable-area, entrance, interaction, sprite-position and foreground-occlusion adjustments for later integration. A candidate request alone does not authorize those code changes. Keep UI overlay space and intended aspect ratio in the brief, and assess the scene with representative approved sprites at actual gameplay size. Existing sprites retain their approved appearance during background review.

Use separate runtime contact shadows beneath characters, anchored to the feet/ground point and rendered under the sprite. A soft, flattened ellipse with tunable width, opacity and edge softness can supply grounding without regenerating sprite frames. Keep it stable during idle, adapt it only when motion or elevation warrants, and respect furniture occlusion. Keep shadows from modular scenery separately editable with their objects when they are authored at all; only neutral form shading belonging to retained terrain stays in the base. Do not bake detached character shadows, dynamic lamp shadows or people into an empty environment. Review light direction, floor contact and occlusion together with the background.

### 3D-anime option prompt anchor

Use this only when the user selects the 3D-anime-rendered 2D JRPG option, then add the actual location, composition, camera, palette and runtime requirements:

The following anchor targets a playable environment. For an expedition backdrop, substitute its actual staging camera for the downward gameplay-camera sentence.

> Drawn 2D anime JRPG game environment matching the attached 3D-to-2D rendering examples: appealing modeled volumes, coherent thickness and support, clear shadow boundaries with gentle shading across broad forms, selective edge accents, warm/cool color relationships and distinct simplified materials. Preserve an inhabited fantasy world's regional design, deliberate colors and maintained wear. Use the separate gameplay-camera reference for a substantially downward view of the traversable ground. Keep footprints and routes readable. Avoid uniform brown shading, identical dark contours, flat prop-token appearance, photorealistic CGI, uniform PBR gloss, micro-gradients, scattered tiny highlights, excessive texture and cinematic blur. Keep runtime emissions and effects separate.

Keep final empty backgrounds free of characters, character contact shadows, UI, unrequested text and pseudo-writing. Review the image for the described properties; repeating the prompt is not proof of a style match.

For playable base generation, append the actual layout and this composition requirement: approximately 80% broad, connected open ground with restrained lived-in wear and about 20% major landscape structure; wide roads and clear circulation; no baked buildings, walls, trees, lamps, stages, flags, banners, crates or other placeable props; no painted water; and no emissive fixtures, light pools, bloom, godrays or volumetric effects. Brief objects separately on transparent sheets using the same camera, source density, scale and neutral lighting. Apply the open-space target again when composing them into the scene.

## Diagnose an integration mismatch before changing artwork

When an approved sprite looks rough only after integration, first compare the same frozen frame, scale, position and background with the current material and a plain alpha-rendering path. Inspect source alpha, color fringes, import filtering and downsampling; an already transparent export may still be receiving a legacy chroma-key shader. Its presence is a hypothesis to test, not proof of damage.

Then inspect the unchanged sprite on neutral grounds and in the room to distinguish an authored/extracted edge defect from background competition. Choose a rendering correction only when the comparison supports it. If the artifact is already present in the export, targeted contour/alpha cleanup requires an authorized asset revision. Consider local background refinement after these checks. Do not regenerate identity, change proportions, blanket-blur the room or permanently alter import settings merely because one preview looks off. Record what was actually verified; a frozen-frame comparison does not establish motion stability.

## Character-camera compatibility — 2026-09-18

New IMC world sprites use elevated orthographic top-down projection. Front is Down viewed from above, with all four cardinal facings sharing one elevation and body scale. A stage hosting them must share that ground/camera logic; a frontal wall view or a receding perspective floor is not automatically compatible. The current tavern comparison staging is under revision and supplies no approved camera lock. Resolve the location camera without copying a rejected character candidate.

Previous Tristitia base-sprite approval and reference roles are revoked. Do not use those candidates to lock an environment or as evidence of character/environment compatibility. Keep contact shadows separate, test stable foot anchors and occlusion, and compare sprites at the same size and floor position. Preserve readability through broad value and color relationships; do not solve mismatch by indiscriminate blur, stronger sticker outlines or global darkening. A provisional preview is not approval of either asset family.
