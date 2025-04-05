#mplement an 'eraser' on a canvas.

#The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

import tkinter as tk

Canvas_Width:int=500
Canvas_Height:int=500

Cell_Size:int=40
Eraser_Size:int=20

class EraserCanvas:
    def __init__(self,root):
        self.root=root
        self.canvas=tk.Canvas(root,width=Canvas_Width,height=Canvas_Height)
        self.canvas.pack()

        self.cells={}  #Store references to each cell
        self.draw_grid()


        # create eraser that move with the movement of mouse
        self.Eraser=self.canvas.create_rectangle(0,0,Eraser_Size, Eraser_Size, outline="red" ,width=2 )
       
        # Bind mouse motion for erasing effect
        self.canvas.bind("<B1-Motion>", self.erase)


    def draw_grid(self):
     """Draws a grid of blue cells"""
     for y in range(0,Canvas_Height,Cell_Size):
        for x in range(0,Canvas_Width,Cell_Size):
           cell=self.canvas.create_rectangle (x,y, x + Cell_Size, y+Cell_Size ,fill="blue" ,outline="white")
           self.cells[(x,y)]=cell

    def erase(self, event):
        """Moves eraser and erases touched cells"""
        x, y = event.x, event.y
        self.canvas.coords(self.erase, x, y, x + Eraser_Size, y + Eraser_Size)

        # Find and erase cells within the eraser
        for (cx, cy), cell in self.cells.items():
            if cx < x + Eraser_Size and cx + Cell_Size > x and cy < y + Eraser_Size and cy + Cell_Size > y:
                self.canvas.itemconfig(cell, fill="white")            



# Run the application
root = tk.Tk()
root.title("Canvas Eraser")
app = EraserCanvas(root)
root.mainloop()