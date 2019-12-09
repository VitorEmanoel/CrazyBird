from game import Game
from engine.pygame_engine import Sprite, RenderGroup
import pygame

game = Game("CrazyBird", 30, 1280, 512)

birds_group = RenderGroup()

background_image = 0


def game_posload(engine):
    pygame.display.set_icon(pygame.image.load('flappy.ico'))
    bird = Sprite(pygame.image.load('./assets/sprites/yellowbird-midflap.png'))
    birds_group.add_render(bird)
    engine.set_data('bird', bird)
    print(bird.size)


def on_space(event):
    bird = game.get_data('bird')
    bird.move(1, -100)


def game_render(engine):
    game.get_screen().blit(pygame.image.load('./assets/sprites/background-night.png').convert(), [0, 0])
    bird = engine.get_data('bird')
    if bird.y + bird.size[1] < 512:
        bird.move(1, 5)
    bird.render(engine.get_screen())
    pygame.display.flip()


game.on_key(pygame.K_SPACE, on_space)
game.pos_load(game_posload)
game.on_render(game_render)

game.start()
