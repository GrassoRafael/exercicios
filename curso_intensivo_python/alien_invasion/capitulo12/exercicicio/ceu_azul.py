import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
bg_color = (0, 0, 255)  # Cor azul

# Cria a tela
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tela Azul")

# Loop principal
while True:
    # Trata eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualiza a tela
    screen.fill(bg_color)
    pygame.display.flip()
