# Source of truth for the six BeFree Gantry style presets + WCAG contrast check.
import json,os,sys
BF=dict(gold='#d7c785',gold_text='#d7c785',gold_ink='#1c1708',card='#101820',raised='#162232',line='#2a3a4e',muted='#8ea0b5',navy='#0a2344',paper='#e7eef6',ink='#070d14')
def dark(**o):
    p=dict(base_bg='#050505',text='#f1f1ec',live='#9bff2e',link='#25f4ee',header_bg='#050505',header_tx='#f1f1ec',nav_bg='#08182e',nav_tx='#e7eef6',
           showcase_bg='#0a0a09',showcase_tx='#f1f1ec',feature_bg='#0a0a09',feature_tx='#f1f1ec',subfeature_bg='#070d14',subfeature_tx='#e7eef6',
           main_bg='#0a0a09',main_tx='#f1f1ec',footer_bg='#070d14',footer_tx='#8b8b84',off_bg='#070d14',off_tx='#f1f1ec',variant='standard',radius='14px',**BF)
    p.update(o);return p
P={
 'preset1':('Meld Neon (default)','if.finance lime and cyan neon on BeFree dark industrial',dark()),
 'preset2':('Industrial','Hazard stripes, blueprint grid, chamfered gold-plate cards',dark(variant='industrial',radius='0px')),
 'preset3':('BeFree Navy','BeFree\'s own navy and gold palette, no neon',dark(base_bg='#070d14',live='#d7c785',link='#8fc3ff',header_bg='#0a2344',header_tx='#e7eef6',nav_bg='#08182e',
     showcase_bg='#0a2344',showcase_tx='#e7eef6',feature_bg='#070d14',feature_tx='#e7eef6',main_bg='#070d14',main_tx='#e7eef6',footer_tx='#8ea0b5',text='#e7eef6',off_bg='#0a2344',off_tx='#e7eef6')),
 # Replaces Cyan Night in the preset4 slot. Violet, rose and amber is the light
 # colorful pair used across current Tailwind-style UI; jewel tones keep AA.
 'preset4':('Bloom','Light and colorful: violet, rose and amber on a bright ground',dict(
     base_bg='#fbf8ff',text='#1e1233',live='#6d28d9',link='#be123c',header_bg='#ffffff',header_tx='#1e1233',
     nav_bg='#3b0764',nav_tx='#faf5ff',showcase_bg='#f3e8ff',showcase_tx='#1e1233',feature_bg='#fbf8ff',feature_tx='#1e1233',
     subfeature_bg='#ffe4e6',subfeature_tx='#1e1233',main_bg='#fbf8ff',main_tx='#1e1233',slideshow_bg='#ffffff',slideshow_tx='#1e1233',
     footer_bg='#3b0764',footer_tx='#f5f3ff',off_bg='#3b0764',off_tx='#faf5ff',variant='light',radius='14px',
     gold='#f59e0b',gold_text='#92400e',gold_ink='#1c1204',card='#ffffff',raised='#f6f0ff',line='#e9d5ff',muted='#5b4674',
     navy='#3b0764',paper='#1e1233',ink='#3b0764')),
 'preset5':('Lime Terminal','Lime-led terminal look: lime for live and links on near-black',dark(base_bg='#030503',text='#e9f5e0',live='#9bff2e',link='#c6ff7a',header_bg='#030503',header_tx='#e9f5e0',nav_bg='#0a140a',nav_tx='#e9f5e0',showcase_bg='#070b07',showcase_tx='#e9f5e0',feature_bg='#070b07',feature_tx='#e9f5e0',subfeature_bg='#0a140a',subfeature_tx='#e9f5e0',main_bg='#070b07',main_tx='#e9f5e0',footer_bg='#0a140a',footer_tx='#93a58a',card='#0d170d',raised='#142314',line='#284028',muted='#93a58a',off_bg='#0a140a',off_tx='#e9f5e0')),
 'preset6':('Light Paper','Light variant on BeFree paper #e7eef6 with deep navy text',dict(base_bg='#e7eef6',text='#0a1a2e',live='#2f6b00',link='#005f73',header_bg='#ffffff',header_tx='#0a1a2e',nav_bg='#0a2344',nav_tx='#e7eef6',
     showcase_bg='#dfe7f1',showcase_tx='#0a1a2e',feature_bg='#e7eef6',feature_tx='#0a1a2e',subfeature_bg='#dfe7f1',subfeature_tx='#0a1a2e',main_bg='#e7eef6',main_tx='#0a1a2e',footer_bg='#0a2344',footer_tx='#c9d5e3',off_bg='#0a2344',off_tx='#e7eef6',
     variant='light',radius='14px',gold='#d7c785',gold_text='#6b5a12',gold_ink='#1c1708',card='#ffffff',raised='#f3f6fa',line='#c3cfdd',muted='#4a5a6e',navy='#0a2344',paper='#0a1a2e',ink='#0a2344')),
}
# Slideshow matches Main on presets that do not set their own, including Light Paper.
for _k,(_n,_d,_p) in P.items():
    _p.setdefault('slideshow_bg', _p['main_bg'])
    _p.setdefault('slideshow_tx', _p['main_tx'])
def lum(h):
    h=h.lstrip('#');c=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    c=[x/12.92 if x<=.03928 else ((x+.055)/1.055)**2.4 for x in c];return .2126*c[0]+.7152*c[1]+.0722*c[2]
def cr(a,b):
    A,B=lum(a),lum(b);return (max(A,B)+.05)/(min(A,B)+.05)
if __name__=='__main__':
    ok=True;rows=[]
    for k,(n,d,p) in P.items():
        checks=[('text/base',p['text'],p['base_bg']),('text/main',p['main_tx'],p['main_bg']),('text/card',p['text'],p['card']),('live/main',p['live'],p['main_bg']),('link/main',p['link'],p['main_bg']),('link/card',p['link'],p['card']),
                ('muted/card',p['muted'],p['card']),('header',p['header_tx'],p['header_bg']),('nav',p['nav_tx'],p['nav_bg']),('footer',p['footer_tx'],p['footer_bg']),('gold-ink/gold',p['gold_ink'],p['gold']),('goldtext/card',p['gold_text'],p['card']),('goldtext/main',p['gold_text'],p['main_bg']),('offcanvas',p['off_tx'],p['off_bg']),
                ('slideshow',p['slideshow_tx'],p['slideshow_bg']),('showcase',p['showcase_tx'],p['showcase_bg']),('feature',p['feature_tx'],p['feature_bg']),('subfeature',p['subfeature_tx'],p['subfeature_bg'])]
        for c,f,b in checks:
            r=cr(f,b);flag='OK' if r>=4.5 else 'FAIL';ok&=r>=4.5;rows.append(f"{k} {n:22} {c:14} {f} on {b}: {r:5.2f} {flag}")
    print('\n'.join(rows));print('ALL >= 4.5:1' if ok else 'SOME FAIL')
    for k,(n,d,p) in P.items():
        ratios=[cr(f,b) for c,f,b in [('text/base',p['text'],p['base_bg']),('text/main',p['main_tx'],p['main_bg']),('text/card',p['text'],p['card']),('live/main',p['live'],p['main_bg']),('link/main',p['link'],p['main_bg']),('link/card',p['link'],p['card']),('muted/card',p['muted'],p['card']),('header',p['header_tx'],p['header_bg']),('nav',p['nav_tx'],p['nav_bg']),('footer',p['footer_tx'],p['footer_bg']),('gold-ink/gold',p['gold_ink'],p['gold']),('goldtext/card',p['gold_text'],p['card']),('goldtext/main',p['gold_text'],p['main_bg']),('offcanvas',p['off_tx'],p['off_bg']),('slideshow',p['slideshow_tx'],p['slideshow_bg']),('showcase',p['showcase_tx'],p['showcase_bg']),('feature',p['feature_tx'],p['feature_bg']),('subfeature',p['subfeature_tx'],p['subfeature_bg'])]]
        print(f'MIN {k} {n}: {min(ratios):.2f}:1')
    json.dump({k:dict(name=n,desc=d,**p) for k,(n,d,p) in P.items()},open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'palettes.json'),'w'),indent=1)
