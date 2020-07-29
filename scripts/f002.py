import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.OsuMap import OsuMap


def f002(m: OsuMap):
    events = [SvOsuMeasureLineEvent(
              firstOffset=937 + i, lastOffset=6637 + i,
              startX=2.5, endX=35,
              startY=-0.5, endY=0.5,
              funcs=[
                  lambda x:   1 / np.log(x ** 2) - .13,
                  lambda x: - 1 / np.log(x ** 2) + .13
              ]) for i in np.linspace(0, 6637 - 937, 10)]

    f = svOsuMeasureLineMD(events,
                           scalingFactor=SCALE,
                           firstOffset=937,
                           lastOffset=6637,
                           paddingSize=PADDING,
                           endBpm=250)

    m.svs.extend(f[0])
    m.bpms.extend(f[1])

