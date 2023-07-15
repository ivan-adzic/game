input.onButtonPressed(Button.A, function () {
    dot.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.AB, function () {
    list.push(game.createSprite(dot.get(LedSpriteProperty.X), dot.get(LedSpriteProperty.Y) - 1))
})
input.onButtonPressed(Button.B, function () {
    dot.change(LedSpriteProperty.X, 1)
})
let list: game.LedSprite[] = []
let dot: game.LedSprite = null
dot = game.createSprite(2, 4)
list = []
loops.everyInterval(500, function () {
    for (let value of list) {
        if (value.get(LedSpriteProperty.Y) == 0) {
            value.delete()
            list.removeAt(list.indexOf(value))
        }
        if (!(value.isDeleted())) {
            value.change(LedSpriteProperty.Y, -1)
        }
    }
})
