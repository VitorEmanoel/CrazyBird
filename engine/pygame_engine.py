import pygame
import types


class PyGameEngine:
    screen = 0

    def __init__(self, title, height, width):
        self.width = width
        self.height = height
        self.title = title

    def show(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        pygame.display.flip()

    def get_screen(self):
        return self.screen


class EventNotify:
    keys = {}

    def __init__(self, event_name):
        self.event_nane = event_name

    def add_handler(self, key, func):
        self.keys[key] = func

    def notify(self, event_key, event_object):
        if event_key in self.keys:
            event_func = self.keys[event_key]
            if isinstance(event_func, types.FunctionType):
                event_func(event_object)


class Sprite:
    x = 0
    y = 0

    def __init__(self, sprite_image):
        self.size = sprite_image.get_rect().size
        self.sprite_image = sprite_image.convert()

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def render(self, screen):
        screen.blit(self.sprite_image, [self.x, self.y])
