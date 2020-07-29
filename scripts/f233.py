import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.OsuMap import OsuMap


# 01:32:822 (92822|2,92882|2,92942|2,93062|2) -

def f233(m: OsuMap):

    events = [SvOsuMeasureLineEvent(
              firstOffset=92102, lastOffset=92822,
              startX=-2, endX=2,
              startY=-6, endY=6,
              funcs=[
                  lambda x, i=i: np.abs(x) + np.sin(5 * x) * x ** 2 * i for i in range(-5, 6)
              ]),
              SvOsuMeasureLineEvent(
              firstOffset=92822, lastOffset=92822 + 10,
              startX=0, endX=1,
              startY=0.2, endY=0.8,
              funcs=[
                  *[lambda x, i=i: i for i in np.linspace(0, 1, RAND_SIZE * 2)],
              ]),
              SvOsuMeasureLineEvent(
              firstOffset=92822 + 10, lastOffset=92882,
              startX=0, endX=0.2,
              startY=0.2, endY=0.8,
              funcs=[
              ]),
              SvOsuMeasureLineEvent(
              firstOffset=92882, lastOffset=92882 + 10,
              startX=0.01, endX=0.05,
              startY=0.2, endY=0.8,
              funcs=[
                  *[lambda x, i=i: i for i in np.linspace(0, 1, RAND_SIZE // 3)],
              ]),
              SvOsuMeasureLineEvent(
              firstOffset=92882 + 10, lastOffset=92942,
              startX=0, endX=0.2,
              startY=0.2, endY=0.8,
              funcs=[
              ]),
              SvOsuMeasureLineEvent(
              firstOffset=92942, lastOffset=93062,
              startX=0, endX=0.05,
              startY=0.2, endY=0.8,
              funcs=[
                  *[lambda x, i=i: i + x for i in np.linspace(0, 1, RAND_SIZE // 2)],
              ]),
              SvOsuMeasureLineEvent(
              firstOffset=93062, lastOffset=93302,
              startX=0, endX=0.05,
              startY=0.2, endY=0.8,
              funcs=[
                  *[lambda x, i=i: i - x for i in np.linspace(0, 1, RAND_SIZE)],
              ]),
              SvOsuMeasureLineEvent(
              firstOffset=93302, lastOffset=93482,
              startX=0, endX=0.05,
              startY=0, endY=1,
              funcs=[

              ]),
              SvOsuMeasureLineEvent(
              firstOffset=93482, lastOffset=93902,
              startX=0, endX=0.2,
              startY=0.2, endY=0.8,
              funcs=[
                  *[lambda x, i=i: i - x for i in np.linspace(0, 1, RAND_SIZE // 3)],
                  *[lambda x, i=i: i + x for i in np.linspace(0, 1, RAND_SIZE // 2)],
              ]),
              *[SvOsuMeasureLineEvent(
              firstOffset=j, lastOffset=97442 - (j - 93902) % 500,
              startX=0.01, endX=20,
              startY=-3, endY=3,
              funcs=[
                  *[lambda x, i=i: i / 100 / (x ** 1.7) for i in np.random.randint(-100, 100, RAND_SIZE // 10)],
              ]) for j in np.random.randint(93902, 97442 - 100, RAND_SIZE * 2)],
              SvOsuMeasureLineEvent(
              firstOffset=97502, lastOffset=97742,
              startX=0, endX=1,
              startY=0, endY=1,
              funcs=[
                  lambda x: 0.5
              ]),
    ]

    svs, bpms = svOsuMeasureLineMD(events,
                                   scalingFactor=SCALE,
                                   firstOffset=92102,
                                   lastOffset=97742,
                                   paddingSize=PADDING,
                                   endBpm=250)

    m.svs.extend(svs)
    m.bpms.extend(bpms)
