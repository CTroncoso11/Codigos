#moverse
#poner bomba
#morir
#salir
import pygame
import turtle
import msvcrt
from pygame.locals import*
import curses
import curses.textpad
import time
pygame.init()
pos=[0,0]
cont=1

def movin():
 a=msvcrt.getch()
 if a=="w":
  pos[1]+=1
 if a=="s":
  pos[1]-=1
 if a=="a": 
  pos[0]-=1
 if a=="d":
  pos[0]+=1
 print(a)

while cont<2:
 print(movin())
 cont+=1
 
