let PT = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    led.plot((PT / 5)%5, PT % 5)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    led.unplot((PT / 5)%5, PT % 5)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    PT = PT+1;
    led.plot((PT / 5)%5, PT % 5)
    basic.pause(100)
    led.unplot((PT / 5)%5, PT % 5)

})
basic.forever(function on_forever() {
})
