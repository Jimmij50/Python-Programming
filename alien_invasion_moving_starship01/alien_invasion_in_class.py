import sys
import pygame
from settings import Settings
from ship import Ship
class AlienInvasion:
   def __init__(self):
      pygame.init()
      self.settings = Settings()
      
      self.screen = pygame.display.set_mode(
         (self.settings.screen_width,self.settings.screen_height)
      )
      self.screen.fill(self.settings.bg_color)
      pygame.display.set_caption("Alien Invasion")
      self.screen.fill(self.settings.bg_color)
      
      self.ship = Ship(self)

   def run_game(self):
      """ Start the main loop for the game"""
      while True:
         self._check_events()
         self._update_screen()
         
   def _check_events(self):
      """Respond to keypresses and mouse events."""
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
               sys.exit()
         elif event.type == pygame.KEYDOWN:
               self._check_keydown_events(event)
 

   def _check_keydown_events(self, event):
      """Respond to keypresses."""
      if event.key == pygame.K_RIGHT:
         self.ship.moving_right = True
         self.ship.move_right()
      elif event.key == pygame.K_LEFT:
         self.ship.moving_left = True
      elif event.key == pygame.K_q:
         sys.exit()
      # elif event.key == pygame.K_SPACE:
      #    self._fire_bullet() 
         
   def _update_screen(self):
      """Update images on the screen, and flip to the new screen."""
      self.screen.fill(self.settings.bg_color)
      #   for bullet in self.bullets.sprites():
      #       bullet.draw_bullet()
      self.ship.blitme()
      #   self.aliens.draw(self.screen)
      pygame.display.flip()
         

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()