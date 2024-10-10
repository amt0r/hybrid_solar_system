import tkinter as tk
from tkinter import messagebox


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Hybrid system efficiency")
        self.master.geometry("200x300+250+100")
        self.master.configure(bg='black')
        
        self.latitude_label = tk.Label(self.master, text="Latitude (°):", bg='black', fg='white')
        self.latitude_label.pack()
        self.latitude_entry = tk.Entry(self.master)
        self.latitude_entry.pack()

        self.longitude_label = tk.Label(self.master, text="Longitude (°):", bg='black', fg='white')
        self.longitude_label.pack()
        self.longitude_entry = tk.Entry(self.master)
        self.longitude_entry.pack()

        self.year_usage_label = tk.Label(self.master, text="Yearly Usage (kW-hr):", bg='black', fg='white')
        self.year_usage_label.pack()
        self.year_usage_entry = tk.Entry(self.master)
        self.year_usage_entry.pack()

        self.generate_label = tk.Label(self.master, text="Solar Panel Power (kW):", bg='black', fg='white')
        self.generate_label.pack()
        self.generate_entry = tk.Entry(self.master)
        self.generate_entry.pack()

        self.kW_price_label = tk.Label(self.master, text="Price of kW-hr:", bg='black', fg='white')
        self.kW_price_label.pack()
        self.kW_price_entry = tk.Entry(self.master)
        self.kW_price_entry.pack()

        self.year_label = tk.Label(self.master, text="Year to modulate (YYYY):", bg='black', fg='white')
        self.year_label.pack()
        self.year_entry = tk.Entry(self.master)
        self.year_entry.pack()

        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit, bg='pink', fg='black')
        self.submit_button.pack(pady=20)

        self.latitude = 0
        self.longitude = 0
        self.year_usage = 0
        self.generate = 0
        self.year = 0
        self.kW_price = 0

    def submit(self):
        try:
            self.latitude = float(self.latitude_entry.get())
            self.longitude = float(self.longitude_entry.get())
            self.year_usage = float(self.year_usage_entry.get())
            self.generate = float(self.generate_entry.get())
            self.kW_price = float(self.kW_price_entry.get())
            self.year = str(self.year_entry.get())
            
            if not (-90 <= self.latitude <= 90):
                messagebox.showerror("Error", "Latitude must be between -90 and 90.")
                return
            if not (-180 <= self.longitude <= 180):
                messagebox.showerror("Error", "Longitude must be between -180 and 180.")
                return
            if self.year_usage <= 0:
                messagebox.showerror("Error", "Yearly usage must be a positive number.")
                return
            if self.generate < 0:
                messagebox.showerror("Error", "Solar panel power must be a non negative number.")
                return
            if self.kW_price <0:
                messagebox.showerror("Error", "Price of kW must be a positive number.")
                return
            if not (1984 <= int(self.year) <=2022):
                messagebox.showerror("Error", "Nasa API support from 1984 to 2022 years.")
                return

            self.master.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values.")

    def get_user_inputs(self):
        return self.latitude, self.longitude, self.year_usage, self.generate, self.year, self.kW_price

    def run(self):
        self.master.mainloop()
