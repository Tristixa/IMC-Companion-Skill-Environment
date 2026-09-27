# Playable camera: top-down front-facing

The user clarified this camera with game-asset examples on 2026-09-18. It is a substantially downward view onto traversable space with front faces still readable. The front axis specifies horizontal orientation; it does not mean a frontal backdrop with a shallow floor stage. Carry forward the user's camera answer for the same run rather than asking again because the rendering style changes.

## Retained reference roles

| Reference | Role and provenance |
|---|---|
| [Eurydica city](media/camera/eurydica-city.png) | Illustrated exterior projection and movement-plane readability. Unchanged copy of `D:/Godot Projects/IMC-godot/assets/visual/world/city.png`. The user's in-game screenshot shows the same ground at a closer gameplay crop. Do not import the city's density, water or lighting into the new brief. |
| [Playable office](media/camera/playable-office.jpeg) | Primary interior camera example: visible desk surface, central carpet footprint, circulation around the desk and furniture at different ground positions. Unchanged copy of `D:/Download/WhatsApp Image 2026-09-16 at 10.11.21 PM.jpeg`. Ignore the characters, HUD, dense furnishing and baked light effects; it is not a rendering or density target. |
| [Pixel courtyard](media/camera/pixel-courtyard.jpg) | Stronger orthographic-like top/front construction; roofs, walls, table surfaces and courtyard routes are legible. Unchanged copy of `D:/Download/5cd35cf0-bc94-4d73-968b-e7c3b70f62a1_scaled.jpg`. Camera only; no pixel rendering requirement. |
| [Fantasy shop](media/camera/fantasy-shop.jpg) | Downward exterior view with readable building front and roof, clear footprints and near/far ground relationships. Unchanged copy of `D:/Download/maxresdefault.jpg`. Camera only; no requirement to copy props, palette, pixel rendering or content. |

These examples vary in projection. Do not claim an exact numeric angle from them or force every example into strict isometric/orthographic terminology. Use the closest relevant example for the requested interior or exterior and explicitly assign it the camera role in generation. Rendering examples remain separate inputs.

## Acceptance criteria

- The ground reads as a traversable plane extending both horizontally and into depth, not just open floor in front of a rear-wall illustration.
- Table/counter tops, step treads, wall tops and roofs (where present) are clearly visible. Front faces remain readable but do not dominate through oversized vertical elevations.
- Object footprints and routes around or behind furniture are understandable. A character can occupy multiple ground positions at a reasonably consistent gameplay scale.
- Use modest perspective convergence and foreshortening consistent with the reference; avoid exaggerated shrinking toward a rear focal point.
- All architecture, furniture, ground detail and later modular assets share the same camera. Props can face different directions under that camera.
- Judge the whole scene and a representative character's intended scale. This may be checked in an offline assembly; it does not require game integration when the user requests only an art test.

The former three tavern tests are not camera targets. They emphasized facing a counter/fireplace and gave too little prominence to the top surfaces and movement plane. Correcting that requires a better gameplay projection, not a change to the already accepted Unicorn Overlord or PawPop 2 rendering directions. A fixed camera still uses this playable projection; fixed versus scrolling determines coverage, not whether the scene becomes a backdrop.
