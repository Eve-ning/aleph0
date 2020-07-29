import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.OsuMap import OsuMap


def f024(m: OsuMap):
    events = [*[SvOsuMeasureLineEvent(
              firstOffset=i, lastOffset=9337,
              startX=1, endX=0,
              startY=-1, endY=0,
              funcs=[
                  lambda x, j=j: -x + j for j in np.linspace(0, 1, 15)
              ]) for i in np.linspace(8857, 9337, 8)],

              *[SvOsuMeasureLineEvent(
              firstOffset=9337, lastOffset=11017,
              startX=i, endX=i + 1,
              startY=-1, endY=1,
              funcs=[
                  lambda x: -x + 2
              ]) for i in np.linspace(0, 1, 50)],

              *[SvOsuMeasureLineEvent(
              firstOffset=9337, lastOffset=11017,
              startX=i, endX=i + 1,
              startY=-1, endY=1,
              funcs=[
                  lambda x: x - 2
              ]) for i in np.linspace(0, 1, 50)],
              ]
    f = svOsuMeasureLineMD(events,
                           scalingFactor=SCALE,
                           firstOffset=8857,
                           lastOffset=11017,
                           paddingSize=PADDING,
                           endBpm=250)

    m.svs.extend(f[0])
    m.bpms.extend(f[1])
