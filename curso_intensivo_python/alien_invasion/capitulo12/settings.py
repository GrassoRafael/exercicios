class Settings:
    """Classe para armazenar as configurações do jogo Invasão Alienígena"""

    def __init__(self):
        """Inicializa as configurações do jogo"""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (1, 15, 38)

        # Velocidade da nave 
        self.ship_speed = 4
        self.ship_limit = 3

        # Configurações do projétil
        self.bullet_speed = 8.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 15

        # Configuração na nave inimiga
        self.alien_enemies = 9 # Quanto maior o número, menor a quantidade de inimigos (9 é uma boa quantidade)
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # flee_direction de 1 representa a direita; -1 representa a esquerda
        self.fleet_direction = 1
        