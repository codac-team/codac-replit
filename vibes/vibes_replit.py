import os

def init():
  os.system('rm ../.vibes.json')
  os.environ["XDG_RUNTIME_DIR"] = "/tmp/runtime-runner" # avoids a Qt warning

  import pygame
  pygame.init()
  os.system('chmod +x vibes/VIBes-viewer && ./vibes/VIBes-viewer &')
  import time

  os.system('clear') # removing prior warnings in the terminal

  while not os.path.exists('../.vibes.json'):
    time.sleep(1)
    os.system('clear')
    print("Waiting for VIBes to open...")
  
  os.system('clear')

def pauseDrawing():
  import sys
  sys.stdin.read(1) # prevent the GUI from closing...

init()