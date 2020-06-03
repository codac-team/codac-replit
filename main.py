import vibes_replit
vibes_replit.init() # this is needed for VIBes in repl.it
from tubex_lib import *

x = Tube(Interval(0,10), 0.01, TFunction("cos(t)+abs(t-5)*[-0.1,0.1]"))
print(x)

beginDrawing()
fig = VIBesFigTube("My first tube")
fig.add_tube(x, "x")
fig.show()

vibes_replit.pauseDrawing() # this is needed for VIBes in repl.it