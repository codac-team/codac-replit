import os

def init():
  import pygame
  pygame.init()
  os.system('chmod +x VIBes-viewer && ./VIBes-viewer &')
  import time
  time.sleep(1) # waiting for VIBes to be ready
  os.system('clear') # removing prior warnings in the terminal

def pauseDrawing():
  import sys
  sys.stdin.read(1) # prevent the GUI closing...