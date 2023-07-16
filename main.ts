// Press button "A" to move Dot to the left.
input.onButtonPressed(Button.A, function () {
    dot.change(LedSpriteProperty.X, -1)
})
// Launch Bullet by pressing buttons "A+B" together.
// TODO: Could be replaced by e.g. tilting device on "x" axe. 
input.onButtonPressed(Button.AB, function () {
    a_bullets.push(game.createSprite(dot.get(LedSpriteProperty.X), dot.get(LedSpriteProperty.Y) - 1))
})
// Press button "B" to move Dot to the right.
input.onButtonPressed(Button.B, function () {
    dot.change(LedSpriteProperty.X, 1)
})
let a_bullets: game.LedSprite[] = []
let dot: game.LedSprite = null
serial.setBaudRate(BaudRate.BaudRate115200)
serial.redirectToUSB()
serial.writeString("Game Start")
dot = game.createSprite(2, 4)
a_bullets = []
let a_enemies: game.LedSprite[] = []
let life = 3
let score = 0
let level = 0
let tmp_level = 0
let play = true
// Check if Enemy has reached the bottom. 
loops.everyInterval(1000, function () {
    for (let enemy of a_enemies) {
        if (enemy.get(LedSpriteProperty.Y) == 4) {
            enemy.delete()
            a_enemies.removeAt(a_enemies.indexOf(enemy))
            life += -1
        }
        if (!(enemy.isDeleted())) {
            enemy.change(LedSpriteProperty.Y, 1)
        }
    }
})
// Check if Bullet has hit the Enemy.
loops.everyInterval(10, function () {
    for (let bullet of a_bullets) {
        for (let enemy of a_enemies) {
            if (bullet.isTouching(enemy)) {
                enemy.delete()
                a_enemies.removeAt(a_enemies.indexOf(enemy))
                bullet.delete()
                a_bullets.removeAt(a_bullets.indexOf(bullet))
                score += 1
            }
        }
    }
    if (life <= 0) {
        game.setScore(score)
        game.gameOver()
    }
})
// Check if bullet is out of the screen, if yes delete Bullet from the list.
loops.everyInterval(500, function () {
    for (let bullet of a_bullets) {
        if (bullet.get(LedSpriteProperty.Y) == 0) {
            bullet.delete()
            a_bullets.removeAt(a_bullets.indexOf(bullet))
        }
        if (!(bullet.isDeleted())) {
            bullet.change(LedSpriteProperty.Y, -1)
        }
    }
})
// Create Enemy every 3 seconds.
loops.everyInterval(2000, function () {
    if (play) {
        a_enemies.push(game.createSprite(randint(0, 4), -1))
        basic.pause(1000)
    }
})
// Create Enemy every 3 seconds.
loops.everyInterval(100, function () {
    level = score / 10
    if (score % 10 == 0 && level != tmp_level) {
        play = false
        tmp_level += 1
        serial.writeString("" + (tmp_level))
        basic.showString("Level")
        basic.showNumber(tmp_level)
        play = true
    }
})
