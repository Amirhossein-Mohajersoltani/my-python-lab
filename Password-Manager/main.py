from tkinter import *
from tkinter import messagebox
from tkinter import Toplevel
from random import choice, randint, shuffle
import pyperclip
import json

from sympy.ntheory.factor_ import ecm_msg


# ---------------------------- SHOW INFORMATION ------------------------------- #

def show_info():
    with open("data.json") as data_file:
        content = json.load(data_file)
        websites = ""
        for website in content:
            websites += website + "\n\n"
        messagebox.showinfo(title="Websites:", message=websites)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def search():
    website_name = website_entry.get()
    with open("data.json") as data_file:
        content = json.load(data_file)
        try:
            courses = "\n"
            counter = 1
            for course_name,course_url in content[website_name]["courses"].items():
                courses += f"{counter}-\nname: {course_name}\nurl: {course_url}\n"
                counter += 1

            certificates = "\n"
            counter = 1
            for certificate_name,certificate_url in content[website_name]["certificates"].items():
                certificates += f"{counter}-\nname: {certificate_name}\nurl: {certificate_url}\n"
                counter += 1


            # messagebox.showinfo(
            #     title=website_name,
            #     message=f'this is the detail of website {website_name}:\n\nEmail: {content[website_name]["email"]}\n\nPassword: {content[website_name]["password"]}\n\nCourses: {courses}\nCertificates: {certificates}')
            top = Toplevel()
            top.title(f"{website_name} Details")

            text = Text(top, wrap='word', width=60, height=15)
            text.pack(padx=10, pady=10)

            # Insert content into Text widget
            detail_text = (
                f"This is the detail of website {website_name}:\n\n"
                f"Email: {content[website_name]['email']}\n\n"
                f"Password: {content[website_name]['password']}\n\n"
                f"Courses: {courses}\n"
                f"Certificates: {certificates}"
            )
            text.insert('1.0', detail_text)
            text.config(state='disabled')
        except:
            messagebox.showerror(title="Oops!",message=f"there is no detail for website {website_name}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    certificates = {}
    courses = {}
    if course_name_entry.get() and course_url_entry.get():
        courses[course_name_entry.get()] = course_url_entry.get()
    if certificate_name_entry.get() and certificate_url_entry.get():
        certificates[certificate_name_entry.get()] = certificate_url_entry.get()

    new_data = {
        website:{
            "email":email,
            "password":password,
            "certificates":certificates,
            "courses":courses,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data,data_file)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data,data_file)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            course_name_entry.delete(0, END)
            course_url_entry.delete(0, END)
            certificate_name_entry.delete(0, END)
            certificate_url_entry.delete(0, END)

# ---------------------------- UPDATE ------------------------------- #

def update():
    # Base
    website = website_entry.get()
    # New Date
    email = email_entry.get()
    password = password_entry.get()
    course_name = course_name_entry.get()
    course_url = course_url_entry.get()
    certificate_name = certificate_name_entry.get()
    certificate_url = certificate_url_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Oops!", message=f"there is no detail")
    else:
        try:
            if email:
                data[website]["email"] = email
            if password:
                data[website]["password"] = password
            if certificate_name and certificate_url:
                data[website]["certificates"][certificate_name] = certificate_url
            if course_name and course_url:
                data[website]["courses"][course_name] = course_url
            with open("data.json", "w") as data_file:
                json.dump(data, data_file)
        except KeyError:
            messagebox.showerror(title="Oops!", message=f"there is no detail for website {website}")
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        course_name_entry.delete(0, END)
        course_url_entry.delete(0, END)
        certificate_name_entry.delete(0, END)
        certificate_url_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

courses_name_label = Label(text="Course Name:")
courses_name_label.grid(row=4, column=0)

courses_url_label = Label(text="Course URL:")
courses_url_label.grid(row=5, column=0)

certificates_name_label = Label(text="Certificate Name:")
certificates_name_label.grid(row=6, column=0)

certificates_url_label = Label(text="Certificate URL:")
certificates_url_label.grid(row=7, column=0)


#Entries
website_entry = Entry(width=53)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "ah.mohajersoltani@gmail.com")


password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

course_name_entry = Entry(width=52)
course_name_entry.grid(row=4, column=1, columnspan=2)

course_url_entry = Entry(width=52)
course_url_entry.grid(row=5, column=1, columnspan=2)

certificate_name_entry = Entry(width=52)
certificate_name_entry.grid(row=6, column=1, columnspan=2)

certificate_url_entry = Entry(width=52)
certificate_url_entry.grid(row=7, column=1, columnspan=2)

# Buttons
search_button = Button(text="Search",command=search,width=15)
search_button.grid(row=1,column=2)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=8, column=1, columnspan=2)

update_button = Button(text="Update", width=44, command=update)
update_button.grid(row=9, column=1, columnspan=2)

show_info_button = Button(text="show websites", width=44, command=show_info)
show_info_button.grid(row=10, column=1, columnspan=2)

window.mainloop()



