import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.OsuMap import OsuMap

# 00:28:537 (28537|3,28777|2,29017|2,29257|2,29497|1,29737|2,29977|3) -

SHUTTER_WAIT = 200

def f072(m: OsuMap):
    events = [SvOsuMeasureLineEvent(
              firstOffset=28537, lastOffset=28777,
              startX=0.001, endX=4,
              startY=0, endY=4,
              funcs=[
                  lambda x: np.sqrt(x)
              ]),
              *[SvOsuMeasureLineEvent(
              firstOffset=28777, lastOffset=29017,
              startX=0, endX=1,
              startY=0, endY=1,
              funcs=[
                  lambda x, i=i: i + x / 100
              ]) for i in np.linspace(0, 1, 50)],
              *[SvOsuMeasureLineEvent(
              firstOffset=29017, lastOffset=29257,
              startX=0, endX=1,
              startY=-5, endY=5,
              funcs=[
                  lambda x, i=i: 1 / (x + 1)
              ]) for i in np.linspace(0, 1, 15)],
              *[SvOsuMeasureLineEvent(
              firstOffset=29017, lastOffset=29257,
              startX=0, endX=1,
              startY=-5, endY=5,
              funcs=[
                  lambda x, i=i: -1 / (x + 1)
              ]) for i in np.linspace(0, 1, 15)],
              *[SvOsuMeasureLineEvent(
              firstOffset=29257 + i * SHUTTER_WAIT, lastOffset=31177 - (1 - i) * SHUTTER_WAIT * 8,
              startX=0, endX=1,
              startY=0, endY=4,
              funcs=[
                  lambda x, i=i: 1 - i
              ]) for i in np.linspace(0, 1, 15)],
              *[SvOsuMeasureLineEvent(
              firstOffset=29497 + i * SHUTTER_WAIT, lastOffset=31177 - (1 - i) * SHUTTER_WAIT * 6,
              startX=0, endX=1,
              startY=0, endY=4,
              funcs=[
                  lambda x, i=i: 1 - i + 1
              ]) for i in np.linspace(0, 1, 15)],
              *[SvOsuMeasureLineEvent(
              firstOffset=29737 + i * SHUTTER_WAIT, lastOffset=31177 - (1 - i) * SHUTTER_WAIT * 4,
              startX=0, endX=1,
              startY=0, endY=4,
              funcs=[
                  lambda x, i=i: 1 - i + 2
              ]) for i in np.linspace(0, 1, 15)],
              *[SvOsuMeasureLineEvent(
              firstOffset=29977 + i * SHUTTER_WAIT, lastOffset=31177 - (1 - i) * SHUTTER_WAIT * 2,
              startX=0, endX=1,
              startY=0, endY=4,
              funcs=[
                  lambda x, i=i: 1 - i + 3
              ]) for i in np.linspace(0, 1, 15)],

              # 00:31:177 (31177|0,31417|1,31657|2,31897|3,32137|3) -
              *[SvOsuMeasureLineEvent(
              firstOffset=31177 + i * SHUTTER_WAIT, lastOffset=32857 - (1 - i) * SHUTTER_WAIT * 4,
              startX=0, endX=1,
              startY=0, endY=4,
              funcs=[
                  lambda x, i=i: 1 - i
              ]) for i in np.linspace(0, 1, 15)],
              *[SvOsuMeasureLineEvent(
              firstOffset=31417 + i * SHUTTER_WAIT * 2, lastOffset=32857 - (1 - i) * SHUTTER_WAIT * 3,
              startX=0, endX=1,
              startY=0, endY=4,
              funcs=[
                  lambda x, i=i: 1 - i + 1
              ]) for i in np.linspace(0, 1, 20)],
              *[SvOsuMeasureLineEvent(
              firstOffset=31657 + i * SHUTTER_WAIT * 3, lastOffset=32857 - (1 - i) * SHUTTER_WAIT * 2,
              startX=0, endX=1,
              startY=0, endY=4,
              funcs=[
                  lambda x, i=i: 1 - i + 2
              ]) for i in np.linspace(0, 1, 35)],
              *[SvOsuMeasureLineEvent(
              firstOffset=31897 + i * (32857 - 31897), lastOffset=32857 - (1 - i) * SHUTTER_WAIT * 2,
              startX=0, endX=1,
              startY=0, endY=4,
              funcs=[
                  lambda x, i=i: 1 - i + 3
              ]) for i in np.linspace(0, 1, 50)]

    ]
    svs, bpms = svOsuMeasureLineMD(events,
                                   scalingFactor=SCALE,
                                   firstOffset=28537,
                                   lastOffset=33097,
                                   paddingSize=PADDING,
                                   endBpm=250)

    m.svs.extend(svs)
    m.bpms.extend(bpms)
