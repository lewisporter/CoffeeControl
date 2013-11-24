#!/usr/bin/python

#import modules
import cgi, cgitb
import PIL
import Image

#enable debugging output
cgitb.enable()

# Create instance of FieldStorage 
textInput = cgi.FieldStorage()

#initialise LCD
lcdContents = [[0], [0]]
lcdContents[0] = textInput.getvalue('rowOne')
lcdContents[1] = textInput.getvalue('rowTwo')
background = Image.open("images/lcd/lcdtemplate.png")

#LCD functions
def drawChar(x, y):
    if lcdContents[x][y] == " ":
        pass
    elif lcdContents[x][y] == ".":
        charImage = Image.open("images/lcd/characters/dot.png")
        if x == 0:
            background.paste(charImage, (25 * y + 4 - y, 4), charImage)
        elif x == 1:
            background.paste(charImage, (25 * y + 4 - y, 40), charImage)
        else:
            raise Exception("drawChar function trying to draw on nonexistent row!")


    else:
        charImage = Image.open("images/lcd/characters/" + lcdContents[x][y] + ".png")
        if x == 0:
            background.paste(charImage, (25 * y + 4 - y, 4), charImage)
        elif x == 1:
            background.paste(charImage, (25 * y + 4 - y, 40), charImage)
        else:
            raise Exception("drawChar function trying to draw on nonexistent row!")


def drawLine(line):
    if textInput.getvalue('rowOne') is None and line == 0:
        pass
    elif textInput.getvalue('rowTwo') is None and line == 1:
        pass
    else:
        charsRemaining = len(lcdContents[line]) - 1
        while charsRemaining >= 0:
            drawChar(line, charsRemaining)
            charsRemaining = charsRemaining - 1


def drawDisplay():
    drawLine(0)
    drawLine(1)


#program flow begins here		

drawDisplay()
background.save("output.png")