__author__ = 'bm'
import pygame

pygame.init()
screen = pygame.display.set_mode([600,400])

pygame.event.pump()

while True:
    event = pygame.event.poll()
    if event.type != pygame.NOEVENT:
        print event
        # print event.__dict__