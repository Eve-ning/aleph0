from math import pi

import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.OsuMap import OsuMap

SIN_CURVE = 0.1
DURATION = 1500
THICKNESS = 0.05
CAP = 1 - THICKNESS

# 03:22:782 () - 

offsets = [202782, 203022, 203262, 203502, 203742, 203982, 204222, 204462, 204702, 204942, 205182]
positions = np.linspace(0, 1, len(offsets)) % CAP


def f513(m: OsuMap):

    events = [
        # P: Position
        # P_: Individual line position
        # OD: Offset with delay
        *[SvOsuMeasureLineEvent(
            firstOffset=o, lastOffset=205182,
            startX=0, endX=1,
            startY=0, endY=1,
            funcs=[
                lambda x, p_=p_: np.sin(x * pi / 2) ** SIN_CURVE * p_
                for p_ in np.linspace(p, p + THICKNESS, RAND_SIZE // 3)
            ]
        ) for o, p in zip(offsets, positions)
        ],

        *[SvOsuMeasureLineEvent(
            firstOffset=205182, lastOffset=205662,
            startX=0, endX=1,
            startY=0, endY=1,
            funcs=[
                lambda x, p_=p_:
                (- np.sin(x * pi / 2) ** (SIN_CURVE * 3) + 1) * p_
                + 0.5 * np.sin(x * pi / 2) ** (SIN_CURVE * 3)      # This offsets the close to 0.5 with sin easing
                for p_ in np.linspace(p, p + THICKNESS, RAND_SIZE // 3)
            ]
        ) for o, p in zip(offsets, positions)
        ]
    ]


    svs, bpms = svOsuMeasureLineMD(events,
                                   scalingFactor=SCALE,
                                   firstOffset=202782,
                                   lastOffset=205662,
                                   paddingSize=PADDING,
                                   endBpm=250)

    m.svs.extend(svs)
    m.bpms.extend(bpms)
