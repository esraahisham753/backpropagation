import tkinter as tk
from  tkinter import *
from tkinter import ttk
from  tkinter import messagebox
import training

def save_hidden():
    global num_neurons_per_layer
    global hidden_entries
    global num_hidden_layers
    for i in range(0, num_hidden_layers):
        num_neurons_per_layer.append(int(hidden_entries[i].get()))
    messagebox.showinfo("Success", "Input filled successfully")

def hidden_gui():
    global hidden_labels
    global hidden_entries
    start_y = 330
    for i in range(0, num_hidden_layers):
        hidden_labels.append(ttk.Label(main_form, text = "hidden neurons in layer " + str(i + 1)))
        hidden_labels[i].place(x = 30, y = start_y)
        hidden_entries.append(ttk.Entry(main_form))
        hidden_entries[i].place(x = 200, y = start_y)
        start_y += 50
    save_hidden_b = ttk.Button(main_form, text = "Save hidden info", command = save_hidden)
    save_hidden_b.place(x = 30, y = start_y)
    start_y += 50
    train_btn = ttk.Button(main_form, text = "train", command = lambda : training.train(m, eta, num_hidden_layers, num_neurons_per_layer,bias, activation))
    train_btn.place(x  = 30, y = start_y)


def save():
    global  num_hidden_layers
    global eta
    global m
    global activation
    global bias
    num_hidden_layers = int(num_hidden_layers_entry.get())
    eta = float(eta_entry.get())
    m = int(m_entry.get())
    activation = activation_combo.get()
    bias = b.get()
    hidden_gui()
main_form = tk.Tk(className='User Input')
main_form.geometry("1000x1000")


#global variables
hidden_labels = []
hidden_entries = []
num_hidden_layers = 0
num_neurons_per_layer = []
eta = 0
m =0
activation = "sigmoid"
b = IntVar()
bias = 0

#generate labels
eta_l = ttk.Label(main_form, text = "Enter learning rate(eta): ")
eta_l.place(x = 30, y = 30)

m_l = ttk.Label(main_form, text = "Enter number of epochs(m): ")
m_l.place(x = 30, y = 80)

activation_l = ttk.Label(main_form, text = "Choose activation function: ")
activation_l.place(x = 30, y = 130)

num_hidden_layers_l = ttk.Label(main_form, text = "Enter number of hidden layers: ")
num_hidden_layers_l.place(x = 30, y= 180)
#generate textboxes
eta_entry = ttk.Entry(main_form)
eta_entry.place(x= 200, y = 30)

m_entry = ttk.Entry(main_form)
m_entry.place(x = 200, y = 80)

num_hidden_layers_entry = ttk.Entry(main_form)
num_hidden_layers_entry.place(x = 200, y = 180)
#generate combobox
activation_combo = ttk.Combobox(main_form, values = ["sigmoid", "hyperbolic"])
activation_combo.place(x = 200, y = 130)
#bias checkbox
b_c = ttk.Checkbutton(main_form, variable = b, text = "Add bias: " )
b_c.place(x = 30, y = 230)
#save button
save1_button = ttk.Button(main_form, text = "Save", command = save)
save1_button.place(x = 30, y = 280)















main_form.mainloop()