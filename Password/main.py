from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]  
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website1 = website_input.get()
    email1 = email_input.get()
    password1 = password_input.get()
    new_data = {
        website1: {
            "email": email1,
            "password": password1,
        }
    }

   
    if len(website1) == 0 or len(password1) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leavea any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website1, message=f"These are the details entered: \nEmail: {email1} \nPassword: {password1} \nIs It ok to save?")

    
        if is_ok:
            try:
                with open("data.json", "r") as data:
                    #Reading old data
                    data1 = json.load(data)

            except FileNotFoundError:
                with open("data.json", "w") as data:
                    json.dump(new_data, data, indent= 4)
            else:
                data1.update(new_data)

                with open("data.json", "w") as data:
                    #Saving update data
                    json.dump(data1, data, indent= 4)
            finally:
                    website_input.delete(0, END)
                    email_input.delete(0, END)
                    password_input.delete(0, END)
                    website_input.focus()

def find_password():
    website1 = website_input.get()
    try:
        with open("data.json", "r") as data:
            data1 = json.load(data)

        if website1 in data1:
            messagebox.showinfo(title=website1, message=f"Email: {data1[website1]['email']} \nPassword: {data1[website1]['password']}")
        else: 
            messagebox.showinfo(title="Erros", message=f"No details for the {website1} exist")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
           




# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

password = Label(text="Password")
password.grid(row=3, column=0)


website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()


email_input = Entry(width=40)
email_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=21)
password_input.grid(row=3, column=1)


button_generate = Button(text="Generate Password", command= generate)
button_generate.grid(row=3, column=2)

button_add = Button(text="Add", width=40, command=save)
button_add.grid(row=4, column=1, columnspan=2)

button_search = Button(text="Search", width=13, command=find_password)
button_search.grid(row=1, column=2)

window.mainloop()