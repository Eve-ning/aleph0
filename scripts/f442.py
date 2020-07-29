from math import pi

import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.OsuMap import OsuMap

SIN_CURVE = 0.2  # Curvature of sine < 0.5 for fast init, > 0.5 for fast out never negative
POW_CURVE = 0.4  # Curvature of x axis power modifier

rand = np.linspace(-1, 1, RAND_SIZE)

def f442(m: OsuMap):

    # noinspection PyTypeChecker
    events = [
        [SvOsuMeasureLineEvent(
            firstOffset=174702, lastOffset=175362,
            startX=0, endX=1,
            startY=-1, endY=1,
            funcs=[
                lambda x, r=r: r * np.sin(x * pi / 2) ** SIN_CURVE
            ]),
        SvOsuMeasureLineEvent(
            firstOffset=175362, lastOffset=176142,
            startX=0, endX=1,
            startY=-1, endY=1,
            funcs=[
                lambda x, r=r: r * np.cos(x ** POW_CURVE * pi)
            ]),
        SvOsuMeasureLineEvent(
            firstOffset=176142, lastOffset=176382,
            startX=0, endX=1,
            startY=-1, endY=1,
            funcs=[
                lambda x, r=r: -r * (1 - np.sin(x * pi / 2) ** SIN_CURVE)
            ])] for r in rand]

    svs, bpms = svOsuMeasureLineMD([i for j in events for i in j],
                                   scalingFactor=SCALE,
                                   firstOffset=174702,
                                   lastOffset=176382,
                                   paddingSize=PADDING,
                                   endBpm=250)

    m.svs.extend(svs)
    m.bpms.extend(bpms)
