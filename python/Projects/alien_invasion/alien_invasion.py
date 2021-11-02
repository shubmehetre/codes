import sys

import pygame

import game_settings

import ship_module

import bullet_module

import alien_module

import stats_module

import time

import button_module

import math

import os

# from scorecard_module import ScoreCard
import scorecard_module

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

        # Creating a empty sprite group named bullets_group --> more abt it here https://stackoverflow.com/questions/13851051/how-to-use-sprite-groups-in-pygame
        self.bullets_group = pygame.sprite.Group()
        # sprit.Group is a list of all the sprites that are created by bullet_module instance and
        # added to this group using self.bullet_group.add(bullet instance)

        # alien group same as above
        self.aliens_group = pygame.sprite.Group()
        # create fleet at start of game itself

        # statistics module init
        self.stats = stats_module.Stats(self)

        # scoreboard init
        self.sb = scorecard_module.ScoreCard(self)

        self._create_fleet()

        # creating button at start
        self.play_button = button_module.Button(self, 'Play!')



    def run_game(self):
        """
        Main game loop
        """
        # running game window infinitely until QUIT event is triggered
        while True:

            # helper method to check for events
            self._check_events()

            if self.stats.game_running:
                # update ships position according to right/left keypresses

                self.ship.update()

                # update bullet's position
                self._update_bullets()

                # update aliens movement
                self._update_aliens()
                #
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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button_click(mouse_pos)

    def _key_down_events(self, event):

        # until the key remains pressed down, ship.moving.right flag remains true
        # hence the ship.update() will keep moving
        # ship's position (ship.rect.x) to right(i.e. adding ship_speed value to x attribute of ship's rect (ship.rect.x))

        # move ship right
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        # move ship left
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        # exit game
        elif event.key == pygame.K_q:
            sys.exit()

        # fire bullets
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

        # start game
        elif event.key == pygame.K_p:
            self._start_game()

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
        alien.y = alien.rect.height + 1.4 * alien_height * row_number
        alien.rect.y = int(alien.y)

        # add the alien with their x,y axis set, to the alien sprite group
        self.aliens_group.add(alien)

        # the _update_screen actually draws the alien once we set its x,y cordinates

    def _update_aliens(self):
        """manage movement of aliens"""

        # checks if alien fleet hits edges.
        # it inherently calls fleet's direction changing method
        self._check_fleet_edges()

        # method to check if bullet hit alien
        self._check_bullet_alien_collision()
        #
        # method to chekc if alien and ship collide
        self._check_alien_ship_collision()

        # method to check if alien reach bottom
        self._check_alien_bottom_collision()


        # call the update() from alien module
        self.aliens_group.update()

    def _check_fleet_edges(self):
        """check if the alien hits edge"""
        for alien in self.aliens_group.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_bullet_alien_collision(self):
        """
        checks for collision of bullets and aliens
        also repopulates fleet
        """

        # True True here will
        collisions = pygame.sprite.groupcollide(
            self.bullets_group, self.aliens_group, True, True)
        # this will return a dictionary of all collisions that happen
        # this is not of much use, but we can use it to keep score

        # print(self.settings.alien_points)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        # repopulate aliens fleet
        # checking if aliens groups is empty
        if not self.aliens_group:
            # empting bullets group before creating new fleet
            self.bullets_group.empty()
            self._create_fleet()
            self.settings.game_speed_increase()

            # increase level stat after clearing the fleet
            self.stats.level += 1
            self.sb.prep_level()


    def _check_alien_ship_collision(self):
        """TODOs if aliens hit ship/bottom"""

        # call _ship_hit if alien hit ship/bottom
        if pygame.sprite.spritecollideany(self.ship, self.aliens_group):
            self._alien_hit_ship()

    def _check_alien_bottom_collision(self):
        """checks if any alien hits bottom of the screen"""

        for alien in self.aliens_group.sprites():
            if alien.rect.bottom >= self.screen.get_rect().bottom:
                # treat same as if ship is hit
                self._alien_hit_ship()
                break

    def _change_fleet_direction(self):
        """drops the fleet and changes direction"""

        for alien in self.aliens_group.sprites():
            alien.rect.y += self.settings.alien_drop_speed
        self.settings.fleet_direction *= -1

    def _alien_hit_ship(self):
        """Operations todo after aliens hit the ship or the bottom of screen"""

        if self.stats.ship_left > 0:
            # decrement the ship remainnig count
            self.stats.ship_left -= 1

            # update ship limit sprites on screen
            self.sb.prep_ship()

            # clear the bullets and aliens sprite group
            self.bullets_group.empty()
            self.aliens_group.empty()

            # create a new fleet and centre the new ship
            self._create_fleet()
            # self.ship.rect.midbottom = self.screen.get_rect().midbottom
            self.ship.center_ship()

            # pause
            time.sleep(0.5)
        else:
            # stop the  game
            self.stats.game_running = False

    def _check_play_button_click(self, mouse_pos):
        """checks if user clicked on play button"""

        # check if the mouse click and the play_button rect collide
        play_button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        # if button clicked and game is not running, start the game
        if play_button_clicked and not self.stats.game_running:
            # start new game
            self.settings.initialize_dynamic_settings()
            self._start_game()

        # when game is not running, make cursor visible again
        # to be able click the play button
        elif not self.stats.game_running:
            pygame.mouse.set_visible(True)

    def _start_game(self):
        """start the game if play button or P is presses"""
        # reset game stats
        self.stats.reset_stats()
        self.stats.game_running = True


        # these are called again when player starts the game
        # or wanna play again if all ships are finished
        # (either at the start or in the middle wen ship limit is up)

        # reset score to 0
        self.sb.prep_score()

        # reset level to 1
        self.sb.prep_level()

        # reset ships remainig to 2
        self.sb.prep_ship()

        # empty the alien and bullet group
        self.bullets_group.empty()
        self.aliens_group.empty()

        # Create new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()

        # hide mouse if game is running
        pygame.mouse.set_visible(False)

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

            # draw scoreboard
            self.sb.show_score()

            # showing button if game_running is False that is game is inactive
            if not self.stats.game_running:
                self.play_button.draw_button()
            # draw the play button at last so that its at the top of all other stuff

            # make most recently drawn screen visible
            # continually updates display to show new positions of objects
            pygame.display.flip()
            # keep this at last to update everything above

if __name__ == "__main__":

    # make a game instance and run game
    ai = AlienInvasion()
    ai.run_game()
