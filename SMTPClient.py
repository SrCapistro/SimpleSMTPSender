import smtplib
import tkinter as tk
from tkinter import *
from tkinter import messagebox

class MainSender:
    def __init__(self):
        #Definimos los elementos de la ventana
        self.ventanaMain=tk.Tk();
        self.ventanaMain.title("SIMPLE SMPT SENDER")
        self.labelMain = tk.Label(self.ventanaMain,text="SIMPLE SMTP SENDER", font=("bold",25)).pack()
        self.ventanaMain.geometry("450x300")
        self.labelCorreo = tk.Label(self.ventanaMain,text="Correo:", font=("bold")).pack()
        self.correoElectronico=tk.StringVar()
        self.entryCorreo=tk.Entry(self.ventanaMain,textvariable=self.correoElectronico).pack()
        self.labelContra = tk.Label(self.ventanaMain,text="Contraseña:", font=("bold")).pack()
        self.contra=tk.StringVar()
        self.entryContra=tk.Entry(self.ventanaMain,show="*",textvariable=self.contra).pack()
        self.labelDestinatario=tk.Label(self.ventanaMain,text="Destinatario:", font=("bold")).pack()
        self.Destinatario=tk.StringVar()
        self.entryDestinatario=tk.Entry(self.ventanaMain,textvariable=self.Destinatario).pack()
        self.asunto=tk.StringVar()
        self.labelAsunto=tk.Label(self.ventanaMain,text="Asunto", font=("bold")).pack()
        self.entryAsunto=tk.Entry(self.ventanaMain,textvariable=self.asunto).pack()
        self.labelMensaje=tk.Label(self.ventanaMain,text="Cuerpo del mensaje:", font=("bold")).pack()
        self.mensaje=tk.StringVar()
        self.entryMensaje=tk.Entry(self.ventanaMain,textvariable=self.mensaje,width=50).pack()
        self.botonEnviar=tk.Button(self.ventanaMain,text="Enviar", command=self.enviarCorreo).pack()
        self.ventanaMain.mainloop();

    def enviarCorreo(self):
        try:
            mensajeCompleto = 'Subject: {}\n\n{}'.format(self.asunto.get(), self.mensaje.get())
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(self.correoElectronico.get(),self.contra.get())
            server.sendmail(self.correoElectronico.get(), self.Destinatario.get(),mensajeCompleto)
            messagebox.showinfo("Correo enviado","Su correo ha sido enviado correctamenta a: "+self.Destinatario.get())
            server.quit()
        except:
            messagebox.showerror("Error", "Compruebe su información e intentélo de nuevo")

main = MainSender()
