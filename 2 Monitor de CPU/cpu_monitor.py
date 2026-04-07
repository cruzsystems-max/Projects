#Trabajo Práctico 3

#Autor: Cruz Asencios, Cristian Elvis
#link: https://youtu.be/KCCHcp1aB5E

import tkinter.ttk as ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import psutil
import datetime
import tkinter as tk
class App(tk.Tk):
    '''
    Esta clase crea una aplicación. La aplicación muestra información acerca del uso de la CPU,
    la Ram y el disco duro
    '''
    def __init__(self):
        super().__init__()

        #Configuración básica de la aplicación
        self.title("Monitor de Recursos")
        self.resizable(0,0)

        #Delacración de variable
        self.tiempo = np.arange(1,100,1)
        self.data = np.zeros(99)

        #Estilo para mejorar la apariencia del widged ProgessBar
        s = ttk.Style()
        s.theme_use('default')
        s.configure("custom.Horizontal.TProgressbar"
                    ,troughcolor='#5A504E'
                    ,background='#76ff03'
                    ,darkcolor="#390439"
                    ,lightcolor="#ED28F0"
                    ,bordercolor="black")

        #Frame principal: Este frame contiene otros 3 frames (para la gráfica, monitores e información adicional)
        main_frame=tk.Frame(self)
        main_frame.pack()
        main_frame.config(background="#424242")

        #aFrame: Frame para la información adicional
        self.aFrame=tk.Frame(main_frame, relief=tk.SUNKEN)
        self.aFrame.pack(padx=10,pady=10,side=tk.BOTTOM,fill=tk.X)
        self.aFrame.config(background="#212121")
        self.pack_information=tk.Label(self.aFrame,background="#212121", foreground="#76ff03")
        self.data_information=tk.Label(self.aFrame,background="#212121", foreground="#76ff03")
        self.pack_information.pack(padx=10,side=tk.LEFT)
        self.data_information.pack(padx=10,side=tk.RIGHT)

        #mFrame: Frame para la barra de procesos
        self.mFrame=tk.Frame(main_frame)
        self.mFrame.pack(padx=10,pady=10,side=tk.LEFT, fill=tk.X)
        self.mFrame.config(background="#616161")

        #pFrame: Frame para la gráfica del uso del CPU
        self.pFrame=tk.Frame(main_frame)
        self.pFrame.pack(padx=10,pady=10,side=tk.RIGHT,fill=tk.X)
        self.pFrame.config(background="#76ff03")

        #creamos 3 frames dentro adicionales dentro de pFrame
        self.p1Frame=tk.Frame(self.mFrame, background="#616161")
        self.p2Frame=tk.Frame(self.mFrame, background="#616161")
        self.p3Frame=tk.Frame(self.mFrame, background="#616161")
        self.p1Frame.pack(pady=15)
        self.p2Frame.pack(pady=15)
        self.p3Frame.pack(pady=15)
        #Ubicación de labels y progressbar dentro de p1Frame, p2Frame y p3Frame
        self.lblMonitor1=tk.Label(self.p1Frame,  font="Arial 10 bold", background="#616161")
        self.lblMonitor2=tk.Label(self.p2Frame,  font="Arial 10 bold", background="#616161")
        self.lblMonitor3=tk.Label(self.p3Frame,  font="Arial 10 bold", background="#616161")
        self.pVarMonitor1=ttk.Progressbar(self.p1Frame,length=250,style="custom.Horizontal.TProgressbar")
        self.pVarMonitor2=ttk.Progressbar(self.p2Frame,length=250,style="custom.Horizontal.TProgressbar")
        self.pVarMonitor3=ttk.Progressbar(self.p3Frame,length=250,style="custom.Horizontal.TProgressbar")
        self.lblMonitor1.grid(row=0,padx=5,pady=5,sticky=tk.W)
        self.pVarMonitor1.grid(row=1,padx=5,pady=5,sticky=tk.W)
        self.lblMonitor2.grid(row=0,padx=5,pady=5,sticky=tk.W)
        self.pVarMonitor2.grid(row=1,padx=5,pady=5,sticky=tk.W)
        self.lblMonitor3.grid(row=0,padx=5,pady=5,sticky=tk.W)
        self.pVarMonitor3.grid(row=1,padx=5,pady=5,sticky=tk.W)

        #gráfica del proceso de la cpu
        self.fig, self.ax = plt.subplots(figsize=(4, 2.75), facecolor="#616161")
        self.line, = self.ax.plot(self.tiempo,self.data,color="#76ff03")
        self.ax.set_title("CPU Usage [%]")
        self.ax.set_ylim(0, 105)
        self.ax.grid(linestyle='dashed')
        self.ax.set_facecolor("#072d0d")
        self.ax.tick_params(colors='black')
        self.ax.set_xticklabels([])
        self.graph = FigureCanvasTkAgg(self.fig, master=self.pFrame)
        self.graph.get_tk_widget().pack(expand=True, fill=tk.X)
        self.actualiza()

    def actualiza(self):
        '''Método que permite actualizar los datos y mostrarlos en la pantalla'''

        # tasa de uso de cpu
        cup_per = psutil.cpu_percent()
        self.cpu_per=tk.DoubleVar(value=cup_per)

        # Información de la memoria
        memory_info = psutil.virtual_memory()
        self.memory_infor_prog=tk.DoubleVar(value=memory_info.percent)

        # Información del disco duro
        disk_info = psutil.disk_usage("/") # Información del disco del directorio raíz
        self.disk_info_pers=tk.DoubleVar(value=disk_info.percent)
        # Información de Internet

        net_info = psutil.net_io_counters()
        # Obtener la hora actual del sistema
        current_time = datetime.datetime.now().strftime("%F %T") #% F año mes día% T hora, minuto y segundo

        self.data = np.roll(self.data,-1)
        self.data[-1] = cup_per
        self.line.set_ydata(self.data)
        self.graph.draw()

        self.pack_information.config(text=f"Net Info [in: {net_info.bytes_recv:,}|out: {net_info.bytes_sent:,}]")
        self.data_information.config(text=f"{current_time}")
        self.lblMonitor1.config(text=f"CPU Usage ({psutil.cpu_count(logical=False)} core): {cup_per}%")
        self.lblMonitor2.config(text=f"RAM usage (Total: {memory_info.total/1024/1024/1024:.2f} Gb): {memory_info.percent}%")
        self.lblMonitor3.config(text=f"HDD Usage (Total: {disk_info.total/1024/1024/1024:.2f} Gb): {disk_info.percent}%")
        self.pVarMonitor1.config(variable=self.cpu_per)
        self.pVarMonitor2.config(variable=self.memory_infor_prog)
        self.pVarMonitor3.config(variable=self.disk_info_pers)

        self.after(250, self.actualiza)

def main():
    app = App()#se instancia una aplicación de la clase App:
    app.mainloop()
if __name__=='__main__':
    main()
