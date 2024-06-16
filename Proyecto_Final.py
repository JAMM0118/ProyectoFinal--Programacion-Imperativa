from ntpath import join
from tkinter import * 
from tkinter import  messagebox, ttk
def salir():
    program.destroy()

def continuacion_De_orden():
    global mjs_2, historial_1, contador, contador_2, total_price
    pregunta =messagebox.askyesno("AGREGAR", "¿Necesitas agregar mas productos y servicios a esta orden?")
    if pregunta == True:
        Reiniciar()
        messagebox.showinfo("AGREGAR","Digite los productos y servicios que desea agregar")
        mjs_2 += f"Codigo: {codigo_Servicio} --- Valor unidad: ${precios.setdefault(str(z))} --- Cantidad: {cantidad_Servicio}\n\
Codigo: {codigo_producto} --- Valor unidad: ${precios.setdefault(str(n))} --- Cantidad: {cantidad_producto}\n"
        if contador == contador_2:
            historial_1 = ""
            contador_2 -=1
        else: contador_2 +=1
        if contador > 1:
            contador -=1
        else: contador = 1
    else:
        sugerencia()
        history["state"] =NORMAL
        mjs_2 = ""
        total_price = 0
        return 0
            
def noserepite(codigo_3):
    global codes_1, codes
    for i in range(len(codes_1)):
        if codigo_3 == codes_1[i]:
            return True
    for i in range(len(codes)):
        if codigo_3 == codes[i]:
            return True
    return False
def historial():
    if historial_1 != None:
        history["state"] = NORMAL
        messagebox.showinfo("HISTORIAL",f"{historial_1}")

def agregados():
    global program_2
    codigo_new = (codigo_.get())
    descripcion_new = descripcion_.get()
    valor_new = valor_.get()
    if descripcion_new and codigo_new and valor_new != "":
        if not noserepite(int(codigo_new)):
            if int(codigo_new) < 10000 and what == "servicio" :
                if int(valor_new) < 100000000  :
                    codes_1.append(int(codigo_new))
                    precios[codigo_new] = int(valor_new)
                    servicio_new_1 = f"\nCodigo {codigo_new} : ${valor_new}    --"
                    servicio_new = f" {codigo_new} : {descripcion_new} --"
                    significado_codigos_1.append(servicio_new) 
                    precios2.append(servicio_new_1) 
                    messagebox.showinfo("EXITO","TU SERVICIO HA SIDO AGREGADO CON EXITO")
                    program_2.destroy()    
                else: 
                    messagebox.showwarning("¡CUIDADO!", "El VALOR INGRESADO ES DEMASIADO ALTO VERIFICA SI EL VALOR ES CORRECTO")
                    program_2.destroy()
            elif int(codigo_new) < 10000 and what == "producto" :
                if int(valor_new) < 100000000 :
                    codes.append(int(codigo_new))
                    precios[codigo_new] = int(valor_new)
                    producto_new = f" {codigo_new} : {descripcion_new} --"
                    producto_new_1 = f"\nCodigo {codigo_new} : ${valor_new}    --"
                    significado_codigos.append(producto_new)
                    precios2.append(producto_new_1)
                    program_2.destroy()
                    messagebox.showinfo("EXITO","TU PRODUCTO HA SIDO AGREGADO CON EXITO")
                else: 
                    messagebox.showwarning("¡CUIDADO!", "El VALOR INGRESADO ES DEMASIADO ALTO VERIFICA SI EL PRECIO ES CORRECTO")
                    program_2.destroy()
            else:
                messagebox.showwarning("¡CUIDADO!", f"El CODIDO DEL {what.upper()} SOLO DEBE CONTENER 4 DIGITOS")
                program_2.destroy()
        else:
            messagebox.showwarning("¡CUIDADO!", f"ESTE CODIDO YA EXISTE")
            program_2.destroy()
    else:
        messagebox.showwarning("¡CUIDADO!", f"PRIMERO DEBES DIGITAR TODOS LOS CAMPOS")
        program_2.destroy()

def añadidos():
    global codigo_, descripcion_,valor_,  what, program_2
    what = ""
    nuevos = messagebox.askyesnocancel("Nuevos productos y/o servicios", "¿Que deseas agregar? Producto o Servicio \nPresiona (si) para agregar un producto, Presiona (no) para un servicio" )
    if nuevos == True:
        what += "producto"
    elif nuevos == False:
        what = "servicio"
    else:
        return 0
    program_2 = Tk()
    program_2.title("Nice Two")
    program_2.geometry("300x190")
    program_2.config(bg="#213141")
    program_2.iconbitmap("favicon.ico")
    second_title = Label(program_2,text=f"Datos del nuevo {what}", font=("Swift",16),bg="#17202A", fg="white", width="100", height="1")
    second_title.pack()
    codigo= Label(program_2,text= "CODIGO")
    codigo_= Entry(program_2,width=20)  
    valor= Label(program_2,text= f"VALOR DEL {what.upper()}")
    valor_= Entry(program_2,width=20)  
    descripcion= Label(program_2,text= "DESCRIPCION")
    descripcion_= Entry(program_2,width=20)
    agregar = ttk.Button(program_2,text="SUBMIT", command= agregados)
    agregar.place(x=117,y=155)
    codigo.place(x=15, y=60)
    codigo_.place(x=157, y=60)
    descripcion.place(x=15,y=90)
    descripcion_.place(x=157,y=90)
    valor_.place(x=157,y=120)
    valor.place(x=15,y=120)
    program_2.mainloop()
    
def sugerencia():
    messagebox.showinfo("SUGERENCIA", "SI DESEAS CALCULAR EL PRECIO DE OTRO PRODUCTO Y SERVICIO PRESIONA EL BOTON REINICIAR")

def alerta():
    messagebox.showwarning("¡ALERTA!","Debes digitar toda la informacion de manera correcta")

def error(who):
    messagebox.showerror("¡REVISA LOS DATOS INGRESADOS!", f"El codigo del {who} ingresado no existe, vuelve a ingresar los datos")

def codigos():
    messagebox.showinfo("¡AYUDA!", "".join(significado_codigos) +"\n" +"".join(significado_codigos_1))
def precios__():
    messagebox.showinfo("¡INFORMACION!", "".join(precios2))

def Reiniciar():
    cantidad_1.delete(0,END)
    precio_1.delete(0,END)
    precio_.delete(0,END)
    cantidad_.delete(0,END)
    total_.delete(0,END)
    servicio_.delete(0,END)
    producto_.delete(0,END)
    reiniciar["state"] = DISABLED
    
def calcular_precios():
    global historial_1, contador, mjs_2, codigo_producto, codigo_Servicio,cantidad_producto, cantidad_Servicio, n ,z, total_price
    codigo_Servicio = (servicio_.get())
    codigo_producto = (producto_.get())
    cantidad_producto = (cantidad_1.get())
    cantidad_Servicio = (cantidad_.get())
    precio_total = 0
    if codigo_producto and codigo_Servicio and cantidad_Servicio and cantidad_producto != "" :
        for z in codes_1:
            if codigo_Servicio == str(z):
                precio_.delete(0,END)
                precio_.insert(0,f"${(precios.setdefault(str(z)))*int(cantidad_Servicio)}")
                precio_total += (precios.setdefault(str(z)))*int(cantidad_Servicio) 
                break 
        for n in codes:        
            if codigo_producto == str(n):
                precio_1.delete(0,END)
                precio_1.insert(0,f"${(precios.setdefault(str(n)))*int(cantidad_producto)}")
                precio_total += (precios.setdefault(str(n)))*int(cantidad_producto)
                break
        total_price += precio_total    
        if int(cantidad_Servicio) and int(cantidad_producto) > 0 :
            if codigo_producto != str(n):
                error(who="producto")
                Reiniciar()
            elif codigo_Servicio != str(z):
                error(who= "servicio")
                Reiniciar()
            else:    
                reiniciar["state"] = NORMAL
                total_.delete(0,END)
                total_.insert(0,f"${precio_total}")
                for i in range(contador,contador+1):
                    mjs = f"Orden {i} \n\nCodigo: {codigo_Servicio} --- Valor unidad: ${precios.setdefault(str(z))} --- Cantidad: {cantidad_Servicio}\n\
Codigo: {codigo_producto} --- Valor unidad: ${precios.setdefault(str(n))} --- Cantidad: {cantidad_producto}\n{mjs_2}\n\nTotal a pagar: ${total_price}\n\n" 
                    historial_1 +=(mjs)
                    contador +=1
                continuacion_De_orden()
        else:
            alerta()
            Reiniciar()   
    else:
        alerta()
historial_1 = ""
mjs_2 = ""
contador=1
contador_2 = 2
total_price = 0
codes = [1431,2432,1500,2440,2502]
codes_1 = [1214,1987,1377,1133,1213]
precios = {"1431" : 110000, "2432" : 35000, "1500" : 135000,"2440" : 150000, "2502" : 75000, "1214" : 400000,
"1987" : 8000,"1377" : 415000,"1133" : 435000,"1213" : 300000 }
precios2 = ["Codigo 1431: $110.000   --  Codigo 2432 : $35.000 -- \nCodigo 1500 : $135.000  --  Codigo 2440 : $150.000 -- \nCodigo 2502 : $75.000 \
   --  Codigo 1214 : $400.000 --\nCodigo 1987 : $8.000      --  Codigo 1377 : $415.000 --\nCodigo 1133 : $435.000  --  Codigo 1213 : $300.000 --"]
significado_codigos = ["Productos = 1431: Bujías -- 2432: Filtro de aire -- \
\n1500: Calibrador de llantas -- 2440: Baterías --\n2502: Lubricantes --" ]
significado_codigos_1 = ["\nServicios = 1214: Limpieza integral -- 1133: Cambio de bujías -- 1377: Hojalatería y pintura -- \
1213: Cambio de filtro de aire -- 1987: Calibracion de llantas con nitrogeno --"] 
program = Tk()
program.title("Nice")
program.geometry("734x300")
program.iconbitmap("favicon.ico")
program.config(bg="#213141")
first_title = Label(text="Centro de Servicio Automotriz", font=("Swift",16),bg="#17202A", fg="white", width="100", height="1")
servicio= Label(program,text= "INGRESA EL CODIGO DEL SERVICIO A REALIZAR")
servicio_= Entry(program,width=20)
producto= Label(program,text= "INGRESA EL CODIGO DEL PRODUCTO A VENDER")
producto_= Entry(program,width=20)
help = Label(program, text="EN CASO DE NO RECORDAR LOS CODIGOS \n PRESIONE EL BOTON ¡CODIGOS!")
help1 = Label(program, text="SI DESEAS VER EL VALOR UNITARIO \nDE CADA SERVICIO Y/O PRODUCTO \nPRESIONE EL BOTON ¡PRECIOS!")
ayuda = ttk.Button(program,text="¡Codigos!", command=codigos)
ayuda1 = ttk.Button(program,text="¡Precios!", command=precios__)
precio =ttk.Button(program,text="CALCULAR PRECIO", command=  calcular_precios )
reiniciar = ttk.Button(program,text="REINICIAR", command=  Reiniciar, state=DISABLED )
nuevos = ttk.Button(program,text="AÑADIR UN PRODUCTO Y/O SERVICIO", command= añadidos)
precio_servicio = Label(program, text="VALOR DEL SERVICIO")
precio_producto = Label(program, text="VALOR DEL PRODUCTO")
precio_1= Entry(program,width=20)
precio_= Entry(program,width=20)
cantidad_servi = Label(program, text="¿Cantidad de veces que se realizara este servicio?")
cantidad_product = Label(program, text="¿Cantidad de productos a vender?")
cantidad_1= Entry(program,width=20)
cantidad_= Entry(program,width=20)
total_ = Entry(program,width=20)
total = Label(program, text="PRECIO TOTAL")
salir1 = ttk.Button(program,text="EXIT", command=salir)
history = ttk.Button(program,text="HISTORIAL", command=historial, state=DISABLED)

first_title.pack()
producto.place(x=20,y=50)
reiniciar.place(x=441, y=260)
salir1.place(x=641, y=260)
history.place(x=541, y=260)
producto_.place(x=290, y=50)
cantidad_product.place(x=20, y=80)
cantidad_1.place(x=290, y=80)
servicio.place(x=20,y=110)
servicio_.place(x=290,y=110)
cantidad_servi.place(x=20,y=140)
cantidad_.place(x=290, y=140)
help.place(x=450,y=50)
help1.place(x=475,y=130)
ayuda.place(x=540,y=90)
ayuda1.place(x=545,y=190)
precio.place(x=150,y=170)
precio_servicio.place(x=20, y=200)
precio_.place(x=290,y=200)
precio_producto.place(x=20, y=230)
precio_1.place(x=290, y=230)
total.place(x=20, y=260)
total_.place(x=290, y=260)
nuevos.place(x=475,y=225)

program.mainloop()