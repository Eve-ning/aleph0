from math import pi

import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.OsuMap import OsuMap

# notes: 01:37:742 (97742|2,125moves993|2) -

SHAKES = np.array(
        [100560, 100790, 101018, 101245,
         104124, 104340, 104556, 104770,
         107487, 107692, 107896, 108099,
         110674, 110867, 111059, 111156, 111252, 111348,
         113698, 113882, 114065, 114248,
         116577, 116753, 116928, 117103,
         119326, 119494, 119661, 119827,
         121953, 122114, 122275, 122434,
         122594, 122673, 122752, 122831, 123068,
         123147, 123226, 123304, 123383, 123539,
         123618, 123696, 123773, 123851, 124007,
         124084, 124162, 124239, 124316, 124471,
         124547, 124624, 124701, 124778, 124932,
         125008, 125084, 125160, 125236, 125388,
         125464, 125540, 125616, 125692, 125767, 125842, 125918, 125993])

def f247(m: OsuMap):

    notes = sorted([n for n in m.notes.hits() if 97742 < n.offset <= 125993])

    BASE_SHAKE_AMP = 0.010
    INC_SHAKE_AMP = 0.0010
    SHAKE_WINDOW = 250
    NOTE_DURATION = 2000
    # noinspection PyTypeChecker
    events = [
        *[SvOsuMeasureLineEvent(
            firstOffset=n.offset - NOTE_DURATION - t, lastOffset=n.offset - t,
            startX=n.offset - NOTE_DURATION - t, endX=n.offset - t,
            startY=-1 + en / 500 , endY=1 - en / 500,
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
            ]) for en, n in enumerate(notes) for t in np.linspace(0, 24, NOTE_THICKNESS)]
    ]

    svs, bpms = svOsuMeasureLineMD(events,
                                   scalingFactor=SCALE,
                                   firstOffset=97742,
                                   lastOffset=125993,
                                   paddingSize=PADDING,
                                   endBpm=250)

    m.svs.extend(svs)
    m.bpms.extend(bpms)
