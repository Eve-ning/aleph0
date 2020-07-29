from math import pi

import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.OsuMap import OsuMap


def f028(m: OsuMap):
    events = [SvOsuMeasureLineEvent(
              firstOffset=11017, lastOffset=12937,
              startX=0, endX=1,
              startY=0, endY=1,
              funcs=[
                  lambda x: 0.5
              ]),
              SvOsuMeasureLineEvent(
              firstOffset=12667, lastOffset=12757,
              startX=0, endX=pi,
              startY=0, endY=1,
              funcs=[
                  lambda x: np.abs(np.sin(x)) / 4 + 0.5
              ]),
              SvOsuMeasureLineEvent(
              firstOffset=12757, lastOffset=12887,
              startX=0, endX=pi,
              startY=0, endY=1,
              funcs=[
                  lambda x: -np.abs(np.sin(x)) / 4 + 0.5
              ]),
              *[SvOsuMeasureLineEvent(
              firstOffset=12757 + i, lastOffset=15337,
              startX=-5, endX=0.5,
              startY=0, endY=1,
              funcs=[
                  lambda x: np.e ** x + 0.5
              ]) for i in np.linspace(0, 15337 - 12757, 50)],
              *[SvOsuMeasureLineEvent(
              firstOffset=12757 + i, lastOffset=15337,
              startX=-5, endX=0.5,
              startY=0, endY=1,
              funcs=[
                  lambda x: - np.e ** x + 0.5
              ]) for i in np.linspace(0, 15337 - 12757, 50)]


              ]
    f = svOsuMeasureLineMD(events,
                           scalingFactor=SCALE,
                           firstOffset=11017,
                           lastOffset=15337,
                           paddingSize=PADDING,
                           endBpm=250)

    m.svs.extend(f[0])
    m.bpms.extend(f[1])
