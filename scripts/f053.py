from math import pi

import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.OsuBpm import OsuBpm, MAX_BPM
from reamber.osu.OsuMap import OsuMap
from reamber.osu.OsuSv import OsuSv


def f053(m: OsuMap):
    events = [SvOsuMeasureLineEvent(
              firstOffset=20857, lastOffset=21097,
              startX=0, endX=pi,
              startY=0, endY=2,
              funcs=[
                  lambda x: np.sin(x)
              ])]
    svs, bpms = svOsuMeasureLineMD(events,
                                   scalingFactor=SCALE,
                                   firstOffset=20857,
                                   lastOffset=21097,
                                   paddingSize=PADDING,
                                   endBpm=MAX_BPM)
    bpms.extend([OsuBpm(21337, 0.001),
                 OsuBpm(21576, 54750),
                 OsuBpm(21577, 250, metronome=999)])
    svs.extend([OsuSv(17737, multiplier=0.6),
                OsuSv(18457, multiplier=0.6),
                OsuSv(21577, multiplier=0.6)])

    m.svs.extend(svs)
    m.bpms.extend(bpms)
