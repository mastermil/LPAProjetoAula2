#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame as pygame
fundo  = pygame.image.load('MenuBg.png')

from code.Const import WIN_WIDTH,WIN_HEIGHT
from code.Menu import Menu
pygame.init()
class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.window = pygame.display.set_caption("criando MountainShooter")


    game_on = True
    while game_on:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
    pygame.quit()

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass

class Menu:
    def __init__(window):
        window: Surface = window
        surf = pygame.image.load('./asset/MenuBg.png')
        rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        menu_option = 0
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # desenhar menu
            # logica para desenahr titulo menu
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))
            # logica desenhar opções do menu
            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[I], COLOR_YELLOW, (WIN_WIDTH / 2, 200 + 30 * i))
            else:
                self.menu_text(20, MENU_OPTION[I], COLOR_WHITE, (WIN_WIDTH / 2, 200 + 30 * i))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    if event.type == pygame.KEYDOWN:  # testar se alguma tecla foi pressionada
                        if event.key == pygame.K_DOWN:  # testar se seta pra baixo foi pressionada
                            if menu_option < len(MENU_OPTION) - 1:
                                menu_option += 1
                        else:
                            menu_option = 0

                if event.key == pygame.K_UP:  # testar se seta pra cima foi pressionada
                    if menu_option > 0:
                        menu_option -= 1
                    else:
                        menu_option = len(MENU_OPTION) - 1
                if event.key == pygame.K_RETURN:
                    return menu_option


def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
    text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
    text_surf: Surface = text_font.render(text, True, text_color)
    text_rect: Rect = text_surf.get_rect(center=text_center_pos)
    self.window.blit(source=text_surf, dest=text_rect)
