from cs1graphics import *
from TallySheet import TallySheet
import sys

class TallySheetWithGraph(TallySheet):
    def __init__(self, minVal, maxVal):
        super().__init__(minVal, maxVal)

    def drawBar(self):
        height_scale = 10
        bar_width = 25
        canvas = Canvas(1100,1000)
        x = 15
        y = 750
        total_dimensions = [500,400]

        for i in range(len(self._tallies)):
            if self._tallies[i] * height_scale != 0:
                bar_height = self._tallies[i] * height_scale
            else:
                bar_height = 1
            bar = Rectangle(bar_width,bar_height)
            bar.setFillColor("dark green")
            bar.adjustReference(0, bar_height / 2)

            canvas.add(bar)
            text = Text(self._makeLabel(i), 10)
            dimensions = text.getDimensions()
            total_dimensions[0] += dimensions[0]
            canvas.add(text)
            text.moveTo(x, y + 7)
            bar.moveTo(x, y)
            x += 40
        return canvas

if __name__ == '__main__':
    categories = TallySheetWithGraph('A','Z')
    try:
        with open('message.txt') as file:
            for list in file:
                list = list.split()
                for word in list:
                    for char in word:
                        if char.isalpha():
                            categories.increment(char.upper())
        
    except FileNotFoundError:
        print("File is not found")


    categories.writeTable(sys.stdout) 
    categories.drawBar()
    print()


