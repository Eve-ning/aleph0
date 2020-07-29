import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
# 15817 16297 16777 17257 17737
from reamber.osu.OsuMap import OsuMap


def f039(m: OsuMap):
    events = [*[SvOsuMeasureLineEvent(
              firstOffset=15337 + i * (17737 - 15337), lastOffset=17737,
              startX=0, endX=1,
              startY=0, endY=1,
              funcs=[
                  lambda x, i=i: i * 0.20
              ]) for i in np.linspace(0, 1, 30)],
              *[SvOsuMeasureLineEvent(
              firstOffset=15817 + i * (17737 - 15817), lastOffset=17737,
              startX=0, endX=1,
              startY=0, endY=1,
              funcs=[
                  lambda x, i=i: i * 0.20 + 0.20
              ]) for i in np.linspace(0, 1, 25)],
              *[SvOsuMeasureLineEvent(
              firstOffset=16297 + i * (17737 - 16297), lastOffset=17737,
              startX=0, endX=1,
              startY=0, endY=1,
              funcs=[
                  lambda x, i=i: i * 0.20 + 0.40
              ]) for i in np.linspace(0, 1, 20)],
              *[SvOsuMeasureLineEvent(
              firstOffset=16777 + i * (17737 - 16777), lastOffset=17737,
              startX=0, endX=1,
              startY=0, endY=1,
              funcs=[
                  lambda x, i=i: i * 0.20 + 0.60
              ]) for i in np.linspace(0, 1, 15)],
              *[SvOsuMeasureLineEvent(
              firstOffset=17257 + i * (17737 - 17257), lastOffset=17737,
              startX=0, endX=1,
              startY=0, endY=1,
              funcs=[
                  lambda x, i=i: i * 0.20 + 0.80
              ]) for i in np.linspace(0, 1, 10)],

              ]
    f = svOsuMeasureLineMD(events,
                           scalingFactor=SCALE,
                           firstOffset=15337,
                           lastOffset=17737,
                           paddingSize=PADDING,
                           endBpm=250,
                           metronome=999)

    m.svs.extend(f[0])
    m.bpms.extend(f[1])
