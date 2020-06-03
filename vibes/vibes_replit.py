import os

def init():
  if os.environ.get('Foo') is None:
    os.environ["XDG_RUNTIME_DIR"] = "/tmp/runtime-runner" # avoids a Qt warning
    added_delay_at_first_use=2
  else:
    added_delay_at_first_use=0
    
  import pygame
  pygame.init()
  os.system('chmod +x vibes/VIBes-viewer && ./vibes/VIBes-viewer &')
  import time
  time.sleep(1+added_delay_at_first_use) # waiting for VIBes to be ready
  os.system('clear') # removing prior warnings in the terminal

def pauseDrawing():
  import sys
  sys.stdin.read(1) # prevent the GUI from closing...

init()