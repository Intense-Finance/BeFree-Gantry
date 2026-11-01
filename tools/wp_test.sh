#!/bin/bash
# Local render test helper: sync theme into the local WP, apply a style preset / layout, screenshot.
# Usage: wp_test.sh sync | preset <presetN> | layout <name> | shot <file> <w,h> <url>
WP=/workspace/bfg-test/wordpress; TH=$WP/wp-content/themes/befree-gantry; OUT=/workspace/befree-gantry/test
case "$1" in
 sync) rsync -a --delete --exclude custom /workspace/befree-gantry/repo/befree-gantry/ $TH/; rm -rf $TH/custom/css-compiled ;;
 preset) python3 - "$2" "$TH" <<'PY'
import yaml,sys
p=yaml.safe_load(open(sys.argv[2]+'/gantry/presets.yaml'))[sys.argv[1]]['styles']
p['preset']=sys.argv[1]
for o in ['default','home']:
    import os; os.makedirs(f'{sys.argv[2]}/custom/config/{o}',exist_ok=True)
    yaml.safe_dump(p,open(f'{sys.argv[2]}/custom/config/{o}/styles.yaml','w'))
PY
  rm -rf $TH/custom/css-compiled ;;
 layout) if [ "$2" = none ]; then rm -f $TH/custom/config/default/layout.yaml; else cp $TH/layouts/$2.yaml $TH/custom/config/default/layout.yaml; fi ;;
 shot) timeout 120 google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars --virtual-time-budget=8000 --window-size=$3 --screenshot=$OUT/$2.png "$4" >/dev/null 2>&1; echo "$2.png $(stat -c %s $OUT/$2.png)";;
esac
