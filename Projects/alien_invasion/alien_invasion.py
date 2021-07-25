import sys

import pygame

import game_settings

import ship_module

import bullet_module

import alien_module

import stats_module

import time

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
        # create fleet at start of game itself
        self._create_fleet()

        # statistics module init
        self.stats = stats_module.Stats(self)


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

            # update bullet's position
            self._update_bullets()

            # update aliens movement
            self._update_aliens()

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
        avail_space_x  = self.settings.screen_width - (2 * alien_width)
        num_x = avail_space_x // (2 * alien.rect.width)
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

        # setting the x,y cordinates of the every new alien created 
        # in the _create_fleet nested for loop        
        alien.x = (alien_width / 2) + 2 * alien_width * alien_number
        alien.rect.x = int(alien.x)
        alien.y = 1.5 * alien_height * row_number
        alien.rect.y = int(alien.y)

        # add the alien with their x,y axis set, to the alien sprite group
        self.aliens_group.add(alien)

    def _update_aliens(self):
        """manage movement of aliens"""

        # checks if alien fleet hits edges. 
        # it inherently calls fleet's direction changing method
        self._check_fleet_edges()

        # method to check if bullet hit alien
        self._check_bullet_alien_collision()

        # method to chekc if alien and ship collide
        # self._check_alien_ship_collision()

        if pygame.sprite.spritecollideany(self.ship, self.aliens_group):
            self.aliens_group.empty()
            self.bullets_group.empty()
            self.ship
            self._create_fleet()
        # call the update() from alien module
        self.aliens_group.update()

    def _check_fleet_edges(self):
        """check if the alien hits edge"""
        for alien in self.aliens_group.sprites():
            if alien.check_edges():            
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """drops the fleet and changes direction"""

        for alien in self.aliens_group.sprites():
            alien.rect.y += self.settings.alien_drop_speed
        self.settings.alien_direction *= -1


    def _check_bullet_alien_collision(self):
        """
        checks for collision of bullets and aliens
        also repopulates fleet
        """

        # this will return a dictionary of all collisions that happen
        collisions = pygame.sprite.groupcollide(self.bullets_group, self.aliens_group, True, True)
        # this is not of much use, but we can use it to keep score

        # repopulate aliens fleet 
        # checking if aliens groups is empty
        if not self.aliens_group:
            # empting bullets group before creating new fleet
            self.bullets_group.empty()
            self._create_fleet()

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

    # def _ship_hit(self):
        

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



    