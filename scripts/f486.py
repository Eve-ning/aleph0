from math import pi

import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.OsuMap import OsuMap

MOVE_DURATION = 120
WHEEL_SLOTS = 10
COS_POWER = 0.5

# 02:56:382 (176382|1,176622|0,191982|1) -

def f486(m: OsuMap):
    notes = sorted(
        [*[h for h in m.notes.hits() if 191982 <= h.offset <= 198462],
         *[h for h in m.notes.holds() if 191982 <= h.offset <= 198462]],
        key=lambda x: x.offset)

    # These are the offsets that trigger a move
    offsets = [n.offset for n in notes] + [201582] * WHEEL_SLOTS * 2

    # These are the wheel columns
    cols    = [n.column + 1 for n in notes] + [0] * WHEEL_SLOTS * 2

    events = [
        # We'll set up the wheel here
        # Depending on the column, we need to adjust it accordingly.

        # The method is to look at WHEEL items at once, then show a slowed image or move

        # MOVE
        *[SvOsuMeasureLineEvent(
            firstOffset=o, lastOffset=offsets[i + 1],
            startX=0, endX=1,
            startY=0.2, endY=WHEEL_SLOTS - 1,
            funcs=[
                *[lambda x, i=i, c=c, cp=cp, cv=cv, t=t:
                  c / (cv + 1)                             # The relative spot to the cv
                  + cp + 1                                 # Correct placement of wheel slot
                  + (np.cos(x * pi / 2) ** COS_POWER - 1)  # Cosine easing
                  - t                                      # Add thickness
                  + 1 / (cv + 1)                           # Make all in center
                  # For each i, we get the col value
                  for cp, cv in enumerate(cols[i + 1: i + WHEEL_SLOTS])
                  # For each col value, we loop through it to make each column line
                  for c in range(cv)
                  # For each col line, we make it thicker by repeating
                  for t in np.linspace(-0.025, 0.025, int(NOTE_THICKNESS * 1.5))],

                # Add note hit positions
                *[lambda x, w=w:
                  1 + (np.cos(x * pi / 2) ** COS_POWER - 1) + w
                  for w in range(WHEEL_SLOTS)]

            ]) for i, o in enumerate(offsets[:-WHEEL_SLOTS])]
        ]

    svs, bpms = svOsuMeasureLineMD(events,
                                   scalingFactor=SCALE,
                                   firstOffset=191982,
                                   lastOffset=201582,
                                   paddingSize=PADDING,
                                   endBpm=250)

    m.svs.extend(svs)
    m.bpms.extend(bpms)
