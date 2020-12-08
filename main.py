def Start():
    global Zufällige_Zahl
    basic.pause(2000)
    ZufÄllige_Zahl = randint(0, 100)
    basic.show_string("" + str((angezeigte_Zahl)))
    basic.pause(1000)
    basic.show_leds("""
        # . . . .
        # # . . #
        # . . . #
        # . . # #
        . . . . #
        """)
    basic.pause(1000)
    basic.set_led_color(0x00ff00)

def on_button_pressed_a():
    global Anzahl_Versuche
    basic.set_led_color(0xff0000)
    Anzahl_Versuche += 1
    basic.pause(1000)
    if angezeigte_Zahl > Zufällige_Zahl:
        basic.set_led_color(0xff8000)
        basic.show_icon(IconNames.SMALL_HEART)
        music.start_melody(music.built_in_melody(Melodies.JUMP_UP), MelodyOptions.ONCE)
        basic.show_icon(IconNames.HEART)
        basic.pause(500)
        basic.clear_screen()
        Start()
    else:
        basic.set_led_color(0x000000)
        music.start_melody(music.built_in_melody(Melodies.WAWAWAWAA),
            MelodyOptions.ONCE)
        basic.show_icon(IconNames.NO)
        basic.pause(500)
        basic.show_icon(IconNames.CHESSBOARD)
        basic.pause(500)
        basic.clear_screen()
        basic.show_icon(IconNames.SAD)
        basic.pause(2000)
        game.set_score(Anzahl_Versuche - 1)
        game.game_over()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Anzahl_Versuche
    basic.set_led_color(0xff0000)
    Anzahl_Versuche += 1
    basic.pause(1000)
    if angezeigte_Zahl < Zufällige_Zahl:
        basic.show_icon(IconNames.SMALL_HEART)
        music.start_melody(music.built_in_melody(Melodies.JUMP_UP), MelodyOptions.ONCE)
        basic.show_icon(IconNames.HEART)
        basic.pause(500)
        basic.clear_screen()
        basic.set_led_color(0xff8000)
        Start()
    else:
        basic.set_led_color(0x000000)
        music.start_melody(music.built_in_melody(Melodies.WAWAWAWAA),
            MelodyOptions.ONCE)
        basic.show_icon(IconNames.NO)
        basic.pause(500)
        basic.show_icon(IconNames.CHESSBOARD)
        basic.pause(500)
        basic.clear_screen()
        basic.show_icon(IconNames.SAD)
        basic.pause(2000)
        game.set_score(Anzahl_Versuche - 1)
        game.game_over()
input.on_button_pressed(Button.B, on_button_pressed_b)

Zufällige_Zahl = 0
angezeigte_Zahl = 0
Anzahl_Versuche = 0
basic.set_led_color(0xff0000)
music.start_melody(music.built_in_melody(Melodies.BA_DING), MelodyOptions.ONCE)
basic.pause(2000)
basic.show_leds("""
    . . # . .
    . # # # .
    # . # . #
    . . # . .
    . . # . .
    """)
basic.pause(500)
basic.clear_screen()
basic.show_string("or")
basic.show_leds("""
    . . # . .
    . . # . .
    # . # . #
    . # # # .
    . . # . .
    """)
basic.pause(500)
basic.clear_screen()
Anzahl_Versuche = 0
angezeigte_Zahl = randint(40, 60)
basic.set_led_color(0xff8000)
Start()