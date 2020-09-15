#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Modulos
import sys, pygame

# Constantes
WIDTH = 510
HEIGHT = 410

# Clases
# ---------------------------------------------------------------------
class Bola(pygame.sprite.Sprite):
    def __init__(self,speed_x=0, speed_y=0, init_x=0, init_y=0):
        self.speed_x, self.speed_y = speed_x, speed_y
        self.init_x, self.init_y = init_x, init_y
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("./img/car_r.jpg", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = init_x
        self.rect.centery = init_y
        self.speed = [speed_x, speed_y]

    def actualizar(self, time, carro, edif, edif2):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time
        if (pygame.sprite.collide_rect(self, edif)):
            self.speed[0] = -self.speed[0]
            self.speed[1] = -self.speed[1]
            self.rect.centerx +=self.speed[0] * time
            self.rect.centery +=self.speed[1] * time
        if (pygame.sprite.collide_rect(self, carro)):
            self.speed[0] = -self.speed[0]
            self.speed[1] = -self.speed[1]
            self.rect.centerx +=self.speed[0] * time
            self.rect.centery +=self.speed[1] * time
        if (pygame.sprite.collide_rect(self, edif2)):
            self.speed[0] = -self.speed[0]
            self.speed[1] = -self.speed[1]
            self.rect.centerx +=self.speed[0] * time
            self.rect.centery +=self.speed[1] * time

# ---------------------------------------------------------------------
class edificio(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("./img/b1.jpg", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
    #def actualizar(sefl,time, carro)
    #    if pygame.sprite.collide_rect(self,carro):

# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------

def load_image(filename, transparent=False):
        try: 
            image = pygame.image.load(filename)
        except pygame.error as message:
            pass # message
        image = image.convert()
  #      if transparent:
  #              color = image.get_at((0,0))
  #              image.set_colorkey(color, RLEACCEL)
        return image

# ---------------------------------------------------------------------

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("º<>º")

    background_image = load_image('./img/floor.jpg')
    edificio_SI =  edificio(75, 75)
    edificio_SD =  edificio(435, 75)
    #edificio_II =  edificio()
    #edificio_ID =  edificio()
    bola = Bola(0.15, -0.1, 300, 70)
    bols = Bola(-0.1, -0.11, 220, 70)
    clock = pygame.time.Clock()
    print(edificio_SI.rect.centerx, edificio_SI.rect.centery)
    print(bols.speed_x, bols.speed_y, bola.speed_x, bola.speed_y)
    while True:
        time = clock.tick(60)
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                sys.exit(0)
        bola.actualizar(time,bols, edificio_SI, edificio_SD)
        bols.actualizar(time+8, bola, edificio_SI, edificio_SD)
        screen.blit(background_image, (0, 0))
        screen.blit(edificio_SI.image, edificio_SI.rect) #actualizar la imagen del edificio
        screen.blit(edificio_SD.image, edificio_SD.rect) #actualizar la imagen del edificio
        screen.blit(bola.image, bola.rect)
        screen.blit(bols.image, bols.rect)
    
    pygame.display.flip()

    return 0



if __name__ == '__main__':
    pygame.init()
    main()
