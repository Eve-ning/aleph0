""" This file was deprecated but left as back up. See f247 for the updated one """

from math import pi

import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.OsuMap import OsuMap

# notes: 01:37:742 (97742|2,125moves993|2) -

START_Y = -12
END_Y = 12

START = 97742
MOVE_0 = (100560, 100790, 101018, 101245, 101471, 101697)
MOVE_1 = (104124, 104340, 104556, 104770, 104983, 105195)
MOVE_2 = (107487, 107692, 107896, 108099, 108301, 108503)
MOVE_3 = (110674, 110867, 111059, 111156, 111252, 111348, 111444, 111539)
MOVE_4 = (113698, 113882, 114065, 114248, 114432, 114614)
MOVE_5 = (116577, 116753, 116928, 117103, 117276, 117363)
MOVE_6 = (119326, 119494, 119661, 119827, 119994, 120076)
MOVE_7 = (121953, 122114, 122275, 122434, 122594)

MOVE_8 = (122594, 122673, 122752, 122831, 122910, 123068, 123147, 123226, 123304, 123383,
          123539, 123618, 123696, 123773, 123851, 124007, 124084, 124162, 124239, 124316, 124471,
          124547, 124624, 124701, 124778, 124932, 125008, 125084, 125160, 125236, 125388, 125464,
          125540, 125616, 125692, 125767, 125842, 125918, 125993)

def STILL(from_, to_, CURR_POS, CURR_SCALE):
    return SvOsuMeasureLineEvent(
              firstOffset=from_, lastOffset=to_,
              startX=0, endX=0,
              startY=START_Y, endY=END_Y,
              funcs=[
                  lambda x, i=i, pos=CURR_POS[0], scale=CURR_SCALE[0]:
                  i * pos * scale for i in range(0, 3)
              ])

def SWAP(from_, to_, CURR_POS, CURR_SCALE):
    # this will swap it from 1 to -1, to 1, ...
    CURR_POS[0] *= -1
    CURR_SCALE[0] *= 1.035

    return SvOsuMeasureLineEvent(
              firstOffset=from_, lastOffset=to_,
              startX=0, endX=1,
              startY=START_Y, endY=END_Y,
              funcs=[
                  lambda x, i=i, pos=CURR_POS[0], scale=CURR_SCALE[0]:
                  i * pos * scale * np.sin(x * pi / 2) for i in range(0, 3)
              ])

def NOTES(notes, notBefore, CURR_POS, CURR_SCALE):
    return [SvOsuMeasureLineEvent(
            firstOffset=max(notBefore, n.offset - 1000), lastOffset=n.offset,
            startX=1 if notBefore < n.offset - 1000 else 1 + (n.offset - 1000 - notBefore) / 1000, endX=0,
            startY=START_Y, endY=END_Y,
            funcs=[
                lambda x, n=n, pos=CURR_POS[0], scale=CURR_SCALE[0]:
                (x * scale + (n.column // 3 - (1  if n.column < 1 else 0)) * scale) * pos
                * (-1 if n.column < 1 else 1)

            ]) for n in notes]

def f247(m: OsuMap):
    CURR_POS = [1]
    CURR_SCALE = [1]

    notes = [n for n in m.notes.hits() if 97742 < n.offset <= 125993]

    events = [STILL(START, MOVE_0[0], CURR_POS, CURR_SCALE),
              *NOTES([n for n in notes if START <= n.offset < MOVE_0[0]], 0, CURR_POS, CURR_SCALE),

              *[SWAP(m0, m1, CURR_POS, CURR_SCALE) for m0, m1 in zip(MOVE_0[:-1], MOVE_0[1:])],
              STILL(MOVE_0[-1], MOVE_1[0], CURR_POS, CURR_SCALE),
              *NOTES([n for n in notes if MOVE_0[-1] <= n.offset < MOVE_1[0]], MOVE_0[-1], CURR_POS, CURR_SCALE),

              *[SWAP(m0, m1, CURR_POS, CURR_SCALE) for m0, m1 in zip(MOVE_1[:-1], MOVE_1[1:])],
              STILL(MOVE_1[-1], MOVE_2[0], CURR_POS, CURR_SCALE),
              *NOTES([n for n in notes if MOVE_1[-1] <= n.offset < MOVE_2[0]], MOVE_1[-1], CURR_POS, CURR_SCALE),

              *[SWAP(m0, m1, CURR_POS, CURR_SCALE) for m0, m1 in zip(MOVE_2[:-1], MOVE_2[1:])],
              STILL(MOVE_2[-1], MOVE_3[0], CURR_POS, CURR_SCALE),
              *NOTES([n for n in notes if MOVE_2[-1] <= n.offset < MOVE_3[0]], MOVE_2[-1], CURR_POS, CURR_SCALE),

              *[SWAP(m0, m1, CURR_POS, CURR_SCALE) for m0, m1 in zip(MOVE_3[:-1], MOVE_3[1:])],
              STILL(MOVE_3[-1], MOVE_4[0], CURR_POS, CURR_SCALE),
              *NOTES([n for n in notes if MOVE_3[-1] <= n.offset < MOVE_4[0]], MOVE_3[-1], CURR_POS, CURR_SCALE),

              *[SWAP(m0, m1, CURR_POS, CURR_SCALE) for m0, m1 in zip(MOVE_4[:-1], MOVE_4[1:])],
              STILL(MOVE_4[-1], MOVE_5[0], CURR_POS, CURR_SCALE),
              *NOTES([n for n in notes if MOVE_4[-1] <= n.offset < MOVE_5[0]], MOVE_4[-1], CURR_POS, CURR_SCALE),

              *[SWAP(m0, m1, CURR_POS, CURR_SCALE) for m0, m1 in zip(MOVE_5[:-1], MOVE_5[1:])],
              STILL(MOVE_5[-1], MOVE_6[0], CURR_POS, CURR_SCALE),
              *NOTES([n for n in notes if MOVE_5[-1] <= n.offset < MOVE_6[0]], MOVE_5[-1], CURR_POS, CURR_SCALE),

              *[SWAP(m0, m1, CURR_POS, CURR_SCALE) for m0, m1 in zip(MOVE_6[:-1], MOVE_6[1:])],
              STILL(MOVE_6[-1], MOVE_7[0], CURR_POS, CURR_SCALE),
              *NOTES([n for n in notes if MOVE_6[-1] <= n.offset < MOVE_7[0]], MOVE_6[-1], CURR_POS, CURR_SCALE),

              *[SWAP(m0, m1, CURR_POS, CURR_SCALE) for m0, m1 in zip(MOVE_7[:-1], MOVE_7[1:])],
              *[SWAP(m0, m1, CURR_POS, CURR_SCALE) for m0, m1 in zip(MOVE_8[:-1], MOVE_8[1:])],
    ]

    svs, bpms = svOsuMeasureLineMD(events,
                                   scalingFactor=SCALE,
                                   firstOffset=97742,
                                   lastOffset=MOVE_8[-1],
                                   paddingSize=PADDING,
                                   endBpm=250)

    m.svs.extend(svs)
    m.bpms.extend(bpms)
