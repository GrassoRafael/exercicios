import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats

class AlienInvasion:
    """Classe geral para gerenciar ativos e comportamentos do jogo"""

    def __init__(self):
        """Inicializa o jogo e cria recursos do jogo"""
        pygame.init()
        # Seta a taxa de frames
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # Cria uma instância para armazenar estatísticas do jogo
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Define a cor do background
        self.bg_color = (1, 15, 38)


    def _create_fleet(self):
        """Cria a frota de alienígenas"""
        # Cria um alien e adiciona até ficar sem espaço
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - self.settings.alien_enemies * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y) # Cria um aliente na coordenada x e y
                current_x += 2 * alien_width

            # Termina uma fileira, redefne o valor de x e incrementa o valor de y
            current_x = alien_width
            current_y += 2 * alien_height


    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)


    def _check_fleet_edges(self):
        """Verifica se o alien inimigo alcançou uma borda"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """Faz a frota inimiga descer e mudar de direção"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def run_game(self):
        """Inicia o loop principal do jogo"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)


    def _check_events(self):
        """Responde as teclas pressionadas e a eventos de mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Pressiona a tecla - Move para direita e esquerda
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Responde a teclas pressionadas"""
        if event.key == pygame.K_RIGHT: 
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event):
        """Responde a teclas soltas"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):
        """Cria um novo projétil e o adciona ao grupo de projéteis"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Atualiza a posição dos projéteis e descarta os projéteis antigos"""
        self.bullets.update()

        # Descarta os projétis
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()
        

    def _check_bullet_alien_collisions(self):
        # Responde a colisão com os aliens
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            # Destrói os projéteis existentes e cria uma nova frota
            self.bullets.empty()
            self._create_fleet()


    def _update_aliens(self):
        """Atualiza as posições de todos os aliens na frota inimiga"""
        self._check_fleet_edges()
        self.aliens.update()

        # Detecta Colisões entre alienígenas e espaçonaves
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print('Ship hit!!!')


    def _ship_hit(self):
        """Responde a espaçonove quando é abatida"""
        # Decrementa ships_left
        self.stats.ships_left -= 1

        # Descarga quaisquer projéteis e aliens restantes
        self.bullets.empty()
        self.aliens.empty()

        # Cria uma nova frota e centraliza novamente a nave
        self._create_alien()
        self.ship.center_ship()

        # Pausa
        sleep(0.5)

    def _update_screen(self):
        """Atualiza as imagens na tela e alterna para a nova tela"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # Cria uma instância do jogo e executa o jogo
    ai = AlienInvasion()
    ai.run_game()
