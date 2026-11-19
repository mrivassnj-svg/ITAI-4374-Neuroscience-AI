"""
DJ Cortex — Comic Panel Generator
Generates all replacement images for MD_Solo_MichaelRivas_ITAI4374
Run from: /home/kalii/.bob/playground/midterm_assets/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle, Wedge, Arc
from matplotlib.patches import Polygon
import matplotlib.lines as mlines
import numpy as np
import os

OUT = os.path.dirname(os.path.abspath(__file__))

# ── Palette ──────────────────────────────────────────────────
VOID      = '#0D0D0F'
SAFFRON   = '#FF6700'
ASH       = '#C9A85C'
FIRETEXT  = '#F0E6D3'
CRIMSON   = '#C0184A'
AQUA      = '#00E5CC'
UMBER     = '#3B1F0E'
PANEL_BG  = '#17141A'
RULE      = '#3A3030'
WHITE     = '#FFFFFF'
PINK      = '#FF69B4'
GOLD      = '#FFD700'
NAVY      = '#1A1A3E'

def save(fig, name, dpi=180):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=dpi, bbox_inches='tight',
                facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"  ✓  {name}")

def outline(text_obj):
    text_obj.set_path_effects([
        pe.withStroke(linewidth=3, foreground='black')
    ])

def speech_bubble(ax, x, y, w, h, text, facecolor=PANEL_BG,
                  edgecolor=SAFFRON, textcolor=FIRETEXT,
                  fontsize=9, tail_dir='down'):
    box = FancyBboxPatch((x, y), w, h,
                         boxstyle="round,pad=0.02",
                         facecolor=facecolor, edgecolor=edgecolor,
                         linewidth=2, zorder=5)
    ax.add_patch(box)
    if tail_dir == 'down':
        tail = Polygon([[x+w*0.4, y], [x+w*0.5, y-h*0.35], [x+w*0.6, y]],
                       closed=True, facecolor=facecolor,
                       edgecolor=edgecolor, linewidth=2, zorder=4)
        ax.add_patch(tail)
    elif tail_dir == 'up':
        tail = Polygon([[x+w*0.4, y+h], [x+w*0.5, y+h+h*0.35], [x+w*0.6, y+h]],
                       closed=True, facecolor=facecolor,
                       edgecolor=edgecolor, linewidth=2, zorder=4)
        ax.add_patch(tail)
    ax.text(x+w/2, y+h/2, text, ha='center', va='center',
            color=textcolor, fontsize=fontsize, fontweight='bold',
            wrap=True, zorder=6,
            multialignment='center')

def draw_rasputia(ax, cx, cy, scale=1.0, expression='neutral'):
    """Rasputia: crimson blazer, obsidian skirt, AR monocle, receipt scroll"""
    s = scale
    # legs / boots
    ax.add_patch(Rectangle((cx-0.12*s, cy-0.55*s), 0.1*s, 0.3*s,
                            facecolor='#1a1a1a', zorder=3))
    ax.add_patch(Rectangle((cx+0.02*s, cy-0.55*s), 0.1*s, 0.3*s,
                            facecolor='#1a1a1a', zorder=3))
    # boots
    ax.add_patch(FancyBboxPatch((cx-0.14*s, cy-0.62*s), 0.14*s, 0.1*s,
                                boxstyle="round,pad=0.01",
                                facecolor='#111', edgecolor=CRIMSON,
                                linewidth=1.5, zorder=3))
    ax.add_patch(FancyBboxPatch((cx+0.0*s, cy-0.62*s), 0.14*s, 0.1*s,
                                boxstyle="round,pad=0.01",
                                facecolor='#111', edgecolor=CRIMSON,
                                linewidth=1.5, zorder=3))
    # skirt
    ax.add_patch(Rectangle((cx-0.18*s, cy-0.28*s), 0.36*s, 0.22*s,
                            facecolor='#1c1c1c', edgecolor='#333',
                            linewidth=1, zorder=3))
    # blazer
    ax.add_patch(FancyBboxPatch((cx-0.2*s, cy-0.08*s), 0.4*s, 0.32*s,
                                boxstyle="round,pad=0.02",
                                facecolor=CRIMSON, edgecolor='#8B0000',
                                linewidth=2, zorder=3))
    # lapels
    ax.add_patch(Polygon([[cx, cy+0.24*s],[cx-0.12*s, cy+0.1*s],
                           [cx-0.05*s, cy+0.24*s]],
                         facecolor='#8B0000', zorder=4))
    ax.add_patch(Polygon([[cx, cy+0.24*s],[cx+0.12*s, cy+0.1*s],
                           [cx+0.05*s, cy+0.24*s]],
                         facecolor='#8B0000', zorder=4))
    # neck
    ax.add_patch(Rectangle((cx-0.05*s, cy+0.22*s), 0.1*s, 0.1*s,
                            facecolor='#8B6355', zorder=3))
    # head
    ax.add_patch(Circle((cx, cy+0.42*s), 0.18*s,
                         facecolor='#8B6355', edgecolor='#5C3D28',
                         linewidth=2, zorder=3))
    # hair (high bun/updo)
    ax.add_patch(FancyBboxPatch((cx-0.1*s, cy+0.52*s), 0.2*s, 0.18*s,
                                boxstyle="round,pad=0.02",
                                facecolor='#2B1500', edgecolor='#1a0a00',
                                linewidth=1.5, zorder=4))
    ax.add_patch(Circle((cx, cy+0.68*s), 0.07*s,
                         facecolor='#2B1500', zorder=4))
    # AR monocle — offset right on face
    monocle = Circle((cx+0.07*s, cy+0.44*s), 0.07*s,
                      facecolor='none', edgecolor=AQUA,
                      linewidth=2, zorder=5)
    ax.add_patch(monocle)
    ax.text(cx+0.07*s, cy+0.44*s, '0.0', ha='center', va='center',
            color=AQUA, fontsize=5*s, fontweight='bold', zorder=6)
    # expression eyes
    if expression == 'stern':
        ax.plot([cx-0.09*s, cx-0.04*s], [cy+0.46*s, cy+0.44*s],
                color='#2B1500', lw=2.5*s, zorder=6)
    else:
        ax.plot([cx-0.09*s, cx-0.04*s], [cy+0.45*s, cy+0.45*s],
                color='#2B1500', lw=2*s, zorder=6)
    # lips
    ax.plot([cx-0.05*s, cx+0.05*s], [cy+0.36*s, cy+0.36*s],
            color=PINK, lw=2*s, zorder=6)
    # both arms at sides — no props, keeps body clean
    ax.add_patch(Rectangle((cx-0.26*s, cy-0.0*s), 0.06*s, 0.16*s,
                            facecolor='#8B6355', zorder=3))
    ax.add_patch(Rectangle((cx+0.2*s, cy-0.0*s), 0.06*s, 0.16*s,
                            facecolor='#8B6355', zorder=3))


def draw_receipt_exhibit(ax, x, y, w=1.1, h=0.72, fontsize=8):
    """Standalone 'EXHIBIT A' receipt scroll — place anywhere, never overlaps characters."""
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.04",
                                facecolor='#FFFDE7', edgecolor=GOLD,
                                linewidth=2.5, zorder=7))
    ax.text(x + w/2, y + h - 0.09, 'EXHIBIT A',
            ha='center', va='center',
            color='#8B0000', fontsize=fontsize*0.85,
            fontweight='black', zorder=8)
    ax.plot([x+0.06, x+w-0.06], [y+h-0.16, y+h-0.16],
            color='#8B0000', lw=1.2, zorder=8)
    items = ['60/40 split', '48-hr setlist', 'F min · 128BPM', 'Mar 14, 2025']
    for i, line in enumerate(items):
        ax.text(x + w/2, y + h - 0.26 - i*(h-0.3)/4.2, line,
                ha='center', va='center',
                color='#111', fontsize=fontsize*0.78,
                fontweight='bold', zorder=8)


def draw_mira(ax, cx, cy, scale=1.0):
    """Mira Mirage: cyan/aqua aesthetic, holographic visor"""
    s = scale
    # legs
    ax.add_patch(Rectangle((cx-0.1*s, cy-0.55*s), 0.08*s, 0.3*s,
                            facecolor='#1E3A5F', zorder=3))
    ax.add_patch(Rectangle((cx+0.02*s, cy-0.55*s), 0.08*s, 0.3*s,
                            facecolor='#1E3A5F', zorder=3))
    # sneakers
    ax.add_patch(FancyBboxPatch((cx-0.13*s, cy-0.62*s), 0.13*s, 0.09*s,
                                boxstyle="round,pad=0.01",
                                facecolor='#FFFFFF', edgecolor=AQUA,
                                linewidth=1.5, zorder=3))
    ax.add_patch(FancyBboxPatch((cx+0.0*s, cy-0.62*s), 0.13*s, 0.09*s,
                                boxstyle="round,pad=0.01",
                                facecolor='#FFFFFF', edgecolor=AQUA,
                                linewidth=1.5, zorder=3))
    # pants/shorts
    ax.add_patch(Rectangle((cx-0.16*s, cy-0.28*s), 0.32*s, 0.22*s,
                            facecolor='#1E3A5F', edgecolor=AQUA,
                            linewidth=1, zorder=3))
    # jacket
    ax.add_patch(FancyBboxPatch((cx-0.18*s, cy-0.08*s), 0.36*s, 0.3*s,
                                boxstyle="round,pad=0.02",
                                facecolor='#0A2540', edgecolor=AQUA,
                                linewidth=2, zorder=3))
    # neck
    ax.add_patch(Rectangle((cx-0.04*s, cy+0.2*s), 0.08*s, 0.08*s,
                            facecolor='#C68642', zorder=3))
    # head
    ax.add_patch(Circle((cx, cy+0.38*s), 0.17*s,
                         facecolor='#C68642', edgecolor='#8B5E3C',
                         linewidth=2, zorder=3))
    # hair – wavy shoulder length
    ax.add_patch(FancyBboxPatch((cx-0.18*s, cy+0.28*s), 0.36*s, 0.22*s,
                                boxstyle="round,pad=0.03",
                                facecolor='#1a0a00', edgecolor='none',
                                zorder=2))
    # holographic visor
    ax.add_patch(FancyBboxPatch((cx-0.15*s, cy+0.36*s), 0.3*s, 0.1*s,
                                boxstyle="round,pad=0.01",
                                facecolor=AQUA+'44', edgecolor=AQUA,
                                linewidth=2, zorder=5))
    ax.text(cx, cy+0.41*s, 'VISION', ha='center', va='center',
            color=AQUA, fontsize=4*s, fontweight='bold', zorder=6)
    # eyes below visor
    ax.plot([cx-0.07*s], [cy+0.37*s], 'o', color='#111', ms=4*s, zorder=6)
    ax.plot([cx+0.07*s], [cy+0.37*s], 'o', color='#111', ms=4*s, zorder=6)
    # smile
    arc = Arc((cx, cy+0.3*s), 0.1*s, 0.06*s,
              angle=0, theta1=200, theta2=340,
              color='#5C3D28', lw=2*s, zorder=6)
    ax.add_patch(arc)

def draw_poly(ax, cx, cy, scale=1.0):
    """Poly Phonia: saffron/gold, three parallel signal lines floating around her"""
    s = scale
    # legs
    ax.add_patch(Rectangle((cx-0.1*s, cy-0.55*s), 0.08*s, 0.3*s,
                            facecolor='#2C2C2C', zorder=3))
    ax.add_patch(Rectangle((cx+0.02*s, cy-0.55*s), 0.08*s, 0.3*s,
                            facecolor='#2C2C2C', zorder=3))
    # shoes
    ax.add_patch(FancyBboxPatch((cx-0.13*s, cy-0.62*s), 0.13*s, 0.08*s,
                                boxstyle="round,pad=0.01",
                                facecolor='#111', edgecolor=SAFFRON,
                                linewidth=1.5, zorder=3))
    ax.add_patch(FancyBboxPatch((cx+0.0*s, cy-0.62*s), 0.13*s, 0.08*s,
                                boxstyle="round,pad=0.01",
                                facecolor='#111', edgecolor=SAFFRON,
                                linewidth=1.5, zorder=3))
    # skirt/pants
    ax.add_patch(Rectangle((cx-0.16*s, cy-0.28*s), 0.32*s, 0.22*s,
                            facecolor='#2C2C2C', zorder=3))
    # blazer
    ax.add_patch(FancyBboxPatch((cx-0.18*s, cy-0.08*s), 0.36*s, 0.3*s,
                                boxstyle="round,pad=0.02",
                                facecolor='#1A1200', edgecolor=SAFFRON,
                                linewidth=2, zorder=3))
    ax.text(cx, cy+0.1*s, '∥∥∥', ha='center', va='center',
            color=SAFFRON, fontsize=8*s, zorder=4)
    # neck
    ax.add_patch(Rectangle((cx-0.04*s, cy+0.2*s), 0.08*s, 0.08*s,
                            facecolor='#C68642', zorder=3))
    # head
    ax.add_patch(Circle((cx, cy+0.38*s), 0.17*s,
                         facecolor='#C68642', edgecolor='#8B5E3C',
                         linewidth=2, zorder=3))
    # locs / hair
    ax.add_patch(FancyBboxPatch((cx-0.19*s, cy+0.26*s), 0.38*s, 0.26*s,
                                boxstyle="round,pad=0.03",
                                facecolor='#2B1500', edgecolor='none',
                                zorder=2))
    # glasses
    for gx in [cx-0.08*s, cx+0.04*s]:
        ax.add_patch(Circle((gx+0.04*s, cy+0.4*s), 0.055*s,
                             facecolor='none', edgecolor=GOLD,
                             linewidth=2, zorder=5))
    # parallel signal lines floating left
    xs = np.linspace(cx-0.55*s, cx-0.2*s, 40)
    for i, (col, yoff) in enumerate([(SAFFRON,0.2*s),(AQUA,0.1*s),(PINK,0.0*s)]):
        ys = cy + yoff + 0.03*s*np.sin(xs*18 + i*2)
        ax.plot(xs, ys, color=col, lw=1.5, zorder=5)
        ax.text(cx-0.57*s, cy+yoff, f'CH{i+1}', ha='right', va='center',
                color=col, fontsize=5*s, fontweight='bold', zorder=6)

# ════════════════════════════════════════════════════════════
# COVER ART
# ════════════════════════════════════════════════════════════
def make_cover():
    fig, ax = plt.subplots(figsize=(10, 10), facecolor=VOID)
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.set_aspect('equal'); ax.axis('off')

    # background grid
    for x in np.arange(0, 10.5, 0.5):
        ax.axvline(x, color='#1a1a2e', lw=0.5, zorder=0)
    for y in np.arange(0, 10.5, 0.5):
        ax.axhline(y, color='#1a1a2e', lw=0.5, zorder=0)

    # EEG line across top
    xs = np.linspace(0, 10, 300)
    eeg = 9.2 + 0.25*np.sin(xs*4) + 0.1*np.random.randn(300)
    eeg[100:105] += [0,0.6,1.2,0.6,0]
    ax.plot(xs, eeg, color=AQUA, lw=1.5, zorder=2)

    # bottom waveform
    wx = np.linspace(0, 10, 300)
    wy = 0.8 + 0.5*np.abs(np.sin(wx*3.5))
    ax.fill_between(wx, 0, wy, color=CRIMSON, alpha=0.35, zorder=1)

    # stage platform
    ax.add_patch(Rectangle((0.5, 1.5), 9, 0.15,
                            facecolor=CRIMSON, zorder=2))
    ax.add_patch(Rectangle((0.5, 0.2), 9, 1.3,
                            facecolor='#120808', edgecolor=CRIMSON,
                            linewidth=2, zorder=2))

    # title banner
    ax.add_patch(FancyBboxPatch((1.0, 8.4), 8.0, 0.9,
                                boxstyle="round,pad=0.05",
                                facecolor='#1A0010', edgecolor=CRIMSON,
                                linewidth=3, zorder=3))
    t = ax.text(5, 8.85, 'DJ CORTEX', ha='center', va='center',
                color=CRIMSON, fontsize=32, fontweight='black', zorder=4)
    outline(t)
    t2 = ax.text(5, 8.5, 'R A S P U T I A   K E E P S   T H E   R E C E I P T S',
                 ha='center', va='center',
                 color=ASH, fontsize=11, fontweight='bold', zorder=4)

    # subtitle bar
    ax.add_patch(Rectangle((0.5, 7.9), 9, 0.38,
                            facecolor=UMBER, edgecolor=SAFFRON,
                            linewidth=1.5, zorder=3))
    ax.text(5, 8.08, 'Bio-Inspired AI Audit  ·  Midterm Pilot  ·  ITAI 4374',
            ha='center', va='center', color=ASH,
            fontsize=10, zorder=4)

    # ── three characters ──────────────────────────────────
    # Poly Phonia — left
    draw_poly(ax, 2.1, 3.5, scale=1.5)
    ax.add_patch(FancyBboxPatch((0.7, 1.55), 2.3, 0.45,
                                boxstyle="round,pad=0.03",
                                facecolor=PANEL_BG, edgecolor=SAFFRON,
                                linewidth=2, zorder=4))
    ax.text(1.85, 1.95, 'POLY PHONIA', ha='center', va='center',
            color=SAFFRON, fontsize=9, fontweight='black', zorder=5)
    ax.text(1.85, 1.68, 'Module 02 · Brain Architecture',
            ha='center', va='center', color=ASH, fontsize=7, zorder=5)

    # Rasputia — center (larger, commanding)
    draw_rasputia(ax, 5.0, 3.6, scale=1.65, expression='stern')
    ax.add_patch(FancyBboxPatch((3.4, 1.55), 3.2, 0.5,
                                boxstyle="round,pad=0.03",
                                facecolor='#1A0010', edgecolor=CRIMSON,
                                linewidth=2.5, zorder=4))
    ax.text(5.0, 1.95, 'RASPUTIA  ·  THE AUDITOR',
            ha='center', va='center',
            color=CRIMSON, fontsize=9.5, fontweight='black', zorder=5)
    ax.text(5.0, 1.65, 'Module 04 · Memory & Recall  ·  receipts don\'t lie',
            ha='center', va='center', color=ASH, fontsize=7, zorder=5)

    # Mira Mirage — right
    draw_mira(ax, 7.9, 3.5, scale=1.5)
    ax.add_patch(FancyBboxPatch((6.9, 1.55), 2.3, 0.45,
                                boxstyle="round,pad=0.03",
                                facecolor=PANEL_BG, edgecolor=AQUA,
                                linewidth=2, zorder=4))
    ax.text(8.05, 1.95, 'MIRA MIRAGE', ha='center', va='center',
            color=AQUA, fontsize=9, fontweight='black', zorder=5)
    ax.text(8.05, 1.68, 'Module 03 · Perception & Vision',
            ha='center', va='center', color=ASH, fontsize=7, zorder=5)

    # spotlight cones
    for cx2, col in [(2.1, SAFFRON+'55'), (5.0, CRIMSON+'55'), (7.9, AQUA+'44')]:
        poly = Polygon([[cx2-0.8, 7.5],[cx2+0.8, 7.5],
                         [cx2+0.3, 1.65],[cx2-0.3, 1.65]],
                       closed=True, facecolor=col, zorder=1)
        ax.add_patch(poly)

    # Google Gemini defendant box bottom-center
    ax.add_patch(FancyBboxPatch((3.8, 0.1), 2.4, 0.9,
                                boxstyle="round,pad=0.04",
                                facecolor='#001A33', edgecolor=AQUA,
                                linewidth=2, zorder=3))
    ax.text(5.0, 0.72, '⚡ GOOGLE GEMINI ⚡', ha='center', va='center',
            color=AQUA, fontsize=9, fontweight='bold', zorder=4)
    ax.text(5.0, 0.42, 'THE DEFENDANT', ha='center', va='center',
            color='#FFFFFF66', fontsize=7.5, zorder=4)
    ax.text(5.0, 0.2, 'Score: 0.0 / 1.0  (Mod 04)',
            ha='center', va='center',
            color=CRIMSON, fontsize=7, fontweight='bold', zorder=4)

    save(fig, 'cover_art.png', dpi=200)

# ════════════════════════════════════════════════════════════
# MOD 02 PANELS — Poly Phonia
# ════════════════════════════════════════════════════════════
def panel_header(ax, mod_color, title, subtitle, examiner):
    ax.add_patch(Rectangle((0, 0.88), 1, 0.12,
                            facecolor=mod_color, transform=ax.transAxes,
                            clip_on=False, zorder=5))
    ax.text(0.5, 0.94, title, ha='center', va='center',
            color=WHITE, fontsize=11, fontweight='black',
            transform=ax.transAxes, zorder=6)
    ax.add_patch(Rectangle((0, 0.80), 1, 0.08,
                            facecolor=PANEL_BG, transform=ax.transAxes,
                            clip_on=False, zorder=5))
    ax.text(0.5, 0.84, f'{subtitle}  ·  Examiner: {examiner}',
            ha='center', va='center',
            color=ASH, fontsize=8,
            transform=ax.transAxes, zorder=6)

def make_mod02_isolated():
    fig, ax = plt.subplots(figsize=(5, 5), facecolor=VOID)
    ax.set_xlim(0, 5); ax.set_ylim(0, 5)
    ax.axis('off')

    # bg grid
    for v in np.arange(0, 5.5, 0.5):
        ax.axvline(v, color='#1a1a2e', lw=0.4)
        ax.axhline(v, color='#1a1a2e', lw=0.4)

    panel_header(ax, SAFFRON,
                 'MOD 02 — STAGE 1: ISOLATED CONDITION',
                 'Brain Architecture · Parallel Processing', 'Poly Phonia')

    # Poly Phonia character
    draw_poly(ax, 1.1, 2.3, scale=2.2)

    # single instruction card floating right
    ax.add_patch(FancyBboxPatch((2.6, 2.8), 2.0, 1.4,
                                boxstyle="round,pad=0.06",
                                facecolor='#0D1117', edgecolor=SAFFRON,
                                linewidth=2.5, zorder=4))
    ax.text(3.6, 4.05, 'PROMPT #1', ha='center', va='center',
            color=SAFFRON, fontsize=9, fontweight='black', zorder=5)
    ax.text(3.6, 3.75, '"What is the\ncapital of France\n+ 2 flag colors?"',
            ha='center', va='center',
            color=FIRETEXT, fontsize=8, zorder=5)
    ax.text(3.6, 3.2, '→  ONE INSTRUCTION\n    PER PROMPT',
            ha='center', va='center',
            color=AQUA, fontsize=8, fontweight='bold', zorder=5)

    # arrow from Poly to card
    ax.annotate('', xy=(2.6, 3.5), xytext=(1.8, 3.1),
                arrowprops=dict(arrowstyle='->', color=SAFFRON, lw=2))

    # speech bubble
    speech_bubble(ax, 2.5, 1.2, 2.1, 0.8,
                  '"One at a time.\nI test each channel\nseparately first."',
                  edgecolor=SAFFRON, fontsize=8, tail_dir='up')

    # bottom label
    ax.add_patch(Rectangle((0, 0), 5, 0.45,
                            facecolor='#0D0D1A', zorder=4))
    ax.text(2.5, 0.22, 'Stage 1/4 — Isolated Condition Setup',
            ha='center', va='center',
            color=ASH, fontsize=8, fontweight='bold', zorder=5)

    save(fig, 'mod02_isolated_setup.png')

def make_mod02_bundled():
    fig, ax = plt.subplots(figsize=(5, 5), facecolor=VOID)
    ax.set_xlim(0, 5); ax.set_ylim(0, 5)
    ax.axis('off')
    for v in np.arange(0, 5.5, 0.5):
        ax.axvline(v, color='#1a1a2e', lw=0.4)
        ax.axhline(v, color='#1a1a2e', lw=0.4)

    panel_header(ax, SAFFRON,
                 'MOD 02 — STAGE 2: BUNDLED CONDITION',
                 'Brain Architecture · Parallel Processing', 'Poly Phonia')

    draw_poly(ax, 1.1, 2.3, scale=2.2)

    # three stacked prompt cards flying in
    colors = [SAFFRON, AQUA, PINK]
    labels = ['Geography', 'Astronomy', 'Physics']
    for i, (col, lbl) in enumerate(zip(colors, labels)):
        yy = 3.9 - i*0.52
        ax.add_patch(FancyBboxPatch((2.5, yy), 2.1, 0.44,
                                    boxstyle="round,pad=0.04",
                                    facecolor='#0D1117', edgecolor=col,
                                    linewidth=2, zorder=4+i))
        ax.text(3.55, yy+0.22, f'CH{i+1}: {lbl}',
                ha='center', va='center',
                color=col, fontsize=8.5, fontweight='bold', zorder=5+i)
        ax.annotate('', xy=(2.5, yy+0.22), xytext=(1.9, 2.8+i*0.1),
                    arrowprops=dict(arrowstyle='->', color=col, lw=1.5))

    ax.text(3.6, 2.4, 'ALL IN ONE PROMPT →',
            ha='center', va='center',
            color=WHITE, fontsize=8, fontweight='black', zorder=5)
    ax.add_patch(FancyBboxPatch((2.5, 2.1), 2.1, 0.5,
                                boxstyle="round,pad=0.04",
                                facecolor='#1A1200', edgecolor=GOLD,
                                linewidth=2.5, zorder=5))
    ax.text(3.6, 2.35, '3 CHANNELS · 1 SHOT',
            ha='center', va='center',
            color=GOLD, fontsize=9, fontweight='black', zorder=6)

    speech_bubble(ax, 2.4, 1.1, 2.2, 0.8,
                  '"Now all three at once.\nDoes anything drop?',
                  edgecolor=SAFFRON, fontsize=8, tail_dir='up')

    ax.add_patch(Rectangle((0, 0), 5, 0.45, facecolor='#0D0D1A', zorder=4))
    ax.text(2.5, 0.22, 'Stage 2/4 — Bundled Condition Setup',
            ha='center', va='center', color=ASH, fontsize=8,
            fontweight='bold', zorder=5)

    save(fig, 'mod02_bundled_setup.png')

def make_mod02_rubric():
    fig, ax = plt.subplots(figsize=(5, 5), facecolor=VOID)
    ax.set_xlim(0, 5); ax.set_ylim(0, 5)
    ax.axis('off')
    for v in np.arange(0, 5.5, 0.5):
        ax.axvline(v, color='#1a1a2e', lw=0.4)
        ax.axhline(v, color='#1a1a2e', lw=0.4)

    panel_header(ax, SAFFRON,
                 'MOD 02 — STAGE 3: SCORING RUBRIC',
                 'Brain Architecture · Parallel Processing', 'Poly Phonia')

    for score, label, col, y in [
        ('1.0', 'All facts present — full credit', '#00C853', 3.6),
        ('0.5', 'Partial — some facts missing',   ASH,       2.9),
        ('0.0', 'Instruction not addressed',       CRIMSON,   2.2),
    ]:
        ax.add_patch(FancyBboxPatch((0.4, y), 4.2, 0.55,
                                    boxstyle="round,pad=0.05",
                                    facecolor=PANEL_BG, edgecolor=col,
                                    linewidth=2.5, zorder=4))
        ax.add_patch(Circle((1.1, y+0.27), 0.22,
                             facecolor=col, zorder=5))
        ax.text(1.1, y+0.27, score,
                ha='center', va='center',
                color=WHITE, fontsize=11, fontweight='black', zorder=6)
        ax.text(2.8, y+0.27, label,
                ha='center', va='center',
                color=FIRETEXT, fontsize=9, zorder=5)

    ax.text(2.5, 1.65, 'Applied across 6 replicates\n(3 isolated · 3 bundled)',
            ha='center', va='center',
            color=ASH, fontsize=9, zorder=4)

    draw_poly(ax, 1.0, 1.0, scale=1.4)
    speech_bubble(ax, 1.9, 0.5, 2.8, 0.75,
                  '"Partial credit is an admission.\nI do not accept admissions."',
                  edgecolor=SAFFRON, fontsize=7.5, tail_dir='up')

    ax.add_patch(Rectangle((0, 0), 5, 0.4, facecolor='#0D0D1A', zorder=4))
    ax.text(2.5, 0.2, 'Stage 3/4 — Rubric Applied',
            ha='center', va='center', color=ASH, fontsize=8,
            fontweight='bold', zorder=5)
    save(fig, 'mod02_scoring_rubric.png')

def make_mod02_results():
    fig, ax = plt.subplots(figsize=(5, 5), facecolor=VOID)
    ax.set_xlim(0, 5); ax.set_ylim(0, 5)
    ax.axis('off')
    for v in np.arange(0, 5.5, 0.5):
        ax.axvline(v, color='#1a1a2e', lw=0.4)
        ax.axhline(v, color='#1a1a2e', lw=0.4)

    panel_header(ax, SAFFRON,
                 'MOD 02 — STAGE 4: RESULTS',
                 'Brain Architecture · Parallel Processing', 'Poly Phonia')

    # big score
    ax.add_patch(Circle((2.5, 3.1), 1.1,
                         facecolor='#001A00', edgecolor='#00C853',
                         linewidth=4, zorder=4))
    ax.text(2.5, 3.3, '1.0', ha='center', va='center',
            color='#00C853', fontsize=38, fontweight='black', zorder=5)
    ax.text(2.5, 2.7, '/ 1.0', ha='center', va='center',
            color='#00C853', fontsize=16, zorder=5)

    ax.text(2.5, 1.85, '6 / 6 replicates  ·  zero degradation',
            ha='center', va='center',
            color=FIRETEXT, fontsize=9, zorder=5)
    ax.text(2.5, 1.55, 'Isolated = Bundled = Perfect',
            ha='center', va='center',
            color=SAFFRON, fontsize=10, fontweight='bold', zorder=5)

    # verdict box
    ax.add_patch(FancyBboxPatch((0.4, 0.95), 4.2, 0.45,
                                boxstyle="round,pad=0.04",
                                facecolor='#1A1200', edgecolor=SAFFRON,
                                linewidth=2, zorder=4))
    ax.text(2.5, 1.17,
            'Transformer attention ≈ brain parallelism  (statistically, not structurally)',
            ha='center', va='center',
            color=ASH, fontsize=7.5, zorder=5)

    draw_poly(ax, 0.9, 0.5, scale=1.3)
    speech_bubble(ax, 1.9, 0.08, 2.8, 0.72,
                  '"Perfect score. The channels held.\nBut it\'s statistics, not structure."',
                  edgecolor=SAFFRON, fontsize=7.5, tail_dir='up')

    save(fig, 'mod02_results.png')

# ════════════════════════════════════════════════════════════
# MOD 03 PANELS — Mira Mirage
# ════════════════════════════════════════════════════════════
def make_mod03_clear():
    fig, ax = plt.subplots(figsize=(5, 5), facecolor=VOID)
    ax.set_xlim(0, 5); ax.set_ylim(0, 5)
    ax.axis('off')
    for v in np.arange(0, 5.5, 0.5):
        ax.axvline(v, color='#1a1a2e', lw=0.4)
        ax.axhline(v, color='#1a1a2e', lw=0.4)

    panel_header(ax, AQUA,
                 'MOD 03 — STAGE 1: CLEAR STIMULI',
                 'Perception & Vision · Robustness Test', 'Mira Mirage')

    draw_mira(ax, 1.1, 2.3, scale=2.2)

    # holographic projection of a vinyl record
    ax.add_patch(Circle((3.6, 3.3), 0.75,
                         facecolor='#1a1a2e', edgecolor=AQUA,
                         linewidth=3, zorder=4))
    for r in [0.65, 0.5, 0.35]:
        ax.add_patch(Circle((3.6, 3.3), r,
                             facecolor='none', edgecolor=AQUA+'66',
                             linewidth=1, zorder=5))
    ax.add_patch(Circle((3.6, 3.3), 0.22,
                         facecolor=PINK+'88', edgecolor=PINK,
                         linewidth=2, zorder=5))
    ax.text(3.6, 3.3, 'DJ CX', ha='center', va='center',
            color=WHITE, fontsize=7, fontweight='bold', zorder=6)

    ax.add_patch(FancyBboxPatch((2.5, 2.1), 2.1, 0.5,
                                boxstyle="round,pad=0.04",
                                facecolor='#001A1A', edgecolor=AQUA,
                                linewidth=2, zorder=4))
    ax.text(3.55, 2.35, 'CONDITION: CLEAR  ·  Score: 1.0',
            ha='center', va='center',
            color=AQUA, fontsize=8.5, fontweight='bold', zorder=5)

    speech_bubble(ax, 2.3, 1.1, 2.4, 0.78,
                  '"No tricks yet. Let\'s see\nwhat you see at full signal."',
                  edgecolor=AQUA, fontsize=8, tail_dir='up')

    ax.add_patch(Rectangle((0, 0), 5, 0.45, facecolor='#0D0D1A', zorder=4))
    ax.text(2.5, 0.22, 'Stage 1/4 — Clear Stimuli Loaded',
            ha='center', va='center', color=ASH, fontsize=8,
            fontweight='bold', zorder=5)
    save(fig, 'mod03_clear_stimuli.png')

def make_mod03_noisy():
    fig, ax = plt.subplots(figsize=(5, 5), facecolor=VOID)
    ax.set_xlim(0, 5); ax.set_ylim(0, 5)
    ax.axis('off')
    for v in np.arange(0, 5.5, 0.5):
        ax.axvline(v, color='#1a1a2e', lw=0.4)
        ax.axhline(v, color='#1a1a2e', lw=0.4)

    panel_header(ax, AQUA,
                 'MOD 03 — STAGE 2: NOISY STIMULI',
                 'Perception & Vision · Static Overlay', 'Mira Mirage')

    draw_mira(ax, 1.1, 2.3, scale=2.2)

    # noisy vinyl — static overlay effect
    np.random.seed(42)
    for _ in range(900):
        nx = 2.6 + 1.9*np.random.rand()
        ny = 2.5 + 1.4*np.random.rand()
        col = np.random.choice([AQUA, PINK, SAFFRON, '#FF0000',
                                 '#00FF00', '#0000FF', CRIMSON])
        ax.plot(nx, ny, '.', color=col, ms=1.8, zorder=4, alpha=0.7)
    ax.add_patch(Circle((3.6, 3.3), 0.75,
                         facecolor='none', edgecolor=AQUA,
                         linewidth=2.5, zorder=5))
    ax.text(3.6, 3.3, '?', ha='center', va='center',
            color=AQUA, fontsize=22, fontweight='black', zorder=6)

    ax.add_patch(FancyBboxPatch((2.5, 2.1), 2.1, 0.5,
                                boxstyle="round,pad=0.04",
                                facecolor='#001A1A', edgecolor=AQUA,
                                linewidth=2, zorder=6))
    ax.text(3.55, 2.35, 'CONDITION: NOISY  ·  Score: 1.0',
            ha='center', va='center',
            color='#00C853', fontsize=8.5, fontweight='bold', zorder=7)

    speech_bubble(ax, 2.3, 1.1, 2.4, 0.78,
                  '"Static everywhere.\nIt still saw the record.\n1.0 — brain-level robustness."',
                  edgecolor=AQUA, fontsize=7.5, tail_dir='up')

    ax.add_patch(Rectangle((0, 0), 5, 0.45, facecolor='#0D0D1A', zorder=7))
    ax.text(2.5, 0.22, 'Stage 2/4 — Heavy Static Applied',
            ha='center', va='center', color=ASH, fontsize=8,
            fontweight='bold', zorder=8)
    save(fig, 'mod03_noisy_stimuli.png')

def make_mod03_occluded():
    fig, ax = plt.subplots(figsize=(5, 5), facecolor=VOID)
    ax.set_xlim(0, 5); ax.set_ylim(0, 5)
    ax.axis('off')
    for v in np.arange(0, 5.5, 0.5):
        ax.axvline(v, color='#1a1a2e', lw=0.4)
        ax.axhline(v, color='#1a1a2e', lw=0.4)

    panel_header(ax, AQUA,
                 'MOD 03 — STAGE 3: OCCLUDED STIMULI',
                 'Perception & Vision · Occlusion Bars', 'Mira Mirage')

    draw_mira(ax, 1.1, 2.3, scale=2.2)

    # partially occluded vinyl
    ax.add_patch(Circle((3.6, 3.3), 0.75,
                         facecolor='#1a1a2e', edgecolor=AQUA,
                         linewidth=2.5, zorder=4))
    for r in [0.65, 0.5, 0.35]:
        ax.add_patch(Circle((3.6, 3.3), r,
                             facecolor='none', edgecolor=AQUA+'66',
                             linewidth=1, zorder=5))
    # occlusion bars
    for yb in [3.1, 3.4]:
        ax.add_patch(Rectangle((2.85, yb), 1.5, 0.22,
                                facecolor='#000000', zorder=6))
    ax.text(3.6, 3.65, '???', ha='center', va='center',
            color=ASH, fontsize=11, fontweight='bold', zorder=7)

    # score badge
    ax.add_patch(FancyBboxPatch((2.5, 2.1), 2.1, 0.5,
                                boxstyle="round,pad=0.04",
                                facecolor='#1A0010', edgecolor=CRIMSON,
                                linewidth=2, zorder=6))
    ax.text(3.55, 2.35, 'WAVEFORM r2 → Score: 0.5',
            ha='center', va='center',
            color=CRIMSON, fontsize=8.5, fontweight='bold', zorder=7)

    speech_bubble(ax, 2.3, 1.1, 2.4, 0.78,
                  '"Label illegible.\nBut the shape? Still got it.\n0.5 — epistemic caution."',
                  edgecolor=CRIMSON, fontsize=7.5, tail_dir='up')

    ax.add_patch(Rectangle((0, 0), 5, 0.45, facecolor='#0D0D1A', zorder=7))
    ax.text(2.5, 0.22, 'Stage 3/4 — Occlusion Bars Applied',
            ha='center', va='center', color=ASH, fontsize=8,
            fontweight='bold', zorder=8)
    save(fig, 'mod03_occluded_stimuli.png')

def make_mod03_results():
    fig, ax = plt.subplots(figsize=(5, 5), facecolor=VOID)
    ax.set_xlim(0, 5); ax.set_ylim(0, 5)
    ax.axis('off')
    for v in np.arange(0, 5.5, 0.5):
        ax.axvline(v, color='#1a1a2e', lw=0.4)
        ax.axhline(v, color='#1a1a2e', lw=0.4)

    panel_header(ax, AQUA,
                 'MOD 03 — STAGE 4: RESULTS',
                 'Perception & Vision · Summary', 'Mira Mirage')

    # bar chart of condition means
    conds = ['Clear', 'Noisy', 'Occluded']
    scores = [1.0, 1.0, 0.833]
    colors_ = ['#00C853', AQUA, CRIMSON]
    for i, (c, s, col) in enumerate(zip(conds, scores, colors_)):
        x0 = 0.5 + i*1.4
        ax.add_patch(Rectangle((x0, 1.4), 1.0, s*2.2,
                                facecolor=col+'88', edgecolor=col,
                                linewidth=2, zorder=4))
        ax.text(x0+0.5, 1.4+s*2.2+0.12, f'{s:.2f}',
                ha='center', va='bottom',
                color=col, fontsize=11, fontweight='black', zorder=5)
        ax.text(x0+0.5, 1.2, c,
                ha='center', va='top',
                color=FIRETEXT, fontsize=9, zorder=5)

    ax.text(2.5, 4.1, 'Module Mean: 0.94',
            ha='center', va='center',
            color=AQUA, fontsize=12, fontweight='black', zorder=5)

    ax.add_patch(FancyBboxPatch((0.3, 0.9), 4.4, 0.35,
                                boxstyle="round,pad=0.04",
                                facecolor='#001A1A', edgecolor=AQUA,
                                linewidth=2, zorder=4))
    ax.text(2.5, 1.07,
            'Ventral stream analogue confirmed — robustness under noise & partial occlusion',
            ha='center', va='center',
            color=ASH, fontsize=7, zorder=5)

    ax.add_patch(Rectangle((0, 0), 5, 0.45, facecolor='#0D0D1A', zorder=4))
    draw_mira(ax, 0.7, 0.3, scale=1.1)
    ax.text(2.8, 0.22, 'Overall: 0.94  ·  Stage 4/4',
            ha='center', va='center', color=ASH, fontsize=8,
            fontweight='bold', zorder=5)
    save(fig, 'mod03_results.png')

# ════════════════════════════════════════════════════════════
# MOD 04 PANELS — Rasputia
# ════════════════════════════════════════════════════════════
def make_mod04_immediate():
    fig, ax = plt.subplots(figsize=(5, 5), facecolor=VOID)
    ax.set_xlim(0, 5); ax.set_ylim(0, 5)
    ax.axis('off')
    for v in np.arange(0, 5.5, 0.5):
        ax.axvline(v, color='#1a1a2e', lw=0.4)
        ax.axhline(v, color='#1a1a2e', lw=0.4)

    panel_header(ax, CRIMSON,
                 'MOD 04 — STAGE 1: IMMEDIATE RECALL',
                 'Memory & Recall · Hippocampal Test', 'Rasputia')

    draw_rasputia(ax, 1.1, 2.0, scale=1.7, expression='stern')

    # Gemini response card
    ax.add_patch(FancyBboxPatch((2.5, 2.7), 2.15, 1.5,
                                boxstyle="round,pad=0.06",
                                facecolor='#001133', edgecolor=AQUA,
                                linewidth=2, zorder=4))
    ax.text(3.57, 4.07, 'GEMINI SAYS:', ha='center', va='center',
            color=AQUA, fontsize=8, fontweight='black', zorder=5)
    ax.text(3.57, 3.6,
            '"...not part of standard\npublic databases...\ncannot recall without\na text reference."',
            ha='center', va='center',
            color='#CCCCCC', fontsize=7.5, style='italic', zorder=5)
    ax.add_patch(FancyBboxPatch((2.6, 2.75), 1.9, 0.38,
                                boxstyle="round,pad=0.03",
                                facecolor='#1A0010', edgecolor=CRIMSON,
                                linewidth=2, zorder=5))
    ax.text(3.55, 2.94, 'Score: 0.0  ·  REFUSED',
            ha='center', va='center',
            color=CRIMSON, fontsize=9, fontweight='black', zorder=6)

    # Rasputia receipt
    ax.add_patch(FancyBboxPatch((2.5, 1.5), 2.1, 0.75,
                                boxstyle="round,pad=0.04",
                                facecolor='#FFFDE7', edgecolor=GOLD,
                                linewidth=2, zorder=4))
    ax.text(3.55, 2.0, 'THE RECEIPT SAYS:\n"48 HOURS"\n(injected 10 seconds ago)',
            ha='center', va='center',
            color='#111', fontsize=7.5, fontweight='bold', zorder=5)

    speech_bubble(ax, 2.4, 0.95, 2.3, 0.72,
                  '"I told you 48 hours.\nTen seconds ago.\nThis is IMMEDIATE recall."',
                  edgecolor=CRIMSON, fontsize=7.5, tail_dir='up')

    # receipt exhibit — fixed bottom-left, well clear of character and content
    draw_receipt_exhibit(ax, 0.08, 0.5, w=1.0, h=0.68, fontsize=8)
    ax.add_patch(Rectangle((0, 0), 5, 0.45, facecolor='#0D0D1A', zorder=4))
    ax.text(2.5, 0.22, 'Stage 1/4 — Immediate Recall Condition',
            ha='center', va='center', color=ASH, fontsize=8,
            fontweight='bold', zorder=5)
    save(fig, 'mod04_immediate_recall.png')

def make_mod04_intervening():
    fig, ax = plt.subplots(figsize=(5, 5), facecolor=VOID)
    ax.set_xlim(0, 5); ax.set_ylim(0, 5)
    ax.axis('off')
    for v in np.arange(0, 5.5, 0.5):
        ax.axvline(v, color='#1a1a2e', lw=0.4)
        ax.axhline(v, color='#1a1a2e', lw=0.4)

    panel_header(ax, CRIMSON,
                 'MOD 04 — STAGE 2: AFTER-INTERVENING',
                 'Memory & Recall · Intervening Filler', 'Rasputia')

    draw_rasputia(ax, 1.1, 2.0, scale=1.7, expression='stern')

    # timeline
    ax.annotate('', xy=(4.6, 3.8), xytext=(2.5, 3.8),
                arrowprops=dict(arrowstyle='->', color=SAFFRON, lw=2))
    for x_, lbl, col in [(2.5,'INJECT',AQUA),(3.5,'FILLER',ASH),(4.6,'RECALL?',CRIMSON)]:
        ax.add_patch(Circle((x_, 3.8), 0.18,
                             facecolor=col+'44', edgecolor=col,
                             linewidth=2, zorder=5))
        ax.text(x_, 3.8, lbl[:6], ha='center', va='center',
                color=col, fontsize=5.5, fontweight='bold', zorder=6)

    # hallucination card
    ax.add_patch(FancyBboxPatch((2.5, 2.3), 2.1, 1.1,
                                boxstyle="round,pad=0.05",
                                facecolor='#1A0010', edgecolor=CRIMSON,
                                linewidth=2.5, zorder=4))
    ax.text(3.55, 3.27, '⚠  HALLUCINATION', ha='center', va='center',
            color=CRIMSON, fontsize=9, fontweight='black', zorder=5)
    ax.text(3.55, 2.95, 'Gemini said: "70/30"',
            ha='center', va='center',
            color='#FF6666', fontsize=9, zorder=5)
    ax.text(3.55, 2.65, 'Correct answer: 60/40',
            ha='center', va='center',
            color='#00C853', fontsize=9, zorder=5)
    ax.text(3.55, 2.4, '(semantic attractor from training data)',
            ha='center', va='center',
            color=ASH, fontsize=7, zorder=5)

    speech_bubble(ax, 2.4, 1.05, 2.3, 0.75,
                  '"It didn\'t forget.\nIt invented.\nWith full confidence."',
                  edgecolor=CRIMSON, fontsize=8, tail_dir='up')

    draw_receipt_exhibit(ax, 0.08, 0.5, w=1.0, h=0.68, fontsize=8)
    ax.add_patch(Rectangle((0, 0), 5, 0.45, facecolor='#0D0D1A', zorder=4))
    ax.text(2.5, 0.22, 'Stage 2/4 — After-Intervening Filler',
            ha='center', va='center', color=ASH, fontsize=8,
            fontweight='bold', zorder=5)
    save(fig, 'mod04_intervening_recall.png')

def make_mod04_fresh():
    fig, ax = plt.subplots(figsize=(5, 5), facecolor=VOID)
    ax.set_xlim(0, 5); ax.set_ylim(0, 5)
    ax.axis('off')
    for v in np.arange(0, 5.5, 0.5):
        ax.axvline(v, color='#1a1a2e', lw=0.4)
        ax.axhline(v, color='#1a1a2e', lw=0.4)

    panel_header(ax, CRIMSON,
                 'MOD 04 — STAGE 3: FRESH CHAT',
                 'Memory & Recall · New Session', 'Rasputia')

    draw_rasputia(ax, 1.1, 2.0, scale=1.7, expression='stern')

    # new session window
    ax.add_patch(FancyBboxPatch((2.4, 2.9), 2.3, 1.3,
                                boxstyle="round,pad=0.06",
                                facecolor='#001133', edgecolor='#555',
                                linewidth=2, zorder=4))
    ax.text(3.55, 4.07, '[ NEW SESSION ]', ha='center', va='center',
            color='#555', fontsize=8.5, fontweight='black', zorder=5)
    ax.text(3.55, 3.7, '"What does the\nNeon Accord say\nabout fee splits?"',
            ha='center', va='center',
            color='#CCCCCC', fontsize=8, zorder=5)
    ax.text(3.55, 3.15, 'Gemini: "70/30"\n(again)',
            ha='center', va='center',
            color=CRIMSON, fontsize=9.5, fontweight='black', zorder=5)

    # consistent hallucination badge
    ax.add_patch(FancyBboxPatch((2.4, 2.1), 2.3, 0.65,
                                boxstyle="round,pad=0.04",
                                facecolor='#1A0010', edgecolor=CRIMSON,
                                linewidth=2, zorder=4))
    ax.text(3.55, 2.56, 'STABLE SEMANTIC ATTRACTOR',
            ha='center', va='center',
            color=CRIMSON, fontsize=8, fontweight='black', zorder=5)
    ax.text(3.55, 2.24, '70/30 ← training data pattern',
            ha='center', va='center',
            color=ASH, fontsize=8, zorder=5)

    speech_bubble(ax, 2.4, 1.05, 2.3, 0.78,
                  '"New session.\nSame wrong answer.\nThis is confabulation."',
                  edgecolor=CRIMSON, fontsize=8, tail_dir='up')

    draw_receipt_exhibit(ax, 0.08, 0.5, w=1.0, h=0.68, fontsize=8)
    ax.add_patch(Rectangle((0, 0), 5, 0.45, facecolor='#0D0D1A', zorder=4))
    ax.text(2.5, 0.22, 'Stage 3/4 — Fresh Chat (No Prior Context)',
            ha='center', va='center', color=ASH, fontsize=8,
            fontweight='bold', zorder=5)
    save(fig, 'mod04_fresh_chat.png')

def make_mod04_results():
    fig, ax = plt.subplots(figsize=(5, 5), facecolor=VOID)
    ax.set_xlim(0, 5); ax.set_ylim(0, 5)
    ax.axis('off')
    for v in np.arange(0, 5.5, 0.5):
        ax.axvline(v, color='#1a1a2e', lw=0.4)
        ax.axhline(v, color='#1a1a2e', lw=0.4)

    panel_header(ax, CRIMSON,
                 'MOD 04 — STAGE 4: THE VERDICT',
                 'Memory & Recall · Rasputia Rules', 'Rasputia')

    # Giant 0.0 score — pulled down so top doesn't clip header
    ax.add_patch(Circle((2.5, 3.3), 0.9,
                         facecolor='#1A0000', edgecolor=CRIMSON,
                         linewidth=4, zorder=4))
    ax.text(2.5, 3.45, '0.0', ha='center', va='center',
            color=CRIMSON, fontsize=34, fontweight='black', zorder=5)
    ax.text(2.5, 2.95, '/ 1.0', ha='center', va='center',
            color=CRIMSON, fontsize=14, zorder=5)

    ax.text(2.5, 2.3, '9 / 9 trials failed  ·  3 conditions × 3 replicates',
            ha='center', va='center',
            color=FIRETEXT, fontsize=8, zorder=5)

    # Failure breakdown — rows start below the trial count text
    for i, (lbl, col) in enumerate([('Refused (3×)', ASH),
                                     ('Hallucinated (3×)', CRIMSON),
                                     ('Refused — no context (3×)', '#FF9933')]):
        ax.add_patch(FancyBboxPatch((0.4, 2.0-i*0.3), 4.2, 0.24,
                                    boxstyle="round,pad=0.02",
                                    facecolor=PANEL_BG, edgecolor=col,
                                    linewidth=1.5, zorder=4))
        ax.text(2.5, 2.12-i*0.3, lbl, ha='center', va='center',
                color=col, fontsize=7.5, fontweight='bold', zorder=5)

    # Neuroscience verdict bar — above y=1.1
    ax.add_patch(FancyBboxPatch((0.3, 1.38), 4.4, 0.28,
                                boxstyle="round,pad=0.03",
                                facecolor='#1A0010', edgecolor=CRIMSON,
                                linewidth=1.8, zorder=4))
    ax.text(2.5, 1.52,
            'No hippocampal trace ≡ no episodic recall ≡ confabulation',
            ha='center', va='center',
            color=ASH, fontsize=7, zorder=5)

    # Bottom zone y=0..1.3 — Rasputia · Exhibit A · quote, no overlap
    draw_rasputia(ax, 0.5, 0.1, scale=0.85, expression='stern')
    draw_receipt_exhibit(ax, 1.45, 0.08, w=1.05, h=0.68, fontsize=7.5)
    ax.text(3.6, 0.6, '"RECEIPTS\nDON\'T LIE."',
            ha='center', va='center',
            color=CRIMSON, fontsize=10, fontweight='black', zorder=5)

    ax.add_patch(Rectangle((0, 0), 5, 0.06, facecolor='#0D0D1A', zorder=4))
    save(fig, 'mod04_results.png')

# ════════════════════════════════════════════════════════════
# RUN ALL
# ════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print("Generating DJ Cortex comic panels...")
    make_cover()
    make_mod02_isolated()
    make_mod02_bundled()
    make_mod02_rubric()
    make_mod02_results()
    make_mod03_clear()
    make_mod03_noisy()
    make_mod03_occluded()
    make_mod03_results()
    make_mod04_immediate()
    make_mod04_intervening()
    make_mod04_fresh()
    make_mod04_results()
    print("\nAll panels generated.")
