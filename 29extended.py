import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

def search():
    web1 = web_entry.get().title()
    try:
        with open("Password_manager.json") as data_files:
            data = json.load(data_files)
        if web1 in data:
            a = data[web1]["email"]
            b = data[web1]["password"]
            messagebox.showinfo(title="Website", message = f"The email of {web1} is: {a} and password is {b}")
        else:
            if len(web1) == 0:
                messagebox.showinfo(title="Error", message="Please do not leave the field empty")
            else:
                messagebox.showinfo(title = "error", message="No data found")
    except:
        messagebox.showinfo(title="Error", message="Data files does not exist")

def pass_gen():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_list = []

    lett_list = [random.choice(letters) for i in range(random.randint(6,9))]
    num_list = [random.choice(numbers) for i in range(random.randint(1,4))]
    sym_list = [random.choice(symbols) for i in range(random.randint(1,3))]

    pass_list = lett_list + num_list + sym_list

    random.shuffle(pass_list)
    password = ''.join(pass_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
def save():
    website = web_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = { website: { "email" : email, "password": password

    }
    }
    if(len(password)== 0 or len(website)==0):
        messagebox.showinfo(title="oops", message="Please do not leave any fields empty")
    else:
        flag = messagebox.askokcancel(title="Password", message=f"These are the details entered:\n"
                                        f"Website: {website}\nEmail: {email} \nPassword: {password}\n "
                                                                f"Is it ok to save?")
        if flag:
            try:
                with open("Password_manager.json", "r") as data_files:
                    data = json.load(data_files)
                    data.update(new_data)
                with open("Password_manager.json", "w") as v:
                        json.dump(data, v, indent=6)
            except:
                with open("Password_manager.json", "w") as data_files:
                    json.dump(new_data,data_files, indent=6)

        web_entry.delete(0,END)
        password_entry.delete(0, END)

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(height = 200,width = 200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 110, image = logo_img)
canvas.grid(row=0, column =1)

website_label = Label(text="Website")
website_label.grid(row=1, column =0)
web_entry = Entry(width=32)
web_entry.grid(row =1, column =1)
web_entry.focus();
search_button = Button(text="Search", width= 14, command=search)
search_button.grid(row = 1, column = 2)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column =0)
email_entry = Entry(width=50)
email_entry.grid(row =2, column =1,columnspan=2)
email_entry.insert(0,"xyz@gmail.com")
password_label = Label(text ="Password")
password_label.grid(row=3, column =0)
password_entry = Entry(width=32)
password_entry.grid(row =3, column =1)
generate_button = Button(text="Generate Password", command=pass_gen)
generate_button.grid(row=3, column =2)
add_button = Button(text="Add", width=41, command=save)
add_button.grid(row = 4, column =1, columnspan =2)

window.mainloop()