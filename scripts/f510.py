from math import pi

import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.OsuMap import OsuMap

SHAKE_AMP = 0.5
SHAKES = 25
COS_CURVE = 0.5

# 02:56:382 (176382|1,176622|0,191982|1) -

def f510(m: OsuMap):

    events = [
        SvOsuMeasureLineEvent(
            firstOffset=201582, lastOffset=202342,
            startX=0, endX=1,
            startY=-1, endY=1,
            funcs=[
                lambda x, r=r:
                (SHAKE_AMP * np.sin(SHAKES * x * pi) + r) / (x + 1)
                * np.cos(x * pi / 2) ** COS_CURVE
                for r in np.linspace(-1, 1, RAND_SIZE)
            ]
        ),
        # 03:22:342 (202342|2,202382|2,202422|2,202542|2) -

        SvOsuMeasureLineEvent(
            firstOffset=202342, lastOffset=202382,
            startX=0, endX=1,
            startY=-1, endY=1,
            funcs=[
                lambda x, r=r:
                r * np.sin(x * pi / 2) ** 0.5
                for r in np.linspace(-1, 1, 4)
            ]
        ),
        SvOsuMeasureLineEvent(
            firstOffset=202382, lastOffset=202422,
            startX=0, endX=1,
            startY=-1, endY=1,
            funcs=[
                lambda x, r=r:
                -x * r
                for r in np.linspace(0, 1, RAND_SIZE)
            ]
        ),
        SvOsuMeasureLineEvent(
            firstOffset=202422, lastOffset=202542,
            startX=0, endX=1,
            startY=-1, endY=1,
            funcs=[
                lambda x, r=r:
                -x * r
                for r in np.linspace(0, 1, RAND_SIZE)
            ]
        ),
        SvOsuMeasureLineEvent(
            firstOffset=202542, lastOffset=202782,
            startX=0, endX=1,
            startY=-3, endY=3,
            funcs=[
                lambda x: 1 - x,
                lambda x: x - 1
            ]
        ),

    ]

    svs, bpms = svOsuMeasureLineMD(events,
                                   scalingFactor=SCALE,
                                   firstOffset=201582,
                                   lastOffset=202542,
                                   paddingSize=PADDING,
                                   endBpm=250)

    m.svs.extend(svs)
    m.bpms.extend(bpms)
