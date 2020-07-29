import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.OsuMap import OsuMap

BEATS = [172302, 172377, 172452, 172527, 172602, 172677, 172752, 172827, 172902, 172977, 173052, 173127,
         173202, 173277, 173352, 173427, 173502, 173577, 173652, 173727, 173802, 173877, 173952, 174027,
         174102, 174177, 174252, 174327, 174402, 174477, 174552, 174627, 174702]

RETRACT_DURATION = 150

amps, curves = np.random.rand(len(BEATS)), np.random.rand(len(BEATS)) + 3
randAdd = (np.random.rand(RAND_SIZE // 15) % 0.4 - 0.2)

def f430(m: OsuMap):

    # noinspection PyTypeChecker
    events = [
        *[SvOsuMeasureLineEvent(
            firstOffset=d, lastOffset=172302 - RETRACT_DURATION,
            startX=-10, endX=0,
            startY=-1, endY=1,
            funcs=[
                lambda x, a=a, c=c, i=i: i + a * (-1 / (x + 3 * c) + 1 / c + 1) * (-1 / (x + 11) + 1),
                lambda x, a=a, c=c, i=i: i + -a * (-1 / (x + 3 * c) + 1 / c + 1) * (-1 / (x + 11) + 1)
            ]) for a, c, d in
            zip(amps, curves,
                np.random.randint(169902, 172302 - 1250, len(BEATS))) for i in randAdd],
        *[SvOsuMeasureLineEvent(
        firstOffset=172302 - RETRACT_DURATION, lastOffset=b - RETRACT_DURATION,
        startX=0, endX=0,
        startY=-1, endY=1,
        funcs=[
            lambda x, a=a, c=c, i=i: i + a * (-1 / (x + 3 * c) + 1 / c + 1) * (-1 / (x + 11) + 1),
            lambda x, a=a, c=c, i=i: i + -a * (-1 / (x + 3 * c) + 1 / c + 1) * (-1 / (x + 11) + 1)
        ]) for a, c, b in zip(amps, curves, BEATS) for i in randAdd],
        *[SvOsuMeasureLineEvent(
        firstOffset=b - RETRACT_DURATION, lastOffset=b,
        startX=0, endX=-10,
        startY=-1, endY=1,
        funcs=[
            lambda x, a=a, c=c, i=i: i + a * (-1 / (x + 3 * c) + 1 / c + 1) * (-1 / (x + 11) + 1),
            lambda x, a=a, c=c, i=i: i + -a * (-1 / (x + 3 * c) + 1 / c + 1) * (-1 / (x + 11) + 1)
        ]) for a, c, b in zip(amps, curves, BEATS) for i in randAdd]

    ]

    svs, bpms = svOsuMeasureLineMD(events,
                                   scalingFactor=SCALE,
                                   firstOffset=169902,
                                   lastOffset=174802,
                                   paddingSize=PADDING,
                                   endBpm=250)

    m.svs.extend(svs)
    m.bpms.extend(bpms)
