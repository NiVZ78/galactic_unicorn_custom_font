# IMPORTS
from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN as DISPLAY
import time

# INITIALISE GALACTIC UNICORN
gu = GalacticUnicorn()
graphics = PicoGraphics(DISPLAY)

width = GalacticUnicorn.WIDTH
height = GalacticUnicorn.HEIGHT

gu.set_brightness(0.3)

# FONT DATA
# x,y are unused - could be used for drawing above below line
# w, h are width and height
# s is spacing
# data is binary bit representation of pixels, starting at top left

font3x5 = {
            "0": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111101101101111},
            "1": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b110010010010111},
            "2": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111001111100111},
            "3": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111001011001111},
            "4": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b101101111001001},
            "5": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111100111001111},
            "6": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111100111101111},
            "7": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111001010010010},
            "8": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111101111101111},
            "9": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111101111001111},
            "A": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b010101111101101},
            "C": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b011100100100011},
            "E": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111100110100111},
            "F": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111100110100100},
            "I": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111010010010111},
            "L": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b100100100100111},
            "N": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111101101101101},
            "O": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111101101101111},
            "R": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b110101110101101},
            "S": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b011100010001110},
            "P": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111101111100100},
            ":": {"x":0,"y":0,"w":1,"h":5,"s":1,"data":0b01010},
            ".": {"x":0,"y":0,"w":1,"h":5,"s":1,"data":0b00001}
        }



font4x5 = {
            "0": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b01101001100110010110},
            "1": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b110010010010111},
            "2": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b11100001011110001111},
            "3": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b11100001011000011110},
            "4": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b10011001011100010001},
            "5": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b11111000111000011110},
            "6": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b01111000111010010110},
            "7": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b11110001001001000100},
            "8": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b01101001011010010110},
            "9": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b01101001011100011110},
            "A": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b01101001100111111001},
            "B": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b11101001111010011110},
            "C": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b01111000100010000111},
            "D": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b11101001100110011110},
            "E": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b11111000111010001111},
            "F": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b11111000111010001000},
            "G": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b01111000101110010111},
            "H": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b10011001111110011001},
            "I": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111010010010111},
            "J": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111001001001110},
            "K": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b10011010110010101001},
            "L": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b10001000100010001111},
            "M": {"x":0,"y":0,"w":5,"h":5,"s":1,"data":0b1000111011101011000110001},
            "N": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b10011101101110011001},
            "O": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b01101001100110010110},
            "P": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b11101001100111101000},
            "Q": {"x":0,"y":0,"w":5,"h":5,"s":1,"data":0b0110010010100101011001111},
            "R": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b11101001100111101001},
            "S": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b01111000011000011110},
            "T": {"x":0,"y":0,"w":5,"h":5,"s":1,"data":0b1111100100001000010000100},
            "U": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b10011001100110010110},
            "V": {"x":0,"y":0,"w":5,"h":5,"s":1,"data":0b1000110001100010101000100},
            "X": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b10011001011010011001},
            "Y": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b10011001011100011110},
            "Z": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b11110001011010001111},
            
    }


# DRAW A SINGLE CHARACTER
@micropython.native  # noqa: F821
def draw_char(d,x,y,f):
    # LOOP THROUGH ROWS
    for i in range(f[d]["h"]):
        # LOOP THROUGH COLUMNS
        for j in range(f[d]["w"]):
            # IF THIS BIT IS SET THEN DRAW A PIXEL
            if f[d]["data"] & (0b1 << ((i*f[d]["w"])+j)):
                graphics.pixel(f[d]["w"]-1-j+x,f[d]["h"]-1-i+y)

# DRAW A STRING
@micropython.native  # noqa: F821
def draw_text(s,x,y,f,d=1):
    
    # LEFT JUSTIFIED
    if d == 1:
        for i in range(len(s)):
            draw_char(s[i],x,y,f)
            x += f[s[i]]["w"] + f[s[i]]["s"]
    else:
    # RIGHT JUSTIFIED
        for i in reversed(range(len(s))):
            x -= f[s[i]]["w"]
            draw_char(s[i],x,y,f)
            x -= f[s[i]]["s"]
        
# FUNCTION TO DRAW A DUMMY BASKETBALL SCOREBOARD SHOWING BBL TROPHY 2023 FINAL SCORE
def draw_scoreboard():
    graphics.set_pen(graphics.create_pen(0,0,0))
    graphics.clear()
    graphics.set_pen(graphics.create_pen(255,255,255))

    #PERIOD
    draw_text("P4",53,0,font3x5,-1)

    #CLOCK
    draw_text("00:00",53,6,font3x5,-1)

    #HOME
    draw_text("CAL",0,0,font4x5)
    draw_text("73",30,0,font4x5,-1)

    #AWAY
    draw_text("CHE",0,6,font4x5)
    draw_text("70",30,6,font4x5,-1)

    gu.update(graphics)

# INITIAL DRAW
draw_scoreboard()

# MAIN LOOP
while True:
    # adjust brightness with LUX + and -
    # LEDs take a couple of secs to update, so adjust in big (10%) steps
    if gu.is_pressed(GalacticUnicorn.SWITCH_BRIGHTNESS_UP):
        gu.adjust_brightness(+0.1)
        draw_scoreboard()
        print(f"Brightness set to {gu.get_brightness()}")

    if gu.is_pressed(GalacticUnicorn.SWITCH_BRIGHTNESS_DOWN):
        gu.adjust_brightness(-0.1)
        draw_scoreboard()
        print(f"Brightness set to {gu.get_brightness()}")

    # pause for a moment (important or the USB serial device will fail)
    time.sleep(0.1)
