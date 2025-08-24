import random
import sys

import pygame

# Inicializa o pygame
pygame.init()

# Configurações da tela
largura = 400
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Flappy Bird by Gracy")

# Cores
branco = (255, 255, 255)
azul = (135, 206, 250)
verde = (0, 200, 0)

# Relógio
clock = pygame.time.Clock()

# Fonte
fonte = pygame.font.SysFont(None, 40)


# Função para texto
def desenha_texto(texto, fonte, cor, x, y):
    img = fonte.render(texto, True, cor)
    tela.blit(img, (x, y))


# Configurações do passarinho
passaro_x = 50
passaro_y = altura // 2
gravidade = 0.6
velocidade = 0
pulo = -10
raio = 15

# Configurações dos canos
largura_cano = 70
espaco = 150
velocidade_cano = 4

# Lista de canos
canos = []
for i in range(3):
    altura_cano = random.randint(100, 400)
    canos.append([largura + i * 200, altura_cano])

# Pontuação
pontos = 0

# Loop do jogo
rodando = True
while rodando:
    tela.fill(azul)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                velocidade = pulo

    # Movimento do passaro
    velocidade += gravidade
    passaro_y += velocidade

    # Desenhar passaro
    pygame.draw.circle(tela, branco, (passaro_x, int(passaro_y)), raio)

    # Movimentação dos canos
    for c in canos:
        c[0] -= velocidade_cano
        if c[0] < -largura_cano:
            c[0] = largura
            c[1] = random.randint(100, 400)
            pontos += 1

        # Desenha os canos
        pygame.draw.rect(tela, verde, (c[0], 0, largura_cano, c[1]))
        pygame.draw.rect(tela, verde, (c[0], c[1] + espaco, largura_cano, altura))

        # Colisão
        if (
            passaro_x + raio > c[0]
            and passaro_x - raio < c[0] + largura_cano
            and (passaro_y - raio < c[1] or passaro_y + raio > c[1] + espaco)
        ):
            rodando = False

    # Colisão com chão/teto
    if passaro_y - raio < 0 or passaro_y + raio > altura:
        rodando = False

    # Desenha pontuação
    desenha_texto(f"Pontos: {pontos}", fonte, branco, 10, 10)

    pygame.display.update()
    clock.tick(60)

# Tela final
tela.fill((0, 0, 0))
desenha_texto(f"Game Over! Pontos: {pontos}", fonte, branco, 50, altura // 2)
pygame.display.update()
pygame.time.wait(3000)
pygame.quit()
