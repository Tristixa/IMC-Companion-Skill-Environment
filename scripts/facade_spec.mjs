#!/usr/bin/env node
// Write facades-spec.json (the painting contract for HD-2D buildings) from a small buildings file.
// Usage: node facade_spec.mjs buildings.json facades-spec.json
//
// buildings.json:
// {
//   "location": "eurydica-south",
//   "buildings": {
//     "<id>": { "concept": "<approved concept file and label>", "footprint_m": [w_x, d_z], "wall_height_m": H,
//               "ridge_axis": "x" | "z", "door_face": "n" | "e" | "s" | "w" | null, "roof": "<roof tile id>",
//               "notes": "<identity, ownership, repairs>",
//               "door": { "width_m": 1.4, "height_m": 2.3 }            // optional; defaults 1.4 × 2.3
//               "arch": { "half_width_m": 2.3, "straight_to_m": 3.0 } // optional walk-through arch on the door face and its opposite
//     } },
//   "roofs": ["green", "violet"], "walls": { "<id>": { "covers_m": [4, 3.4], "notes": "..." } },
//   "attachments": [{ "id": "awning_x", "size_m": [4, 1.6], "notes": "..." }],
//   "props": { "camera": "...", "items": ["barrel", "crate"] }
// }
// Ridge along z: the n and s faces are gable ends (width w); e and w are eaves walls (length d). Ridge along x: the reverse.
import fs from "node:fs";

const [src, dst] = process.argv.slice(2);
if (!src || !dst) { console.error("usage: node facade_spec.mjs buildings.json facades-spec.json"); process.exit(2); }
const input = JSON.parse(fs.readFileSync(src, "utf8")), PX = 64, gableH = W => +Math.min(5, .55 * W).toFixed(2), px = m => Math.round(m * PX);
const opposite = { n: "s", s: "n", e: "w", w: "e" }, faces = [];
for (const [id, b] of Object.entries(input.buildings)) {
  const [w, d] = b.footprint_m, H = b.wall_height_m, gableFaces = b.ridge_axis === "z" ? ["n", "s"] : ["e", "w"];
  const gw = b.ridge_axis === "z" ? w : d, lw = b.ridge_axis === "z" ? d : w, G = gableH(gw);
  for (const f of ["n", "s", "e", "w"]) {
    const gable = gableFaces.includes(f), W = gable ? gw : lw;
    const face = { building: id, face: f, file: `${id}/${f}.png`, type: gable ? "gable" : "wall", width_m: W, wall_height_m: H, gable_height_m: gable ? G : 0, px: [px(W), px(H + (gable ? G : 0))], door: null };
    if (b.arch && (f === b.door_face || f === opposite[b.door_face])) face.arch = { centre_x_m: W / 2, half_width_m: b.arch.half_width_m, straight_to_m: b.arch.straight_to_m, apex_m: b.arch.straight_to_m + b.arch.half_width_m };
    else if (f === b.door_face) face.door = { centre_x_m: +(W / 2).toFixed(2), width_m: b.door?.width_m ?? 1.4, height_m: b.door?.height_m ?? 2.3 };
    faces.push(face);
  }
}
const spec = {
  location: input.location, purpose: "Painted facade textures for the 3D building volumes of an HD-2D town. Each PNG is UV-mapped flat onto one face of a box, so every face is a straight-on ORTHOGRAPHIC ELEVATION, not a scene view.",
  px_per_m: PX, ground_is_bottom_edge: true,
  gable_profile: "For a gable face of width W, wall height H and gable height G: opaque below H across the full width; above H the opaque top edge is y = H + G * (1 - u)^1.4 where u = |x - W/2| / (W/2) (y up from the bottom edge, x from the left edge). Everything above that curve is alpha 0. The roof is separate 3D geometry that covers this edge by 0.45 m.",
  arch_profile: "Arch faces: transparent where |x - centre| <= half_width up to straight_to, then a semicircle of radius half_width centred at straight_to.",
  face_orientation: "Each face is painted as seen from OUTSIDE the building, standing in front of that face. Left/right in the image = the viewer's left/right.",
  buildings: input.buildings, faces,
  roof_tiles: (input.roofs || []).map(r => ({ id: r, file: `roofs/${r}.png`, px: [512, 512], covers_m: [8, 8], seamless: "both axes", courses_run: "horizontally (parallel to the ridge)" })),
  walls: Object.entries(input.walls || {}).map(([id, v]) => ({ id, file: `walls/${id}.png`, px: v.covers_m.map(px), covers_m: v.covers_m, seamless: "horizontal", notes: v.notes })),
  attachments: (input.attachments || []).map(a => ({ ...a, file: `attachments/${a.id}.png`, px: a.size_m.map(px) })),
  props_sheet: input.props ? { file: "props/sheet.png", camera: input.props.camera, items: input.props.items,
    cutouts: "props/<item>.png, each with a transparent margin, plus props/anchors.json { item: { px: [w, h], anchor_px: [x, y] (bottom-centre ground contact), height_m } }" } : null
};
fs.writeFileSync(dst, JSON.stringify(spec, null, 1));
console.log(`${faces.length} faces for ${Object.keys(input.buildings).length} buildings -> ${dst}`);
