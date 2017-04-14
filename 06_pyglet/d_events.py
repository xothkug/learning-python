import pyglet
from pyglet.window import key

window = pyglet.window.Window(800, 600)
sound = pyglet.resource.media('assets/shoot.wav', streaming=False)

image = pyglet.resource.image('assets/spaceship.png')
sprite = pyglet.sprite.Sprite(image)

@window.event
def on_draw():
    window.clear()
    sprite.draw()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.SPACE:
        sound.play()
    if symbol == key.UP:
        sprite.y += 10

pyglet.app.run()
