import cocos
from cocos.actions import *


class HelloWorld(cocos.layer.ColorLayer):
    def __init__(self):
        # blueish color
        super(HelloWorld, self).__init__(64, 64, 224, 255)

        sprite = cocos.sprite.Sprite('assets/spaceship.png')
        sprite.position = 320, 240
        sprite.scale = 3
        self.add(sprite, z=1)
        scale = ScaleBy(3, duration=0.2)

        sprite.do(Repeat(Reverse(scale) + scale))

cocos.director.director.init()
cocos.director.director.run(cocos.scene.Scene(HelloWorld()))
