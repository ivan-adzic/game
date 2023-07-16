# Press button "A" to move Dot to the left.

def on_button_pressed_a():
    dot.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

# Launch Bullet by pressing buttons "A+B" together.
# TODO: Could be replaced by e.g. tilting device on "x" axe. 

def on_button_pressed_ab():
    a_bullets.append(game.create_sprite(dot.get(LedSpriteProperty.X),
            dot.get(LedSpriteProperty.Y) - 1))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# Press button "B" to move Dot to the right.

def on_button_pressed_b():
    dot.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global onStartUp
    onStartUp = False
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

a_bullets: List[game.LedSprite] = []
dot: game.LedSprite = None
onStartUp = False
onStartUp = True
dot = game.create_sprite(2, 4)
a_bullets = []
a_enemies: List[game.LedSprite] = []
life = 3
scoore = 0
# Check if Enemy has reached the bottom. 

def on_every_interval():
    global life
    for enemy in a_enemies:
        if enemy.get(LedSpriteProperty.Y) == 4:
            enemy.delete()
            a_enemies.remove_at(a_enemies.index(enemy))
            life += -1
        if not (enemy.is_deleted()):
            enemy.change(LedSpriteProperty.Y, 1)
loops.every_interval(1000, on_every_interval)

# Check if bullet is out of the screen, if yes delete Bullet from the list.

def on_every_interval2():
    for bullet in a_bullets:
        if bullet.get(LedSpriteProperty.Y) == 0:
            bullet.delete()
            a_bullets.remove_at(a_bullets.index(bullet))
        if not (bullet.is_deleted()):
            bullet.change(LedSpriteProperty.Y, -1)
loops.every_interval(500, on_every_interval2)

# Create Enemy every 3 seconds.

def on_every_interval3():
    a_enemies.append(game.create_sprite(randint(0, 4), -1))
    basic.pause(500)
loops.every_interval(3000, on_every_interval3)

# Check if Bullet has hit the Enemy.

def on_every_interval4():
    global scoore
    for bullet2 in a_bullets:
        for enemy2 in a_enemies:
            if bullet2.is_touching(enemy2):
                enemy2.delete()
                a_enemies.remove_at(a_enemies.index(enemy2))
                bullet2.delete()
                a_bullets.remove_at(a_bullets.index(bullet2))
                scoore += 1
    if life <= 0:
        game.set_score(scoore)
        game.game_over()
loops.every_interval(100, on_every_interval4)
