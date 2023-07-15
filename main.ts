input.onButtonPressed(Button.A, function () {
    dot.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.AB, function () {
    a_bullets.push(game.createSprite(dot.get(LedSpriteProperty.X), dot.get(LedSpriteProperty.Y) - 1))
})
input.onButtonPressed(Button.B, function () {
    dot.change(LedSpriteProperty.X, 1)
})
let a_bullets: game.LedSprite[] = []
let dot: game.LedSprite = null
dot = game.createSprite(2, 4)
a_bullets = []
let a_enemies: game.LedSprite[] = []
game.setLife(3)
loops.everyInterval(1000, function () {
    for (let enemie of a_enemies) {
        if (enemie.get(LedSpriteProperty.Y) == 4) {
            enemie.delete()
            a_enemies.removeAt(a_enemies.indexOf(enemie))
            game.removeLife(1)
        }
        if (!(enemie.isDeleted())) {
            enemie.change(LedSpriteProperty.Y, 1)
        }
    }
})
/**
 * Check if Bullet has reached the top of the screen
 */
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
loops.everyInterval(3000, function () {
    a_enemies.push(game.createSprite(randint(0, 4), -1))
    basic.pause(500)
})
loops.everyInterval(100, function () {
    for (let bullet of a_bullets) {
        for (let enemie of a_enemies) {
            game.addScore(1)
            if (bullet.isTouching(enemie)) {
                enemie.delete()
                a_enemies.removeAt(a_enemies.indexOf(enemie))
                bullet.delete()
                a_bullets.removeAt(a_bullets.indexOf(bullet))
            }
        }
    }
})
