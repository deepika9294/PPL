from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser, filedialog, messagebox
import PIL.ImageGrab as ImageGrab


class Paint():
    def __init__(self, root):
        self.root = root
        self.root.title("MyPaint")
        self.root.geometry("800x520")
        self.root.configure(background="white")
        self.root.resizable(0, 0)
        self.pen_color = "black"
        self.eraser_color = "white"
        self.color_frame = LabelFrame(self.root, text="Color", font=(
            "arial,15"), bd=5, relief=RIDGE, bg="white")
        self.color_frame.place(x=0, y=0, width=76, height=185)

        # self.canvas_shapes_frame = LabelFrame(self.root, text="Shapes", font=(
        #     "arial", 15), bd=5, relief=RIDGE, bg="white")
        # self.canvas_shapes_frame.place(x=0, y=105, width=76, height=80)

        colors = ["#000000", "#FFFFFF", "#FF0000", "#00FF00",
                  "#0000FF", "#FFFF00", "#00FFFF", "#FF00FF", "#FFFACD", "#F5DEB3", "#C0C0C0", "#DEB887"]
        i = j = 0
        for color in colors:
            Button(self.color_frame, bg=color, bd=2, relief=RIDGE,
                   width=1, height=2, command=lambda col=color: self.select_color(col)).grid(row=i, column=j)
            i += 1
            if i == 3 or i == 6:
                i = 0
                j += 1

        self.color_other_button = Button(
            self.color_frame, text="Others", bd=4, bg="white", command=self.color_other, width=8, relief=RIDGE)
        self.color_other_button.place(x=0, y=130, width=68)

        self.eraser_button = Button(
            self.root, text="Eraser", bd=4, bg="white", command=self.eraser, width=8, relief=RIDGE)
        self.eraser_button.place(x=0, y=187, width=76)

        self.clear_button = Button(
            self.root, text="Clear", bd=4, bg="white", command=lambda: self.canvas.delete("all"), width=8, relief=RIDGE)
        self.clear_button.place(x=0, y=217, width=76)

        self.save_button = Button(
            self.root, text="Save", bd=4, bg="white", command=self.save_image, width=8, relief=RIDGE)
        self.save_button.place(x=0, y=247, width=76)

        self.canvas_color_button = Button(
            self.root, text="Canvas", bd=4, bg="white", command=self.canvas_color, width=8, relief=RIDGE)
        self.canvas_color_button.place(x=0, y=277, width=76)

        # creating  a scale for pen and eraser
        self.pen_size_scale_frame = LabelFrame(
            self.root, text="Size", bd=5, bg="white", font=("arial", 15, "bold"), relief=RIDGE)
        self.pen_size_scale_frame.place(x=0, y=310, height=200, width=76)
        self.pen_size = Scale(self.pen_size_scale_frame,
                              orient=VERTICAL, from_=50, to=0, length=170)
        self.pen_size.set(1)
        self.pen_size.grid(row=0, column=1, padx=15)

        # creating the canvas

        self.canvas = Canvas(self.root, bg="white", bd=5,
                             relief=GROOVE, height=500, width=680)
        self.canvas.place(x=100, y=0)

        # binding the canvas
        self.canvas.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        x1, y1 = (event.x-2), (event.y-2)
        x2, y2 = (event.x+2), (event.y+2)

        self.canvas.create_oval(
            x1, y1, x2, y2, fill=self.pen_color, outline=self.pen_color, width=self.pen_size.get())

    def select_color(self, col):
        self.pen_color = col

    def eraser(self):
        self.pen_color = self.eraser_color

    def color_other(self):
        color = colorchooser.askcolor()
        self.pen_color = color[1]

    def canvas_color(self):
        color = colorchooser.askcolor()
        self.canvas.configure(background=color[1])
        self.eraser_color = color[1]

    def save_image(self):
        try:
            filename = filedialog.asksaveasfilename(defaultextension=".jpg")
            x = self.root.winfo_rootx()+self.canvas.winfo_x()
            y = self.root.winfo_rooty()+self.canvas.winfo_y()

            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()

            ImageGrab.grab().crop((x, y, x1, y1)).save(filename)
            messagebox.showinfo(
                "MyPaint says", "Image is saved as" + str(filename))

        except:
            messagebox.showerror("MyPaint says", "Unable to save image")


if __name__ == "__main__":
    root = Tk()
    p = Paint(root)
    root.mainloop()
