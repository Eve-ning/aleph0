import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.OsuMap import OsuMap

LINES = 20

amps, curves = np.random.rand(LINES), np.random.rand(LINES) + 3

def f319(m: OsuMap):

    events = [*[SvOsuMeasureLineEvent(
              firstOffset=125993, lastOffset=128093,
              startX=-10, endX=0,
              startY=-1, endY=1,
              funcs=[
                  lambda x, a=a, c=c:  a * (-1 / (x + 3 * c) + 1 / c + 1) * (-1 / (x + 11) + 1),
                  lambda x, a=a, c=c: -a * (-1 / (x + 3 * c) + 1 / c + 1) * (-1 / (x + 11) + 1)
              ]) for a, c in zip(amps, curves)],
              *[SvOsuMeasureLineEvent(
                  firstOffset=128093, lastOffset=128243,
                  startX=0, endX=2,
                  startY=-1, endY=1,
                  funcs=[
                      lambda x, a=a, c=c:  a / np.power(x + 1, 4),
                      lambda x, a=a, c=c: -a / np.power(x + 1, 4)
              ]) for a, c in zip(amps, curves)],
              SvOsuMeasureLineEvent(
              firstOffset=128243, lastOffset=128393,
              startX=0, endX=1,
              startY=0, endY=1,
              funcs=[
                  lambda x: 0.5
              ]),
    ]

    svs, bpms = svOsuMeasureLineMD(events,
                                   scalingFactor=SCALE,
                                   firstOffset=125993,
                                   lastOffset=128393,
                                   paddingSize=PADDING,
                                   endBpm=250)

    m.svs.extend(svs)
    m.bpms.extend(bpms)
