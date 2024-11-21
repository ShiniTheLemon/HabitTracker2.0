try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("Habit Tracker2.0")  # title of the GUI window
        self.maxsize(900, 600)  # specify the max size the window can expand to
        self.config(bg="skyblue")  # specify background color
        self.resizable(False, False)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others

        self.left_frame = tk.Frame(self, width=200, height=500, bg='grey')
        self.left_frame.grid(row=0, column=0, padx=10, pady=5)
        self.tool_bar = tk.Frame(self.left_frame, width=180, height=185)
        self.tool_bar.grid(row=3, column=0, padx=5, pady=5)


        tk.Button(self.tool_bar, text="Add A Habit", relief=tk.RAISED).grid(row=0, column=0, padx=5, pady=5)  # ipadx is padding inside the Label widget
        tk.Button(self.tool_bar, text="Edit My Habits", relief=tk.RAISED).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(self.tool_bar, text="Track My Habits", relief=tk.RAISED).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(self.tool_bar, text="View My Progress", relief=tk.RAISED).grid(row=3, column=0, padx=5, pady=5)



        self.right_frame = tk.Frame(self, width=650, height=500, bg='grey')
        self.right_frame.grid(row=0, column=1, padx=10, pady=5)

        container = tk.Frame(self.right_frame)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        maxsize=controller.maxsize

        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()