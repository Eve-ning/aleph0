from math import pi

import numpy as np

from aleph.consts import *
from reamber.osu.OsuBpm import OsuBpm, MIN_BPM, MAX_BPM
from reamber.osu.OsuHit import OsuHit
from reamber.osu.OsuMap import OsuMap
from reamber.osu.lists.notes.OsuHitList import OsuHitList

offsets = OsuHitList.readEditorString(
    "05:29:364 ("
    "329364|3,329484|3,329604|3,329724|3,329844|3,329964|3,330084|3,330204|3,"
    "330324|3,330444|3,330564|3,330684|3,330804|3,330924|3,331044|3,331164|3,"
    
    "332244|0,332364|0,332484|0,332604|0,332724|0,332844|0,332964|0,333084|0,"
    "333204|0,333324|0,333444|0,333564|0,333684|0,333804|0,333924|0,334044|0,"
    "334164|0,334284|0,334404|0,334524|0,334644|0,334764|0,334884|0,335004|0,"
    "335124|0,335244|0,335364|0,335484|0,335604|0,335724|0,335844|0,335964|0,"
    
    "337044|0,337164|0,337284|0,337404|0,337524|0,337644|0,337764|0,337884|0,"
    "338004|0,338124|0,338244|0,338364|0,338484|0,338604|0,338724|0,338844|0,"
    
    "339924|0,340044|0,340164|0,340284|0,340404|0,340524|0,340644|0,340764|0,"
    "340884|0,341004|0,341124|0,341244|0,341364|0,341484|0,341604|0,341724|0,"
    "341844|0,341964|0,342084|0,342204|0,342324|0,342444|0,342564|0,342684|0,"
    "342804|0,342924|0,343044|0,343164|0,343284|0,343404|0,343524|0,343644|0,"
    
    "345684|0,345804|0,345924|0,346044|0,346164|0,346284|0,346404|0,346524|0,"
    "346644|0,346764|0,346884|0,347004|0,347124|0,347244|0,347364|0,347484|0,"
    
    "348564|0,348684|0,348804|0,348924|0,349044|0,349164|0,349284|0,349404|0,"
    "349524|0,349644|0,349764|0,349884|0,350004|0,350124|0,350244|0,350364|0,"
    "350484|0,350604|0,350724|0,350844|0,350964|0,351084|0,351204|0,351324|0,"
    "351444|0,351564|0,351684|0,351804|0,351924|0,352044|0,352164|0,352284|0,"
    
    "353364|0,353484|0,353604|0,353724|0,353844|0,353964|0,354084|0,354204|0,"
    "354324|0,354444|0,354564|0,354684|0,354804|0,354924|0,355044|0,355164|0,"
    
    "356244|0,356364|0,356484|0,356604|0,356724|0,356844|0,356964|0,357084|0,"
    "357204|0,357324|0,357444|0,357564|0,357684|0,357804|0,357924|0,358044|0,"
    "358164|0,358284|0,358404|0,358524|0,358644|0,358764|0,358884|0,359004|0"
    ") - ").offsets()

offsetsStart = OsuHitList.readEditorString("05:29:364 (329364|2,332244|2,337044|2,339924|2,345684|2,348564|2,"
                                           "353364|2,356244|2) - ").offsets()

offsetsEnd = OsuHitList.readEditorString("05:31:284 (331284|3,336084|2,338964|3,343764|2,347604|2,352404|2,355284|3,"
                                        "359124|2) - ").offsets()

def CHORD(offset: float, positions: list, m: OsuMap):
    positions_ = [p for p in positions if p >= 0]  # Drop any negatives
    diffs = np.diff(sorted(positions_ + [0]))

    # print(positions, positions_)
    # print(diffs)

    # The larger the size, the larger the BPM used.
    for e, d in enumerate(diffs):
        # print(          dict(offset=e + offset, bpm=max(d * REF_BPM * 450, MIN_BPM)))
        m.bpms.append(OsuBpm(offset=e + offset, bpm=max(d * REF_BPM * 450, MIN_BPM)))

    for e, p in enumerate(np.array(positions_).argsort()):
        # print(                  dict(offset=e + offset + 1, column=int(p)))
        m.notes.hits().append(OsuHit(offset=e + offset + 1, column=int(p)))

    m.bpms.append(OsuBpm(offset=offset + len(diffs), bpm=MAX_BPM))
    m.bpms.append(OsuBpm(offset=offset + len(diffs) + 1, bpm=MIN_BPM))


def f834(m: OsuMap):
    CHORD_ = lambda os, ps, m=m: CHORD(offset=os, positions=ps, m=m)

    it = iter(offsets)
    for _ in np.linspace(0, 1, 8 * 2): CHORD_(os=next(it), ps=[np.random.rand() for _ in range(4)])
    for x in np.linspace(0, 4, 8 * 4): CHORD_(os=next(it),
                                              ps=[np.sin(x * pi / 2 + 0 * pi / 2) / 2 * np.cos(x / 4 * pi / 2) + 0.5,
                                                  np.sin(x * pi / 2 + 1 * pi / 2) / 2 * np.cos(x / 4 * pi / 2) + 0.5,
                                                  np.sin(x * pi / 2 + 2 * pi / 2) / 2 * np.cos(x / 4 * pi / 2) + 0.5,
                                                  np.sin(x * pi / 2 + 3 * pi / 2) / 2 * np.cos(x / 4 * pi / 2) + 0.5])

    for _ in np.linspace(0, 1, 8 * 2): CHORD_(os=next(it), ps=[np.random.rand() for _ in range(4)])
    for x in np.linspace(0, 12, 8 * 4): CHORD_(os=next(it),
                                              ps=[np.sin(x * pi / 4 + 0 * pi / 2) / 2 * np.cos(x / 12 * pi / 2) + 0.5,
                                                  np.sin(x * pi / 3 + 1 * pi / 2) / 2 * np.cos(x / 12 * pi / 2) + 0.5,
                                                  np.sin(x * pi / 2 + 2 * pi / 2) / 2 * np.cos(x / 12 * pi / 2) + 0.5,
                                                  np.sin(x * pi / 1 + 3 * pi / 2) / 2 * np.cos(x / 12 * pi / 2) + 0.5])

    for _ in np.linspace(0, 1, 8 * 2): CHORD_(os=next(it), ps=[np.random.rand() for _ in range(4)])
    for e,x in enumerate(np.linspace(0, 1, 8 * 4)): CHORD_(os=next(it),
                                              ps=[(-1 if e % 2 else 1) * (- 0.5 ) * (np.sin((x + 1) * pi / 2) ** 1.5) + 0.5,
                                                  (-1 if e % 2 else 1) * (- 0.33) * (np.sin((x + 1) * pi / 2) ** 1.5) + 0.5,
                                                  (-1 if e % 2 else 1) * (+ 0.33) * (np.sin((x + 1) * pi / 2) ** 1.5) + 0.5,
                                                  (-1 if e % 2 else 1) * (+ 0.5 ) * (np.sin((x + 1) * pi / 2) ** 1.5) + 0.5])

    for _ in np.linspace(0, 1, 8 * 2): CHORD_(os=next(it), ps=[np.random.rand() for _ in range(4)])
    for x in np.linspace(0, 1, 8 * 3): CHORD_(os=next(it), ps=[(np.random.rand() - 0.5) * np.cos(x * pi / 2) + 0.5
                                                               for _ in range(4)])

    for o in offsetsStart: m.bpms.append(OsuBpm(offset=o - 1, bpm=MAX_BPM))
    for o in offsetsEnd:
        m.bpms.append(OsuBpm(offset=o - 1, bpm=MAX_BPM))
        m.bpms.append(OsuBpm(offset=o, bpm=REF_BPM / 4))

    m.bpms.append(OsuBpm(offset=offsets[-1], bpm=250))