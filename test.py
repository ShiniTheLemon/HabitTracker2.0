import tkinter
from tkinter import *
from tkinter import font as tkfont
from tkcalendar import Calendar
from datetime import date



import dao



dates=[date(2024, 11, 3), date(2024, 11, 1),date(2024, 11, 13)]


#root = Tk()  # create root window

class App(tkinter.Tk):


    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("Habit Tracker2.0")  # title of the GUI window
        self.maxsize(900, 600)  # specify the max size the window can expand to
        self.config(bg="skyblue")  # specify background color
        self.resizable(False,False)

        self.left_frame = Frame(self, width=200, height=500, bg='grey')
        self.left_frame.grid(row=0, column=0, padx=10, pady=5)

        self.right_frame = Frame(self, width=650, height=500, bg='grey')
        self.right_frame.grid(row=0, column=1, padx=10, pady=5)


        # Create tool bar frame
        self.tool_bar = Frame(self.left_frame, width=180, height=185)
        self.tool_bar.grid(row=2, column=0, padx=5, pady=5)

        self.screen = Frame(self.right_frame, width=600, height=450)
        self.screen.grid(row=0, column=1, padx=5, pady=5)


        # Example labels that serve as placeholders for other widgets


        Button(self.tool_bar, text="Add New Habit", relief=RAISED,command=openNewWindow).grid(row=0, column=0, padx=5, pady=5,
                                                                 ipadx=10)  # ipadx is padding inside the Label widget
        Button(self.tool_bar, text="Edit My Habits", relief=RAISED).grid(row=1, column=0, padx=5, pady=5, ipadx=10)
        Button(self.tool_bar, text="Track My Habits", relief=RAISED).grid(row=2, column=0, padx=5, pady=5, ipadx=10)
        Button(self.tool_bar, text="View My Progress", relief=RAISED).grid(row=3, column=0, padx=5, pady=5, ipadx=10)
        self.calendar()

    def calendar(self):
        cal = Calendar(self.screen, selectmode="day", date_pattern="yyyy-mm-dd")
        cal.tag_config('background')
        color = Calendar.bordercolor = "Blue"
        cal.pack(pady=100, padx=100)

        selected_date = Label(self.screen, text="")
        selected_date.pack(pady=50, padx=50)
        for date in dates:
            dt = date
            print(dt)
            cal.calevent_create(dt, 'Hello World', tags="Message")
            cal.tag_config("Message", background='red', foreground='yellow')

        def update_selected_date():
           selected_date.config(text="Selected Date: " + cal.get_date())



        def grad_date():
            dt = date.today()
            print(dt)
            selected_date.config(text="Selected Date is completed: " + dt)
            dt =dt.strftime("%d-%m-%Y") #strptime(dt, "%Y-%m-%d")
            cal.calevent_create(dt, 'Hello World', tags="Message")
            cal.tag_config("Message", background='red', foreground='yellow')


        cal.bind("<<CalendarSelected>>", lambda event: update_selected_date())




def openNewWindow():
        # Toplevel object which will
        # be treated as a new window

    #master = Tk()
    newWindow = Tk()

        # sets the title of the
        # Toplevel widget
    newWindow.title("New Window")

        # sets the geometry of toplevel
    newWindow.geometry("200x200")

        # A Label widget to show in toplevel
    Label(newWindow,
              text="Username").pack()
    text1=tkinter.Text(newWindow,height=2, width=10)

    text2 = tkinter.Text(newWindow, height=2, width=10)

    def save_input():
        username=text1.get(1.0,"end-1c")
        password=text2.get(1.0,"end-1c")

        print(username,password)
        dao.register_admin(username,password)
        newWindow.destroy()
    button=tkinter.Button(newWindow,text="Save",command=save_input)
    text1.pack()
    Label(newWindow,
              text="Password").pack()
    text2.pack()
    button.pack()





app=App()
app.mainloop()