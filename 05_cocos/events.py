import cocos
from cocos.actions import *
import cocos.actions.grid3d_actions


class Game(cocos.layer.ColorLayer):
    is_event_handler = True

    def __init__(self):
        super(Game, self).__init__(64, 64, 224, 255)

        self.sprite = cocos.sprite.Sprite('assets/spaceship.png')
        self.sprite.position = 320, 240
        self.sprite.scale = 1
        self.add(self.sprite, z=1)
        self.keys_pressed = set()

    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)
        self.update_text()

        self.sprite.do(grid3d_actions.Twirl(grid=(32, 24), duration=2))

    def on_key_release(self, key, modifiers):
        self.keys_pressed.remove(key)
        self.update_text()

    def update_text(self):
        print(self.keys_pressed)


cocos.director.director.init()
cocos.director.director.run(cocos.scene.Scene(Game()))
