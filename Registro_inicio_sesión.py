import tkinter
from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
import pymysql

#PANTALLA.

def menu_pantalla():   
    global pantalla
    pantalla=Tk()
    pantalla.geometry("300x480")
    pantalla.title("Bienvenido")
    pantalla.resizable(False,False)
    #Cambiar el ícono en el encabezado.
    pantalla.iconbitmap("hub_de_seguridad.ico")
    
    #Colocar una imagen en la pantalla.
    image=PhotoImage(file="hub_de_seguridad.gif")
    image=image.subsample(3,3)
    label=Label(image=image)
    label.pack()
    
    #Bienvenido
    Label(text="Bienvenido", font=("Arial", 17),height="3").pack()

    #Botón iniciar sesión empresa
    boton_sesion=Button(text="Iniciar Sesión Empresa",font=("Arial", 11), height="2", width="18", command=inicio_sesion_empresa).pack()

    #Botón iniciar sesión
    boton_sesion=Button(text="Iniciar Sesión",font=("Arial", 11), height="2", width="11", command=inicio_sesion).pack()
  
    #Botón registrarse
    boton_registro=Button(text="Registrarse",font=("Arial", 11), height="2", width="11", command=elige).pack()

    pantalla.mainloop()

#PANTALLAS INICIO SESION.
    
def inicio_sesion():
    global pantalla_sesion
    pantalla_sesion = Toplevel(pantalla)
    pantalla_sesion.geometry("300x450")
    pantalla_sesion.title("Inicia sesión")
    pantalla_sesion.resizable(False,False)
    pantalla_sesion.iconbitmap("hub_de_seguridad.ico")
    
    global usuario_verificar
    global contraseña_verificar

    usuario_verificar=StringVar()
    contraseña_verificar=StringVar()

    #Inicia sesión
    Label(pantalla_sesion, text="Inicia sesión", font=("Arial", 17), height="7").pack()

    #Pedir Email
    Label(pantalla_sesion, text="Email", font=("Arial",12)).pack()
    usuario_entry = Entry(pantalla_sesion, textvariable=usuario_verificar)
    usuario_entry.pack()
    Label(pantalla_sesion).pack()

    #Pedir contraseña
    Label(pantalla_sesion, text="Contraseña",font=("Arial",12)).pack()
    contraseña_entry= Entry(pantalla_sesion, textvariable=contraseña_verificar, show="*")
    contraseña_entry.pack()
    Label(pantalla_sesion).pack()

    Label(pantalla_sesion, text="¿Aún no tienes cuenta?",font=("Arial",8)).place(x=60,y=300)
    vinculo=Label(pantalla_sesion, text="Regístrate",font=("Arial",8,"underline"))
    vinculo.place(x=190,y=300)
    vinculo.bind("<Button-1>", pantalla_registro_usuario_X)
    Label(pantalla_sesion).pack()
    
    Button(pantalla_sesion, text="Iniciar Sesión", bg="black", fg="white", font=("Arial", 11), height="1", width="11", command=validacion_datos).pack()
    Label(text="").pack()    

def inicio_sesion_empresa():
    global pantalla_empresa
    pantalla_empresa = Toplevel(pantalla)
    pantalla_empresa.geometry("300x450")
    pantalla_empresa.title("Inicia sesión")
    pantalla_empresa.resizable(False,False)
    pantalla_empresa.iconbitmap("hub_de_seguridad.ico")
    
    global empresa_verificar
    global contra_verificar

    empresa_verificar=StringVar()
    contra_verificar=StringVar()

    #Inicia sesión
    Label(pantalla_empresa, text="Inicia sesión empresa", font=("Arial", 17), height="7").pack()

    #Pedir Email
    Label(pantalla_empresa, text="Email", font=("Arial",12)).pack()
    usuario_entry = Entry(pantalla_empresa, textvariable=empresa_verificar)
    usuario_entry.pack()
    Label(pantalla_empresa).pack()

    #Pedir contraseña
    Label(pantalla_empresa, text="Contraseña",font=("Arial",12)).pack()
    contraseña_entry= Entry(pantalla_empresa, textvariable=contra_verificar, show="*")
    contraseña_entry.pack()
    Label(pantalla_empresa).pack()

    Label(pantalla_empresa, text="¿Aún no tienes cuenta?",font=("Arial",8)).place(x=60,y=300)
    vinculo=Label(pantalla_empresa, text="Regístrate",font=("Arial",8,"underline"))
    vinculo.place(x=190,y=300)
    vinculo.bind("<Button-1>", pantalla_registro_empresa_X)
    Label(pantalla_empresa).pack()
    
    Button(pantalla_empresa, text="Iniciar Sesión", bg="black", fg="white", font=("Arial", 11), height="1", width="11", command=validacion_datos_empresa).pack()
    Label(text="").pack()

def inicio_sesion_X(event=None):
    cerrar_only_pant_usuario()
    global pantalla_sesion
    pantalla_sesion = Toplevel(pantalla)
    pantalla_sesion.geometry("300x450")
    pantalla_sesion.title("Inicia sesión")
    pantalla_sesion.resizable(False,False)
    pantalla_sesion.iconbitmap("hub_de_seguridad.ico")
    
    global usuario_verificar
    global contraseña_verificar

    usuario_verificar=StringVar()
    contraseña_verificar=StringVar()

    #Inicia sesión
    Label(pantalla_sesion, text="Inicia sesión", font=("Arial", 17), height="7").pack()

    #Pedir Email
    Label(pantalla_sesion, text="Email", font=("Arial",12)).pack()
    usuario_entry = Entry(pantalla_sesion, textvariable=usuario_verificar)
    usuario_entry.pack()
    Label(pantalla_sesion).pack()

    #Pedir contraseña
    Label(pantalla_sesion, text="Contraseña",font=("Arial",12)).pack()
    contraseña_entry= Entry(pantalla_sesion, textvariable=contraseña_verificar, show="*")
    contraseña_entry.pack()
    Label(pantalla_sesion).pack()

    Label(pantalla_sesion, text="¿Aún no tienes cuenta?",font=("Arial",8)).place(x=60,y=300)
    vinculo=Label(pantalla_sesion, text="Regístrate",font=("Arial",8,"underline"))
    vinculo.place(x=190,y=300)
    vinculo.bind("<Button-1>", pantalla_registro_usuario_X)
    Label(pantalla_sesion).pack()
    
    Button(pantalla_sesion, text="Iniciar Sesión", bg="black", fg="white", font=("Arial", 11), height="1", width="11", command=validacion_datos).pack()
    Label(text="").pack()    

def inicio_sesion_empresa_X(event=None):
    cerrar_only_pant_empresa()
    global pantalla_empresa
    pantalla_empresa = Toplevel(pantalla)
    pantalla_empresa.geometry("300x450")
    pantalla_empresa.title("Inicia sesión")
    pantalla_empresa.resizable(False,False)
    pantalla_empresa.iconbitmap("hub_de_seguridad.ico")
    
    global empresa_verificar
    global contra_verificar

    empresa_verificar=StringVar()
    contra_verificar=StringVar()

    #Inicia sesión
    Label(pantalla_empresa, text="Inicia sesión empresa", font=("Arial", 17), height="7").pack()

    #Pedir Email
    Label(pantalla_empresa, text="Email", font=("Arial",12)).pack()
    usuario_entry = Entry(pantalla_empresa, textvariable=empresa_verificar)
    usuario_entry.pack()
    Label(pantalla_empresa).pack()

    #Pedir contraseña
    Label(pantalla_empresa, text="Contraseña",font=("Arial",12)).pack()
    contraseña_entry= Entry(pantalla_empresa, textvariable=contra_verificar, show="*")
    contraseña_entry.pack()
    Label(pantalla_empresa).pack()

    Label(pantalla_empresa, text="¿Aún no tienes cuenta?",font=("Arial",8)).place(x=60,y=300)
    vinculo=Label(pantalla_empresa, text="Regístrate",font=("Arial",8,"underline"))
    vinculo.place(x=190,y=300)
    vinculo.bind("<Button-1>", pantalla_registro_empresa_X)
    Label(pantalla_empresa).pack()
    
    Button(pantalla_empresa, text="Iniciar Sesión", bg="black", fg="white", font=("Arial", 11), height="1", width="11", command=validacion_datos_empresa).pack()
    Label(text="").pack()

#ELEGIR REGISTRO.

def elige():
    global eligex
    eligex=Toplevel(pantalla)
    eligex.geometry("300x450")
    eligex.title("Elige")
    eligex.resizable(False,False)
    eligex.iconbitmap("hub_de_seguridad.ico")

    #Elige
    Label(eligex, text="Elige", font=("Arial Black", 16), height="7").pack()

    #Botón registro usuario
    Button(eligex, text="Registrarme como usuario", bg="white", fg="black", font=("Arial", 11), height="1", width="25", command=pantalla_registro_usuario).pack()
    Label(text="").pack()

    #Botón registro empresa
    Label(text="").pack()
    Button(eligex, text="Registrarme como empresa", bg="black", fg="white", font=("Arial", 11), height="1", width="25", command=pantalla_registro_empresa).pack()

#PANTALLAS REGISTRO.
    
def pantalla_registro_usuario():
    cerrar_elige()
    global pant_usuario
    pant_usuario = Toplevel(pantalla)
    pant_usuario.geometry("450x700")
    pant_usuario.title("Registrate")
    pant_usuario.resizable(False,False)
    pant_usuario.iconbitmap("hub_de_seguridad.ico")

    global nombre_usuario
    global apellidos
    global sexo
    global telefono
    global email
    global contraseña

    nombre_usuario=StringVar()
    apellidos=StringVar()
    sexo=StringVar()
    telefono=StringVar()
    email=StringVar()
    contraseña=StringVar()
    
    #Registrate
    Label(pant_usuario, text="Registrate", font=("Arial Black", 16), height="5").pack()

    #Pedir Nombre
    Label(pant_usuario, text="Nombre", font=("Arial",12)).pack()
    nombre_usuario= Entry(pant_usuario, textvariable=nombre_usuario)
    nombre_usuario.pack()
    Label(pant_usuario).pack()

    #Pedir Apellidos
    Label(pant_usuario, text="Apellidos", font=("Arial",12)).pack()
    apellidos= Entry(pant_usuario, textvariable=apellidos)
    apellidos.pack()
    Label(pant_usuario).pack()

    #Pedir Género
    Label(pant_usuario, text="Sexo", font=("Arial",12)).pack()
    opciones=["Masculino","Femenino","Indistinto"]
    sexo=Combobox(pant_usuario, width="17", values=opciones, state="readonly")
    sexo.pack()
    Label(pant_usuario).pack()

    #Pedir Teléfono
    Label(pant_usuario, text="Teléfono", font=("Arial",12)).pack()
    telefono= Entry(pant_usuario, textvariable=telefono)
    telefono.pack()
    Label(pant_usuario).pack()

    #Pedir Email
    Label(pant_usuario, text="Email", font=("Arial",12)).pack()
    email= Entry(pant_usuario, textvariable=email)
    email.pack()
    Label(pant_usuario).pack()

    #Pedir Contraseña
    Label(pant_usuario, text="Contraseña", font=("Arial",12)).pack()
    contraseña= Entry(pant_usuario, textvariable=contraseña, show = "*")
    contraseña.pack()
    Label(pant_usuario).pack()

    Label(pant_usuario, text="¿Ya tienes cuenta?",font=("Arial",8)).place(x=135,y=530)
    vinculo=Label(pant_usuario, text="Inicia Sesión",font=("Arial",8,"underline"))
    vinculo.place(x=250,y=530)
    vinculo.bind("<Button-1>", inicio_sesion_X)
       
    boton_regresar = Button(pant_usuario, text="Regresar", bg="white", fg="black", height="2", width="11", font=("Arial", 10), command=cerrar_pant_usuario).place(x=130,y=560)
    
    boton_registrame = Button(pant_usuario, text="Regístrame", bg="black", fg="white", height="2", width="11", font=("Arial", 10), command=registrar_datos).place(x=250,y=560)
        
def pantalla_registro_empresa():
    cerrar_elige()
    global pant_empresa
    pant_empresa = Toplevel(pantalla)
    pant_empresa.geometry("450x750")
    pant_empresa.title("Registrate")
    pant_empresa.resizable(False,False)
    pant_empresa.iconbitmap("hub_de_seguridad.ico")

    global nombre
    global apellidos
    global razon_social
    global RFC
    global pais
    global ciudad
    global telefono
    global email
    global contraseña

    nombre=StringVar()
    apellidos=StringVar()
    razon_social=StringVar()
    RFC=StringVar()
    pais=StringVar()
    ciudad=StringVar()
    telefono=StringVar()
    email=StringVar()
    contraseña=StringVar()
    
    #Registrate
    Label(pant_empresa, text="Registra tu empresa", font=("Arial Black", 13), height="5").pack()

    #Pedir Nombre
    Label(pant_empresa, text="Nombre", font=("Arial",10)).pack()
    nombre= Entry(pant_empresa, textvariable=nombre)
    nombre.pack()

    #Pedir Apellidos
    Label(pant_empresa, text="Apellidos", font=("Arial",10)).pack()
    apellidos= Entry(pant_empresa, textvariable=apellidos)
    apellidos.pack()

    #Pedir Razon Social
    Label(pant_empresa, text="Razon_Social", font=("Arial",10)).pack()
    razon_social= Entry(pant_empresa, textvariable=razon_social)
    razon_social.pack()

    #Pedir RFC
    Label(pant_empresa, text="RFC", font=("Arial",10)).pack()
    RFC = Entry(pant_empresa, textvariable=RFC)
    RFC.pack()

    #Pedir Pais
    Label(pant_empresa, text="País", font=("Arial",10)).pack()
    opciones=["México","Estados Unidos","Canadá"]
    pais=Combobox(pant_empresa, width="17", values=opciones, state="readonly")
    pais.pack()

    #Pedir Ciudad
    Label(pant_empresa, text="Ciudad", font=("Arial",10)).pack()
    ciudad= Entry(pant_empresa, textvariable=ciudad)
    ciudad.pack()
    
    #Pedir Teléfono
    Label(pant_empresa, text="Teléfono", font=("Arial",10)).pack()
    telefono= Entry(pant_empresa, textvariable=telefono)
    telefono.pack()
    
    #Pedir Email
    Label(pant_empresa, text="Email", font=("Arial",10)).pack()
    email= Entry(pant_empresa, textvariable=email)
    email.pack()

    #Pedir Contraseña
    Label(pant_empresa, text="Contraseña", font=("Arial",10)).pack()
    contraseña= Entry(pant_empresa, textvariable=contraseña, show = "*")
    contraseña.pack()
    Label(pant_empresa).pack()

    Label(pant_empresa, text="¿Ya tienes cuenta?",font=("Arial",8)).place(x=135,y=510)
    vinculo=Label(pant_empresa, text="Inicia Sesión",font=("Arial",8,"underline"))
    vinculo.place(x=250,y=510)
    vinculo.bind("<Button-1>", inicio_sesion_empresa_X)
       
    boton_regresar = Button(pant_empresa, text="Regresar", bg="white", fg="black", height="2", width="11", font=("Arial", 10), command=cerrar_pant_empresa).place(x=130,y=540)
    
    boton_registrame = Button(pant_empresa, text="Regístrame", bg="black", fg="white", height="2", width="11", font=("Arial", 10), command=registrar_datos_empresa).place(x=250,y=540)

def pantalla_registro_usuario_X(event=None):
    cerrar_pantalla_sesion()
    global pant_usuario
    pant_usuario = Toplevel(pantalla)
    pant_usuario.geometry("450x700")
    pant_usuario.title("Registrate")
    pant_usuario.resizable(False,False)
    pant_usuario.iconbitmap("hub_de_seguridad.ico")

    global nombre_usuario
    global apellidos
    global sexo
    global telefono
    global email
    global contraseña

    nombre_usuario=StringVar()
    apellidos=StringVar()
    sexo=StringVar()
    telefono=StringVar()
    email=StringVar()
    contraseña=StringVar()
    
    #Registrate
    Label(pant_usuario, text="Registrate", font=("Arial Black", 16), height="5").pack()

    #Pedir Nombre
    Label(pant_usuario, text="Nombre", font=("Arial",12)).pack()
    nombre_usuario= Entry(pant_usuario, textvariable=nombre_usuario)
    nombre_usuario.pack()
    Label(pant_usuario).pack()

    #Pedir Apellidos
    Label(pant_usuario, text="Apellidos", font=("Arial",12)).pack()
    apellidos= Entry(pant_usuario, textvariable=apellidos)
    apellidos.pack()
    Label(pant_usuario).pack()

    #Pedir Género
    Label(pant_usuario, text="Sexo", font=("Arial",12)).pack()
    opciones=["Masculino","Femenino","Indistinto"]
    sexo=Combobox(pant_usuario, width="17", values=opciones, state="readonly")
    sexo.pack()
    Label(pant_usuario).pack()

    #Pedir Teléfono
    Label(pant_usuario, text="Teléfono", font=("Arial",12)).pack()
    telefono= Entry(pant_usuario, textvariable=telefono)
    telefono.pack()
    Label(pant_usuario).pack()

    #Pedir Email
    Label(pant_usuario, text="Email", font=("Arial",12)).pack()
    email= Entry(pant_usuario, textvariable=email)
    email.pack()
    Label(pant_usuario).pack()

    #Pedir Contraseña
    Label(pant_usuario, text="Contraseña", font=("Arial",12)).pack()
    contraseña= Entry(pant_usuario, textvariable=contraseña, show = "*")
    contraseña.pack()
    Label(pant_usuario).pack()

    Label(pant_usuario, text="¿Ya tienes cuenta?",font=("Arial",8)).place(x=135,y=530)
    vinculo=Label(pant_usuario, text="Inicia Sesión",font=("Arial",8,"underline"))
    vinculo.place(x=250,y=530)
    vinculo.bind("<Button-1>", inicio_sesion_X)
       
    boton_regresar = Button(pant_usuario, text="Regresar", bg="white", fg="black", height="2", width="11", font=("Arial", 10), command=cerrar_pant_usuario).place(x=130,y=560)
    
    boton_registrame = Button(pant_usuario, text="Regístrame", bg="black", fg="white", height="2", width="11", font=("Arial", 10), command=registrar_datos).place(x=250,y=560)
        
def pantalla_registro_empresa_X(event=None):
    cerrar_pantalla_empresa()
    global pant_empresa
    pant_empresa = Toplevel(pantalla)
    pant_empresa.geometry("450x750")
    pant_empresa.title("Registrate")
    pant_empresa.resizable(False,False)
    pant_empresa.iconbitmap("hub_de_seguridad.ico")

    global nombre
    global apellidos
    global razon_social
    global RFC
    global pais
    global ciudad
    global telefono
    global email
    global contraseña

    nombre=StringVar()
    apellidos=StringVar()
    razon_social=StringVar()
    RFC=StringVar()
    pais=StringVar()
    ciudad=StringVar()
    telefono=StringVar()
    email=StringVar()
    contraseña=StringVar()
    
    #Registrate
    Label(pant_empresa, text="Registra tu empresa", font=("Arial Black", 13), height="5").pack()

    #Pedir Nombre
    Label(pant_empresa, text="Nombre", font=("Arial",10)).pack()
    nombre= Entry(pant_empresa, textvariable=nombre)
    nombre.pack()

    #Pedir Apellidos
    Label(pant_empresa, text="Apellidos", font=("Arial",10)).pack()
    apellidos= Entry(pant_empresa, textvariable=apellidos)
    apellidos.pack()

    #Pedir Razon Social
    Label(pant_empresa, text="Razon_Social", font=("Arial",10)).pack()
    razon_social= Entry(pant_empresa, textvariable=razon_social)
    razon_social.pack()

    #Pedir RFC
    Label(pant_empresa, text="RFC", font=("Arial",10)).pack()
    RFC = Entry(pant_empresa, textvariable=RFC)
    RFC.pack()

    #Pedir Pais
    Label(pant_empresa, text="País", font=("Arial",10)).pack()
    opciones=["México","Estados Unidos","Canadá"]
    pais=Combobox(pant_empresa, width="17", values=opciones, state="readonly")
    pais.pack()

    #Pedir Ciudad
    Label(pant_empresa, text="Ciudad", font=("Arial",10)).pack()
    ciudad= Entry(pant_empresa, textvariable=ciudad)
    ciudad.pack()
    
    #Pedir Teléfono
    Label(pant_empresa, text="Teléfono", font=("Arial",10)).pack()
    telefono= Entry(pant_empresa, textvariable=telefono)
    telefono.pack()
    
    #Pedir Email
    Label(pant_empresa, text="Email", font=("Arial",10)).pack()
    email= Entry(pant_empresa, textvariable=email)
    email.pack()

    #Pedir Contraseña
    Label(pant_empresa, text="Contraseña", font=("Arial",10)).pack()
    contraseña= Entry(pant_empresa, textvariable=contraseña, show = "*")
    contraseña.pack()
    Label(pant_empresa).pack()

    Label(pant_empresa, text="¿Ya tienes cuenta?",font=("Arial",8)).place(x=135,y=510)
    vinculo=Label(pant_empresa, text="Inicia Sesión",font=("Arial",8,"underline"))
    vinculo.place(x=250,y=510)
    vinculo.bind("<Button-1>", inicio_sesion_empresa_X)
       
    boton_regresar = Button(pant_empresa, text="Regresar", bg="white", fg="black", height="2", width="11", font=("Arial", 10), command=cerrar_pant_empresa).place(x=130,y=540)
    
    boton_registrame = Button(pant_empresa, text="Regístrame", bg="black", fg="white", height="2", width="11", font=("Arial", 10), command=registrar_datos_empresa).place(x=250,y=540)

#CERRAR PANTALLAS.

def cerrar_elige():
    eligex.destroy()

def cerrar_pantalla():
    pantalla.destroy()

def cerrar_pantalla_sesion():
    pantalla_sesion.destroy()
    
def cerrar_pantalla_empresa():
    pantalla_empresa.destroy()

def cerrar_pant_empresa():
    pant_empresa.destroy()
    elige()

def cerrar_pant_usuario():
    pant_usuario.destroy()
    elige()

def cerrar_only_pant_empresa():
    pant_empresa.destroy()
    
def cerrar_only_pant_usuario():
    pant_usuario.destroy()

#PANTALLAS MENSAJE BIENVENIDA.
           
def pantalla_mensaje_sesion():
    global pant_inicio_sesion
    pant_inicio_sesion = Toplevel(pantalla)
    pant_inicio_sesion.geometry("300x300")
    pant_inicio_sesion.resizable(False,False)
    pant_inicio_sesion.iconbitmap("hub_de_seguridad.ico")

    #Bienvenido
    Label(pant_inicio_sesion, text="Bienvenid@, \n" + cadena, font=("Arial Black", 16), height="7").pack()
    
def pantalla_mensaje_empresa():
    global pant_inicio_sesion_empresa
    pant_inicio_sesion_empresa = Toplevel(pantalla)
    pant_inicio_sesion_empresa.geometry("500x300")
    pant_inicio_sesion_empresa.resizable(False,False)
    pant_inicio_sesion_empresa.iconbitmap("hub_de_seguridad.ico")

    #Bienvenido
    Label(pant_inicio_sesion_empresa, text="Bienvenido, \n" + cadena, font=("Arial Black", 16), height="7").pack()

#REGISTRAR DATOS

def registrar_datos():
    if (nombre_usuario.get()=="" or apellidos.get()=="" or sexo.get()=="" or telefono.get()=="" or email.get()=="" or contraseña.get()==""):
        messagebox.showinfo(message="Completa todos los campos")
    else:
        bd=pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            db="base_registro"
            )

        fcursor=bd.cursor()

        sql="INSERT INTO login(nombre, apellidos, sexo, telefono, email, contraseña) VALUES('{0}','{1}','{2}','{3}','{4}','{5}')".format(nombre_usuario.get(), apellidos.get(), sexo.get(), telefono.get(), email.get(), contraseña.get())

        try:
            fcursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Registro exitoso", title="Aviso")
            cerrar_only_pant_usuario()
            cerrar_elige()
        except:
            bd.rollback
            messagebox.showinfo(message="No registrado", title="Aviso")

        bd.close()

def registrar_datos_empresa():
    if (nombre.get()=="" or apellidos.get()=="" or razon_social.get()=="" or RFC.get()=="" or pais.get()=="" or ciudad.get()=="" or telefono.get()=="" or email.get()=="" or contraseña.get()==""):
        messagebox.showinfo(message="Completa todos los campos")
    else:
        bd=pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            db="base_registro"
            )

        fcursor=bd.cursor()

        sql="INSERT INTO login_empresa(nombre, apellidos, razon_social, RFC, pais, ciudad, telefono, email, contraseña) VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')".format(nombre.get(), apellidos.get(), razon_social.get(), RFC.get(), pais.get(), ciudad.get(), telefono.get(), email.get(), contraseña.get())

        try:
            fcursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Registro exitoso")
            cerrar_only_pant_empresa()
            cerrar_elige()
        except:
            bd.rollback
            messagebox.showinfo(message="No registrado")

        bd.close()

#VALIDAR DATOS
        
def validacion_datos():
    global user
    global cadena
    
    if (usuario_verificar.get()=="" or contraseña_verificar.get()==""):
        messagebox.showinfo(message="Completa todos los campos")
    else:
        bd=pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            db="base_registro"
            )

        fcursor=bd.cursor()

        validacion="SELECT contraseña and nombre FROM login WHERE email='"+usuario_verificar.get()+"' and contraseña='"+contraseña_verificar.get()+"'"
        usuario="SELECT nombre, apellidos FROM login WHERE email='"+usuario_verificar.get()+"' and contraseña='"+contraseña_verificar.get()+"'"

        fcursor.execute(validacion)
        
        if fcursor.fetchall():
            cerrar_pantalla_sesion()
            fcursor.execute(usuario)
            user=fcursor.fetchone()
            cadena=str(user)
            cerrar_pantalla_sesion()
            pantalla_mensaje_sesion()
        else:
            messagebox.showinfo(message="Email o Contraseña incorrecto, intenta nuevamente")

        bd.close()
    
def validacion_datos_empresa():
    global user
    global cadena
    
    if (empresa_verificar.get()=="" or contra_verificar.get()==""):
        messagebox.showinfo(message="Completa todos los campos")
    else:
        bd=pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            db="base_registro"
            )

        fcursor=bd.cursor()

        validacion="SELECT contraseña FROM login_empresa WHERE email='"+empresa_verificar.get()+"' and contraseña='"+contra_verificar.get()+"'"
        empresa="SELECT razon_social FROM login_empresa WHERE email='"+empresa_verificar.get()+"' and contraseña='"+contra_verificar.get()+"'"
                    
        fcursor.execute(validacion)
        
        if fcursor.fetchall():
            cerrar_pantalla_empresa()
            fcursor.execute(empresa)
            user=fcursor.fetchone()
            cadena=str(user)
            cerrar_pantalla_empresa()
            pantalla_mensaje_empresa()
        else:
            messagebox.showinfo(message="Email o Contraseña incorrecto, intenta nuevamente")

        bd.close()
    
menu_pantalla()
