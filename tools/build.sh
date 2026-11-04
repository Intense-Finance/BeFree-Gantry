#!/usr/bin/env bash
# Build the installable theme zip: dist/befree-gantry-<version>.zip (+ .sha256)
# Top-level folder in the zip is befree-gantry/ (required by Appearance > Themes > Upload).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# Child outlines must inherit style presets from Base. A shipped styles
# file would pin colors and ignore a preset saved on the Base Outline.
if find "$ROOT/befree-gantry/install/outlines" "$ROOT/befree-gantry/config" -iname 'styles*' -print -quit | grep -q .; then
  echo "Refusing to build: a shipped outline or config path contains style overrides." >&2
  find "$ROOT/befree-gantry/install/outlines" "$ROOT/befree-gantry/config" -iname 'styles*' -print >&2
  exit 1
fi
VER="$(sed -n 's/^Version: *//p' "$ROOT/befree-gantry/style.css" | tr -d '\r')"
OUT="${DIST:-$ROOT/dist}"; mkdir -p "$OUT"
ZIP="$OUT/befree-gantry-$VER.zip"
python3 - "$ROOT" "$ZIP" <<'PY'
import os, sys, zipfile
root, zpath = sys.argv[1], sys.argv[2]
src = os.path.join(root, 'befree-gantry')
with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for d, dirs, files in os.walk(src):
        dirs[:] = sorted(x for x in dirs if not (d == src and x == 'custom'))
        for f in sorted(files):
            if f == '.DS_Store': continue
            p = os.path.join(d, f); arc = os.path.relpath(p, root)
            zi = zipfile.ZipInfo(arc, date_time=(2026, 11, 4, 0, 0, 0))  # reproducible
            zi.external_attr = 0o644 << 16; zi.compress_type = zipfile.ZIP_DEFLATED
            with open(p, 'rb') as fh: z.writestr(zi, fh.read())
PY
( cd "$OUT" && sha256sum "$(basename "$ZIP")" > "$(basename "$ZIP").sha256" )
cat "$ZIP.sha256"
