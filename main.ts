input.onButtonPressed(Button.A, function on_button_pressed_a() {
    dot.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    bullet = game.createSprite(dot.get(LedSpriteProperty.X), dot.get(LedSpriteProperty.Y) - 1)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    dot.change(LedSpriteProperty.X, 1)
})
let bullet : game.LedSprite = null
let dot : game.LedSprite = null
dot = game.createSprite(0, 4)
bullet = game.createSprite(0, -1)
loops.everyInterval(1000, function on_every_interval() {
    if (bullet.get(LedSpriteProperty.Y) == 0) {
        bullet.delete()
    }
    
    if (!bullet.isDeleted()) {
        bullet.change(LedSpriteProperty.Y, -1)
    }
    
})
