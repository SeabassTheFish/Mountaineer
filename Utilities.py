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

def limCoords(entity, xmin, xmax, ymin, ymax):
    if entity.attributes["x"] < xmin:
        entity.attributes["x"] = xmin
    if entity.attributes["y"] < ymin:
        entity.attributes["y"] = ymin
    if entity.attributes["x"] > xmax:
        entity.attributes["x"] = xmax
    if entity.attributes["y"] > ymax:
        entity.attributes["y"] = ymax
