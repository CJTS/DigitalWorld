from pprint import pprint
from digitalWorld import DigitalWorld
from eatermon import Eatermon

# Initialize world
digitalWorld = DigitalWorld()
digitalWorld.start()
pprint(digitalWorld.grid)

# Initialize Eatrmon
eatermon = Eatermon()
while(True):
    if not eatermon.live(digitalWorld.grid):
        break

# The End
print "Ate!"
pprint(digitalWorld.grid)