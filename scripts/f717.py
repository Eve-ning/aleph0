from reamber.osu.OsuBpm import OsuBpm
from reamber.osu.OsuMap import OsuMap


def f717(m: OsuMap):
    m.bpms.extend([OsuBpm(283284, bpm=1000000),
                   OsuBpm(283286, bpm=250, metronome=999)])
