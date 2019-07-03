from tkinter import Tk, Canvas, PhotoImage, mainloop
class ImagePainter():
    #create the window and image then display the image
    def __init__(self, size):
        self.window = Tk()
        self.size = size
        self.img = PhotoImage(width=size, height=size)
    def display(self,gradient, name, type):
        canvas = Canvas(self.window, width=self.size, height=self.size, bg=gradient[0])
        canvas.pack()
        canvas.create_image(((self.size / 2), (self.size/ 2)), image=self.img, state="normal")
        self.img.write(name + type)
        mainloop()