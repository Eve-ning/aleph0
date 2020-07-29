from math import pi

import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.lists.notes.OsuHitList import OsuHitList

# 00:28:537 (28537|3,28777|2,29017|2,29257|2,29497|1,29737|2,29977|3) -

SHUTTER_WAIT = 200
from reamber.osu.OsuMap import OsuMap

def f083(m: OsuMap):
    notes = [h for h in  m.notes.hits() if 33000 < h.offset < 55200]
    notes2 = [h for h in  m.notes.hits() if 55900 < h.offset < 63900]
    sweeps = OsuHitList.readEditorString("00:36:457 (36457|3,40297|3,44137|3,47977|3,51817|3,59497|3)").offsets()

    events = [SvOsuMeasureLineEvent(
              firstOffset=32857, lastOffset=55177,
              startX=0, endX=1,
              startY=0, endY=1,
              funcs=[
                  lambda x: 0.25,
                  lambda x: 0.50,
                  lambda x: 0.75,
                  lambda x: 1,
              ]),
             *[SvOsuMeasureLineEvent(
              firstOffset=n.offset - 500, lastOffset=n.offset,
              startX=1, endX=0,
              startY=0, endY=4,
              funcs=[
                  lambda x, n=n, t=t: x - t + n.column for t in np.linspace(0, 0.05, NOTE_THICKNESS)
              ]) for n in notes],

              *[SvOsuMeasureLineEvent(
              firstOffset=55177, lastOffset=55777,
              startX=0, endX=1,
              startY=0, endY=1,
              funcs=[
                  lambda x, i=i: 0    + x + np.random.rand() % 0.2,
                  lambda x, i=i: 0.25 + x + np.random.rand() % 0.2,
                  lambda x, i=i: 0.50 + x + np.random.rand() % 0.2,
                  lambda x, i=i: 0.75 + x + np.random.rand() % 0.2,

                  lambda x, i=i: 0    - x + np.random.rand() % 0.2,
                  lambda x, i=i: 0.25 - x + np.random.rand() % 0.2,
                  lambda x, i=i: 0.50 - x + np.random.rand() % 0.2,
                  lambda x, i=i: 0.75 - x + np.random.rand() % 0.2,
              ]) for i in range(0, RAND_SIZE // 3)],
              SvOsuMeasureLineEvent(
              firstOffset=55777, lastOffset=63817,
              startX=0, endX=8,
              startY=0, endY=1,
              funcs=[
                  lambda x: 0.25,
                  lambda x: 0.50,
                  lambda x: 0.75,
                  lambda x: 1,
              ]),
             *[SvOsuMeasureLineEvent(
              firstOffset=n.offset - 500, lastOffset=n.offset,
              startX=0, endX=1,
              startY=0, endY=4,
              funcs=[
                  lambda x, n=n, t=t: x - t + n.column
                  for t in np.linspace(0, 0.05, NOTE_THICKNESS)
              ]) for n in notes2],
              # These are the sweeps
              *[SvOsuMeasureLineEvent(
              firstOffset=s - 240, lastOffset=s + 240,
              startX=-1, endX=1,
              startY=0, endY=1,
              funcs=[
                  lambda x, t=t: (1 / np.random.rand() ** 2 * np.abs(np.sin((x - t) * pi)) + (x - t) ** 2) % 1
                  for t in np.linspace(0, 0.25, RAND_SIZE // 2)
              ]) for s in sweeps]

    ]
    svs, bpms = svOsuMeasureLineMD(events,
                                   scalingFactor=SCALE,
                                   firstOffset=32857,
                                   lastOffset=63817,
                                   paddingSize=PADDING,
                                   endBpm=250,
                                   metronome=999)

    m.svs.extend(svs)
    m.bpms.extend(bpms)
