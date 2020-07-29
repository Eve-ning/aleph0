import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.OsuMap import OsuMap


def f017(m: OsuMap):
    events = [SvOsuMeasureLineEvent(
              firstOffset=6697, lastOffset=7177,
              startX=5, endX=60,
              startY=-25, endY=25,
              funcs=[
                  *[lambda x, i=i: np.sin(5 * (x + i)) * (x + i) ** 2 / 100 for i in np.linspace(0, 20, 10)]
              ])]

    f = svOsuMeasureLineMD(events,
                           scalingFactor=SCALE,
                           firstOffset=6697,
                           lastOffset=7177,
                           paddingSize=PADDING,
                           endBpm=250)

    m.svs.extend(f[0])
    m.bpms.extend(f[1])
