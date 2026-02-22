#!/usr/bin/env python3
"""Generate all diagrams for the quantum computing book."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import os

OUTDIR = os.path.join(os.path.dirname(__file__), 'diagrams')
os.makedirs(OUTDIR, exist_ok=True)

# Color palette
BLUE = '#2196F3'
ORANGE = '#FF9800'
GREEN = '#4CAF50'
RED = '#F44336'
PURPLE = '#9C27B0'
DARK = '#333333'
LIGHT_BLUE = '#BBDEFB'
LIGHT_ORANGE = '#FFE0B2'

def save(fig, name):
    fig.savefig(os.path.join(OUTDIR, name), dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"  ✓ {name}")

def draw_bloch_wireframe(ax, alpha=0.15):
    """Draw a wireframe Bloch sphere on a 3D axis."""
    u = np.linspace(0, 2*np.pi, 50)
    v = np.linspace(0, np.pi, 30)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones_like(u), np.cos(v))
    ax.plot_surface(x, y, z, alpha=0.05, color=BLUE, linewidth=0)
    # equator
    ax.plot(np.cos(u), np.sin(u), 0, color='gray', alpha=0.3, lw=0.8)
    # meridians
    ax.plot(np.cos(u), np.zeros_like(u), np.sin(u), color='gray', alpha=0.3, lw=0.8)
    ax.plot(np.zeros_like(u), np.cos(u), np.sin(u), color='gray', alpha=0.3, lw=0.8)
    # axes
    ax.plot([-1.3,1.3],[0,0],[0,0], 'k-', lw=0.5, alpha=0.4)
    ax.plot([0,0],[-1.3,1.3],[0,0], 'k-', lw=0.5, alpha=0.4)
    ax.plot([0,0],[0,0],[-1.3,1.3], 'k-', lw=0.5, alpha=0.4)

def setup_bloch_ax(ax):
    ax.set_xlim([-1.5,1.5]); ax.set_ylim([-1.5,1.5]); ax.set_zlim([-1.5,1.5])
    ax.set_axis_off()
    ax.view_init(elev=20, azim=-60)

# ─── 1. Bloch Sphere ───
print("Generating diagrams...")
fig = plt.figure(figsize=(8,7))
ax = fig.add_subplot(111, projection='3d')
draw_bloch_wireframe(ax)
setup_bloch_ax(ax)
# Labels
ax.text(0,0,1.4, '|0⟩', fontsize=14, ha='center', fontweight='bold', color=BLUE)
ax.text(0,0,-1.5, '|1⟩', fontsize=14, ha='center', fontweight='bold', color=BLUE)
ax.text(1.5,0,0, '|+⟩', fontsize=13, ha='center', color=GREEN)
ax.text(-1.5,0,0, '|−⟩', fontsize=13, ha='center', color=GREEN)
ax.text(1.5,0.2,0.1, 'X', fontsize=11, color='gray')
ax.text(0,1.5,0.1, 'Y', fontsize=11, color='gray')
ax.text(0.1,0,1.55, 'Z', fontsize=11, color='gray')
# State vector (example: theta=pi/3, phi=pi/4)
theta, phi = np.pi/3, np.pi/4
sx = np.sin(theta)*np.cos(phi)
sy = np.sin(theta)*np.sin(phi)
sz = np.cos(theta)
ax.quiver(0,0,0, sx,sy,sz, color=ORANGE, arrow_length_ratio=0.12, lw=2.5)
ax.text(sx+0.15, sy+0.15, sz+0.1, '|ψ⟩', fontsize=13, color=ORANGE, fontweight='bold')
fig.suptitle('Bloch Sphere Representation of a Qubit', fontsize=16, fontweight='bold', y=0.95)
save(fig, 'bloch-sphere.png')

# ─── 2. Classical vs Qubit ───
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))
fig.suptitle('Classical Bit vs Qubit', fontsize=16, fontweight='bold')

# Classical bit
ax1.set_xlim(-1,3); ax1.set_ylim(-1,3); ax1.set_aspect('equal'); ax1.axis('off')
ax1.set_title('Classical Bit', fontsize=14, fontweight='bold', pad=15)
for i, (x, label) in enumerate([(0.3,'0'), (1.7,'1')]):
    rect = patches.FancyBboxPatch((x-0.35, 0.7), 0.7, 0.7, boxstyle="round,pad=0.05",
                                   facecolor=LIGHT_BLUE if i==1 else 'white',
                                   edgecolor=BLUE, lw=2)
    ax1.add_patch(rect)
    ax1.text(x, 1.05, label, fontsize=20, ha='center', va='center', fontweight='bold', color=DARK)
# Arrow pointing to "1"
ax1.annotate('', xy=(1.7, 1.7), xytext=(1.0, 2.2),
            arrowprops=dict(arrowstyle='->', color=RED, lw=2.5))
ax1.text(1.0, 2.35, 'Definite state', fontsize=11, ha='center', color=RED)

# Qubit
ax2.set_xlim(-1.5,1.5); ax2.set_ylim(-1.5,1.5); ax2.set_aspect('equal'); ax2.axis('off')
ax2.set_title('Qubit', fontsize=14, fontweight='bold', pad=15)
circle = plt.Circle((0,0), 1.0, fill=False, edgecolor=BLUE, lw=2)
ax2.add_patch(circle)
# Gradient-like fill with colored wedges
for a in np.linspace(0, 2*np.pi, 40):
    ax2.plot([0, 0.9*np.cos(a)], [0, 0.9*np.sin(a)], color=BLUE, alpha=0.08, lw=3)
ax2.text(0, 1.15, '|0⟩', fontsize=13, ha='center', fontweight='bold', color=BLUE)
ax2.text(0, -1.25, '|1⟩', fontsize=13, ha='center', fontweight='bold', color=BLUE)
ax2.text(0, 0, 'α|0⟩ + β|1⟩', fontsize=12, ha='center', va='center', color=ORANGE, fontweight='bold')
ax2.text(0, -1.6, 'Superposition — exists in\nboth states simultaneously', fontsize=10, ha='center', color=DARK)

plt.tight_layout()
save(fig, 'classical-vs-qubit.png')

# ─── 3. Phase Interference ───
fig, axes = plt.subplots(2, 3, figsize=(12,7))
fig.suptitle('Quantum Interference', fontsize=16, fontweight='bold')
x = np.linspace(0, 4*np.pi, 300)

# Constructive
axes[0,0].plot(x, np.sin(x), color=BLUE, lw=1.5, label='Wave 1')
axes[0,0].set_title('Wave 1', fontsize=11); axes[0,0].set_ylim(-2.2,2.2)
axes[0,1].plot(x, np.sin(x), color=GREEN, lw=1.5, label='Wave 2 (in phase)')
axes[0,1].set_title('Wave 2 (in phase)', fontsize=11); axes[0,1].set_ylim(-2.2,2.2)
axes[0,2].plot(x, 2*np.sin(x), color=ORANGE, lw=2.5)
axes[0,2].set_title('Constructive Interference', fontsize=11, color=ORANGE, fontweight='bold')
axes[0,2].set_ylim(-2.2,2.2)
axes[0,2].fill_between(x, 2*np.sin(x), alpha=0.2, color=ORANGE)

# Destructive
axes[1,0].plot(x, np.sin(x), color=BLUE, lw=1.5)
axes[1,0].set_title('Wave 1', fontsize=11); axes[1,0].set_ylim(-2.2,2.2)
axes[1,1].plot(x, -np.sin(x), color=RED, lw=1.5)
axes[1,1].set_title('Wave 2 (out of phase)', fontsize=11); axes[1,1].set_ylim(-2.2,2.2)
axes[1,2].plot(x, np.zeros_like(x), color=DARK, lw=2.5)
axes[1,2].set_title('Destructive Interference', fontsize=11, color=RED, fontweight='bold')
axes[1,2].set_ylim(-2.2,2.2)
axes[1,2].axhline(y=0, color='gray', lw=0.5, ls='--')

for row in axes:
    for a in row:
        a.set_xticks([]); a.spines['top'].set_visible(False); a.spines['right'].set_visible(False)

# Add + and = signs
for col in [0,1]:
    for row in [0,1]:
        sign = '+' if col==0 else '='
        fig.text(0.355+col*0.33, 0.72-row*0.44, sign, fontsize=22, fontweight='bold',
                ha='center', va='center', color=DARK)

plt.tight_layout(rect=[0,0,1,0.93])
save(fig, 'phase-interference.png')

# ─── 4. Measurement Collapse ───
fig, ax = plt.subplots(figsize=(10,5))
ax.set_xlim(-0.5, 10); ax.set_ylim(-1, 5); ax.axis('off')
fig.suptitle('Quantum Measurement Collapse', fontsize=16, fontweight='bold')

# Superposition state (left)
circle = plt.Circle((2, 2.5), 1.2, fill=True, facecolor=LIGHT_BLUE, edgecolor=BLUE, lw=2)
ax.add_patch(circle)
ax.text(2, 2.5, 'α|0⟩ + β|1⟩', fontsize=13, ha='center', va='center', fontweight='bold', color=DARK)
ax.text(2, 0.8, 'Superposition', fontsize=11, ha='center', color=BLUE)

# Arrow
ax.annotate('', xy=(5.5, 2.5), xytext=(3.5, 2.5),
           arrowprops=dict(arrowstyle='->', color=RED, lw=3))
ax.text(4.5, 2.9, 'Measure', fontsize=13, ha='center', fontweight='bold', color=RED)

# Outcome |0⟩
rect0 = patches.FancyBboxPatch((6, 3.3), 2.5, 1.2, boxstyle="round,pad=0.1",
                                facecolor=LIGHT_BLUE, edgecolor=BLUE, lw=2)
ax.add_patch(rect0)
ax.text(7.25, 3.9, '|0⟩', fontsize=18, ha='center', va='center', fontweight='bold', color=BLUE)
ax.text(7.25, 3.45, 'prob = |α|²', fontsize=11, ha='center', color=DARK)

# Outcome |1⟩
rect1 = patches.FancyBboxPatch((6, 1.0), 2.5, 1.2, boxstyle="round,pad=0.1",
                                facecolor=LIGHT_ORANGE, edgecolor=ORANGE, lw=2)
ax.add_patch(rect1)
ax.text(7.25, 1.6, '|1⟩', fontsize=18, ha='center', va='center', fontweight='bold', color=ORANGE)
ax.text(7.25, 1.15, 'prob = |β|²', fontsize=11, ha='center', color=DARK)

# Branching arrows
ax.annotate('', xy=(6, 3.9), xytext=(5.5, 2.7),
           arrowprops=dict(arrowstyle='->', color=BLUE, lw=1.5))
ax.annotate('', xy=(6, 1.6), xytext=(5.5, 2.3),
           arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.5))

save(fig, 'measurement-collapse.png')

# ─── 5. Quantum Gates on Bloch Sphere ───
fig = plt.figure(figsize=(14,5))
fig.suptitle('Quantum Gate Operations on the Bloch Sphere', fontsize=16, fontweight='bold', y=1.0)

gates = [('X Gate\n(π rotation around X)', 'X'), ('Z Gate\n(π rotation around Z)', 'Z'), ('H Gate\n(rotation to equator)', 'H')]
for i, (title, gate) in enumerate(gates):
    ax = fig.add_subplot(1, 3, i+1, projection='3d')
    draw_bloch_wireframe(ax)
    setup_bloch_ax(ax)
    ax.set_title(title, fontsize=12, fontweight='bold', pad=10)

    if gate == 'X':
        ax.quiver(0,0,0, 0,0,0.95, color=BLUE, arrow_length_ratio=0.15, lw=2)
        ax.quiver(0,0,0, 0,0,-0.95, color=ORANGE, arrow_length_ratio=0.15, lw=2)
        ax.text(0.1,0,1.15, '|0⟩', fontsize=10, color=BLUE)
        ax.text(0.1,0,-1.2, '|1⟩', fontsize=10, color=ORANGE)
        # curved arrow for rotation
        t = np.linspace(0.3, 2.8, 30)
        ax.plot(0.3*np.cos(t), 0.3*np.sin(t), np.cos(t)*0.7, color=RED, lw=2, alpha=0.7)
    elif gate == 'Z':
        ax.quiver(0,0,0, 0.95,0,0, color=BLUE, arrow_length_ratio=0.15, lw=2)
        ax.quiver(0,0,0, -0.95,0,0, color=ORANGE, arrow_length_ratio=0.15, lw=2)
        ax.text(1.1,0,0.1, '|+⟩', fontsize=10, color=BLUE)
        ax.text(-1.2,0,0.1, '|−⟩', fontsize=10, color=ORANGE)
        t = np.linspace(0.3, 2.8, 30)
        ax.plot(np.cos(t)*0.7, np.sin(t)*0.7, 0.3*np.cos(t), color=RED, lw=2, alpha=0.7)
    elif gate == 'H':
        ax.quiver(0,0,0, 0,0,0.95, color=BLUE, arrow_length_ratio=0.15, lw=2)
        ax.quiver(0,0,0, 0.95,0,0, color=ORANGE, arrow_length_ratio=0.15, lw=2)
        ax.text(0.1,0,1.15, '|0⟩', fontsize=10, color=BLUE)
        ax.text(1.1,0,0.1, '|+⟩', fontsize=10, color=ORANGE)
        t = np.linspace(0, np.pi/2, 30)
        ax.plot(np.sin(t)*0.6, np.zeros_like(t), np.cos(t)*0.6, color=RED, lw=2, alpha=0.7)

plt.tight_layout()
save(fig, 'quantum-gates.png')

# ─── 6. Bell State Circuit ───
fig, ax = plt.subplots(figsize=(9,4))
ax.set_xlim(-0.5, 8); ax.set_ylim(-0.5, 4); ax.axis('off')
fig.suptitle('Bell State Preparation Circuit', fontsize=16, fontweight='bold')

y1, y2 = 2.8, 1.2  # qubit lines
# Qubit labels
ax.text(-0.3, y1, '|0⟩', fontsize=14, va='center', fontweight='bold', color=DARK)
ax.text(-0.3, y2, '|0⟩', fontsize=14, va='center', fontweight='bold', color=DARK)

# Lines
ax.plot([0.3, 7], [y1,y1], 'k-', lw=1.5)
ax.plot([0.3, 7], [y2,y2], 'k-', lw=1.5)

# H gate
rect = patches.FancyBboxPatch((1.5, y1-0.35), 0.7, 0.7, boxstyle="round,pad=0.02",
                               facecolor=LIGHT_BLUE, edgecolor=BLUE, lw=2)
ax.add_patch(rect)
ax.text(1.85, y1, 'H', fontsize=16, ha='center', va='center', fontweight='bold', color=BLUE)

# CNOT - control dot
ax.plot(3.5, y1, 'o', color=DARK, markersize=10, zorder=5)
# CNOT - target
circle = plt.Circle((3.5, y2), 0.25, fill=False, edgecolor=DARK, lw=2)
ax.add_patch(circle)
ax.plot([3.5,3.5], [y1, y2], 'k-', lw=1.5)
ax.plot([3.25,3.75], [y2,y2], 'k-', lw=2)  # + horizontal
ax.plot([3.5,3.5], [y2-0.25,y2+0.25], 'k-', lw=2)  # + vertical

# Measurement symbols
for y in [y1, y2]:
    mx = 5.5
    rect = patches.FancyBboxPatch((mx-0.35, y-0.35), 0.7, 0.7, boxstyle="round,pad=0.02",
                                   facecolor='#F5F5F5', edgecolor=DARK, lw=1.5)
    ax.add_patch(rect)
    # meter arc
    t = np.linspace(np.pi, 0, 30)
    ax.plot(mx + 0.2*np.cos(t), y-0.1 + 0.2*np.sin(t), color=DARK, lw=1.2)
    # meter needle
    ax.plot([mx, mx+0.15], [y-0.1, y+0.2], color=DARK, lw=1.5)

# Output labels
ax.text(7.2, y1, 'β₀₀', fontsize=12, va='center', color=DARK)
ax.text(7.2, y2, '', fontsize=12, va='center', color=DARK)

# Annotation
ax.text(4.5, 0.3, '|Φ⁺⟩ = (|00⟩ + |11⟩) / √2', fontsize=13, ha='center',
       style='italic', color=PURPLE, fontweight='bold')

save(fig, 'bell-state-circuit.png')

# ─── 7. Grover's Amplification ───
fig, axes = plt.subplots(1, 4, figsize=(14,4), sharey=True)
fig.suptitle("Grover's Amplitude Amplification", fontsize=16, fontweight='bold')

items = ['Item 1', 'Item 2', 'Target', 'Item 4']
colors = [BLUE, BLUE, ORANGE, BLUE]

# Simulate amplitudes for N=4, target=index 2
N = 4
amps = [np.ones(N)/np.sqrt(N)]  # iteration 0
for it in range(3):
    a = amps[-1].copy()
    # Oracle: flip target
    a[2] = -a[2]
    # Diffusion
    mean = np.mean(a)
    a = 2*mean - a
    amps.append(a)

for i, (ax, amp) in enumerate(zip(axes, amps)):
    c = [ORANGE if j==2 else BLUE for j in range(N)]
    ax.bar(range(N), amp, color=c, edgecolor='white', lw=1.5, width=0.6)
    ax.set_title(f'Iteration {i}', fontsize=12, fontweight='bold')
    ax.set_xticks(range(N))
    ax.set_xticklabels(items, fontsize=8, rotation=15)
    ax.axhline(y=0, color='gray', lw=0.5)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    if i==0: ax.set_ylabel('Amplitude', fontsize=11)

axes[0].set_ylim(-0.6, 1.1)
plt.tight_layout(rect=[0,0,1,0.92])
save(fig, 'grovers-amplification.png')

# ─── 8. Hardware Comparison ───
categories = ['Gate Speed', 'Coherence\nTime', 'Connectivity', 'Scalability', 'Current\nMaturity']
platforms = ['Superconducting', 'Trapped Ion', 'Photonic', 'Neutral Atom', 'Topological']
# Scores 1-5 (relative comparison)
data = {
    'Superconducting': [5, 2, 3, 4, 5],
    'Trapped Ion':     [2, 5, 4, 2, 4],
    'Photonic':        [4, 3, 5, 3, 2],
    'Neutral Atom':    [3, 4, 4, 4, 3],
    'Topological':     [4, 5, 3, 5, 1],
}
plat_colors = [BLUE, ORANGE, GREEN, PURPLE, RED]

N_cat = len(categories)
angles = np.linspace(0, 2*np.pi, N_cat, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8,8), subplot_kw=dict(polar=True))
fig.suptitle('Quantum Hardware Comparison', fontsize=16, fontweight='bold', y=1.02)

for i, (plat, color) in enumerate(zip(platforms, plat_colors)):
    vals = data[plat] + data[plat][:1]
    ax.plot(angles, vals, 'o-', color=color, lw=2, label=plat, markersize=5)
    ax.fill(angles, vals, alpha=0.08, color=color)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11)
ax.set_ylim(0, 5.5)
ax.set_yticks([1,2,3,4,5])
ax.set_yticklabels(['1','2','3','4','5'], fontsize=9, color='gray')
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)
ax.grid(True, alpha=0.3)

plt.tight_layout()
save(fig, 'hardware-comparison.png')

print("\nAll diagrams generated!")
