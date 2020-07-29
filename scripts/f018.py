import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.OsuMap import OsuMap


def f018(m: OsuMap):
    events = [*[SvOsuMeasureLineEvent(
              firstOffset=7297 + i, lastOffset=7297 + 500 + i,
              startX=0.01, endX=40,
              startY=-10, endY=10,
              funcs=[
                  lambda x: np.log(x)
              ]) for i in np.linspace(0, 500, 5)],
              *[SvOsuMeasureLineEvent(
              firstOffset=7417 + i, lastOffset=7417 + 500 + i,
              startX=0.01, endX=40,
              startY=-10, endY=10,
              funcs=[
                  lambda x: np.log(x)
              ]) for i in np.linspace(0, 500, 5)],
              *[SvOsuMeasureLineEvent(
              firstOffset=7447, lastOffset=7657,
              startX=0, endX=1,
              startY=0, endY=1,
              funcs=[
                  lambda x, i=i: i * x for i in np.linspace(0, 1, 100)
              ])]
              ]

    f = svOsuMeasureLineMD(events,
                           scalingFactor=SCALE,
                           firstOffset=7297,
                           lastOffset=7657,
                           paddingSize=PADDING,
                           endBpm=250)

    m.svs.extend(f[0])
    m.bpms.extend(f[1])
