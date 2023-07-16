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

a_bullets: List[game.LedSprite] = []
dot: game.LedSprite = None
serial.set_baud_rate(BaudRate.BAUD_RATE115200)
serial.redirect_to_usb()
serial.write_string("Game Start")
dot = game.create_sprite(2, 4)
a_bullets = []
a_enemies: List[game.LedSprite] = []
life = 3
score = 0
level = 0
tmp_level = 0
play = True
speed = 0
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

# Create Enemy every 3 seconds.

def on_every_interval2():
    if play:
        a_enemies.append(game.create_sprite(randint(0, 4), -1))
        basic.pause(1000)
loops.every_interval(2000 - speed * 100, on_every_interval2)

# Check if Bullet has hit the Enemy.

def on_every_interval3():
    global score
    for bullet in a_bullets:
        for enemy2 in a_enemies:
            if bullet.is_touching(enemy2):
                enemy2.delete()
                a_enemies.remove_at(a_enemies.index(enemy2))
                bullet.delete()
                a_bullets.remove_at(a_bullets.index(bullet))
                score += 1
    if life <= 0:
        game.set_score(score)
        game.game_over()
loops.every_interval(10, on_every_interval3)

# Check if bullet is out of the screen, if yes delete Bullet from the list.

def on_every_interval4():
    for bullet2 in a_bullets:
        if bullet2.get(LedSpriteProperty.Y) == 0:
            bullet2.delete()
            a_bullets.remove_at(a_bullets.index(bullet2))
        if not (bullet2.is_deleted()):
            bullet2.change(LedSpriteProperty.Y, -1)
loops.every_interval(500, on_every_interval4)

# Create Enemy every 3 seconds.

def on_every_interval5():
    global level, play, tmp_level, speed
    level = score / 10
    if score % 10 == 0 and level != tmp_level:
        play = False
        tmp_level += 1
        speed += 1
        serial.write_string("" + str((tmp_level)))
        basic.show_string("Level")
        basic.show_number(tmp_level)
        play = True
loops.every_interval(100, on_every_interval5)
