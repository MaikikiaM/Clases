import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['mathtext.fontset'] = 'cm'

bbox_props = dict(boxstyle='round,pad=0.25', facecolor='white', edgecolor='#78909c', alpha=0.96, lw=0.8)

def setup_ax(ax, title, xlim, ylim):
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.axhline(0, color='black', lw=0.9, zorder=2)
    ax.axvline(0, color='black', lw=0.9, zorder=2)
    ax.grid(True, linestyle=':', alpha=0.55, zorder=1)
    ax.set_title(title, fontsize=11, fontweight='bold', pad=10)
    ax.set_xlabel(r'$x$', fontsize=10, loc='right')
    ax.set_ylabel(r'$y$', fontsize=10, loc='top')

# ==============================================================================
# FIG 1A: f(x) = x^2 / (x - 1)
# ==============================================================================
fig, ax = plt.subplots(figsize=(5.6, 4.0), dpi=300)
setup_ax(ax, r'1A: $f(x) = \frac{x^2}{x-1}$', (-5, 6), (-7, 9.5))
x1 = np.linspace(-5, 0.93, 400)
x2 = np.linspace(1.07, 6, 400)
ax.plot(x1, x1**2 / (x1 - 1), '#0d47a1', lw=1.8, zorder=3)
ax.plot(x2, x2**2 / (x2 - 1), '#0d47a1', lw=1.8, zorder=3)
ax.axvline(1, color='#d32f2f', linestyle='--', lw=1.2, label=r'A.V. $x=1$')
x_ao = np.linspace(-5, 6, 200)
ax.plot(x_ao, x_ao + 1, '#c2185b', linestyle='--', lw=1.2, label=r'A.O. $y=x+1$')

# Máx (0, 0): In open region (0.5, 0.8) pointing down-left to (0.05, 0.05) - NO intersection!
ax.plot(0, 0, 'o', color='#1b5e20', markersize=5.5, zorder=5)
ax.annotate('Máx (0, 0)', xy=(0, 0), xytext=(0.5, 0.8),
            arrowprops=dict(arrowstyle='->', lw=0.9, color='#1b5e20'),
            fontsize=8.5, fontweight='bold', bbox=bbox_props, zorder=6)

# Mín (2, 4): Inside the bowl, straight above at (2.0, 6.0)
ax.plot(2, 4, 'o', color='#1b5e20', markersize=5.5, zorder=5)
ax.annotate('Mín (2, 4)', xy=(2, 4), xytext=(2.0, 6.0),
            arrowprops=dict(arrowstyle='->', lw=0.9, color='#1b5e20'),
            fontsize=8.5, fontweight='bold', bbox=bbox_props, zorder=6, ha='center')

ax.legend(loc='lower right', fontsize=8, framealpha=0.95)
plt.savefig('fig_1a.pdf', bbox_inches='tight')
plt.savefig('fig_1a.png', bbox_inches='tight')
plt.close()

# ==============================================================================
# FIG 1B: g(x) = x^2 / (x + 1)
# ==============================================================================
fig, ax = plt.subplots(figsize=(5.6, 4.0), dpi=300)
setup_ax(ax, r'1B: $g(x) = \frac{x^2}{x+1}$', (-6, 5), (-9.5, 7))
x1 = np.linspace(-6, -1.07, 400)
x2 = np.linspace(-0.93, 5, 400)
ax.plot(x1, x1**2 / (x1 + 1), '#0d47a1', lw=1.8, zorder=3)
ax.plot(x2, x2**2 / (x2 + 1), '#0d47a1', lw=1.8, zorder=3)
ax.axvline(-1, color='#d32f2f', linestyle='--', lw=1.2, label=r'A.V. $x=-1$')
x_ao = np.linspace(-6, 5, 200)
ax.plot(x_ao, x_ao - 1, '#c2185b', linestyle='--', lw=1.2, label=r'A.O. $y=x-1$')

# Máx (-2, -4): Straight below inside the bowl at (-2.0, -6.0)
ax.plot(-2, -4, 'o', color='#1b5e20', markersize=5.5, zorder=5)
ax.annotate('Máx (-2, -4)', xy=(-2, -4), xytext=(-2.0, -6.0),
            arrowprops=dict(arrowstyle='->', lw=0.9, color='#1b5e20'),
            fontsize=8.5, fontweight='bold', bbox=bbox_props, zorder=6, ha='center')

# Mín (0, 0): In open region (-0.5, -0.8) pointing up-right to (-0.05, -0.05) - NO intersection!
ax.plot(0, 0, 'o', color='#1b5e20', markersize=5.5, zorder=5)
ax.annotate('Mín (0, 0)', xy=(0, 0), xytext=(-0.5, -0.8),
            arrowprops=dict(arrowstyle='->', lw=0.9, color='#1b5e20'),
            fontsize=8.5, fontweight='bold', bbox=bbox_props, zorder=6, ha='right')

ax.legend(loc='lower right', fontsize=8, framealpha=0.95)
plt.savefig('fig_1b.pdf', bbox_inches='tight')
plt.savefig('fig_1b.png', bbox_inches='tight')
plt.close()

# ==============================================================================
# FIG 2A: f(x) = (x^2 - 3)e^{-x}
# ==============================================================================
fig, ax = plt.subplots(figsize=(5.6, 4.0), dpi=300)
setup_ax(ax, r'2A: $f(x) = (x^2 - 3)e^{-x}$', (-3.2, 7), (-7.2, 5.0))
x = np.linspace(-3, 7, 500)
y = (x**2 - 3) * np.exp(-x)
ax.plot(x, y, '#0d47a1', lw=1.8, zorder=3)
ax.axhline(0, color='#d32f2f', linestyle='--', lw=1.2, label=r'A.H. $y=0$ ($x \to +\infty$)')

# Mín (-1, -2e) ~ (-1, -5.44)
ax.plot(-1, -2*np.e, 'o', color='#1b5e20', markersize=5.5, zorder=5)
ax.annotate('Mín (-1, -2e)', xy=(-1, -2*np.e), xytext=(-1.0, -6.6),
            arrowprops=dict(arrowstyle='->', lw=0.9, color='#1b5e20'),
            fontsize=8.5, fontweight='bold', bbox=bbox_props, zorder=6, ha='center')

# Máx (3, 6/e^3) ~ (3, 0.30)
ax.plot(3, 6*np.exp(-3), 'o', color='#1b5e20', markersize=5.5, zorder=5)
ax.annotate(r'Máx $(3, \frac{6}{e^3})$', xy=(3, 6*np.exp(-3)), xytext=(3.0, 1.8),
            arrowprops=dict(arrowstyle='->', lw=0.9, color='#1b5e20'),
            fontsize=8.5, fontweight='bold', bbox=bbox_props, zorder=6, ha='center')

# Cortes con ejes
sqrt3 = np.sqrt(3)
ax.plot([-sqrt3, sqrt3], [0, 0], 's', color='#e65100', markersize=4.5, zorder=5)
ax.annotate(r'$(-\sqrt{3},0)$', xy=(-sqrt3, 0), xytext=(-2.6, 1.3),
            arrowprops=dict(arrowstyle='->', lw=0.7, color='#e65100'),
            fontsize=7.5, bbox=bbox_props, zorder=6)
ax.annotate(r'$(\sqrt{3},0)$', xy=(sqrt3, 0), xytext=(1.73, -1.6),
            arrowprops=dict(arrowstyle='->', lw=0.7, color='#e65100'),
            fontsize=7.5, bbox=bbox_props, zorder=6, ha='center')

ax.plot(0, -3, 's', color='#e65100', markersize=4.5, zorder=5)
ax.annotate(r'$(0,-3)$', xy=(0, -3), xytext=(1.0, -3.2),
            arrowprops=dict(arrowstyle='->', lw=0.7, color='#e65100'),
            fontsize=7.5, bbox=bbox_props, zorder=6)

# Puntos de Inflexión
xi1 = 2 - np.sqrt(5)
yi1 = (xi1**2 - 3)*np.exp(-xi1)
xi2 = 2 + np.sqrt(5)
yi2 = (xi2**2 - 3)*np.exp(-xi2)
ax.plot([xi1, xi2], [yi1, yi2], '^', color='#6a1b9a', markersize=5.5, zorder=5, label='P. Inflexión')

ax.legend(loc='upper right', fontsize=8, framealpha=0.95)
plt.savefig('fig_2a.pdf', bbox_inches='tight')
plt.savefig('fig_2a.png', bbox_inches='tight')
plt.close()

# ==============================================================================
# FIG 2B: g(x) = (x^2 - 3)e^x
# ==============================================================================
fig, ax = plt.subplots(figsize=(5.6, 4.0), dpi=300)
setup_ax(ax, r'2B: $g(x) = (x^2 - 3)e^{x}$', (-7, 3.2), (-7.2, 5.0))
x = np.linspace(-7, 3, 500)
y = (x**2 - 3) * np.exp(x)
ax.plot(x, y, '#0d47a1', lw=1.8, zorder=3)
ax.axhline(0, color='#d32f2f', linestyle='--', lw=1.2, label=r'A.H. $y=0$ ($x \to -\infty$)')

# Mín (1, -2e) ~ (1, -5.44)
ax.plot(1, -2*np.e, 'o', color='#1b5e20', markersize=5.5, zorder=5)
ax.annotate('Mín (1, -2e)', xy=(1, -2*np.e), xytext=(1.0, -6.6),
            arrowprops=dict(arrowstyle='->', lw=0.9, color='#1b5e20'),
            fontsize=8.5, fontweight='bold', bbox=bbox_props, zorder=6, ha='center')

# Máx (-3, 6/e^3) ~ (-3, 0.30)
ax.plot(-3, 6*np.exp(-3), 'o', color='#1b5e20', markersize=5.5, zorder=5)
ax.annotate(r'Máx $(-3, \frac{6}{e^3})$', xy=(-3, 6*np.exp(-3)), xytext=(-3.0, 1.8),
            arrowprops=dict(arrowstyle='->', lw=0.9, color='#1b5e20'),
            fontsize=8.5, fontweight='bold', bbox=bbox_props, zorder=6, ha='center')

# Cortes con ejes
ax.plot([-sqrt3, sqrt3], [0, 0], 's', color='#e65100', markersize=4.5, zorder=5)
ax.annotate(r'$(-\sqrt{3},0)$', xy=(-sqrt3, 0), xytext=(-1.73, -1.6),
            arrowprops=dict(arrowstyle='->', lw=0.7, color='#e65100'),
            fontsize=7.5, bbox=bbox_props, zorder=6, ha='center')
ax.annotate(r'$(\sqrt{3},0)$', xy=(sqrt3, 0), xytext=(2.6, 1.3),
            arrowprops=dict(arrowstyle='->', lw=0.7, color='#e65100'),
            fontsize=7.5, bbox=bbox_props, zorder=6)

ax.plot(0, -3, 's', color='#e65100', markersize=4.5, zorder=5)
ax.annotate(r'$(0,-3)$', xy=(0, -3), xytext=(-1.0, -3.2),
            arrowprops=dict(arrowstyle='->', lw=0.7, color='#e65100'),
            fontsize=7.5, bbox=bbox_props, zorder=6, ha='right')

# Puntos de Inflexión
xi1_b = -2 - np.sqrt(5)
yi1_b = (xi1_b**2 - 3)*np.exp(xi1_b)
xi2_b = -2 + np.sqrt(5)
yi2_b = (xi2_b**2 - 3)*np.exp(xi2_b)
ax.plot([xi1_b, xi2_b], [yi1_b, yi2_b], '^', color='#6a1b9a', markersize=5.5, zorder=5, label='P. Inflexión')

ax.legend(loc='upper left', fontsize=8, framealpha=0.95)
plt.savefig('fig_2b.pdf', bbox_inches='tight')
plt.savefig('fig_2b.png', bbox_inches='tight')
plt.close()

print('ALL_FIGURES_PERFECT')
