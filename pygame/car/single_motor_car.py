#!/usr/bin/env python3

import pygame
import sys
pygame.init()

size = screen_w, screen_h = 1500, 1100
speed = [2,2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
ball = pygame.image.load("pygame/img/car.png")
ballrect = ball.get_rect()



class motor:
    """
    receives voltage 
    outputs rpm
    """
    pass

class motor_controller:
    """
    receives a 0-100 representing motor speed
    outputs the voltage required in the motor
    """
    pass

class car:
    ml = motor_controller()
    mr = motor_controller()
    wheel_base = 15
    length = 25
    def update(self, ml_v, mr_v):
        """
        update the state of the car with the updated voltajes
        """
        print "Motor speed"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > screen_w:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > screen_h:
        speed[1] = -speed[1]
    
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()