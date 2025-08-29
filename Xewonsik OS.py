
# Основа

import tkinter as tk
from tkinter import messagebox
import platform
import sys

class PhoneOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Xewonsik OS")
        self.root.geometry("300x500")
        self.os_version = "Xewonsik OS"
        self.apps = {
            "WiFi": self.open_wifi, 
            "Игры": self.open_game, 
            "Калькулятор": self.open_calculator,
            "Календарь": self.open_calendar,
            "Контакты": self.open_contact, 
            "Файловый менеджер": self.open_files, 
            "Настройки": self.open_nas, 
            "Информация": self.open_settings,
            "О системе": self.show_system_info
        }
        
        # Стиль
        bg_color = "#f0f0f0"
        btn_color = "#e0e0e0"
        
        self.root.config(bg=bg_color)
        
        # Верхняя панель (статус бар)
        self.status_bar = tk.Frame(root, bg="black", height=20)
        self.status_bar.pack(fill=tk.X)
        
        self.time_label = tk.Label(self.status_bar, text="12:00", fg="white", bg="black")
        self.time_label.pack(side=tk.RIGHT, padx=5)
        
        # Основной интерфейс
        self.main_frame = tk.Frame(root, bg=bg_color)
        self.main_frame.pack(expand=True, fill=tk.BOTH)
        
        # Отображение версии ОС
        self.os_label = tk.Label(self.main_frame, text=self.os_version, font=("Arial", 12), bg=bg_color)
        self.os_label.pack(pady=10)
        
        # Кнопки приложений
        for app_name, app_command in self.apps.items():
            btn = tk.Button(self.main_frame, text=app_name, width=20, height=2, 
                          bg=btn_color, command=app_command)
            btn.pack(pady=5)
            
        # Кнопка выключения
        self.power_btn = tk.Button(root, text="Выключить", command=self.shutdown, bg="#ffcccc")
        self.power_btn.pack(pady=10, fill=tk.X)
        
    
    def open_nas(self):
        nas_window = tk.Toplevel(self.root)
        nas_window.title("Настройки")
        nas_window.geometry("250x200") 
        
        tk.Label(nas_window, text=f"Настройки пока что не доступны!").pack() 
        
    def open_game(self):
        game_window = tk.Toplevel(self.root) 
        game_window.title("Игры") 
        game_window.geometry("250x200") 
        
        tk.Label(game_window, text="Игры", font=12) 
        tk.Label(game_window, text=f"Игры пока что не доступны").pack()
    
    def open_calculator(self):
        calc_window = tk.Toplevel(self.root)
        calc_window.title("Калькулятор")
        calc_window.geometry("250x300")
        
        entry = tk.Entry(calc_window, width=20, font=("Arial", 14))
        entry.grid(row=0, column=0, columnspan=4, pady=10)
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        def on_click(char):
            if char == '=':
                try:
                    result = eval(entry.get())
                    entry.delete(0, tk.END)
                    entry.insert(0, str(result))
                except:
                    entry.delete(0, tk.END)
                    entry.insert(0, "Ошибка")
            elif char == 'C':
                entry.delete(0, tk.END)
            else:
                entry.insert(tk.END, char)
        
        for i, char in enumerate(buttons):
            btn = tk.Button(calc_window, text=char, width=5, height=2,
                          command=lambda c=char: on_click(c))
            btn.grid(row=1 + i//4, column=i%4, padx=2, pady=2)
    
    def open_calendar(self):
        calendar_window = tk.Toplevel(self.root)
        calendar_window.title("Календарь")
        calendar_window.geometry("250x250")
        
        from datetime import datetime
        now = datetime.now()
        
        date_label = tk.Label(calendar_window, text=now.strftime("%d.%m.%Y"), font=("Arial", 16))
        date_label.pack(pady=20)
        
        time_label = tk.Label(calendar_window, text=now.strftime("%H:%M:%S"), font=("Arial", 14))
        time_label.pack(pady=10)
        
        def update_time():
            now = datetime.now()
            time_label.config(text=now.strftime("%H:%M:%S"))
            time_label.after(1000, update_time)
        
        update_time()
    
    def open_settings(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Информация")
        settings_window.geometry("250x200")
        
        tk.Label(settings_window, text="Информация", font=("Arial", 12)).pack(pady=10)
        
        # Получаем реальную информацию о системе
        real_os = platform.system() + " " + platform.release()
        python_version = "Python " + platform.python_version()
        
        tk.Label(settings_window, text=f"Версия ОС: 0.1").pack() 
        tk.Label(setting_window, text=f"Название ОС: Xewonsik OS").pack()
        tk.Label(setting_window, text=f"Програмиа: Python").pack()
        
    
    def open_wifi(self):
        wifi_window = tk.Toplevel(self.root) 
        wifi_window.title("WiFi")
        wifi_window.geometry("250x200")
        
        tk.Label(wifi_window, text="WiFi", font=12) 
        tk.Label(wifi_window, text=f"WiFi Подключëн").pack() 
        
    def open_contact(self):
        contact_window = tk.Toplevel(self.root)
        contact_window.title("Контакты") 
        contact_window.geometry("250x200")
        
        tk.Label(contact_window, text="Контакты", font=12) 
        tk.Label(contact_window, text=f"Контакты:").pack() 
        tk.Label(contact_window, text=f"Друг").pack() 
        tk.Label(contact_window, text=f"Разработчик").pack()
        
    def open_files(self):
        files_window = tk.Toplevel(self.root) 
        files_window.title("Файловый менеджер")
        files_window.geometry("250x200")
        
        tk.Label(files_window, text="Файловый менеджер", font=12) 
        tk.Label(files_window, text=f"Файлы:").pack()
        
        tk.Label(files_window, text=f"1. file_home").pack() 
        tk.Label(files_window, text=f"2. file_user").pack() 
        tk.Label(files_window, text=f"3. file_OS").pack() 
        tk.Label(files_window, text=f"4. file_setting").pack()
        tk.Label(files_window, text=f"5. file_time").pack()
        
    
    def show_system_info(self):
        real_os = platform.system() + " " + platform.release()
        python_version = "Python " + platform.python_version()
        
        info = f"""Симулятор PhoneOS
Версия: {self.os_version}

Реальная система:
ОС: {real_os}
Python: {python_version}"""
        
        messagebox.showinfo("О системе", info)
    
    def shutdown(self):
        if messagebox.askyesno("Выключение", "Вы уверены, что хотите выключить систему?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    os = PhoneOS(root)
    root.mainloop()
