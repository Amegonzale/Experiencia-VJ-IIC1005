'''
Hola este es modulo game,
este modulo manejara la escena donde ocurre nuestro juego
'''

import pygame
import random

from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

from elements.jorge import Player

from elements.bug import Enemy


def StartScene():
    ''' iniciamos los modulos de pygame'''

    pygame.init()

    ''' Creamos y editamos la ventana de pygame (escena) '''
    ''' 1.-definir el tamaño de la ventana'''
    SCREEN_WIDTH = 1000  
    SCREEN_HEIGHT = 700

    ''' 2.- crear el objeto pantalla'''
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image = pygame.image.load("assets/pixelBackground.jpg").convert()

    ''' Preparamos el gameloop '''
    ''' 1.- creamos el reloj del juego'''
    clock = pygame.time.Clock()
    clock.tick(40)

    ''' 2.- generador de enemigos'''
# hay q pasarle parametros
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 600)

    ''' 3.- creamos la instancia de jugador'''
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

    ''' 4.- contenedores de enemigos y jugador'''
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    ''' hora de hacer el gameloop '''
    running = True

    while running:
        clock.tick(100)

        # vemos si glaun enemigo a chocado con el jugador
        if pygame.sprite.spritecollideany (player, enemies):
            # si pasa, cenovemos al jugador y detenemos el loop del juego
            player.kill()
            running = False

        screen.blit(background_image, [0, 0])
        # obtenenos todas las tecias presionados actualmente
        pressed_keys = pygame. key.get_pressed ()
        # actualizamos el sprite del jugador basado en las tectas presionadas
        player.update (pressed_keys)
        # actualizamos los enemigos
        enemies.update ()

        for event in pygame.event.get():
            
            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    running = False

            elif event.type == QUIT:
                running = False
            
            elif event.type == ADDENEMY:
                new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy) 
        
        # dibuiamos todos Los sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        pygame.display.flip()