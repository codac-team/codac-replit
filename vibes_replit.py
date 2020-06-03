import os

def init():
  os.system('[ ! -d squashfs-root ] && wget https://github.com/ENSTABretagneRobotics/VIBES/releases/download/0.2.3/VIBes-0.2.3-linux.AppImage && chmod +x ./VIBes-0.2.3-linux.AppImage && ./VIBes-0.2.3-linux.AppImage --appimage-extract')
  os.system('cd squashfs-root && chmod +x ./VIBes-viewer && ./VIBes-viewer &')
  import time
  time.sleep(1) # needed for finalizing the previous installation
  os.system('clear')

def pauseDrawing():
  import sys
  sys.stdin.read(1) # without that the GUI closes...