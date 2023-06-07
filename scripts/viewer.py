import tkinter as tk
from PIL import Image, ImageTk

class GIFViewer:
    def __init__(self, path):
        self.idx = 0
        self.frames = []

        # Create the root window
        self.root = tk.Tk()
        self.root.overrideredirect(True)  # This removes the border

        # Load the GIF
        with Image.open(path) as image:
            while True:
                try:
                    self.frames.append(ImageTk.PhotoImage(image.copy()))
                    image.seek(len(self.frames))  # Skip to next frame
                except EOFError:
                    break  # We're done

        # Create a label and add the image to it
        self.label = tk.Label(self.root, image=self.frames[0], borderwidth=0, highlightthickness=0)
        self.label.pack()

        # Allow the window to be dragged around.
        self.label.bind("<Button-1>", self.start_move)
        self.label.bind("<ButtonRelease-1>", self.stop_move)
        self.label.bind("<B1-Motion>", self.do_move)

        # Pressing Escape will quit the application
        self.root.bind("<Escape>", lambda e: self.root.quit())

        # Animate the GIF
        self.root.after(0, self.update_frame)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        dx = event.x - self.x
        dy = event.y - self.y
        self.root.geometry(f"+{self.root.winfo_x()+dx}+{self.root.winfo_y()+dy}")

    def update_frame(self):
        self.idx = (self.idx + 1) % len(self.frames)
        self.label.config(image=self.frames[self.idx])
        self.root.after(100, self.update_frame)  # Change this to adjust the speed

    def run(self):
        self.root.mainloop()

# Replace 'your_gif.gif' with the path to your GIF file
viewer = GIFViewer('../gifs/blockchains.gif')
viewer.run()
