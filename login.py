import tkinter as tk
from tkinter import messagebox

class janela_login:
    def __init__(self, master):
        self.master = master
        master.title("Janela de Login")
        
      
        master.configure(bg='#f2f2f2')
      
        self.label_username = tk.Label(master, text="Usuário:", bg='#f2f2f2')
        self.label_password = tk.Label(master, text="Senha:", bg='#f2f2f2')

        self.entry_username = tk.Entry(master)
        self.entry_password = tk.Entry(master, show="*")

        self.button_login = tk.Button(master, text="Login", command=self.login)
        
        self.label_username.grid(row=0, column=0, pady=10)
        self.label_password.grid(row=1, column=0, pady=10)
        self.entry_username.grid(row=0, column=1, pady=10)
        self.entry_password.grid(row=1, column=1, pady=10)
        self.button_login.grid(columnspan=2, pady=10)

    def login(self):        
        if (self.entry_username.get() == "Teste" and self.entry_password.get() == "senhateste"):
            messagebox.showinfo('Sucesso', 'Seja bem vindo!') 
            self.master.destroy()
        else:
            messagebox.showerror("Erro", "usuário ou senha incorretos")
            self.master.destroy()

root = tk.Tk()
root.configure(bg='#f2f2f2')

my_window = janela_login(root)

root.geometry("300x150+400+200")

root.mainloop()
