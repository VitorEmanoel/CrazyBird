BODY_RELATIVE = 0
BODY_STATIC = 1
BODY_WORLD = 2
BODY_KINEMATIC = 3


class Physic:
    bodies = []

    def __init__(self):
        self.bodies = []

    def append_body(self, body):
        self.bodies.append(body)

    def get_bodies(self):
        return self.bodies


class Body:
    force = 0

    def __init__(self, body_name, body_type):
        self.body_name = body_name
        self.body_type = body_type

    def add_force(self, force):
        self.force += force

    def apply_force(self, force):
        self.force += force

    def get_force(self):
        return self.force

    def set_force(self, force):
        self.force = force


class StaticBody(Body):

    def __init__(self, body_name):
        super().__init__(body_name, BODY_STATIC)


class RelativeBody(Body):

    def __init__(self, body_name):
        super().__init__(body_name, BODY_RELATIVE)


class WorldBody(Body):

    def __init__(self, body_name):
        super().__init__(body_name, BODY_WORLD)


class KinematicBody(Body):

    def __init__(self, body_name):
        super().__init__(body_name, BODY_KINEMATIC)
