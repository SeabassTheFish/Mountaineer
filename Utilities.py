def makeFont(fontSize):
    return createFont("zx_spectrum-7.ttf", fontSize)

def checkButtons(buttonList, x, y):
    for btn in buttonList:
        if btn.xyOver(x, y):
            btn.showClicked()
            return btn.actionTo
    return ""

def intToRGB(input):
    return color(input >> 16 & 255, input >> 8 & 255, input & 255, input >> 24 & 255)
