import vibes.vibes_replit as gui
from codac import *

x = Tube(Interval(0,10), 0.01, TFunction("cos(t)+abs(t-5)*[-0.1,0.1]"))
print(x)

beginDrawing()
fig = VIBesFigTube("My first tube")
fig.add_tube(x, "x")
fig.show()

gui.pauseDrawing() # prevent the GUI from closing