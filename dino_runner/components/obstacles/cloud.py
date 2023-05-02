import pygame
import random

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 200


CLOUD_IMAGE = pygame.image.load("assets/other/cloud.png")


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

      
        self.rect = CLOUD_IMAGE.get_rect(
            center=(random.randint(WINDOW_WIDTH, WINDOW_WIDTH + 200), random.randint(0, WINDOW_HEIGHT))
        )

        self.speed = random.randint(1, 3)

    def update(self):
     
        self.rect.move_ip(-self.speed, 0)
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Dino Runner")
        clouds = pygame.sprite.Group()


        ADD_CLOUD_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(ADD_CLOUD_EVENT, 1000)
        running = True
       
    while running:
        for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == ADD_CLOUD_EVENT:
          
            clouds.add(Cloud())

    
    clouds.update()

    screen.fill((135, 206, 250))
    clouds.draw(screen)

    # Atualizar a janela do jogo
    pygame.display.flip()

pygame.quit()
