from math import pi

import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.OsuMap import OsuMap
from reamber.osu.lists.notes.OsuHitList import OsuHitList

# 03:22:782 () -

offsets0 = OsuHitList.readEditorString("03:56:382 (236382|2,236622|2,236862|2,237102|2,237342|2,237582|2,237822|2,"
                                       "238062|2,238302|2) - ").offsets()
offsets1 = OsuHitList.readEditorString("03:58:302 (238302|2,238542|2,238782|2,239022|2,239262|2,239502|2,239742|2,"
                                       "239982|2,240222|2) - ").offsets()

rands = - np.random.rand(len(offsets0) - 1)

COS_CURVE = 0.15

def f598(m: OsuMap):
    events = [
        *[SvOsuMeasureLineEvent(
            firstOffset=o0, lastOffset=o1,
            startX=-1, endX=1,
            startY=-1, endY=1,
            funcs=[
                lambda x, r=r, s=s:
                    s * r * np.cos(x * pi / 2) ** COS_CURVE,
            ]
        ) for r, o0, o1 in zip(rands, offsets0[:-1], offsets1[:-1])
          for s in np.linspace(0.8, 1, RAND_SIZE // 4)],
        SvOsuMeasureLineEvent(
            firstOffset=236382, lastOffset=240222,
            startX=-1, endX=1,
            startY=-1, endY=1,
            funcs=[
                lambda x, n=n:
                    n * np.cos(x * pi / 2) ** 0.45
                for n in np.linspace(0, 0.8, 50)
            ]
        )
    ]

    svs, bpms = svOsuMeasureLineMD(events,
                                   scalingFactor=SCALE,
                                   firstOffset=offsets0[0],
                                   lastOffset=offsets1[-1],
                                   paddingSize=PADDING,
                                   endBpm=250)

    m.svs.extend(svs)
    m.bpms.extend(bpms)

