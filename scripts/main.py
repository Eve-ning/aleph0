""" This is the main file where aleph-0 is generated > _<)b

The workflow I'm using is simple:
fXYZ => At XY.Z0% of the map
f002 => At 00.20% of the map
f510 => At 51.00% of the map

So these svs are organized and easy to turn on and off o wo)b

They all take a OsuMap reference, so they can directly modify the osu map.
Because OsuMap is a custom class, it'll be passed by reference, so any modifications made in that function is applied
to the original one.

e.g.
osu = OsuMap()
f123(osu)  # Double bpm
osu        # Doubled Bpm

This helps also in passing other information such as notes.
----------

They all import constants from consts.py, that one handles frame rate, how many random lines, reference bpm, etc.
----------

It's not recommended to copy my style of coding in those files because I was speed coding from my mind, however, it's
fun to try to translate some code into mathematical functions! I used Desmos a lot to visualize what happens in each
function o wo)b
----------

There's also storyboard, reamber currently doesn't support it, so I whipped up a custom generated storyboard, details
in sb.py

"""

import logging

import numpy as np

from aleph.consts import *
from aleph.f002 import f002
from aleph.f017 import f017
from aleph.f018 import f018
from aleph.f019 import f019
from aleph.f024 import f024
from aleph.f028 import f028
from aleph.f039 import f039
from aleph.f053 import f053
from aleph.f072 import f072
from aleph.f083 import f083
from aleph.f162 import f162
from aleph.f233 import f233
from aleph.f247 import f247
from aleph.f319 import f319
from aleph.f325 import f325
from aleph.f430 import f430
from aleph.f442 import f442
from aleph.f447 import f447
from aleph.f486 import f486
from aleph.f510 import f510
from aleph.f513 import f513
from aleph.f520 import f520
from aleph.f559 import f559
from aleph.f598 import f598
from aleph.f608 import f608
from aleph.f834 import f834
from aleph.f919 import f919
from aleph.f950 import f950
from reamber.osu.OsuBpm import OsuBpm
from reamber.osu.OsuMap import OsuMap

logging.basicConfig(filename="event.log", filemode="w+", level=logging.DEBUG)

# Path is redacted
path = "LeaF - Aleph-0 (extended ver.) (Evening) [Easy 1].osu"

np.random.seed(2)

osu = OsuMap.readFile(path)

osu.bpms.clear()

# Comment out anything here to remove that section

f002(osu)
f017(osu)
f018(osu)
f019(osu)
f024(osu)
f028(osu)
f039(osu)
f053(osu)
f072(osu)
f083(osu)
f162(osu)
f233(osu)
f247(osu)
f319(osu)
f325(osu)
f430(osu)
f442(osu)
f447(osu)
f486(osu)
f510(osu)
f513(osu)
f520(osu)
f559(osu)
f598(osu)
f608(osu)
f834(osu)
f919(osu)
f950(osu)

VERSION = "Boundless"

# This is to correct the bpm reference
osu.bpms.append(OsuBpm(0, REF_BPM))

osu.version = VERSION

# Path is redacted
outpath = f"LeaF - Aleph-0 (extended ver.) (Evening) [{VERSION}].osu"

highest = sorted([o for o in osu.bpms if o.bpm != 10000000], key=lambda b: b.bpm)[-1]
print("MAXIMUM BPM USED: ", highest.bpm, highest.offset)
osu.writeFile(outpath)  
