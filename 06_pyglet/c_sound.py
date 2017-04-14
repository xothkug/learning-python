import pyglet

window = pyglet.window.Window()

sound = pyglet.resource.media('assets/shoot.wav', streaming=False)


@window.event
def on_draw():
    window.clear()
    sound.play()


pyglet.app.run()
