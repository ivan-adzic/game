def on_button_pressed_a():
    dot.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    a_bullets.append(game.create_sprite(dot.get(LedSpriteProperty.X),
            dot.get(LedSpriteProperty.Y) - 1))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    dot.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

a_bullets: List[game.LedSprite] = []
dot: game.LedSprite = None
dot = game.create_sprite(2, 4)
a_bullets = []
a_enemies: List[game.LedSprite] = []
game.set_life(3)

def on_every_interval():
    for enemie in a_enemies:
        if enemie.get(LedSpriteProperty.Y) == 4:
            enemie.delete()
            a_enemies.remove_at(a_enemies.index(enemie))
        if not (enemie.is_deleted()):
            enemie.change(LedSpriteProperty.Y, 1)
loops.every_interval(1000, on_every_interval)

def on_every_interval2():
    for bullet in a_bullets:
        if bullet.get(LedSpriteProperty.Y) == 0:
            bullet.delete()
            a_bullets.remove_at(a_bullets.index(bullet))
        if not (bullet.is_deleted()):
            bullet.change(LedSpriteProperty.Y, -1)
loops.every_interval(500, on_every_interval2)

def on_every_interval3():
    a_enemies.append(game.create_sprite(randint(0, 4), -1))
    basic.pause(500)
loops.every_interval(3000, on_every_interval3)

def on_every_interval4():
    for bullet2 in a_bullets:
        for enemie2 in a_enemies:
            if bullet2.is_touching(enemie2):
                enemie2.delete()
                a_enemies.remove_at(a_enemies.index(enemie2))
                bullet2.delete()
                a_bullets.remove_at(a_bullets.index(bullet2))
loops.every_interval(100, on_every_interval4)
