import pygame
import os
import sys
import math
from pygame.locals import *
from Classes import *
from Functions import *
from Regles import LoiGravitation
import time
import Trajectoires

# VARIABLES
appDimensions = [600, 400]
screen = Screen(appDimensions[0], appDimensions[1])
CameraMoveSpeed = 10
CameraScrollSpeed = 300
stepSize = 1000000000000000
stepSpeed = 0.04 # makes a step every 0.2 seconds
edition = True
simulation = True

mainScreen = Screen(600, 400)

pygame.init()
clock = pygame.time.Clock()
background = pygame.Surface((1920, 1080))
background.fill("gray")

Bodies = []
Renderer = []


pygame.mouse.set_visible(1)
pygame.display.set_caption("Simulation Gravitationelle (Q/Esc pour sortir)")

sprite1 = Body([300, 300], [0, -5], 0.3, "Sprites/PlanetRed.png", 0, 0, 0)

sprite2 = Body([-300, -300], [0, 5], 0.3, "Sprites/PlanetRed.png")

#sprite3 = Body([0, 500], [20, 0], 1, "Sprites/PlanetRed.png")

#sprite4 = Body([-200, 100], [0, 0], 1, "Sprites/PlanetRed.png")


Bodies.append(sprite1)
Bodies.append(sprite2)
#Bodies.append(sprite3)
#Bodies.append(sprite4)


def EventHandler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                pygame.quit()
        if event.type == pygame.MOUSEWHEEL:
            mainScreen.camera.AddZoom(event.y * -CameraScrollSpeed)

    # Keyboard movement
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        mainScreen.camera.position[1] -= CameraMoveSpeed * mainScreen.camera.scale
    if keys[K_s]:
        mainScreen.camera.position[1] += CameraMoveSpeed * mainScreen.camera.scale
    if keys[K_a]:
        mainScreen.camera.position[0] -= CameraMoveSpeed * mainScreen.camera.scale
    if keys[K_d]:
        mainScreen.camera.position[0] += CameraMoveSpeed * mainScreen.camera.scale

lastStep = time.time()
#sprite1.apply_force(5, -3.14/2)
# Main game loop
while edition == True:
    clock.tick(60)
    mainScreen.screen.blit(background, (0, -2))

    EventHandler()

    # print(sprite1.position)

    # Body renderer
    for body in Bodies:
        body.draw(mainScreen)

    # Renderer
    for sprite in Renderer:
        sprite.draw(mainScreen)


    pygame.display.update()


while simulation == True:
    clock.tick(60)
    mainScreen.screen.blit(background, (0, -2))

    
    if time.time() - lastStep > stepSpeed:
        lastStep = time.time()
        # Bodies
        # Applies the law for all the bodies
        Bodies = LoiGravitation.apply(Bodies, stepSize)
        for body in Bodies:
            body.position = [body.position[0] + body.momentum[0], body.position[1] + body.momentum[1]]


    EventHandler()

    # print(sprite1.position)

    # Body renderer
    for body in Bodies:
        body.draw(mainScreen)

    # Renderer
    for sprite in Renderer:
        sprite.draw(mainScreen)


    pygame.display.update()