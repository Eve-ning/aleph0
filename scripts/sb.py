""" This generates the SB at the end! """

import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent

from reamber.osu.OsuMap import OsuMap
from math import pi

RED = "red.jpg"
BLUE = "blue.jpg"
GREEN = "green.jpg"

START = 375444
END = 383124 - 100
DURATION = END - START
EVENT_DURATION = 25

np.random.seed(0)

def EVENT(img, start, duration, opacity, positionX, positionY, scale):
    end = start + duration

    return f"Sprite,Overlay,Centre,\"{img}\",320,240\n"\
           f" V,0,{int(start)},{int(end)},{3.5},{scale}\n"\
           f" F,0,{int(start)},{int(end)},{opacity},{opacity}\n"\
           f" M,0,{int(start)},{int(end)},{positionX},{positionY}\n"

def sb(osbPath: str):
    with open(osbPath, "w") as f:
        f.write("[Events]\n"
                "//Background and Video events\n"
                "//Storyboard Layer 0 (Background)\n"
                "//Storyboard Layer 1 (Fail)\n"
                "//Storyboard Layer 2 (Pass)\n"
                "//Storyboard Layer 3 (Foreground)\n"
                "//Storyboard Layer 4 (Overlay)\n"
                ""
                "Sprite,Overlay,Centre,\"black.jpg\",320,240\n"
                " S,0,0,5000,3.158545\n"
                " F,1,1000,5000,1,0\n"
                "Sprite,Overlay,Centre,\"black.jpg\",320,240\n"
                " M,0,375444,,300.8,235.3454\n"
                " S,0,375444,,3.158545\n"
                " F,0,375444,383124,0,1\n"
                " F,0,383124,392000,1\n"
                "Sprite,Overlay,Centre,\"creditTexture.jpg\",320,240\n"
                " M,1,383124,392000,320,230,310,270\n"
                " F,0,383124,392000,0.8,0.6\n"
                " S,0,385049,,0.2087273\n"
                "Sprite,Overlay,Centre,\"leaf.png\",320,240\n"
                " S,0,383124,,0.1\n"
                " M,0,383124,392000,320,205\n"
                "Sprite,Overlay,Centre,\"eve.png\",320,240\n"
                " F,0,383124,,1\n"
                " S,0,383124,,0.18\n"
                " M,0,383124,392000,320,275\n"
                "Sprite,Overlay,Centre,\"credits.png\",320,240\n"
                " F,0,383124,,0.7\n"
                " S,0,383124,,0.4\n"
                " M,0,383124,392000,321,330\n")

        for r in np.sin(np.random.rand(50) * pi / 2) ** 0.25:
            start = DURATION * r + START
            duration = EVENT_DURATION / r

            f.write(EVENT(np.random.choice([RED, GREEN, BLUE]), start, duration,
                          np.random.rand() ** 2 * 1 / r,
                          2 * (np.random.rand() ** 0.2 - 0.5) * 500,
                          2 * (np.random.rand() - 0.5) * 500,
                          np.random.rand() ** 2 * 4
                          ))

        f.write(
                "//Storyboard Sound Samples\n")


# Redacted Path
osbPath = f"LeaF - Aleph-0 (extended ver)/LeaF - Aleph-0 (extended ver.) (Evening).osb"

sb(osbPath)