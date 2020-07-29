from math import pi

import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent

# 01:03:817 (63817|2,70674|2,77531|2,84388|1,91245|2) -

SWAY_MAG = 0.05
WAIT = 1000
from reamber.osu.OsuMap import OsuMap

def f162(m: OsuMap):
    hits0 = [h for h in m.notes.hits() if 63817 <= h.offset < 70674]
    hits1 = [h for h in m.notes.hits() if 70674 <= h.offset < 77531]
    holds2 = [h for h in m.notes.holds() if 77531 <= h.offset < 84388]
    holds3 = [h for h in m.notes.holds() if 84388 <= h.offset < 90388]
    hits4 = [h for h in m.notes.hits() if 90388 <= h.offset <= 91245]

    events = [SvOsuMeasureLineEvent(
              firstOffset=63817, lastOffset=70674,
              startX=0, endX=1,
              startY=0, endY=1,
              funcs=[
                  lambda x: 0    + SWAY_MAG * np.sin(x * pi * 4),
                  lambda x: 0.25 + SWAY_MAG * np.sin(x * pi * 4),
                  lambda x: 0.50 + SWAY_MAG * np.sin(x * pi * 4),
                  lambda x: 0.75 + SWAY_MAG * np.sin(x * pi * 4),
                  lambda x: 1    + SWAY_MAG * np.sin(x * pi * 4),
              ]),
             *[SvOsuMeasureLineEvent(
              firstOffset=h.offset - WAIT, lastOffset=h.offset,
              startX=1, endX=0,
              startY=0, endY=1,
              funcs=[
                  lambda x, h=h, i=i:
                        x * 0.25 + i + h.column * 0.25
                        + SWAY_MAG * np.sin((h.offset - 63817) / (70674 - 63817) * pi * 4)
                        for i in np.linspace(0, 0.02, int(1 + e / 2))
              ]) for e, h in enumerate(hits0)],


              SvOsuMeasureLineEvent(
              firstOffset=70674, lastOffset=77531,
              startX=0, endX=1,
              startY=0, endY=1,
              funcs=[
                  lambda x: 0    + SWAY_MAG * np.sin(x * pi * 4),
                  lambda x: 0.25 + SWAY_MAG * np.sin(x * pi * 4),
                  lambda x: 0.50 + SWAY_MAG * np.sin(x * pi * 4),
                  lambda x: 0.75 + SWAY_MAG * np.sin(x * pi * 4),
                  lambda x: 1    + SWAY_MAG * np.sin(x * pi * 4),
              ]),
             *[SvOsuMeasureLineEvent(
              firstOffset=h.offset - WAIT, lastOffset=h.offset,
              startX=0, endX=1,
              startY=0, endY=1,
              funcs=[
                  lambda x, h=h, i=i:
                        x * 0.25 - i + h.column * 0.25
                        + SWAY_MAG * np.sin((h.offset - 70674) / (77531 - 70674) * pi * 4)
                        for i in np.linspace(0, 0.02, max(1, int(10 - e / 2)))
              ]) for e, h in enumerate(hits1)],


              SvOsuMeasureLineEvent(
              firstOffset=77531, lastOffset=84388,
              startX=0, endX=1,
              startY=0, endY=1,
              funcs=[
                  lambda x: 0    + SWAY_MAG * np.sin(x * pi * 4),
                  lambda x: 0.25 + SWAY_MAG * np.sin(x * pi * 4),
                  lambda x: 0.50 + SWAY_MAG * np.sin(x * pi * 4),
                  lambda x: 0.75 + SWAY_MAG * np.sin(x * pi * 4),
                  lambda x: 1    + SWAY_MAG * np.sin(x * pi * 4)
              ]),
             *[SvOsuMeasureLineEvent(
              firstOffset=h.offset - WAIT + i, lastOffset=h.offset + i,
              startX=1, endX=0,
              startY=0, endY=1,
              funcs=[
                  lambda x, h=h:
                        x * 0.25 + h.column * 0.25
                        + SWAY_MAG * np.sin((h.offset - 77531) / (84388 - 77531) * pi * 4)
              ]) for h in holds2 for i in np.linspace(0, h.length, NOTE_THICKNESS)],


              SvOsuMeasureLineEvent(
              firstOffset=84388, lastOffset=90388,
              startX=0, endX=1,
              startY=0, endY=1,
              funcs=[
                  lambda x: 0    + SWAY_MAG * np.sin(x * pi * 3.5),
                  lambda x: 0.25 + SWAY_MAG * np.sin(x * pi * 3.5),
                  lambda x: 0.50 + SWAY_MAG * np.sin(x * pi * 3.5),
                  lambda x: 0.75 + SWAY_MAG * np.sin(x * pi * 3.5),
                  lambda x: 1    + SWAY_MAG * np.sin(x * pi * 3.5),
              ]),
             *[SvOsuMeasureLineEvent(
              firstOffset=h.offset - WAIT + i, lastOffset=h.offset + i,
              startX=0, endX=1,
              startY=0, endY=1,
              funcs=[
                  lambda x, h=h:
                        x * 0.25 + h.column * 0.25
                        + SWAY_MAG * np.sin((h.offset - 84388) / (91245 - 84388) * pi * 4)
              ]) for h in holds3 for i in np.linspace(0, h.length, NOTE_THICKNESS)],

            SvOsuMeasureLineEvent(
                firstOffset=90388, lastOffset=91245,
                startX=0, endX=1,
                startY=0, endY=1,
                funcs=[
                    lambda x: 0    ,
                    lambda x: 0.25 ,
                    lambda x: 0.50 ,
                    lambda x: 0.75 ,
                    lambda x: 1 ,
                ]),
            *[SvOsuMeasureLineEvent(
                firstOffset=h.offset - WAIT / 2, lastOffset=h.offset,
                startX=1, endX=0,
                startY=0, endY=1,
                funcs=[
                    lambda x, h=h, i=i:
                    x * 0.25 - i + h.column * 0.25
                    for i in np.linspace(0, 0.02, NOTE_THICKNESS)
                ]) for h in hits4],

    ]

    svs, bpms = svOsuMeasureLineMD(events,
                                   scalingFactor=SCALE,
                                   firstOffset=63817,
                                   lastOffset=91245,
                                   paddingSize=PADDING,
                                   endBpm=250)

    m.svs.extend(svs)
    m.bpms.extend(bpms)
