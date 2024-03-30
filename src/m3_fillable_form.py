import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (6 pts)
#
#   1) Create a tkinter window with the title "Form".
#
#   2) Add a label and an entry box for each of the following pieces of
#      information.
#
#       - Name
#       - Address Line 1
#       - Address Line 2
#       - City
#       - State
#       - Zip Code
#       - Phone Number
#       - Email Address
#
#   3) Add a "Submit" button at the bottom of your form.
#
#   4) Give your form a color theme by changing the colors of your widgets.
#      Also, feel free to change the sizes of the widgets as you see fit.
#
#   5) Make sure you call the window's mainloop() method so your window will
#      appear.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
window = tk.Tk()
window.title("Form")


def submit_form():
    name = name_entry.get()
    address1 = address1_entry.get()
    address2 = address2_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    zip_code = zip_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    
    print("Name:", name)
    print("Address Line 1:", address1)
    print("Address Line 2:", address2)
    print("City:", city)
    print("State:", state)
    print("Zip Code:", zip_code)
    print("Phone Number:", phone)
    print("Email Address:", email)

name_label = tk.Label(window, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=5)

address1_label = tk.Label(window, text="Address Line 1:")
address1_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
address1_entry = tk.Entry(window)
address1_entry.grid(row=1, column=1, padx=10, pady=5)

address2_label = tk.Label(window, text="Address Line 2:")
address2_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
address2_entry = tk.Entry(window)
address2_entry.grid(row=2, column=1, padx=10, pady=5)

city_label = tk.Label(window, text="City:")
city_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
city_entry = tk.Entry(window)
city_entry.grid(row=3, column=1, padx=10, pady=5)

state_label = tk.Label(window, text="State:")
state_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
state_entry = tk.Entry(window)
state_entry.grid(row=4, column=1, padx=10, pady=5)

zip_label = tk.Label(window, text="Zip Code:")
zip_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
zip_entry = tk.Entry(window)
zip_entry.grid(row=5, column=1, padx=10, pady=5)

phone_label = tk.Label(window, text="Phone Number:")
phone_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
phone_entry = tk.Entry(window)
phone_entry.grid(row=6, column=1, padx=10, pady=5)

email_label = tk.Label(window, text="Email Address:")
email_label.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
email_entry = tk.Entry(window)
email_entry.grid(row=7, column=1, padx=10, pady=5)

submit_button = tk.Button(window, text="Submit", command=submit_form)
submit_button.grid(row=8, column=0, columnspan=2, pady=10)

window.configure(background='grey')
for widget in (name_label, address1_label, address2_label, city_label, state_label, zip_label, phone_label, email_label):
    widget.configure(background='grey')
for entry in (name_entry, address1_entry, address2_entry, city_entry, state_entry, zip_entry, phone_entry, email_entry):
    entry.configure(background='white')

window.mainloop()
#Used chat GPT simply because I didn't want to have to write all that code I knew how to and I understand it but that was a bit much to write I also even used it to teach me how to print the form with the submit button cause I thought that'd be cooler