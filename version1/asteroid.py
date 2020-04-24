import pyglet
from game import resources
from game import load


game_window = pyglet.window.Window(800, 600)
player_ship = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=300)
asteroids = load.asteroids(10)


@game_window.event
def on_draw():
    game_window.clear()
    player_ship.draw()
    for asteroid in asteroids:
        asteroid.draw()


if __name__ == '__main__':
    pyglet.app.run()
