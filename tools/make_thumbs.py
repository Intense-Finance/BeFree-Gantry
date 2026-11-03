#!/usr/bin/env python3
"""Generate Gantry admin preset + layout thumbnails for BeFree Gantry."""
import os
from PIL import Image, ImageDraw, ImageFont
ROOT = '/workspace/befree-gantry/repo'
THEME = f'{ROOT}/befree-gantry'
TEST = '/workspace/befree-gantry/test'
PV = f'{ROOT}/docs/previews'
os.makedirs(f'{THEME}/admin/images/presets', exist_ok=True)
os.makedirs(f'{THEME}/admin/images/layouts', exist_ok=True)
os.makedirs(f'{PV}/presets', exist_ok=True); os.makedirs(f'{PV}/layouts', exist_ok=True)
# Preset thumbs (500x400, Hydrogen size) cropped from local WP renders
for n in ['meld-neon','industrial','befree-navy','bloom','lime-terminal','light-paper']:
    src = f'{TEST}/wp-home-{n}-1440.png'
    if not os.path.exists(src):
        continue
    im = Image.open(src).convert('RGB').crop((0,0,1440,1152)).resize((500,400), Image.LANCZOS)
    im.save(f'{THEME}/admin/images/presets/{n}.png', optimize=True)
    im.save(f'{PV}/presets/{n}.png', optimize=True)
# Layout diagrams (200x250, Gantry size)
BG='#0a0f14'; HDR='#0a2344'; MAIN='#16202c'; SIDE='#d7c785'; LIME='#a3ff12'; CYAN='#22d3ee'; LINE='#2a3a4e'
try: F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 11)
except Exception: F = ImageFont.load_default()
def base(label):
    im = Image.new('RGB',(200,250),BG); d = ImageDraw.Draw(im)
    d.rectangle((0,0,199,6),fill=SIDE)
    d.rectangle((10,14,189,30),fill=HDR); d.rectangle((14,20,60,24),fill=LIME)
    d.rectangle((10,224,189,240),fill=HDR)
    d.text((100,232),label,fill='#e6edf3',font=F,anchor='mm')
    return im,d
def box(d,x0,y0,x1,y1,c,o=None): d.rectangle((x0,y0,x1,y1),fill=c,outline=o or LINE)
def L(name,label,fn):
    im,d = base(label); fn(d); im.save(f'{THEME}/admin/images/layouts/{name}.png',optimize=True)
    im.resize((400,500),Image.NEAREST).save(f'{PV}/layouts/{name}.png',optimize=True)
L('befree-right-sidebar','MAIN + RIGHT', lambda d:(box(d,10,38,131,216,MAIN),box(d,137,38,189,216,MAIN,SIDE),box(d,140,180,186,212,SIDE)))
L('befree-left-sidebar','LEFT + MAIN', lambda d:(box(d,10,38,62,216,MAIN,SIDE),box(d,68,38,189,216,MAIN),box(d,13,180,59,212,SIDE)))
L('befree-both-sidebars','BOTH SIDEBARS', lambda d:(box(d,10,38,48,216,MAIN,SIDE),box(d,54,38,145,216,MAIN),box(d,151,38,189,216,MAIN,SIDE),box(d,154,180,186,212,SIDE)))
L('befree-full-width','FULL WIDTH', lambda d:(box(d,10,38,189,180,MAIN),box(d,10,186,189,216,SIDE)))
def mag(d):
    box(d,10,38,189,84,HDR,CYAN); d.rectangle((18,50,110,58),fill='#e6edf3'); d.rectangle((18,64,60,72),fill=SIDE)
    for i in range(3): box(d,10+i*61,90,67+i*61,118,MAIN,CYAN)
    box(d,10,124,131,200,MAIN); box(d,137,124,189,200,MAIN,SIDE); box(d,10,206,189,216,MAIN)
L('befree-magazine','MAGAZINE HOME', mag)
def off(d):
    box(d,30,70,169,190,MAIN,SIDE); d.text((100,110),'OFFLINE',fill=SIDE,font=F,anchor='mm'); d.rectangle((60,140,139,150),fill=LIME)
L('befree-offline','OFFLINE', off)
def err(d):
    box(d,10,38,189,216,MAIN); d.text((100,110),'404',fill=LIME,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',40) if os.path.exists('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf') else F,anchor='mm'); d.rectangle((60,150,139,158),fill=CYAN)
L('befree-error','ERROR', err)
print('ok')
