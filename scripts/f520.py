import numpy as np

from aleph.consts import *
from reamber.algorithms.generate.sv.SvSequence import SvSequence
from reamber.osu.OsuBpm import OsuBpm
from reamber.osu.OsuMap import OsuMap

# 03:22:782 () -

buzzes = [206382, 207582, 208302, 208542, 210102, 210132, 210162, 210192, 210222, 210942,
          212142, 212262, 213342, 213462, 214062, 214092, 214122, 214152, 214182, 214962,
          215982, 216102, 217872, 218862, 219822, 220062]

offsets = [202782, 203022, 203262, 203502, 203742, 203982, 204222, 204462, 204702, 204942, 205182]


def f520(m: OsuMap):

    bpms = SvSequence([(b, 1000000) for b in buzzes[::2]]).writeAsBpm(OsuBpm)
    bpms.extend(SvSequence([(b, REF_BPM * 0.75)
                            for b0, b1 in zip(buzzes[::2], buzzes[1::2])
                            for b in np.arange(b0 + 1, b1, 2)]).writeAsBpm(OsuBpm, metronome=999))

    m.bpms.extend(bpms)
