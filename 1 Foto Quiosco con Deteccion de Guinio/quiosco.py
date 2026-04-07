#autor: Cruz Asencios, Cristian Elvis
#link:https://youtu.be/MKwdiutVYjU
#importación de las libreías necesarias
import tkinter as tk
from PIL import Image, ImageTk
import cv2
from datetime import datetime
from tkinter.messagebox import showinfo
#Definición de la clase App
class App(tk.Tk):
    '''
        Esta clase crea una aplicación que está basado en algoritmos entrenados (haarcascade) para
        la detección de rostro y la toma de captura mediante el guiño de un ojo.
        '''
    def __init__(self):
        super().__init__()

        #Configuraciones básicas de la aplicación
        self.geometry("600x460+100+100")
        self.title("Foto Quiosco by UPC")
        self.resizable(0, 0)
        self.protocol("WM_DELETE_WINDOW", self.quit)

        #inicialización de variables necesarias para el funcionamiento del problema
        self.width, self.height = 600, 400
        self.faces = []
        self.eyes = []
        self.cont = 0
        self.condition=True
        self.unicavez=True
        self.cap = cv2.VideoCapture(1)

        #haarcascades->Detección de rostro y ojos
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

        #LabelFrame- Canvas - statusbar
        frm = tk.LabelFrame(self, text="Image Preview")
        frm.pack(padx=10, pady=10)

        self.canvas = tk.Canvas(frm, width=self.width, height=self.height, borderwidth=1, relief='sunken')
        self.canvas.pack()
        self.statusbar = tk.Label(self, text="Listo…", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)



        self.update_image()

    def update_image(self):
        '''Método para actualizar cada uno de los fotogramas y mostrarlo como video '''
        # Este bloque se ejecuta una única vez. Sirve para inicializar el objeto fotoCap de la clase Details_Photo
        if self.unicavez==True:
            ret, frame = self.cap.read()
            _, x_win_pos, y_win_pos = self.geometry().split("+")
            self.fotoCap=Details_Photo(x_win_pos, y_win_pos, frame)
            self.fotoCap.quit2()
            self.unicavez=False


        ret, self.frame = self.cap.read()
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.frame = cv2.resize(self.frame, (self.width, self.height))
        self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

        self.faces = self.face_cascade.detectMultiScale(self.gray, scaleFactor=1.3,
                                       minNeighbors=5,
                                       minSize=(20,20),
                                       maxSize=(300,300))

        #Se grafica un rectángulo para la detección de rostro
        for (fx, fy, fw, fh) in self.faces:
            cv2.rectangle(self.frame, (fx, fy-20), (fx + fw, fy ), (0,255,0), thickness=-2)
            cv2.putText(self.frame, org=(fx+25,fy-5),text="ROSTRO DETECTADO", fontFace=cv2.FONT_HERSHEY_DUPLEX ,fontScale=0.5,color=(0,0,0),thickness=2)
            cv2.rectangle(self.frame, (fx, fy), (fx + fw, fy + fh), (0,255,0), thickness=2)

            #roi: para que la detección de los ojos se lleve a cabo dentro del cuadrado cuando se detecte el rostro
            roi_gray = self.gray[fy:fy + fh - 80, fx:fx + fw]
            roi_color = self.frame[fy:fy + fh, fx:fx + fw]

            self.eyes = self.eyes_cascade.detectMultiScale(roi_gray,scaleFactor=1.3,
                                       minNeighbors=5,
                                       minSize=(10,10),
                                       maxSize=(400,400))
            #se grafica un rectángulo para la detección de los ojos
            for (ex, ey, ew, eh) in self.eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 255), 2)

        #Si len(self.eyes)==0: -> No se detectan los ojos
        #si len(self.eyes)==1: -> Detección de un ojo
        #si len(self.eyes)==2: -> Detección de los dos ojo
        if (len(self.eyes) == 1):
            # se implemeta un contador para evitar falsos positivos. Es decir, para evitar casos en donde se toma
            #una captura sin haber guiñado el ojo o por simples parpadeos
            self.cont = self.cont + 1
            if self.cont == 5:
                self.cont = 0
                #Esta lógica sirve para controlar la captura. Se realiza otra captura, si y solo si, se guarda
                #o descarta la imagen o se cierra la otra ventana.
                if self.condition==True:
                    self.statusbar.config(text='Imagen Capturada')
                    ret, frame = self.cap.read()
                    _, x_win_pos, y_win_pos = self.geometry().split("+")
                    self.fotoCap= Details_Photo(x_win_pos, y_win_pos, frame)
                    self.condition=False
                else:
                    pass
        else:
            self.cont = 0


        try:
            photo = ImageTk.PhotoImage(image=Image.fromarray(self.frame))
            self.canvas.create_image(0, 0, image=photo, anchor='nw')

            self.canvas.image = photo
        except:
            pass

        #Statusbar para indicar el estado de de la detección de rostro
        if len(self.faces) == 1:
            self.statusbar.config(text='Rostro detectado')
        else:
            self.statusbar.config(text='Detectando rostro')
        self.condition=self.fotoCap.flag_control()
        self.after(100, self.update_image)

    def quit(self):
        '''Método para cerrar la ventana'''
        if self.cap.isOpened():
            self.cap.release()
        self.destroy()


class Details_Photo(tk.Toplevel):
    '''Esta clase muestra una captura. Se puede guardar o descartar la imagen capturada'''
    def __init__(self, x_win_pos, y_win_pos, frame,):

        super().__init__()
        self.title("Details Window")
        self.geometry(f"700x500+{int(x_win_pos) + 100}+{int(y_win_pos) + 100}")
        self.protocol("WM_DELETE_WINDOW", self.quit2)
        self.resizable(0, 0)
        self.grab_set()
        self.focus()
        self.condicion=False
        self.frame = frame
        self.width, self.height = 600, 400
        frm1 = tk.LabelFrame(self, text="Image Preview")
        frm2 = tk.Frame(self)
        frm1.pack(padx=10, pady=10)
        frm2.pack(padx=10, pady=10)

        self.canvas = tk.Canvas(frm1, width=self.width, height=self.height, borderwidth=1, relief='sunken')
        self.canvas.pack()

        self.Guardar = tk.Button(frm2, text="Guardar", width=16, command=self.guardar_photo)
        self.descartar = tk.Button(frm2, text="Descartar", width=16, command=self.descartar_photo)
        self.Guardar.grid(row=0, column=0, padx=10, pady=10)
        self.descartar.grid(row=0, column=1, padx=10, pady=10)

        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.frame = cv2.resize(self.frame, (self.width, self.height))

        try:
            photo = ImageTk.PhotoImage(image=Image.fromarray(self.frame))
            self.canvas.create_image(0, 0, image=photo, anchor='nw')
            self.canvas.image = photo
        except:
            pass

    def guardar_photo(self):
        '''Método relacionado al boton para capturar la imagen'''
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.frame = cv2.resize(self.frame, (self.width, self.height))
        filename = f"{datetime.now():'%d%m%Y_%H_%M'}.jpg"
        cv2.imwrite(filename, self.frame)
        showinfo("Foto guardada", f"Se guardo una captura de la imagen en {filename}")
        self.condicion=True
        self.destroy()

    def descartar_photo(self):
        '''Método relacionado al boton para descartar la imagen'''
        self.condicion=True
        self.destroy()


    def flag_control(self):
        '''Retorna verdadero si se ha pulsado el boton guardar o descartar'''
        if self.condicion==True:
            return True
        else:
            return False
    def quit2(self):
        '''Método relacionado para cerrar la venta'''
        self.condicion=True
        self.destroy()

app = App().mainloop()

