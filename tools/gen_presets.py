import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
D=json.load(open(os.path.join(HERE, 'palettes.json')))
out=["# BeFree Gantry style presets. Generated from tools/palettes.py (every text/background pair checked >= 4.5:1 WCAG AA).",""]
for k,p in D.items():
    out+=[f"{k}:",f"  image: 'gantry-admin://images/presets/{p['name'].split(' (')[0].lower().replace(' ','-')}.png'",f"  description: '{p['name']}'",
    "  colors:",f"    - '{p['live']}'",f"    - '{p['link']}'",f"    - '{p['gold']}'","","  styles:",
    "    base:",f"      background: '{p['base_bg']}'",f"      text-color: '{p['text']}'","      body-font: 'outfit, sans-serif'","      heading-font: 'barlowcondensed, sans-serif'",
    "    accent:",f"      color-1: '{p['live']}'",f"      color-2: '{p['link']}'"]
    for sec,bg,tx in [('header','header_bg','header_tx'),('navigation','nav_bg','nav_tx'),('slideshow','slideshow_bg','slideshow_tx'),('showcase','showcase_bg','showcase_tx'),('feature','feature_bg','feature_tx'),('subfeature','subfeature_bg','subfeature_tx'),('main','main_bg','main_tx'),('footer','footer_bg','footer_tx'),('offcanvas','off_bg','off_tx')]:
        out+=[f"    {sec}:",f"      background: '{p[bg]}'",f"      text-color: '{p[tx]}'"]
        if sec=='navigation': out.append("      overlay: 'rgba(0, 0, 0, 0.4)'")
        if sec=='offcanvas': out.append(f"      toggle-color: '{p['off_tx']}'")
        if sec=='showcase': out.append("      image: ''")
    out+=["    befree:",f"      variant: '{p['variant']}'",f"      radius: '{p['radius']}'"]
    for f in ['gold','gold_text','gold_ink','card','raised','line','muted','navy','paper','ink']:
        out.append(f"      {f.replace('_','-')}: '{p[f]}'")
    out.append("")
open(os.path.join(os.path.dirname(HERE), 'befree-gantry', 'gantry', 'presets.yaml'), 'w').write("\n".join(out))
