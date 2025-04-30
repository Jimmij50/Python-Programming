import pygame
class Ship():
    # def __init__(self, screen):
    def __init__(self,ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.ai_settings = ai_game.settings
        # Load the ship image and get its rect.
        self.image = pygame.image.load(r'.\images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.moving_right = False
        
        self.center = float(self.rect.centerx)
        
    def update(self):
        """Update the ship's position based on the movement flag"""
        # if self.moving_right and self.rect.right<self.screen_rect.right:
        #     #self.rect.centerx +=1
        #     self.center += self.ai_settings.ship_speed_factor
        # self.rect.centerx = self.center

        self.rect.centerx += self.ai_settings.ship_speed_factor
    def move_right(self):
        self.rect.centerx += self.ai_settings.ship_speed_factor
            
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)