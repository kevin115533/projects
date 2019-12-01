from tkinter import *
from tkinter import messagebox
import math

class CircleArea(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Cicle Area")
        self.grid()
        self._radiusLabel = Label(self, text = "Radius")
        self._radiusLabel.grid(row = 0, column = 0)
        self._radiusVar = DoubleVar()
        self._radiusEntry = Entry(self, textvariable = self._radiusVar)
        self._radiusEntry.grid(row = 0, column = 1)
        self._areaLabel = Label(self, text = "Area")
        self._areaLabel.grid(row = 1, column = 0)
        self._areaVar = DoubleVar()
        self._areaEntry = Entry(self, textvariable = self._areaVar)
        self._areaEntry.grid(row = 1, column = 1)
        self._button = Button(self, text = "Compute", command = self._area)
        self._button.grid(row = 2, column = 0, columnspan = 2)

    def _area(self):
        try:
            radius = self._radiusVar.get()
            area = radius ** 2 * math.pi
            self._areaVar.set(area)
        except ValueError:
            #messagebox.showerror(message = "Error: Bad format", parent = self)
            messagebox.showerror("Error", "Error message")
        
def main():
    CircleArea().mainloop()

main()
