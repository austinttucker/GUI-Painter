import tkinter as tk
from tkinter import colorchooser, filedialog as fd
import PIL.ImageGrab as ImageGrab
class Paint:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint")
        self.root.geometry("800x600")

        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=5, sticky="nsew")

        self.pen_color = "black"
        self.pen_size = tk.DoubleVar()  # This sets the brush size to the number on the scale/slider
        self.shape='circle'

        self.canvas.bind("<B1-Motion>", self.paint)
        self.buttons()

    def buttons(self):
        self.new_color = tk.Button(self.canvas, text='Change Color', command=self.change_color)     # Button that shows a huge scale of colors to choose from
        self.new_color.grid(row=3, column=1, columnspan=1, sticky='ew')
        self.pen_size_label = tk.Label(self.canvas, text='Pen Size:', bg='white')
        self.pen_size_label.grid(row=1, column=0, columnspan=1)
        self.pen_slider = tk.Scale(self.canvas, variable=self.pen_size, from_=1, to=40, orient='horizontal')    # A slider of the size of the paint brush
        self.pen_slider.grid(row=1, column=1, columnspan=4, sticky='ew')
        self.clear = tk.Button(self.canvas, text='Clear Canvas', command=self.clear_canvas)     # Button that erases all paint on the canvas
        self.clear.grid(row=3, column=2, columnspan=1, sticky='ew')
        self.brush_shape_label = tk.Label(self.canvas, text='Brush Shapes:', bg='white')
        self.brush_shape_label.grid(row=2, column=0, columnspan=1)
        self.brush_square = tk.Button(self.canvas, text='Square', command=self.square)
        self.brush_square.grid(row=2, column=1, columnspan=1, sticky='ew')
        self.set_brush_oval = tk.Button(self.canvas, text='Oval', command=self.oval)
        self.set_brush_oval.grid(row=2, column=2, columnspan=1, sticky='ew')
        self.set_brush_circle = tk.Button(self.canvas, text='Circle', command=self.circle)
        self.set_brush_circle.grid(row=2, column=3, columnspan=1, sticky='ew')
        self.set_brush_rectangle = tk.Button(self.canvas, text='Rectangle', command=self.rectangle)
        self.set_brush_rectangle.grid(row=2, column=4, columnspan=1, sticky='ew')
        self.save = tk.Button(self.canvas, text='Save Image', command=self.save_image)    # This creates a button that saves an image of the canvas
        self.save.grid(row=3, column=3, columnspan=1, sticky='ew')
        self.quit = tk.Button(self.canvas, text='Exit', command=self.root.quit)
        self.quit.grid(row=3, column=4, columnspan=1, sticky='ew')
        self.other = tk.Label(self.canvas, text='Other Options:', bg='white')
        self.other.grid(row=3, column=0, columnspan=1)

    def save_image(self):
        fileLocation = fd.asksaveasfilename(defaultextension='png')
        x = root.winfo_x()
        y = root.winfo_y()
        image = ImageGrab.grab(bbox=(x,y,x+800,y+600))
        image.show()
        image.save(fileLocation)

    def square(self):
        self.shape = 'square'

    def rectangle(self):
        self.shape = 'rectangle'

    def oval(self):
        self.shape = 'oval'

    def circle(self):
        self.shape = 'circle'

    def clear_canvas(self):
        self.canvas.delete('all')           # This command erases all paint on the canvas


    def change_color(self):
        self.pen_color = tk.colorchooser.askcolor(color=self.pen_color)[1]

    def paint(self, event):
        x1, y1 = event.x - self.pen_size.get(), event.y - self.pen_size.get()
        x2, y2 = event.x + self.pen_size.get(), event.y + self.pen_size.get()
        if self.shape == 'circle':
            self.canvas.create_oval(x1, y1, x2, y2, fill=self.pen_color, outline=self.pen_color)
        elif self.shape == 'square':
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.pen_color, outline=self.pen_color)
        elif self.shape == 'oval':
            self.canvas.create_oval(x1-(self.pen_size.get()*2), y1, x2+(self.pen_size.get()*2), y2, fill=self.pen_color, outline=self.pen_color)
        elif self.shape == 'rectangle':
            self.canvas.create_rectangle(x1-(self.pen_size.get()*2), y1, x2+(self.pen_size.get()*2), y2, fill=self.pen_color, outline=self.pen_color)


if __name__ == "__main__":
    root = tk.Tk()
    root.rowconfigure(1, weight=1)
    root.columnconfigure(0, weight=1)
    app = Paint(root)
    root.mainloop()