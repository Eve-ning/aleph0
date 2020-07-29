from math import pi

import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.generators.svOsuMeasureLineMD import svOsuMeasureLineMD, SvOsuMeasureLineEvent
from reamber.osu.OsuBpm import OsuBpm
from reamber.osu.OsuMap import OsuMap
from reamber.osu.lists.notes.OsuHitList import OsuHitList

# 03:22:782 () -

offsets0 = OsuHitList.readEditorString("04:00:222 (240222|2,240650|2,241079|2,241507|2,241936|2,242364|2,242793|2,"
                                       "243222|2,243650|2,244079|2,244507|2,244936|2,245364|2,245793|2,246222|2,"
                                       "246650|2,247079|2) - ").offsets()
offsets1 = OsuHitList.readEditorString("04:07:079 (247079|2,247507|2,247936|2,248364|2,248793|2,249222|2,249650|2,"
                                       "250079|2,250507|2,250936|2,251364|2,251793|2,252222|2,252650|2,253079|2,"
                                       "253507|2,253936|2) - ").offsets()

offsets2 = OsuHitList.readEditorString("04:13:936 (253936|2,254364|2,254793|2,255222|2,255650|2,256079|2,256507|2,"
                                       "256936|2,257364|2,257793|2,258222|2,258650|2,259079|2,259507|2,259936|2,"
                                       "260364|2,260793|2) - ").offsets()
offsets3 = OsuHitList.readEditorString("04:21:222 (260793|2,261222|2,261650|2,262079|2,262507|2,262936|2,263364|2,"
                                       "263793|2,264222|2,264650|2,265079|2,265507|2,265936|2,266364|2,266793|2,"
                                       "267222|2,267650|2) - ").offsets()

offsets4 = OsuHitList.readEditorString("04:27:650 (267650|1,268079|1,268507|1,268936|1,269364|1,269793|1,270222|1,"
                                       "270650|1,271079|1,271507|1,271936|1,272364|1,272793|1,273222|1,273650|1,"
                                       "274079|1,274507|1) - ").offsets()
offsets5 = OsuHitList.readEditorString("04:34:507 (274507|3,274936|3,275364|3,275793|3,276222|3,276650|3,277079|3,"
                                       "277507|3,277936|3,278364|3,278793|3,279222|3,279650|3,280079|3,280507|3,"
                                       "280936|3,281364|3) - ").offsets()

rands = [np.random.rand(len(offsets0) - 2) for i in range(6)]

piano = OsuHitList.readEditorString("04:13:936 (253936|0,254150|0,254364|0,254579|0,254793|0,255007|0,255222|0,"
                                    "255436|0,255650|0,255864|0,256079|0,256293|0,256507|0,256722|0,256936|0,"
                                    "257150|0,257364|0,257579|0,257793|0,258007|0,258222|0,258436|0,258650|0,"
                                    "258864|0,259079|0,259293|0,259507|0,259722|0,259936|0,260150|0,260364|0,"
                                    "260579|0,260793|0,261007|0,261222|0,261436|0,261650|0,261864|0,262079|0,"
                                    "262293|0,262507|0,262722|0,262936|0,263150|0,263364|0,263579|0,263793|0,"
                                    "264007|0,264222|0,264436|0,264650|0,264864|0,265079|0,265293|0,265507|0,"
                                    "265722|0,265936|0,266150|0,266364|0,266579|0,266793|0,267007|0,267222|0,"
                                    "267436|0,267650|0,267757|0,267864|0,267972|0,268079|0,268186|0,268293|0,"
                                    "268400|0,268507|0,268614|0,268722|0,268829|0,268936|0,269043|0,269150|0,"
                                    "269257|0,269364|0,269472|0,269579|0,269686|0,269793|0,269900|0,270007|0,"
                                    "270114|0,270222|0,270329|0,270436|0,270543|0,270650|0,270757|0,270864|0,"
                                    "270972|0,271079|0,271186|0,271293|0,271400|0,271507|0,271614|0,271722|0,"
                                    "271829|0,271936|0,272043|0,272150|0,272257|0,272364|0,272472|0,272579|0,"
                                    "272686|0,272793|0,272900|0,273007|0,273114|0,273222|0,273329|0,273436|0,"
                                    "273543|0,273650|0,273757|0,273864|0,273972|0,274079|0,274186|0,274293|0,"
                                    "274400|0,274507|0,274614|0,274722|0,274829|0,274936|0,275043|0,275150|0,"
                                    "275257|0,275364|0,275472|0,275579|0,275686|0,275793|0,275900|0,276007|0,"
                                    "276114|0,276222|0,276329|0,276436|0,276543|0,276650|0,276757|0,276864|0,"
                                    "276972|0,277079|0,277186|0,277293|0,277400|0,277507|0,277614|0,277722|0,"
                                    "277829|0,277936|0,278043|0,278150|0,278257|0,278364|0,278472|0,278579|0,"
                                    "278686|0,278793|0,278900|0,279007|0,279114|0,279222|0,279329|0,279436|0,"
                                    "279543|0,279650|0,279757|0,279864|0,279972|0,280079|0,280186|0,280293|0,"
                                    "280400|0,280507|0,280614|0,280722|0,280829|0,280936|0,281043|0,281150|0,"
                                    "281257|0,281364|0) - ").offsets()
pianoRands = (np.random.rand(len(piano)) - 0.5) * 2

COS_CURVE = 0.15
SIN_CURVE = 0.3
DAMP = 0.7
EXPLOSION_LINES = 10 
EXPLOSION_RANGE = 0.15

def f608(m: OsuMap):
    events = [

        # [0]------------------

        *[SvOsuMeasureLineEvent(
            firstOffset=offsets0[0], lastOffset=o,
            startX=-1, endX=0,
            startY=-1, endY=1,
            funcs=[
                lambda x, r=r, t=t:
                    (
                        r * (np.cos(x * pi / 2) ** COS_CURVE *
                             np.sin(x * pi / 2)) +
                        r * (x + 1)
                    ) *
                    (
                        - np.sin(x * pi) + DAMP
                    ) + t
                for t in np.linspace(-0.01, 0.01, int(NOTE_THICKNESS * 2.5))
            ]
        ) for r, o in zip(rands[0], offsets0[1:-1])],
        *[SvOsuMeasureLineEvent(
            firstOffset=o, lastOffset=o + 1000,
            startX=0, endX=1,
            startY=-1, endY=1,
            funcs=[
                lambda x, r=r, exp=exp: r * DAMP + exp * np.sin(x * pi) ** SIN_CURVE
                for exp in np.linspace(-EXPLOSION_RANGE, EXPLOSION_RANGE, EXPLOSION_LINES)
            ]
        ) for r, o in zip(rands[0], offsets0[1:-1])],

        # [1]------------------

        SvOsuMeasureLineEvent(
            firstOffset=offsets0[-3], lastOffset=offsets0[-1],
            startX=-1, endX=1,
            startY=1, endY=-1,
            funcs=[
                lambda x, n=n:
                n * np.cos(x * pi / 2) ** 0.45
                for n in np.linspace(0, 0.8, 50)
            ]
        ),

        *[SvOsuMeasureLineEvent(
            firstOffset=offsets1[0], lastOffset=o,
            startX=-1, endX=0,
            startY=1, endY=-1,
            funcs=[
                lambda x, r=r, t=t:
                    (
                        r * (np.cos(x * pi / 2) ** COS_CURVE *
                             np.sin(x * pi / 2)) +
                        r * (x + 1)
                    ) *
                    (
                        - np.sin(x * pi) + DAMP
                    ) + t
                for t in np.linspace(-0.01, 0.01, int(NOTE_THICKNESS * 2.5))
            ]
        ) for r, o in zip(rands[1], offsets1[1:-1])],
        *[SvOsuMeasureLineEvent(
            firstOffset=o, lastOffset=o + 1000,
            startX=0, endX=1,
            startY=1, endY=-1,
            funcs=[
                lambda x, r=r, exp=exp: r * DAMP + exp * np.sin(x * pi) ** SIN_CURVE
                for exp in np.linspace(-EXPLOSION_RANGE, EXPLOSION_RANGE, EXPLOSION_LINES)
            ]
        ) for r, o in zip(rands[1], offsets1[1:-1])],

        # [2]------------------

        SvOsuMeasureLineEvent(
            firstOffset=offsets1[-3], lastOffset=offsets1[-1],
            startX=-1, endX=1,
            startY=-1, endY=1,
            funcs=[
                lambda x, n=n:
                n * np.cos(x * pi / 2) ** 0.45
                for n in np.linspace(0, 0.8, 50)
            ]
        ),

        *[SvOsuMeasureLineEvent(
            firstOffset=offsets2[0], lastOffset=o,
            startX=-1, endX=0,
            startY=-1, endY=1,
            funcs=[
                lambda x, r=r, t=t:
                    (
                        r * (np.cos(x * pi / 2) ** COS_CURVE *
                             np.sin(x * pi / 2)) +
                        r * (x + 1)
                    ) *
                    (
                        - np.sin(x * pi) + DAMP
                    ) + t
                for t in np.linspace(-0.01, 0.01, int(NOTE_THICKNESS * 2.5))
            ]
        ) for r, o in zip(rands[2], offsets2[1:-1])],
        *[SvOsuMeasureLineEvent(
            firstOffset=o, lastOffset=o + 1000,
            startX=0, endX=1,
            startY=-1, endY=1,
            funcs=[
                lambda x, r=r, exp=exp: r * DAMP + exp * np.sin(x * pi) ** SIN_CURVE
                for exp in np.linspace(-EXPLOSION_RANGE, EXPLOSION_RANGE, EXPLOSION_LINES)
            ]
        ) for r, o in zip(rands[2], offsets2[1:-1])],

        # [3]------------------

        SvOsuMeasureLineEvent(
            firstOffset=offsets2[-3], lastOffset=offsets2[-1],
            startX=-1, endX=1,
            startY=1, endY=-1,
            funcs=[
                lambda x, n=n:
                n * np.cos(x * pi / 2) ** 0.45
                for n in np.linspace(0, 0.8, 50)
            ]
        ),

        *[SvOsuMeasureLineEvent(
            firstOffset=offsets3[0], lastOffset=o,
            startX=-1, endX=0,
            startY=1, endY=-1,
            funcs=[
                lambda x, r=r, t=t:
                    (
                        r * (np.cos(x * pi / 2) ** COS_CURVE *
                             np.sin(x * pi / 2)) +
                        r * (x + 1)
                    ) *
                    (
                        - np.sin(x * pi) + DAMP
                    ) + t
                for t in np.linspace(-0.01, 0.01, int(NOTE_THICKNESS * 2.5))
            ]
        ) for r, o in zip(rands[3], offsets3[1:-1])],
        *[SvOsuMeasureLineEvent(
            firstOffset=o, lastOffset=o + 1000,
            startX=0, endX=1,
            startY=1, endY=-1,
            funcs=[
                lambda x, r=r, exp=exp: r * DAMP + exp * np.sin(x * pi) ** SIN_CURVE
                for exp in np.linspace(-EXPLOSION_RANGE, EXPLOSION_RANGE, EXPLOSION_LINES)
            ]
        ) for r, o in zip(rands[3], offsets3[1:-1])],

        # [4]------------------

        SvOsuMeasureLineEvent(
            firstOffset=offsets3[-3], lastOffset=offsets3[-1],
            startX=-1, endX=1,
            startY=-1, endY=1,
            funcs=[
                lambda x, n=n:
                n * np.cos(x * pi / 2) ** 0.45
                for n in np.linspace(0, 0.8, 50)
            ]
        ),

        *[SvOsuMeasureLineEvent(
            firstOffset=offsets4[0], lastOffset=o,
            startX=-1, endX=0,
            startY=-1, endY=1,
            funcs=[
                lambda x, r=r, t=t:
                    (
                        r * (np.cos(x * pi / 2) ** COS_CURVE *
                             np.sin(x * pi / 2)) +
                        r * (x + 1)
                    ) *
                    (
                        - np.sin(x * pi) + DAMP
                    ) + t
                for t in np.linspace(-0.01, 0.01, int(NOTE_THICKNESS * 2.5))
            ]
        ) for r, o in zip(rands[4], offsets4[1:-1])],
        *[SvOsuMeasureLineEvent(
            firstOffset=o, lastOffset=o + 1000,
            startX=0, endX=1,
            startY=-1, endY=1,
            funcs=[
                lambda x, r=r, exp=exp: r * DAMP + exp * np.sin(x * pi) ** SIN_CURVE
                for exp in np.linspace(-EXPLOSION_RANGE, EXPLOSION_RANGE, EXPLOSION_LINES)
            ]
        ) for r, o in zip(rands[4], offsets4[1:-1])],

        # [5]------------------

        SvOsuMeasureLineEvent(
            firstOffset=offsets4[-3], lastOffset=offsets4[-1],
            startX=-1, endX=1,
            startY=1, endY=-1,
            funcs=[
                lambda x, n=n:
                n * np.cos(x * pi / 2) ** 0.45
                for n in np.linspace(0, 0.8, 50)
            ]
        ),

        *[SvOsuMeasureLineEvent(
            firstOffset=offsets5[0], lastOffset=o,
            startX=-1, endX=0,
            startY=1, endY=-1,
            funcs=[
                lambda x, r=r, t=t:
                    (
                        r * (np.cos(x * pi / 2) ** COS_CURVE *
                             np.sin(x * pi / 2)) +
                        r * (x + 1)
                    ) *
                    (
                        - np.sin(x * pi) + DAMP
                    ) + t
                for t in np.linspace(-0.01, 0.01, int(NOTE_THICKNESS * 2.5))
            ]
        ) for r, o in zip(rands[5], offsets5[1:-1])],
        *[SvOsuMeasureLineEvent(
            firstOffset=o, lastOffset=o + 1000,
            startX=0, endX=1,
            startY=1, endY=-1,
            funcs=[
                lambda x, r=r, exp=exp: r * DAMP + exp * np.sin(x * pi) ** SIN_CURVE
                for exp in np.linspace(-EXPLOSION_RANGE, EXPLOSION_RANGE, EXPLOSION_LINES)
            ]
        ) for r, o in zip(rands[5], offsets5[1:-1])],

        # [PIANO] ----------

        *[SvOsuMeasureLineEvent(
            firstOffset=o, lastOffset=o + 500,
            startX=0, endX=1,
            startY=-1, endY=1,
            funcs=[
                *[lambda x, r=r, exp=exp: + r + exp * np.sin(x * pi) ** SIN_CURVE
                for exp in np.linspace(-EXPLOSION_RANGE / 7, EXPLOSION_RANGE / 7, EXPLOSION_LINES // 2)],
                *[lambda x, r=r, exp=exp: - r + exp * np.sin(x * pi) ** SIN_CURVE
                for exp in np.linspace(-EXPLOSION_RANGE / 7, EXPLOSION_RANGE / 7, EXPLOSION_LINES // 2)]
            ]
        ) for r, o in zip(pianoRands, piano)]
    ]

    svs, bpms = svOsuMeasureLineMD(events,
                                   scalingFactor=SCALE,
                                   firstOffset=offsets0[0],
                                   lastOffset=offsets5[-1],
                                   paddingSize=PADDING,
                                   endBpm=250,
                                   metronome=999)

    m.svs.extend(svs)
    m.bpms.extend(bpms)

    m.bpms.append(OsuBpm(offset=314004, bpm=250, metronome=1))

