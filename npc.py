import random

import pygame as pg
from support import loadSprite
from settings import *
from objects import InteractableObjects
from timer import Timer
from support import import_folder
import random

class Merchant(InteractableObjects):
    def __init__(self,group,interactableSprites,dialogue,dynamicUi):
        super().__init__(group)

        self.type = "npc"
        self.dialogueId = "Merchant"
        self.startingPos = (800, 795)

        self.spritePath = "Sprites/Merchant.png"

        self.dialogueSystem = dialogue
        self.dynamicUi = dynamicUi
        self.image = pg.image.load(self.spritePath).convert_alpha()
        self.rect = self.image.get_rect(topleft=self.startingPos)
        self.hitbox = self.rect.inflate(-40,-40)

        self.interactRect = self.image.get_rect(topleft=(self.startingPos[0], self.startingPos[1] + tileSize))
        self.interactHitbox = self.interactRect.inflate(-40,-40)

        self.interactableSprites = interactableSprites
        self.add(self.interactableSprites)


    def interact(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_x]:
            if not self.interacted:
                self.dialogueSystem.startDialogue(self.dialogueId)
                self.interacted = True
            else:
                return

    def disengage(self):
        self.interacted = False

class Chicken(pg.sprite.Sprite):
    def __init__(self,pos,group,collisionSprites):
        super().__init__(group)

        self.type = "npc"
        self.collisionSprites = collisionSprites

        self.imagePath = "Sprites/Chicken/Idle/0.png"
        self.image = pg.image.load(self.imagePath).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(10, 0)

        self.ImportSprites()

        self.direction = pg.math.Vector2()

        self.walkingAnimationTime = 1 / 12
        self.idleAnimationTime = 1 / 120
        self.frameIndex = 0

        self.stateDuration = 8000
        self.currentAnimationState = "Walk"
        self.currentState = -1

        self.states = {
            -1 : self.IdleState,
            1 : self.RoamState
        }

        self.chooseDirection = False
        self.walkSpeed = 0.1
        self.availableDirections = ["Up", "Down", "Left", "Right"]
        self.chosenDirection = "Left"

        self.walkDirection = {
            "Up" : (0,-1),
            "Down": (0,1),
            "Left": (-1, 0),
            "Right": (1, 0),
        }

        self.timer = Timer(self.stateDuration)

    def ImportSprites(self):
        imagePath = "Sprites/Chicken/"
        self.animationStates = {
            "Idle" : [],
            "Walk" : []
        }

        for animation in self.animationStates.keys():
            full_path = imagePath + animation
            self.animationStates[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animationStates[self.currentAnimationState]
        self.frameIndex += self.idleAnimationTime if self.currentState == -1 else self.walkingAnimationTime

        if self.frameIndex >= len(animation):
            self.frameIndex = 0

        self.image = animation[int(self.frameIndex)].convert_alpha()
        self.image = pg.transform.flip(self.image,True,False) if self.direction.x < 0 else pg.transform.flip(self.image,False,False)
        self.rect = self.image.get_rect(topleft=self.hitbox.topleft)

    def IdleState(self):
        self.chooseDirection = False
        self.currentAnimationState = "Idle"

    def RoamState(self):
        if not self.chooseDirection:
            self.chosenDirection = random.choice(self.availableDirections)
            self.currentAnimationState = "Walk"
            self.chooseDirection = True

        newDirection = pg.math.Vector2(self.walkDirection.get(self.chosenDirection))
        self.direction = newDirection

    def movement(self,speed):
        # bug
        self.hitbox.x += self.direction.x * speed if self.direction.x < 0 else self.direction.x * (speed * 10)
        self.checkWallCollision("Horizontal")
        self.hitbox.y += self.direction.y * speed if self.direction.y < 0 else self.direction.y * (speed * 10)
        self.checkWallCollision("Vertical")
        self.rect.center = self.hitbox.center

    def checkWallCollision(self, direction):
        for sprite in self.collisionSprites:
            if sprite.hitbox.colliderect(self.hitbox):
                if direction == "Horizontal":
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
                    else:
                        self.hitbox.right = sprite.hitbox.left
                elif direction == "Vertical":
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
                    else:
                        self.hitbox.bottom = sprite.hitbox.top

    def update(self):
        self.timer.update()
        self.animate()

        if not self.timer.activated:
            self.currentState *= -1
            self.getCurrentState = self.states.get(self.currentState)
            self.timer.activate()

        self.getCurrentState()
        self.movement(self.walkSpeed)