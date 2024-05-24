import tkinter as tk
from tkinter import ttk
import pyautogui
import threading
import time

class AutoClicker:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoClicker")
        
        # Acción seleccionada
        self.action_var = tk.StringVar(value="click")
        ttk.Label(root, text="Acción:").grid(column=0, row=0, padx=10, pady=10)
        self.click_radio = ttk.Radiobutton(root, text="Click Normal", variable=self.action_var, value="click", command=self.update_delay_entry)
        self.click_radio.grid(column=1, row=0, padx=10, pady=10)
        self.double_click_radio = ttk.Radiobutton(root, text="Doble Click", variable=self.action_var, value="double_click", command=self.update_delay_entry)
        self.double_click_radio.grid(column=2, row=0, padx=10, pady=10)
        
        # Intervalo
        self.interval_var = tk.DoubleVar(value=3.0)  # Configuración predeterminada de 3 segundos
        ttk.Label(root, text="Intervalo (segundos):").grid(column=0, row=1, padx=10, pady=10)
        self.interval_entry = ttk.Entry(root, textvariable=self.interval_var)
        self.interval_entry.grid(column=1, row=1, padx=10, pady=10)
        
        # Retraso entre clicks para doble click
        self.delay_var = tk.DoubleVar(value=0.1)
        self.delay_label = ttk.Label(root, text="Retraso entre clicks (segundos):")
        self.delay_entry = ttk.Entry(root, textvariable=self.delay_var)
        
        # Botones Play/Stop
        self.start_button = ttk.Button(root, text="Iniciar", command=self.start_clicking)
        self.start_button.grid(column=0, row=3, padx=10, pady=10)
        self.stop_button = ttk.Button(root, text="Detener", command=self.stop_clicking)
        self.stop_button.grid(column=1, row=3, padx=10, pady=10)
        
        self.running = False
        self.thread = None

        self.update_delay_entry()
    
    def update_delay_entry(self):
        if self.action_var.get() == "double_click":
            self.delay_label.grid(column=0, row=2, padx=10, pady=10)
            self.delay_entry.grid(column=1, row=2, padx=10, pady=10)
        else:
            self.delay_label.grid_forget()
            self.delay_entry.grid_forget()
    
    def click_action(self):
        action = self.action_var.get()
        interval = self.interval_var.get()
        delay = self.delay_var.get()
        while self.running:
            if action == "click":
                pyautogui.click()
            elif action == "double_click":
                pyautogui.click()
                time.sleep(delay)  # Pequeño retraso entre clicks
                pyautogui.click()
            time.sleep(interval)
    
    def start_clicking(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.click_action)
            self.thread.start()
    
    def stop_clicking(self):
        if self.running:
            self.running = False
            if self.thread is not None:
                self.thread.join()
                self.thread = None

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClicker(root)
    root.mainloop()
