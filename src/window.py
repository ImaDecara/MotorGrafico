import moderngl
import pyglet

class Window(pyglet.window.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        self.ctx = moderngl.create_context()
        self.scene = None

    def on_mouse_press(self, x, y, button, modifiers):
        if self.scene is None:
            return
        u = x / self.width
        v = y / self.height
        self.scene.on_mouse_press(u, v)

    def set_scene(self, scene):
        self.scene = scene
        scene.start()

    def on_draw(self):
        self.clear()
        self.ctx.enable(moderngl.DEPTH_TEST)
        self.ctx.clear(0.0, 0.0, 0.0, 1.0, depth=1.0)
        if self.scene:
            self.scene.render()

    def on_resize(self, width, height):
        self.ctx.viewport = (0, 0, width, height)
        if self.scene:
            self.scene.on_resize(width, height)

    def run(self):
        pyglet.app.run()