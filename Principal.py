import re
from tkinter import *
from tkinter import filedialog, messagebox
import os

#Para buscar y selecionar los directorios
def mostrarUrl():
    rutaOriginal = filedialog.askdirectory()
    rutaUrl.configure(text=rutaOriginal)
    inicio = rutaOriginal
    return inicio

def UrlDestino():
    rutaDestino = filedialog.askdirectory()
    rutaUrl2.configure(text=rutaDestino)
    destino = rutaDestino
    return destino


#Imprime la lista de archivos admitidos, si existen y si no existen 
def imprimirLista():
    rutaLista2 = rutaUrl.cget("text")
    listaJPG =[]
    listaMP4 = []
    listaPNG = []
    listaGIF =[]
    listaJPEG = []
    listaMP3 = []
    listawEBP = []
    textolista =textoscroll.get("1.0", "end")
    listFor=[".jpg", ".png", ".gif", ".mp3", ".mp4", ".webp",".jpeg"]
    #Separa los Diferentes formatos del directorio y muestra la cantidad
    if len(rutaLista2) !=0:
        rutaLista = os.listdir(rutaLista2)
        for i in range(len(rutaLista)):
            if re.search(listFor[0],rutaLista[i]):
                listaJPG.append(rutaLista[i])
            elif re.search(listFor[1], rutaLista[i]):
                listaPNG.append(rutaLista[i])
            elif re.search(listFor[2], rutaLista[i]):
                listaGIF.append(rutaLista[i])
            elif re.search(listFor[3], rutaLista[i]):
                listaMP3.append(rutaLista[i])
            elif re.search(listFor[4], rutaLista[i]):
                listaMP4.append(rutaLista[i])
            elif re.search(listFor[5], rutaLista[i]):
                listawEBP.append(rutaLista[i])
            elif re.search(listFor[6], rutaLista[i]):
                listaJPEG.append(rutaLista[i])
        
        datos = ("\nJPG  : "+ str(len(listaJPG))) +("\nJPEG : "+ str(len(listaJPEG))) + ("\nPNG  : "+ str(len(listaPNG)))+("\nGIF  : "+ str(len(listaGIF)))+ ("\nWEBP : "+ str(len(listawEBP)))+ ("\nMP3  : "+ str(len(listaMP3)))+ ("\nMP4  : "+ str(len(listaMP4)))
        if len(textolista) != 0:
            textoscroll.delete("1.0","end")
            textoscroll.insert(END, datos)
        else:
            textoscroll.insert(END, datos)
            
    else:
        messagebox.showerror("Error", "FALTA LA RUTA DEL DIRECTORIO")
   
def MoverArchivos():
    inicio= rutaUrl.cget("text")
    destino= rutaUrl2.cget("text")
    formato =var.get()
    titulo = entradaN.get()
    seleccion= []
    num=1
    #numSeleccion=1
    #Comprobar si existe direcciones
    if len(inicio) != 0 and len(destino) != 0:
        #Pide La casilla del nombre
        if len(titulo) !=0:
            lista = os.listdir(inicio)
            #Busca el Formato seleccionado y lo pone en una lista
            for i in range(len(lista)):
                if re.search("."+formato, lista[i]):
                    seleccion.append(lista[i])
                    #numSeleccion+=1
            #Comprueba si hay ese formato de archvos
            if len(seleccion) !=0:
                #RECORRE LISTA  FORMATO SELECCIONADO Y RENOMBRA Y LO MUEVE
                for j in range(len(seleccion)):
                    ruta1 = str(inicio+"/"+seleccion[j])
                    num2=str(num)
                    ruta2 = str(destino+"/"+titulo+num2+"."+formato)
                    os.rename(ruta1, ruta2)
                    if not seleccion == True and num < len(seleccion):
                        num += 1
                messagebox.showinfo("mensaje", (num,"Archvos Movidos Exitosamente"))
                
            else:
                messagebox.showerror("Error", ("No hay archivos "+ formato +"\nNingun archivo movido"))
        else:
            messagebox.showerror("Aviso","Falta el nombre de los archivos")
    else:
        messagebox.showerror("Aviso", "falta la ruta de directiorios")


    
root = Tk()

root.title("Rename and Move")
#Centrar ventena
ancho_ventana = 460
alto_ventana = 420
x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
root.geometry(posicion)
#root.configure(bg="#333")
root.call('wm','iconphoto', root._w, PhotoImage(file='fondo_icon.png'))
opciones = ["jpg", "jpeg", "mp4", "mp3", "png", "gif", "webp"]
var =StringVar(root)
var.set(opciones[0])
menuBar = OptionMenu(root, var, *opciones)
menuBar.config(width=7, height=2)
menuBar.place(x=340, y=60)

rutaAntrada = Label(root,  text="Ruta: ").place(x=10, y=35)
rutaDestino = Label(root,  text="Destino: ").place(x=10, y=120)
textoformato = Label(root, text="Elija el formato:").place(x=210, y=70)
pedirNombre = Label(root, text="Ingrese Nuevo Nombre: ").place(x=10, y=200)
#Entrada de rutas
rutaUrl = Label(root, bg="white", width=52, height=2)
rutaUrl2 = Label(root,  bg="white", width=52, height=2)
rutaUrl2.place(x=70, y=120)
rutaUrl.place(x=70, y=30)
#BOTONES
btnAbrir = Button(root, text="abrir ruta" , width=10, height=2, command=mostrarUrl).place(x=70, y=63)
btnAbrir1 = Button(root, text="abrir Destino" , width=11, height=2, command= UrlDestino).place(x=70, y=150)
btnAbrir3 = Button(root, text="Listar Archivos" , width=14, height=2, command=imprimirLista).place(x=290, y=150)
btnAbrir2 = Button(root, text="Mover Archivos" , width=12, height=2, command= MoverArchivos).place(x=25, y=260)

entradaN= StringVar()
entradaNombre = Entry(root, textvariable=entradaN, font=("Arial", 10))
entradaNombre.place(x=25, y=220, width=200, height=28 )

#SCROLL TEXTO
textoscroll= Text(root, height=10, width=23, font=("Arial", 15))
scroll = Scrollbar(root)
scroll.place(x=430, y=191, height=198)
textoscroll.place(x=250, y=190, height=200, width=180)

scroll.config(command= textoscroll.yview)
textoscroll.config(yscrollcommand= scroll.set)

root.resizable(0,0)
root.mainloop()
