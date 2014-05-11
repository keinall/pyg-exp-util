# TODO: fix the shebang so it works in IDLE w32 (e.g.on N8 (my main box))
#!/bin/env python
# -- inferior version of the pygame version check

import sys

v = sys.version
vt = sys.version_info

bPygameLoaded = False

try:
    import pygame

    s = pygame.version.ver
    nt = pygame.version.vernum

    print ("pygame version: ", s);
    bPygameLoaded = True 
except:
    print ("Sorry, could not load pygame. Sadness ensues.");

print ("running on python version: ", v);

# -- TODO: find the old file, 
# -- and make this into a cleaner module thingy.



