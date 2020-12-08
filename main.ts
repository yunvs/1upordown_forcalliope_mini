function Start () {
    basic.pause(2000)
    ZufÄllige_Zahl = randint(0, 100)
    basic.showString("" + angezeigte_Zahl)
    basic.pause(1000)
    basic.showLeds(`
        # . . . .
        # # . . #
        # . . . #
        # . . # #
        . . . . #
        `)
    basic.pause(1000)
    basic.setLedColor(0x00ff00)
}
input.onButtonPressed(Button.A, function () {
    basic.setLedColor(0xff0000)
    Anzahl_Versuche += 1
    basic.pause(1000)
    if (angezeigte_Zahl > ZufÄllige_Zahl) {
        basic.setLedColor(0xff8000)
        basic.showIcon(IconNames.SmallHeart)
        music.startMelody(music.builtInMelody(Melodies.JumpUp), MelodyOptions.Once)
        basic.showIcon(IconNames.Heart)
        basic.pause(500)
        basic.clearScreen()
        Start()
    } else {
        basic.setLedColor(0x000000)
        music.startMelody(music.builtInMelody(Melodies.Wawawawaa), MelodyOptions.Once)
        basic.showIcon(IconNames.No)
        basic.pause(500)
        basic.showIcon(IconNames.Chessboard)
        basic.pause(500)
        basic.clearScreen()
        basic.showIcon(IconNames.Sad)
        basic.pause(2000)
        game.setScore(Anzahl_Versuche - 1)
        game.gameOver()
    }
})
input.onButtonPressed(Button.B, function () {
    basic.setLedColor(0xff0000)
    Anzahl_Versuche += 1
    basic.pause(1000)
    if (angezeigte_Zahl < ZufÄllige_Zahl) {
        basic.showIcon(IconNames.SmallHeart)
        music.startMelody(music.builtInMelody(Melodies.JumpUp), MelodyOptions.Once)
        basic.showIcon(IconNames.Heart)
        basic.pause(500)
        basic.clearScreen()
        basic.setLedColor(0xff8000)
        Start()
    } else {
        basic.setLedColor(0x000000)
        music.startMelody(music.builtInMelody(Melodies.Wawawawaa), MelodyOptions.Once)
        basic.showIcon(IconNames.No)
        basic.pause(500)
        basic.showIcon(IconNames.Chessboard)
        basic.pause(500)
        basic.clearScreen()
        basic.showIcon(IconNames.Sad)
        basic.pause(2000)
        game.setScore(Anzahl_Versuche - 1)
        game.gameOver()
    }
})
let ZufÄllige_Zahl = 0
let angezeigte_Zahl = 0
let Anzahl_Versuche = 0
basic.setLedColor(0xff0000)
music.startMelody(music.builtInMelody(Melodies.BaDing), MelodyOptions.Once)
basic.pause(2000)
basic.showLeds(`
    . . # . .
    . # # # .
    # . # . #
    . . # . .
    . . # . .
    `)
basic.pause(500)
basic.clearScreen()
basic.showString("or")
basic.showLeds(`
    . . # . .
    . . # . .
    # . # . #
    . # # # .
    . . # . .
    `)
basic.pause(500)
basic.clearScreen()
Anzahl_Versuche = 0
angezeigte_Zahl = randint(40, 60)
basic.setLedColor(0xff8000)
Start()
