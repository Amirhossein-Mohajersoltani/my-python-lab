from tkinter import *
from nutritionix import Nutritionix
from sheety import Sheety
import datetime as dt

class UserInterface:
    def __init__(self, nutrition: Nutritionix, sheety: Sheety):
        self.nutrition = nutrition
        self.sheety = sheety

        self.exercise = None
        self.duration = None
        self.calories = None
        self.date = None
        self.time = None

        self.window = Tk()
        self.window.config(bg='white', padx=70,pady=30)
        self.window.title("Exercise Tracker")

        self.canvas = Canvas(height=310,width=216, highlightthickness=0, bg='white')
        logo = PhotoImage(file="./images/exercise_logo.png")
        self.canvas.create_image(108,155,image=logo)
        self.canvas.grid(row=0, column=0, columnspan=2)

        # Entries
        self.query_entry = Entry(highlightthickness=5, highlightbackground="blue", width=30)
        self.query_entry.grid(row=1, column=1,padx=10, pady=10)

        # Labels
        # Query
        self.query_label = Label(text ="What did you do?", font=("Arial", 10, "bold"), bg="white", fg="black")
        self.query_label.grid(row=1, column=0)
        # Date
        self.date_label = Label(font=("Arial", 10, "bold"), bg="white", fg="black")
        self.date_label.grid(row=3, column=0)
        # Time
        self.time_label = Label(font=("Arial", 10, "bold"), bg="white", fg="black")
        self.time_label.grid(row=3, column=1)
        # Exercise Type
        self.exercise_label = Label(text=f"Exercise: ", font=("Arial", 10, "bold"), bg="white", fg="black")
        self.exercise_label.grid(row=3, column=2)
        # Duration
        self.duration_label = Label(text=f"Duration: ", font=("Arial", 10, "bold"), bg="white", fg="black")
        self.duration_label.grid(row=4, column=0)
        # Calories
        self.calories_label = Label(text="Calories", font=("Arial", 10, "bold"), bg="white", fg="black")
        self.calories_label.grid(row=4, column=1)

        # button
        submit_button = Button(text="Submit", foreground="white", background="green",width=40, command=self.submit)
        submit_button.grid(row=2, column=0, columnspan=3, pady=10)

        self.set_date_time()

        self.window.mainloop()


    def submit(self):
        # query process
        query = self.query_entry.get()
        processed_data = self.nutrition.post_nutritionix_data(query=query)
        for exercise in processed_data['exercises']:
            self.set_labels_text(exercise)
            self.sheety.post_data(self.date, self.time, self.exercise, self.duration, self.calories)

    def set_labels_text(self, exer):
        self.set_date_time()
        self.exercise = exer["user_input"]
        self.exercise_label.config(text=self.exercise)
        self.duration = exer["duration_min"]
        self.duration_label.config(text=self.duration)
        self.calories = exer["nf_calories"]
        self.calories_label.config(text=self.calories)

    def set_date_time(self):
        now = dt.datetime.now()
        # date
        self.date = now.strftime("20%y/%m/%d")
        self.date_label.config(text=self.date)
        # time
        self.time = now.strftime("%H:%M:%S")
        self.time_label.config(text=self.time)





