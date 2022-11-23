def on_button_pressed_a():
    music.play_melody("C5 - A G - B C5 - ", 180)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    basic.show_icon(IconNames.HEART)
basic.forever(on_forever)
