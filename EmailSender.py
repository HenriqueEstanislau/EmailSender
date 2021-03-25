import smtplib
import ssl
import email.message

from tkinter import *

janela = Tk()
janela.title("Enviar email com Python")
janela["background"] = "#1b1f23"

def bt_click():
    print("bt_click")
    if str(edEmail.get()) != "" and str(edPassword.get()) != "":

        msg = email.message.Message()
        msg['Subject'] = edSubject.get()

        body = texto.get(1.0, END)

        msg['From'] = edEmail.get()
        msg['To'] = edTo.get()
        password = edPassword.get()
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(body)
        if msg['From'] != "" and msg['To'] != "" and password != "":
            context = ssl.create_default_context()
            with smtplib.SMTP('smtp.gmail.com', 587) as conexao:
                conexao.ehlo()
                conexao.starttls(context=context)
                conexao.login(msg['From'], password)
                conexao.sendmail(msg['From'], msg['to'], msg.as_string().encode('utf-8'))

            lb0["text"] = "Email enviado com sucesso"
        else:
            lb0["text"] = "Valores invalidos"
    else:
        lb0["text"] = "Valores invalidos"
lbDiv = Label(janela, text="________________",bd=0,bg="#1b1f23",fg="#e36209", font=("verdana", 20, "bold")).place(x=20, y=35)
lbTitle = Label(janela, text="Write us",bg="#1b1f23",fg="white", font=("verdana", 22, "bold")).place(x=20, y=24)

# Get Email
lbEmail = Label(janela, text="Email:",bg="#1b1f23",fg="lightgray", font=("verdana", 11)).place(x=20, y=98)
lbDiv = Label(janela, text="___________________________",bd=0,bg="#1b1f23",fg="gray", font=("verdana", 18,"bold")).place(x=20, y=115)
edEmail = Entry(janela, width = 32, bd=0,bg="#1b1f23",fg="white", font=("verdana", 12))
edEmail.config(highlightthickness=0)
edEmail.place(x=20, y=120)

# Get Password
lbPassword = Label(janela, text="Senha:",bg="#1b1f23",fg="lightgray", font=("verdana", 11)).place(x=20, y=150)
lbDiv = Label(janela, text="___________________________",bd=0,bg="#1b1f23",fg="gray", font=("verdana", 18,"bold")).place(x=20, y=166)
edPassword = Entry(janela, show="*", width = 32, bd=0,bg="#1b1f23",fg="white", font=("verdana", 12))
edPassword.config(highlightthickness=0)
edPassword.place(x=20, y=170)

# Get To
lbTo = Label(janela, text="Para:",bg="#1b1f23",fg="lightgray", font=("verdana", 11)).place(x=20, y=200)
lbDiv = Label(janela, text="___________________________",bd=0,bg="#1b1f23",fg="gray", font=("verdana", 18,"bold")).place(x=20, y=216)
edTo = Entry(janela, width = 32, bd=0,bg="#1b1f23",fg="white", font=("verdana", 12))
edTo.config(highlightthickness=0)
edTo.place(x=20, y=220)

# Get Title email
lbSubject = Label(janela, text="Título do Email:",bg="#1b1f23",fg="lightgray", font=("verdana", 11)).place(x=400, y=75)
edSubject = Entry(janela, width = 38, font=("verdana", 12))
edSubject.place(x=400, y=100)

# Get email content
texto = Text(janela, height = 10, width = 47)
texto.insert(INSERT, 'Olá pessoal,')
texto.place(x=400, y=130)

# Button
bt = Button(janela, text="Enviar",bd=0,bg="#e36209",fg="white", width = 45, command = bt_click)
bt.config(highlightthickness=0)
bt.place(x=400, y=320)

lb0 = Label(janela, text="",bg="#1b1f23",fg="lightgray")
lb0.place(x=400, y=355)

janela.geometry("850x400+200+200")
janela.mainloop()