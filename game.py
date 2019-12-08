from engine.pygame_engine import PyGameEngine, EventNotify
import pygame


class Game:
    engine = 0
    running = True
    render_func = 0
    preload_func = 0
    posload_func = 0
    clock_rate = 0
    clock = 0
    data = {}

    def __init__(self, title, clock_rate, width, height):
        self.title = title
        self.clock_rate = clock_rate
        self.clock = pygame.time.Clock()
        self.height = height
        self.width = width
        self.keymap_notify = EventNotify("keymap")

    def on_key(self, key, func):
        self.keymap_notify.add_handler(key, func)

    def on_render(self, render):
        self.render_func = render

    def start(self):
        self.engine = PyGameEngine(title=self.title, height=self.height, width=self.width)
        if self.preload_func != 0:
            self.preload_func(self)
        self.engine.show()
        if self.posload_func != 0:
            self.posload_func(self)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    self.keymap_notify.notify(event.key, event)
            self.render_func(self)
            self.clock.tick(self.clock_rate)

    def get_screen(self):
        return self.engine.get_screen()

    def pos_load(self, func):
        self.posload_func = func

    def pre_load(self, func):
        self.preload_func = func

    def set_data(self, key, value):
        self.data[key] = value

    def get_data(self, key):
        if key in self.data:
            return self.data[key]