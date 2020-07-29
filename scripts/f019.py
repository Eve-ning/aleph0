import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.OsuMap import OsuMap


def f019(m: OsuMap):
    events = [*[SvOsuMeasureLineEvent(
              firstOffset=7657, lastOffset=8317,
              startX=1 + i, endX=0 + i,
              startY=-1, endY=0,
              funcs=[
                  lambda x: -x
              ]) for i in np.linspace(0, 1, 100)],
              *[SvOsuMeasureLineEvent(
              firstOffset=8317, lastOffset=8407,
              startX=1 + i, endX=0 + i,
              startY=-1, endY=0,
              funcs=[
                  lambda x: -x
              ]) for i in np.linspace(0, 1, 100)],
              *[SvOsuMeasureLineEvent(
              firstOffset=8407, lastOffset=8557,
              startX=1 + i, endX=0 + i,
              startY=-1, endY=0,
              funcs=[
                  lambda x: -x
              ]) for i in np.linspace(0, 1, 100)]

              ]

    f = svOsuMeasureLineMD(events,
                           scalingFactor=SCALE,
                           firstOffset=7657,
                           lastOffset=8557,
                           paddingSize=PADDING,
                           endBpm=250)

    m.svs.extend(f[0])
    m.bpms.extend(f[1])
