
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

levels = np.arange(6)

triangle_percent = np.array([
    100, 71.1, 49.7, 31.7, 17.4, 7.1
])
triangle_count = np.rint(
    7291 * triangle_percent / 100
).astype(int)

bones = np.array([67, 67, 67, 52, 31, 31])
batches = np.array([10, 10, 10, 7, 7, 2])

bones_pct = bones / 67 * 100
batches_pct = batches / 10 * 100

cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']
c_tri = cycle[0]
c_bone = cycle[1]
c_batch = cycle[2]

fig, ax = plt.subplots(figsize=(13.2, 7.2))
fig.subplots_adjust(
    left=0.08,
    right=0.97,
    top=0.88,
    bottom=0.16
)

ax.step(
    levels, triangle_percent,
    where='mid', linewidth=2.6, color=c_tri
)
ax.plot(
    levels, triangle_percent,
    linestyle='None', marker='o',
    markersize=7, color=c_tri
)

ax.step(
    levels, bones_pct,
    where='mid', linewidth=2.5, color=c_bone
)
ax.plot(
    levels, bones_pct,
    linestyle='None', marker='s',
    markersize=7, color=c_bone
)

ax.step(
    levels, batches_pct,
    where='mid', linewidth=2.5, color=c_batch
)
ax.plot(
    levels, batches_pct,
    linestyle='None', marker='D',
    markersize=6, color=c_batch
)

reference_pct = 100 * 538 / 7291

ax.axhline(
    reference_pct,
    color='gray',
    ls=':',
    lw=1.4,
    alpha=0.65
)
ax.text(
    0.12, reference_pct + 3.0,
    '1998 G-Man: 538 triangles (no LoD)',
    color='dimgray',
    fontsize=9
)

bbox_kw = dict(
    boxstyle='round,pad=0.15',
    facecolor='white',
    edgecolor='none',
    alpha=0.85
)

tri_offsets = [
    (8, -22), (0, -20), (0, -20),
    (0, -20), (0, -20), (0, 12)
]

bone_offsets = [
    (10, 12), (10, 12), (10, 12),
    (10, 10), (10, 10), (10, 10)
]

batch_offsets = [
    (-12, -18), (-12, -18), (-12, -18),
    (-10, -18), (-10, -18), (-10, 12)
]

for (x, y, val), off in zip(
    zip(levels, triangle_percent, triangle_count),
    tri_offsets
):
    ax.annotate(
        f'{val:,}',
        (x, y),
        xytext=off,
        textcoords='offset points',
        ha='center',
        va='center',
        fontsize=10,
        color=c_tri,
        bbox=bbox_kw
    )

for (x, y, val), off in zip(
    zip(levels, bones_pct, bones),
    bone_offsets
):
    ax.annotate(
        f'{val}',
        (x, y),
        xytext=off,
        textcoords='offset points',
        ha='left',
        va='center',
        fontsize=10,
        color=c_bone,
        bbox=bbox_kw
    )

for (x, y, val), off in zip(
    zip(levels, batches_pct, batches),
    batch_offsets
):
    ax.annotate(
        f'{val}',
        (x, y),
        xytext=off,
        textcoords='offset points',
        ha='right',
        va='center',
        fontsize=10,
        color=c_batch,
        bbox=bbox_kw
    )

ax.set_title(
    'G-Man (2004): complexity across levels of detail',
    fontsize=17,
    weight='semibold',
    loc='center',
    pad=17
)

ax.set_ylabel(
    'Remaining relative to LoD 0 (%)',
    fontsize=11
)

ax.set_xlabel(
    'Level of detail (higher = simpler model)',
    fontsize=11
)

ax.set_xticks(
    levels,
    [
        'LoD 0', 'LoD 1', 'LoD 2',
        'LoD 3', 'LoD 4', 'LoD 5\n(shadow)'
    ]
)

ax.set_xlim(-0.25, 5.25)
ax.set_ylim(0, 111)

ax.grid(axis='y', alpha=0.23)
ax.spines[['top', 'right']].set_visible(False)

handles = [
    Line2D(
        [0], [0],
        color=c_tri, marker='o',
        linewidth=2.6, markersize=7,
        label='Triangles'
    ),
    Line2D(
        [0], [0],
        color=c_bone, marker='s',
        linewidth=2.5, markersize=7,
        label='HW bones'
    ),
    Line2D(
        [0], [0],
        color=c_batch, marker='D',
        linewidth=2.5, markersize=6,
        label='Batches'
    )
]

ax.legend(
    handles=handles,
    loc='upper right',
    frameon=False,
    fontsize=10
)

plt.savefig(
    'gman_lod_graph.png',
    dpi=190,
    bbox_inches='tight'
)

plt.show()
