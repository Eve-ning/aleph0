import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.OsuBpm import OsuBpm, MAX_BPM
from reamber.osu.OsuMap import OsuMap
from reamber.osu.lists.notes.OsuHitList import OsuHitList

offsets0 = OsuHitList.readEditorString("06:00:084 (360084|3,361044|3,361524|3,362004|3) - ").offsets()
offsets1 = OsuHitList.readEditorString("06:02:964 (362964|3,363444|3,363924|3,364884|3,365364|3,365844|3,366324|3,"
                                       "366804|3) - ").offsets()
offsets2 = OsuHitList.readEditorString("06:07:764 (367764|3,368724|3,369204|3,369684|2) - ").offsets()
offsets3 = OsuHitList.readEditorString("06:10:644 (370644|3,371604|3,373524|3,374484|3) - ").offsets()

DELAY = 120

np.random.seed(0)

def EVENT(funcs, startX, endX, startY, endY,offsetsFrom, offsetsTo):
    events = [
        (
            SvOsuMeasureLineEvent(
                firstOffset=r0, lastOffset=r1,
                startX=startX, endX=endX,
                startY=startY, endY=endY,
                funcs=funcs),
            SvOsuMeasureLineEvent(
                firstOffset=o0, lastOffset=o1,
                startX=startX, endX=endX,
                startY=startY, endY=endY,
                funcs=funcs)
        ) for o0, o1 in zip(offsetsFrom, offsetsTo)
          for r0, r1 in zip(np.arange(o0, o1, DELAY)[:-1], np.arange(o0, o1, DELAY)[1:])
    ]
    return [i for j in events for i in j]

def f919(m: OsuMap):

    def f0(smallStart, smallEnd, smallSize, bigStart, bigEnd, bigSize):
        return [lambda x, s=s, b=b: x + s + b
              for s in np.linspace(smallStart, smallEnd, smallSize)
              for b in np.linspace(bigStart, bigEnd, bigSize)]

    f00 = f0(0, 0.01, 1, 0, 0.8, 8)
    f01 = f0(0, 0.05, 3, 0.2, 1, 5)
    f02 = f0(0, 0.05, 10, 0, 1, 5)

    events0 = [*EVENT(f00, 0, 0.05, 0, 1, offsets0[:-1], offsets0[1:]),
               *EVENT(f01, 0, 0.05, 0, 1, offsets0[1:-1], offsets0[2:]),
               *EVENT(f02, 0, 0.05, 0, 1, offsets0[2:-1], offsets0[3:])]

    f10 = f0(0, np.random.rand() % 0.05, np.random.randint(1, 4), np.random.rand() % 0.1, np.random.rand() % 0.1 + 0.9, np.random.randint(3, 7))
    f11 = f0(0, np.random.rand() % 0.05, np.random.randint(1, 4), np.random.rand() % 0.1, np.random.rand() % 0.1 + 0.9, np.random.randint(3, 7))
    f12 = f0(0, np.random.rand() % 0.05, np.random.randint(1, 4), np.random.rand() % 0.1, np.random.rand() % 0.1 + 0.9, np.random.randint(3, 7))
    f13 = f0(0, np.random.rand() % 0.05, np.random.randint(1, 4), np.random.rand() % 0.1, np.random.rand() % 0.1 + 0.9, np.random.randint(3, 7))
    f14 = f0(0, np.random.rand() % 0.05, np.random.randint(1, 4), np.random.rand() % 0.1, np.random.rand() % 0.1 + 0.9, np.random.randint(3, 7))
    f15 = f0(0, np.random.rand() % 0.05, np.random.randint(1, 4), np.random.rand() % 0.1, np.random.rand() % 0.1 + 0.9, np.random.randint(3, 7))
    f16 = f0(0, np.random.rand() % 0.05, np.random.randint(1, 4), np.random.rand() % 0.1, np.random.rand() % 0.1 + 0.9, np.random.randint(3, 7))

    events1 = [*EVENT(f10, -0.05, +0.05, 0, 1, offsets1[0:-1], offsets1[1:]),
               *EVENT(f11, +0.05, -0.05, 0, 1, offsets1[1:-1], offsets1[2:]),
               *EVENT(f12, -0.05, +0.05, 0, 1, offsets1[2:-1], offsets1[3:]),
               *EVENT(f13, +0.05, -0.05, 0, 1, offsets1[3:-1], offsets1[4:]),
               *EVENT(f14, -0.05, +0.05, 0, 1, offsets1[4:-1], offsets1[5:]),
               *EVENT(f15, +0.05, -0.05, 0, 1, offsets1[5:-1], offsets1[6:]),
               *EVENT(f16, -0.05, +0.05, 0, 1, offsets1[6:-1], offsets1[7:])]

    f20 = f0(0, np.random.rand() % 0.08 + 0.05, np.random.randint(2, 7), np.random.rand() % 0.1, np.random.rand() % 0.1 + 0.9, np.random.randint(5, 10))
    f21 = f0(0, np.random.rand() % 0.08 + 0.05, np.random.randint(2, 7), np.random.rand() % 0.1, np.random.rand() % 0.1 + 0.9, np.random.randint(5, 10))
    f22 = f0(0, np.random.rand() % 0.08 + 0.05, np.random.randint(2, 7), np.random.rand() % 0.1, np.random.rand() % 0.1 + 0.9, np.random.randint(5, 10))

    events2 = [*EVENT(f20, -0.05, +0.05, 0, 1, offsets2[0:-1], offsets2[1:]),
               *EVENT(f21, +0.05, -0.05, 0, 1, offsets2[1:-1], offsets2[2:]),
               *EVENT(f22, -0.05, +0.05, 0, 1, offsets2[2:-1], offsets2[3:])]

    f30 = f0(0, np.random.rand() % 0.1 + 0.1, np.random.randint(3, 8), 0, 1, np.random.randint(5, 8))
    f31 = f0(0, np.random.rand() % 0.1 + 0.1, np.random.randint(3, 8), 0, 1, np.random.randint(5, 8))
    f32 = f0(0, np.random.rand() % 0.1 + 0.1, np.random.randint(3, 8), 0, 1, np.random.randint(5, 8))

    events3 = [*EVENT(f30, -0.05, +0.05, 0, 1, offsets3[0:-1], offsets3[1:]),
               *EVENT(f31, +0.05, -0.05, 0, 1, offsets3[1:-1], offsets3[2:]),
               *EVENT(f32, -0.05, +0.05, 0, 1, offsets3[2:-1], offsets3[3:])]

    svs, bpms = svOsuMeasureLineMD([*events0,
                                    *events1,
                                    *events2,
                                    *events3],
                                   scalingFactor=SCALE,
                                   firstOffset=offsets0[0],
                                   lastOffset=offsets3[-1],
                                   paddingSize=PADDING,
                                   endBpm=250)

    m.svs.extend(svs)
    m.bpms.extend(bpms)

    m.bpms.append(OsuBpm(offsets0[-1], REF_BPM // 3))
    m.bpms.append(OsuBpm(offsets1[-1], REF_BPM // 3))
    m.bpms.append(OsuBpm(offsets2[-1], REF_BPM // 3))
    m.bpms.append(OsuBpm(offsets3[-1], REF_BPM // 3))

    m.bpms.append(OsuBpm(offsets0[0] - 1, MAX_BPM))
    m.bpms.append(OsuBpm(offsets1[0] - 1, MAX_BPM))
    m.bpms.append(OsuBpm(offsets2[0] - 1, MAX_BPM))
    m.bpms.append(OsuBpm(offsets3[0] - 1, MAX_BPM))
