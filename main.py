def on_button_pressed_a():
    dot.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    list2.append(game.create_sprite(dot.get(LedSpriteProperty.X),
            dot.get(LedSpriteProperty.Y) - 1))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    dot.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

list2: List[game.LedSprite] = []
dot: game.LedSprite = None
dot = game.create_sprite(2, 4)
list2 = []

def on_every_interval():
    for value in list2:
        if value.get(LedSpriteProperty.Y) == 0:
            value.delete()
            list2.remove_at(list2.index(value))
        if not (value.is_deleted()):
            value.change(LedSpriteProperty.Y, -1)
    basic.show_number(len(list2))
loops.every_interval(500, on_every_interval)
