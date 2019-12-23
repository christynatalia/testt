#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 22:10:59 2019

@author: christynataliaj
"""

import pygame 

import sys

from setttings import Settings



    
def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
    x = 30
    y = 30
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(game_settings.bg_color)
        
        pressed = pygame.key.get_pressed()
        
        for press in pressed:
            if pressed[pygame.K_UP]: y -= 3
            if pressed[pygame.K_DOWN]: y += 3
            if pressed[pygame.K_LEFT]: x -= 3
            if pressed[pygame.K_RIGHT]: x += 3
        
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, 60, 60))
        pygame.display.flip()
        clock.tick(20)
run_game()