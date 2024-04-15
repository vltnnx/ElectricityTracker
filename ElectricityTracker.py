import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
import sys
from helper.get_temperature import get_temperatures
from helper.input_consumption import ElectricityTracker
from config import spreadsheet_url

def add_data():
    """ Calls the helper.input_consumption module, sending the user input
    for electricity consumption to be added into the spreadsheet. 
    
    The input window is withdrawn once the input is submitted."""
    start_day = start_day_box.get()
    end_day = end_day_box.get()
    kwh = float(kwh_box.get())
    consumption = float(consumption_box.get())
    transfer = float(transfer_box.get())

    root_input.withdraw()

    user_input = ElectricityTracker(start_day, end_day, kwh, consumption, transfer)
    user_input.append_to_sheet()

    # Clear entry boxes
    start_day_box.delete(0, tk.END)
    end_day_box.delete(0, tk.END)
    kwh_box.delete(0, tk.END)
    consumption_box.delete(0, tk.END)
    transfer_box.delete(0, tk.END)

def on_entry_click(event, entry, placeholder):
    """ Adjusts the color of the input fields in root_input window
    while placeholder texts are visible """
    if entry.get() == placeholder:
        entry.delete(0, "end")  
        entry.insert(0, '')  
        entry.config(fg='gray')  
    else:
        entry.config(fg='black')  

def add_new_month():
    """ Shows the input window when 'Input consumption' is pressed
    in the root_startup window."""
    root_input.deiconify()

def open_spreadsheet():
    """ Opens the spreadsheet determined by the 'url' variable
    in the function. """
    url = spreadsheet_url
    webbrowser.open_new(url)  # Open the URL link in the default web browser

def exit_application():
    """ Closes the root_startup window when 'Exit' button is pressed. """
    root_startup.destroy()
    root_input.destroy()
    sys.exit()

def center_window(window):
    """ Function to center the windows on screen. """
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Input window
root_input = tk.Tk()
root_input.geometry("300x360")
root_input.title("Electricity tracker")
root_input.withdraw()  # Hides the input window initially
center_window(root_input)

# Start-up window
root_startup = tk.Tk()
root_startup.geometry("600x100")
root_startup.title("Electricity tracker")
center_window(root_startup)

# Start-up window
button_frame = tk.Frame(root_startup)
button_frame.pack(side="top", anchor="center", pady=10)

buttons = [
    ("Input consumption", add_new_month),
    ("Open spreadsheet", open_spreadsheet),
    ("Load weather data", get_temperatures)
]

max_button_width = max(len(label) for label, _ in buttons)

for label, command in buttons:
    button = tk.Button(button_frame, text=label.ljust(max_button_width), command=command, width=15)
    button.pack(side="left", padx=5)

exit_button = tk.Button(root_startup, text="Exit", command=exit_application)
exit_button.pack(padx=10, pady=0)


placeholders = {
    "start_day": "dd-mm-yyyy",
    "end_day": "dd-mm-yyyy",
    "kwh": "0.00",
    "consumption": "0.00",
    "transfer": "0.00"
}

# Input window configurations
image = Image.open("static/img/icon.png")
resized_image = image.resize((30,30))
new_image = ImageTk.PhotoImage(resized_image)

image_label = tk.Label(root_input, image=new_image)
image_label.pack(pady=10)

start_day = tk.Label(root_input, text="Start day:")
start_day.pack()
start_day_box = tk.Entry(root_input, justify="center", fg="gray", font=("Helvetica", 12), width=25)
start_day_box.insert(0, placeholders["start_day"])
start_day_box.bind("<FocusIn>", lambda event, entry=start_day_box, placeholder=placeholders["start_day"]: on_entry_click(event, entry, placeholder))
start_day_box.bind("<FocusOut>", lambda event, entry=start_day_box, placeholder=placeholders["start_day"]: on_entry_click(event, entry, placeholder))
start_day_box.pack()

end_day = tk.Label(root_input, text="End day:")
end_day.pack()
end_day_box = tk.Entry(root_input, justify="center", fg="gray", font=("Helvetica", 12), width=25)
end_day_box.insert(0, placeholders["end_day"])
end_day_box.bind("<FocusIn>", lambda event, entry=end_day_box, placeholder=placeholders["end_day"]: on_entry_click(event, entry, placeholder))
end_day_box.bind("<FocusOut>", lambda event, entry=end_day_box, placeholder=placeholders["end_day"]: on_entry_click(event, entry, placeholder))
end_day_box.pack()

kwh = tk.Label(root_input, text="Consumption (kWh):")
kwh.pack()
kwh_box = tk.Entry(root_input,justify="center", fg="gray", font=("Helvetica", 12), width=25)
kwh_box.insert(0, placeholders["kwh"])
kwh_box.bind("<FocusIn>", lambda event, entry=kwh_box, placeholder=placeholders["kwh"]: on_entry_click(event, entry, placeholder))
kwh_box.bind("<FocusOut>", lambda event, entry=kwh_box, placeholder=placeholders["kwh"]: on_entry_click(event, entry, placeholder))
kwh_box.pack()

consumption = tk.Label(root_input, text="Consumption cost (€):")
consumption.pack()
consumption_box = tk.Entry(root_input, justify="center", fg="gray", font=("Helvetica", 12), width=25)
consumption_box.insert(0, placeholders["consumption"])
consumption_box.bind("<FocusIn>", lambda event, entry=consumption_box, placeholder=placeholders["consumption"]: on_entry_click(event, entry, placeholder))
consumption_box.bind("<FocusOut>", lambda event, entry=consumption_box, placeholder=placeholders["consumption"]: on_entry_click(event, entry, placeholder))
consumption_box.pack()

transfer = tk.Label(root_input, text="Transfer cost (€):")
transfer.pack()
transfer_box = tk.Entry(root_input, justify="center", fg="gray", font=("Helvetica", 12), width=25)
transfer_box.insert(0, placeholders["transfer"])
transfer_box.bind("<FocusIn>", lambda event, entry=transfer_box, placeholder=placeholders["transfer"]: on_entry_click(event, entry, placeholder))
transfer_box.bind("<FocusOut>", lambda event, entry=transfer_box, placeholder=placeholders["transfer"]: on_entry_click(event, entry, placeholder))
transfer_box.pack()

submit_button = tk.Button(root_input, text="Update to sheet", command=add_data)
submit_button.pack(padx=10, pady=15)

root_startup.mainloop()
