#Creating a GUI for the stats.hypergeom function in SciPy to turn into an MTG calculator
# Following the tkinter tutorial from NeuralNine on youtube at https://youtu.be/iM3kjbbKHQU

import customtkinter 

#Set the appearance mode of your GUI
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")


root = customtkinter.CTk()
root.geometry("500x350") #dimensions, in pixels, for GUI

def login():
    print("test")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx = 60, fill = "both", expand = True)

label = customtkinter.CTkLabel(master=frame, text = "Login System")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text = "Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show = "*") 
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text = "Calculate", command=login) #need to actually create the function though
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text = "remember me")
checkbox.pack(pady=12, padx=10)

root.mainloop()


