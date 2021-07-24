import sys

import pygame

import game_settings

import ship_module

import bullet_module

import alien_module

class AlienInvasion:
    """
    Class to manage game assets and behavior 
    """

    def __init__(self) -> None:
        
        # initializes all pygame modules
        pygame.init()

        # create instance for settings module
        self.settings = game_settings.Settings()

     
        # Surface - part of screen where game elements are displayed
        # Here display.set_mode is surface for entire game window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # for full sceen use this:
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        # set caption and icon for window
        pygame.display.set_caption(self.settings.caption) 
        pygame.display.set_icon(self.settings.icon)

        # ship module initialization
        self.ship = ship_module.Ship(self)

        # Creating a group --> more abt it here https://stackoverflow.com/questions/13851051/how-to-use-sprite-groups-in-pygame
        self.bullets_group = pygame.sprite.Group()
        # sprit.Group is a list of all the sprites that are created by bullet_module instance and 
        # added to this group using self.bullet_group.add(bullet instance)

        # alien module 
        self.aliens_group = pygame.sprite.Group()
        # create fleet
        self._create_fleet()



    def run_game(self):
        """
        Main game loop
        """
        # running game window infinitely until QUIT event is triggered
        while True:
            
            # helper method to check for events
            self._check_events()

            # update ships position according to right/left keypresses
            self.ship.update()

            # update bullet 
            self._update_bullets()

            # helper method to update screen
            self._update_screen()


    def _check_events(self)    :
            # watch keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._key_down_events(event)

            elif event.type == pygame.KEYUP:
                self._key_up_events(event)
    
    def _key_down_events(self, event):
        
        # until the key remains pressed down, ship.moving.right flag remains true
        # hence the ship.update() will keep moving 
        # ship's position (ship.rect.x) to right(i.e. adding ship_speed value to x attribute of ship's rect (ship.rect.x))
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _key_up_events(self, event):
        if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """create bullet and pass it to sprite.Group"""

        # limiting number of bullets created at a time on screen
        if len(self.bullets_group) < self.settings.bullet_allowed:
            self.new_bullet = bullet_module.Bullet(self)
            self.bullets_group.add(self.new_bullet) 

    
    def _create_fleet(self):
        """creates fleet of aliens"""

        # object create to do calculations and not draw
        alien = alien_module.Alien(self)
        # rect.size returns a tuple (width, height)
        alien_width, alien_height = alien.rect.size

        # calcualting horizontal space for aliens
        avail_space_x  = self.settings.screen_width - (2 * alien.rect.width)
        num_x = avail_space_x // (1.5 * alien.rect.width)
        number_aliens_x = int(num_x)

        # calculating vertical space
        ship_height = self.ship.rect.height

        avail_space_y = (self.settings.screen_height - 
                            (3 * alien_height) - ship_height)
        number_rows = avail_space_y // (2 * alien_height)

        # creating full fleet
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """creating alien using obj, and placing it in row using object's x attribute"""
        
        # object create to do calculations and not draw
        alien = alien_module.Alien(self)
        # rect.size returns a tuple (width, height)
        alien_width, alien_height = alien.rect.size
        
        alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
        
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number

        self.aliens_group.add(alien)

    def _update_bullets(self):
        """all the bullet update related code"""

        # update bullet's position
        # using the group object we access the bullet objects method like update
        self.bullets_group.update()
        # bullet_group has all the bullet objects in it as a list
        # so we are calling each bullet object with its update method
        # once bullet is drawn, this method continuosly updates its y-axis 
        # according to the speed value then as the screen is constantly updated, 
        # the  bullet appears to move in y-axis

        # delete the bullets from group that have left the screen. but still exist
        # NEVER delete elements while iterating a list == >https://www.quora.com/In-Python-why-cant-you-remove-elements-from-a-list-with-a-for-loop-but-you-can-with-a-while-loop?share=1
        # AND ==> https://stackoverflow.com/questions/6022764/python-removing-list-element-while-iterating-over-list
        for bullet in self.bullets_group.copy():
            if bullet.rect.bottom < 0:
                self.bullets_group.remove(bullet)
        # print(len(self.bullets_group)) # check in terminal if bullets are getting deleted



    def _update_screen(self):

            # window's background color
            self.screen.fill(self.settings.bg_color)

            # blit(blit on screen) the ship on screen
            self.ship.blitme()

            # blit alien
            # self.alien.blitme()

            # we store all bullets created by hitting space bar in the bullets_group
            # then we draw bullet if any there in the bullet group created
            for bullet in self.bullets_group.sprites():
                bullet.draw_bullet()

            # drawing the alien via the group
            self.aliens_group.draw(self.screen)

            # make most recently drawn screen visible
            # continually updates display to show new positions of objects
            pygame.display.flip()
            # keep this at last to update everything above


if __name__ == "__main__":

    # make a game instance and run game
    ai = AlienInvasion()
    ai.run_game()



    