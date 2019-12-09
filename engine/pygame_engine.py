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


class RenderGroup:

    renders = []

    def __init__(self):
        self.renders = []

    def add_render(self, render):
        self.renders.append(render)

    def get_renders(self):
        return self.renders

    def set_renders(self, renders):
        self.renders = renders

    def render(self):
        for render in self.renders:
            if isinstance(render, Sprite):
                render.render()


class Renderable:

    def __init__(self, source):
        self.source = source

    def render(self, screen, x, y):
        screen.blit(self.source, [x, y])


class Sprite(Renderable):
    x = 0
    y = 0

    def __init__(self, sprite_image):
        super().__init__(sprite_image)
        self.size = sprite_image.get_rect().size
        self.sprite_image = sprite_image.convert()

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def render(self, screen):
        super().render(screen, self.x, self.y)
