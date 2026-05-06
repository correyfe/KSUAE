# import tkinter as tk
# from tkinter import messagebox

# def say_hello():
#     name = entry.get()

#     if name:
#         greeting_labe1.config(text=f"Привет, {name}!")
#     else:
#         messagebox.showwarning("Внимание","Введите имя!")

# root = tk.Tk()
# root.title("Приветствие")
# root.geometry("300x200")
# labe1 = tk.labe1(root, text = "Введите ваше имя:")
# labe1.pack(pady=10)
# entry = tk.Entry(root)
# labe1.pack(pady=5)
# button = tk.Button(root, text="", font=("Arial", 12))
# button.pack(pady=10)
# greeting_labe1 = tk.labe1(root, text="", font=("Arial", 12))
# greeting_labe1.pack(pady=10)
# root.mainloop()


# count = 0

# count_labe1 = tk.labe1(root, text="Счет : 0", font=("Arial", 14))
# count_labe1.pack(pady=20)

# button_frame = tk.Frame(root)
# button_frame.pack(pady=10)
# inc_button = tk.Button(root, text="Нажми меня", command=increment, width=15)
# inc_button.pack(side=tk.LEFT,)


# import tkinter as tk

# def button_click(value):
#     current = display.get()
#     display.delete(0, tk.END)
#     display.insert(0, current + str(value))
# def clear():
#     display.delete(0, tk.END)
# def calculate():
#     try:
#         result = eval(display.get())
#         display.delete(0, str(result))
#     except:
#         display.delete(0, tk.END)
#         display.insert(0, "ошибка")
# root = tk.Tk()
# root.title("калькуятор")
# root.geometry("300x400")
# display = tk.Entry(root, font=("Arial", 20), justify="right")
# display.pack(fill=tk.BOTH, padx=10, pady=10, ipady=10)
# buttons = [
#     ['7', '8', '9', '/'],
#     ['4', '5', '6', '*'],
#     ['1', '2', '3', '-'],
#     ['0', '.', '=', '+']
# ]
# button_frame = tk.Frame(root)
# button_frame.pack(pady=10)
# for row in buttons:
#     frame = tk.Frame(button_frame)
#     frame.pack()
#     for btn_text in row:
#         if btn_text == "=":
#             btn = tk.Button(frame, text=btn_text, width=8, height=2, command=calculate)
#         else:
#             btn=tk.Button(frame, text=btn_text, width=8, height=2, command=lambda x=btn_text: button_click(x))            
#         btn.pack(side=tk.LEFT,padx=2,pady=2)
# clear_btn=tk.Button(root,text='c', width=10,height=2, command=clear, bg='orange')
# clear_btn.pack(pady=5)
# root.mainloop()



# import tkinter as tk
# from tkinter import messagebox
# def say_hello():
#     name = entry.get()

#     if name:
#         greeting_labe1.config(text=f"Привет, {name}!")
#     else:
#         messagebox.showwarning("Внимание","Введите имя!")
# root = tk.Tk()
# root.title("Приветствие")
# root.geometry("300x200")
# labe1 = tk.labe1(root, text = "Введите ваше имя:")
# labe1.pack(pady=10)
# entry = tk.Entry(root)
# labe1.pack(pady=5)
# button = tk.Button(root, text="", font=("Arial", 12))
# button.pack(pady=10)
# greeting_labe1 = tk.labe1(root, text="", font=("Arial", 12))
# greeting_labe1.pack(pady=10)
# root.mainloop()
# count = 0
# count_labe1 = tk.labe1(root, text="Счет : 0", font=("Arial", 14))
# count_labe1.pack(pady=20)
# button_frame = tk.Frame(root)
# button_frame.pack(pady=10)
# inc_button = tk.Button(root, text="Нажми меня", command=increment, width=15)
# inc_button.pack(side=tk.LEFT,)




# import tkinter as tk
# def submit():
#     login = entry_login.get()
#     password = entry_password.get()
#     print("Логин:", login)
#     print("Пароль:", password)

# root = tk.Tk()
# root.title("Авторизация")
# root.geometry("300x150")
# label_login = tk.Label(root, text="Логин:")
# label_login.pack()
# entry_login = tk.Entry(root)
# entry_login.pack()
# label_password = tk.Label(root, text="Пароль:")
# label_password.pack()
# entry_password = tk.Entry(root, show="*")  # скрытие пароля
# entry_password.pack()
# button = tk.Button(root, text="Войти", command=submit)
# button.pack(pady=10)
# root.mainloop()



# import tkinter as tk
# from tkinter import filedialog, messagebox
# def save_file():
#     if not text_area.get("1.0", tk.END).strip():
#         messagebox.showwarning("Внимание", "Нет текста для сохранения!")
#         return
#     filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
#     if filename:
#         with open(filename, 'w', encoding='utf-8') as file:
#             file.write(text_area.get("1.0", tk.END))
#         messagebox.showinfo("Успех", f"Файл сохранён: {filename}")
# def load_file():
#     filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
#     if filename:
#         try:
#             with open(filename, 'r', encoding='utf-8') as file:
#                 text_area.delete("1.0", tk.END)
#                 text_area.insert(tk.END, file.read())
#             messagebox.showinfo("Успех", f"Файл загружен: {filename}")
#         except Exception as e:
#             messagebox.showerror("Ошибка", f"Не удалось загрузить файл: {e}")
# def clear_text():
#     if messagebox.askyesno("Подтверждение", "Очистить весь текст?"):
#         text_area.delete("1.0", tk.END)
# root = tk.Tk()
# root.title("Текстовый ркдактор")
# root.geometry("600x400")
# button_frame = tk.Frame(root)
# button_frame.pack(pady=5)
# save_btn = tk.Button(button_frame, text="Сохранить", command=save_file, bg="lightgreen", width=12)
# save_btn.pack(side=tk.LEFT, padx=5)
# load_btn = tk.Button(button_frame, text="Загрузить", command=load_file, bg="lightblue", width=12)
# load_btn.pack(side=tk.LEFT, padx=5)
# clear_btn = tk.Button(button_frame, text="Очистить", command=clear_text, bg="orange", width=12)
# clear_btn.pack(side=tk.LEFT, padx=5)
# text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 11))
# text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
# scrollbar = tk.Scrollbar(text_area)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# text_area.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command=text_area.yview)
# root.mainloop()





# import tkinter as tk
# from tkinter import messagebox
# def check_login():
#     username = login_entry.get()
#     password = pass_entry.get() 
#     if username == "admin" and password == "2007":
#         messagebox.showinfo("Успех", "Добро пожаловать в систему!")
#         open_welcome_window() 
#     else:
#         messagebox.showerror("Ошибка", "Неверный логин или пароль!")
# def open_welcome_window():
#     welcome = tk.Toplevel(root)  
#     welcome.title("Приветствие")  
#     welcome.geometry("300x150") 
#     welcome.configure(bg="lightgreen")
#     label = tk.Label(welcome, text="Добро пожаловать, хозяйка!", 
#                      font=("Arial", 14), bg="lightgreen")
#     label.pack(expand=True) 
#     close_btn = tk.Button(welcome, text="Закрыть", command=welcome.destroy)
#     close_btn.pack(pady=10) 
# root = tk.Tk() 
# root.title("Вход в систему") 
# root.geometry("350x250") 
# tk.Label(root, text="Вход в систему", font=("Arial", 16)).pack(pady=20)
# login_frame = tk.Frame(root)
# login_frame.pack(pady=10)
# tk.Label(login_frame, text="Логин:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
# login_entry = tk.Entry(login_frame, width=20) 
# login_entry.grid(row=0, column=1, padx=5)  
# login_entry.focus()  
# tk.Label(login_frame, text="Пароль:", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
# pass_entry = tk.Entry(login_frame, width=20, show="1") 
# pass_entry.grid(row=1, column=1, padx=5, pady=5)  
# login_btn = tk.Button(root, text="Вход", command=check_login, width=15, 
#                        bg="blue", fg="white")
# login_btn.pack(pady=20)
# exit_btn = tk.Button(root, text="Выход", command=root.quit, width=15)
# exit_btn.pack()
# root.mainloop()




# import tkinter as tk
# from tkinter import ttk, messagebox
# def convert():
#     try:
#         rubles = float(rub_entry.get())
#         currency = currency_var.get()
#         if currency == "доллар":
#         result = rubles / 90
#         symbol = "$"
#         else:
#         result = rubles / 98
#         sybmol = "@"
#         result_label.config(text=f"{result:.2f} {symbol}")
#     except ValueError:
#         messagebox.showerror("ошибка")
# root = tk.Tk()
# ro

# import tkinter as tk
# def button_click(value):
#     cur=display.get()
#     display.delite(0, tk.END)
#     display.insert(0, cur+str(value))
# def clear():
#     display.delete(0,tk.END)
# def calculate():
#     try:
#         result=eval(display.get())
#         display.delete(0,tk.END)
#         display.insert(0, cur+str(result))
#     except:


        


