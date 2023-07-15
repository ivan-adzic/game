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
