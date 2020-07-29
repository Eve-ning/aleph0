from math import pi

import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.OsuMap import OsuMap

# notes: 01:37:742 (97742|2,125moves993|2) -

SHAKES = np.array(
        [130218, 130373, 130528, 130683,
         132741, 132902, 133064, 133226,
         135375, 135544, 135713, 135882,
         138128, 138128, 138304, 138392, 138481, 138570, 138659, 138748, 138837,
         141017, 141109, 141202, 141295, 141388, 141574, 141761,
         144050, 144147, 144245, 144343, 144441, 144637, 144834,
         147249, 147352, 147455, 147558, 147661, 147868, 148076,
         150628, 150737, 150846, 150955, 151064, 151173, 151283, 151392, 151502])

def f325(m: OsuMap):

    # Need to split in 2 because the 1/4 in the mids will be too hard to memorise
    notes = sorted([n for n in m.notes.hits() if 128393 < n.offset <= 138837])
    notes2 = sorted([n for n in m.notes.hits() if 138837 < n.offset <= 167558])

    BASE_SHAKE_AMP = 0.05
    INC_SHAKE_AMP = 0
    SHAKE_WINDOW = 250
    NOTE_DURATION = 2000
    # noinspection PyTypeChecker
    events = [
        *[SvOsuMeasureLineEvent(
            firstOffset=n.offset - NOTE_DURATION - t, lastOffset=n.offset - t,
            startX=n.offset - NOTE_DURATION - t, endX=n.offset - t,
            startY=-0.5 - en / 500 , endY=0.5 + en / 500,
            funcs=[
                lambda x, n=n, t=t:
                # This flips the board if it's < 2
                (-1 if n.column < 2 else 1) *
                (
                    np.piecewise(x,
                                 [(i <= x) & (x < i + SHAKE_WINDOW) for i in SHAKES],
                                 [*[lambda x, i=i, es=es:
                                    (BASE_SHAKE_AMP + es * INC_SHAKE_AMP)
                                    * np.sin((x - i) * pi / (SHAKE_WINDOW - es * 3))
                                    for es, i in enumerate(SHAKES)],
                                  lambda x: 0])
                    + (x - (n.offset - t)) / NOTE_DURATION
                )
            ]) for en, n in enumerate(notes) for t in np.linspace(0, 24, NOTE_THICKNESS)],
        *[SvOsuMeasureLineEvent(
            firstOffset=n.offset - NOTE_DURATION - t, lastOffset=n.offset - t,
            startX=n.offset - NOTE_DURATION - t, endX=n.offset - t,
            startY=-1 - en / 250 , endY=1 + en / 250,
            funcs=[
                lambda x, n=n, t=t:
                # This flips the board if it's < 2
                (-1 if n.column < 2 else 1) *
                (
                    np.piecewise(x,
                                 [(i <= x) & (x < i + SHAKE_WINDOW) for i in SHAKES],
                                 [*[lambda x, i=i, es=es:
                                    (BASE_SHAKE_AMP + es * INC_SHAKE_AMP)
                                    * np.sin((x - i) * pi / (SHAKE_WINDOW - es * 3))
                                    for es, i in enumerate(SHAKES)],
                                  lambda x: 0])
                    + (x - (n.offset - t)) / NOTE_DURATION
                )
            ]) for en, n in enumerate(notes2) if n.column == 0 or n.column == 3
               for t in np.linspace(0, 24, NOTE_THICKNESS)],
        *[SvOsuMeasureLineEvent(
            firstOffset=n.offset - NOTE_DURATION - t, lastOffset=n.offset - t,
            startX=n.offset - NOTE_DURATION - t, endX=n.offset - t,
            startY=-1 - en / 250 , endY=1 + en / 250,
            funcs=[
                lambda x, n=n, t=t:
                # This flips the board if it's < 2
                (-1 if n.column < 2 else 1) *
                (
                    np.piecewise(x,
                                 [(i <= x) & (x < i + SHAKE_WINDOW) for i in SHAKES],
                                 [*[lambda x, i=i, es=es:
                                    (BASE_SHAKE_AMP + es * INC_SHAKE_AMP)
                                    * np.sin((x - i) * pi / (SHAKE_WINDOW - es * 3))
                                    for es, i in enumerate(SHAKES)],
                                  lambda x: 0])
                    - (x - (n.offset + t) + NOTE_DURATION) / NOTE_DURATION
                )
            ]) for en, n in enumerate(notes2) if n.column == 1 or n.column == 2
               for t in np.linspace(0, 24, NOTE_THICKNESS)],
        SvOsuMeasureLineEvent(
            firstOffset=128393, lastOffset=167558,
            startX=0, endX=1,
            startY=0, endY=1,
            funcs=[
                lambda x: 0.5,
            ]),
        *[SvOsuMeasureLineEvent(
            firstOffset=j, lastOffset=169902 - (j - 167558) % 500,
            startX=0.01, endX=20,
            startY=-3, endY=3,
            funcs=[
                *[lambda x, i=i: i / 100 / (x ** 1.7) for i in np.random.randint(-100, 100, RAND_SIZE // 10)],
            ]) for j in np.random.randint(167558, 169902 - 100, RAND_SIZE * 2)],
    ]

    svs, bpms = svOsuMeasureLineMD(events,
                                   scalingFactor=SCALE,
                                   firstOffset=128393,
                                   lastOffset=169902,
                                   paddingSize=PADDING,
                                   endBpm=250)

    m.svs.extend(svs)
    m.bpms.extend(bpms)
