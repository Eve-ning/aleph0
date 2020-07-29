from math import pi

import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.OsuBpm import OsuBpm, MIN_BPM
from reamber.osu.OsuMap import OsuMap

COS_POWER = 2

def f950(m: OsuMap):
    FIRST = 375444
    LAST = 383124

    events = [
        *[SvOsuMeasureLineEvent(
        firstOffset=o, lastOffset=LAST,
        startX=0, endX=1,
        startY=-1, endY=1,
        funcs=[
            lambda x: np.cos(x * pi / 2) ** COS_POWER
        ]) for o in np.linspace(FIRST, LAST, 75)],

        *   [SvOsuMeasureLineEvent(
        firstOffset=o, lastOffset=LAST,
        startX=0, endX=1,
        startY=-1, endY=1,
        funcs=[
            lambda x: -np.cos(x * pi / 2) ** COS_POWER
        ]) for o in np.linspace(FIRST, LAST, 75)]
    ]

    for e, (first, last) in enumerate(zip(np.linspace(FIRST, LAST, 10)[:-1], np.linspace(FIRST, LAST, 10)[1:])):
        svs, bpms = svOsuMeasureLineMD(events=events,
                                       scalingFactor=SCALE,
                                       firstOffset=first,
                                       lastOffset=last,
                                       paddingSize=PADDING * e,
                                       endBpm=MIN_BPM)
        m.svs.extend(svs)
        m.bpms.extend(bpms[:-1])

    m.bpms.append(OsuBpm(LAST, 250))
