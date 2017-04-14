import cocos
from cocos.actions import *


class Game(cocos.layer.ColorLayer):
    is_event_handler = True

    def __init__(self):
        super(Game, self).__init__(64, 64, 224, 255)

        sprite = cocos.sprite.Sprite('assets/spaceship.png')
        sprite.position = 320, 240
        sprite.scale = 1
        self.add(sprite, z=1)
        self.keys_pressed = set()

    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)
        self.update_text()

    def on_key_release(self, key, modifiers):
        self.keys_pressed.remove(key)
        self.update_text()

    def update_text(self):
        print(self.keys_pressed)

cocos.director.director.init()
cocos.director.director.run(cocos.scene.Scene(Game()))
