import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definição das cores
BRANCO = (255, 255, 255)
PRETO = (30, 30, 30)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
VERDE = (0, 128, 0)
ROXO = (128, 0, 128)
LARANJA = (255, 165, 0)
CINZA = (175, 175, 175)
ROSA = (255, 20, 147)
MARROM = (139, 69, 19)
VERDE_ESCURO = (0, 70, 0)
AZUL_MARINHO = (0, 0, 128)

# Configurações de janela
JANELA_LARGURA = 1750
JANELA_ALTURA = 900
TAMANHO_QUADRADO = 0

# Inicialização da janela
janela = pygame.display.set_mode((JANELA_LARGURA, JANELA_ALTURA), pygame.RESIZABLE)
pygame.display.set_caption("Monopoly")

# Classe para representar um tile no tabuleiro
class Tile:
    def __init__(self, x, y, largura, altura, cor, nome):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = cor
        self.nome = nome

    def draw(self):
        pygame.draw.rect(janela, self.cor, (self.x, self.y, self.largura, self.altura))
        font_size = min(int(self.largura * 0.3), 30)  # Ajuste do tamanho da fonte
        fonte = pygame.font.Font(None, font_size)
        palavras = self.nome.split(' ')
        linhas = []
        linha_atual = ''
        for palavra in palavras:
            texto_temporario = linha_atual + ' ' + palavra if linha_atual else palavra
            largura_texto, altura_texto = fonte.size(texto_temporario)
            if largura_texto < self.largura:
                linha_atual = texto_temporario
            else:
                linhas.append(linha_atual)
                linha_atual = palavra
        linhas.append(linha_atual)
        y_offset = self.y + (self.altura - len(linhas) * altura_texto) // 2
        for linha in linhas:
            texto = fonte.render(linha, True, BRANCO)
            texto_rect = texto.get_rect(center=(self.x + self.largura // 2, y_offset))
            janela.blit(texto, texto_rect)
            y_offset += altura_texto

# Classe para representar uma peça no tabuleiro
class Peca:
    def __init__(self, cor, posicao):
        self.cor = cor
        self.posicao = posicao

    def draw(self):
        tile = self.posicao
        pygame.draw.circle(janela, self.cor, (tile.x + tile.largura // 2, tile.y + tile.altura // 2), TAMANHO_QUADRADO // 4)

# Função para desenhar o tabuleiro
def desenhar_tabuleiro():
    global LARGURA_RETANGULO, ALTURA_RETANGULO
    ALTURA_RETANGULO =  JANELA_ALTURA // 11
    LARGURA_RETANGULO = JANELA_LARGURA // 11
    espacos = [
        Tile(0, 0, LARGURA_RETANGULO, ALTURA_RETANGULO, ROXO, "Início"),
        Tile(LARGURA_RETANGULO, 0, LARGURA_RETANGULO, ALTURA_RETANGULO, VERMELHO, "Copacabana"),
        Tile(2 * LARGURA_RETANGULO, 0, LARGURA_RETANGULO, ALTURA_RETANGULO, AZUL, "Cofre Comunitário"),
        Tile(3 * LARGURA_RETANGULO, 0, LARGURA_RETANGULO, ALTURA_RETANGULO, VERMELHO, "Ipanema"),
        Tile(4 * LARGURA_RETANGULO, 0, LARGURA_RETANGULO, ALTURA_RETANGULO, AZUL, "Imposto de Renda"),
        Tile(5 * LARGURA_RETANGULO, 0, LARGURA_RETANGULO, ALTURA_RETANGULO, CINZA, "Estação Central"),
        Tile(6 * LARGURA_RETANGULO, 0, LARGURA_RETANGULO, ALTURA_RETANGULO, VERDE, "Leblon"),
        Tile(7 * LARGURA_RETANGULO, 0, LARGURA_RETANGULO, ALTURA_RETANGULO, AZUL, "Sorte"),
        Tile(8 * LARGURA_RETANGULO, 0, LARGURA_RETANGULO, ALTURA_RETANGULO, VERMELHO, "Barra da Tijuca"),
        Tile(9 * LARGURA_RETANGULO, 0, LARGURA_RETANGULO, ALTURA_RETANGULO, VERDE, "Recreio dos Bandeirantes"),
        Tile(10 * LARGURA_RETANGULO, 0, LARGURA_RETANGULO, ALTURA_RETANGULO, PRETO, "Prisão"),
        Tile(10 * LARGURA_RETANGULO, ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, VERDE, "Centro"),
        Tile(10 * LARGURA_RETANGULO, 2 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, ROSA, "Cristo Redentor"),
        Tile(10 * LARGURA_RETANGULO, 3 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, AMARELO, "Tijuca"),
        Tile(10 * LARGURA_RETANGULO, 4 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, AMARELO, "Botafogo"),
        Tile(10 * LARGURA_RETANGULO, 5 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, CINZA, "Estação Botafogo"),
        Tile(10 * LARGURA_RETANGULO, 6 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, AMARELO, "Santa Teresa"),
        Tile(10 * LARGURA_RETANGULO, 7 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, AZUL, "Cofre Comunitário"),
        Tile(10 * LARGURA_RETANGULO, 8 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, MARROM, "Jardim Botânico"),
        Tile(10 * LARGURA_RETANGULO, 9 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, MARROM, "Gávea"),
        Tile(10 * LARGURA_RETANGULO, 10 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, ROXO, "Receba 200"),
        Tile(9 * LARGURA_RETANGULO, 10 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, LARANJA, "Grajaú"),
        Tile(8 * LARGURA_RETANGULO, 10 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, MARROM, "Urca"),
        Tile(7 * LARGURA_RETANGULO, 10 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, AZUL, "Sorte"),
        Tile(6 * LARGURA_RETANGULO, 10 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, ROXO, "Estacionamento Gratuito"),
        Tile(5 * LARGURA_RETANGULO, 10 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, LARANJA, "Laranjeiras"),
        Tile(4 * LARGURA_RETANGULO, 10 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, CINZA, "Estação Maracanã"),
        Tile(3 * LARGURA_RETANGULO, 10 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, LARANJA, "Humaitá"),
        Tile(2 * LARGURA_RETANGULO, 10 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, ROSA, "Pão de Açúcar"),
        Tile(LARGURA_RETANGULO, 10 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, VERDE_ESCURO, "Santa Cruz"),
        Tile(0, 10 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, ROSA, "Arcos da Lapa"),
        Tile(0, 9 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, VERDE_ESCURO, "Campo Grande"),
        Tile(0, 8 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, AZUL, "Sorte"),
        Tile(0, 7 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, VERDE_ESCURO, "Jacarepaguá"),
        Tile(0, 6 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, VERMELHO, "Lapa"),
        Tile(0, 5 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, CINZA, "Estação São Cristóvão"),
        Tile(0, 4 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, AZUL_MARINHO, "Flamengo"),
        Tile(0, 3 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, AZUL, "Cofre Comunitario"),
        Tile(0, 2 * ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, AZUL_MARINHO, "Leme"),
        Tile(0, ALTURA_RETANGULO, LARGURA_RETANGULO, ALTURA_RETANGULO, AZUL, "Taxa de luxo"),
    ]

    for espaco in espacos:
        espaco.draw()

# Função para desenhar as peças
def desenhar_pecas(pecas):
    for peca in pecas:
        peca.draw()

# Loop principal do jogo
def main():
    # Criando as peças
    pecas = [Peca(VERMELHO, Tile(0, 0, TAMANHO_QUADRADO, TAMANHO_QUADRADO, PRETO, "")),
             Peca(AZUL, Tile(0, 0, TAMANHO_QUADRADO, TAMANHO_QUADRADO, PRETO, "")),
             Peca(VERDE, Tile(0, 0, TAMANHO_QUADRADO, TAMANHO_QUADRADO, PRETO, ""))]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        janela.fill(BRANCO)
        desenhar_tabuleiro()
        desenhar_pecas(pecas)
        pygame.display.update()

if __name__ == "__main__":
    main()

