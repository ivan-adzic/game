def on_button_pressed_a():
    dot.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global bullet
    bullet = game.create_sprite(dot.get(LedSpriteProperty.X),
        dot.get(LedSpriteProperty.Y) - 1)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    dot.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

bullet: game.LedSprite = None
dot: game.LedSprite = None
dot = game.create_sprite(0, 4)
bullet = game.create_sprite(0, -1)

def on_every_interval():
    if bullet.get(LedSpriteProperty.Y) == 0:
        bullet.delete()
    if not (bullet.is_deleted()):
        bullet.change(LedSpriteProperty.Y, -1)
loops.every_interval(1000, on_every_interval)
