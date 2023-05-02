import pygame

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, MOVE_X

X_POS = 0
Y_POS = 310
Y_POS_DUCK = 340
JUMP_VEL = 8.5

class Dinosaur:
    def __init__(self):
        self.image = RUNNING[0]
        
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS    
        
        self.steps_count = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        
        self.jump_vel = JUMP_VEL
        self.dino_direction = 1
    
    def update(self, user_input):
        
        if user_input[pygame.K_UP]:
            self.dino_jump = True
            self.dino_run = False
        elif user_input[pygame.K_DOWN]:
            self.dino_duck = True
            self.dino_run = False
        elif user_input[pygame.K_LEFT]:
            self.left()
            self.dino_run = False
        elif user_input[pygame.K_RIGHT]:
            self.right()
            self.dino_run = False
        elif not self.dino_jump:
            self.dino_run = True
            
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
        
        if self.steps_count > 9:
            self.steps_count = 0
        
    def run(self):
        self.image = RUNNING[self.steps_count//5]
        self.dino_rect.y = Y_POS
        self.steps_count+=1
    
    def duck(self):
        self.image = DUCKING[self.steps_count//5]
        self.dino_rect.y = Y_POS_DUCK
        self.steps_count+=1
        
        
    def jump(self):
        self.image = JUMPING
        
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel*4
            self.jump_vel-=0.8
        
        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def right(self):
        self.dino_direction = 1  # define a direção do dinossauro para a direita
        self.dino_rect.x += MOVE_X

    def left(self):
        self.dino_direction = -1  # define a direção do dinossauro para a esquerda
        self.dino_rect.x -= MOVE_X         
        
        
        
    def draw(self,screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


        
