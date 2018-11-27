import pygame
from random import randint
class Hero(object):
    def __init__(self):
        self.x = randint(1,512)
        self.y = randint(1,480)
        self.speed = 10
        self.should_move_down = False
        self.should_move_left = False
        self.should_move_right = False
        self.should_move_up = False
    def shouldMove(self, direction, start = True):
        if direction == "right":
            self.should_move_right = start
        if direction == "left":
            self.should_move_left = start
        if direction == "up":
            self.should_move_up = start
        if direction == "down":
            self.should_move_down = start
    def draw_me(self,w,h):
        if self.should_move_right:
            if self.x <= (w - 64):
                self.x += self.speed
        elif self.should_move_left:
            if self.x >= (32):
                self.x -= self.speed
        if self.should_move_down:
            if self.y <= (h - 64):
                self.y += self.speed
        elif self.should_move_up:
            if self.y >= (32):
                self.y -= self.speed
