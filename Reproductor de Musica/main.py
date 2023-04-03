from tkinter import Button, Label,Tk,filedialog, ttk, Frame, PhotoImage
import pygame
import mutagen

pygame.mixer.init()
pygame.mixer.init(frequency=44100)
musica =''
sentido = ''

def abrir_archivo():
	global sentido, sig, m,musica
	sig = 0
	m = 0
	sentido = filedialog.askopenfilenames(initialdir ='/', 
											title='Elige las canciones', 
										filetype=(('mp3 files', '*.mp3*'),('All files', '*.*')))
	m = len(sentido)
	musica = sentido[sig]

	nombre_m = musica.split('/')
	nombre_m = nombre_m[-1]

def iniciar_reproduccion():
	global musica, sentido, sig, m, update

	musica = sentido[sig]
	nombre_m = musica.split('/')
	nombre_m = nombre_m[-1]
	nombre['text']= nombre_m

	time = pygame.mixer.music.get_pos()
	x = int(int(time)*0.001)
	tiempo['value']= x  #posicion en la barra a lo largo de tiempo

	y = float(int(volumen.get())*0.1)
	pygame.mixer.music.set_volume(y)
	nivel['text']= int(y*100)

	audio = mutagen.File(musica)	
	log = audio.info.length
	min, seg = divmod(log, 60)

	min, seg = int(min), int(seg)
	tt = min*60 + seg
	tiempo['maximum']= tt  #Tiempo que dura la cancion
	texto['text']= str(min) + ":" + str(seg)
	
	update = ventana.after(100 , iniciar_reproduccion)

	if x == tt:
		texto['text']= "00:00"
		if sig != m:
			sig = sig + 1
			ventana.after(100 , iniciar_reproduccion)
			pygame.mixer.music.play()
		if sig == m:
			sig = 0

def iniciar():
	global musica
	pygame.mixer.music.load(musica)
	pygame.mixer.music.play()
	iniciar_reproduccion()

def retroceder():
	global sig,m

	if sig >0:
		sig = sig-1
	else:
		sig = 0
	cantidad['text'] = str(sig)+'/'+str(m)

def adelantar():
	global sig, m

	if sig == m-1:
		sig = 0
	else:
		sig = sig + 1
	cantidad['text'] = str(sig)+'/'+str(m)

def stop():
	global update
	pygame.mixer.music.stop()
	ventana.after_cancel(update)  

def pausa():
	global update
	pygame.mixer.music.pause()
	ventana.after_cancel(update)

def continuar():
	pygame.mixer.music.unpause()
	ventana.after(100 , iniciar_reproduccion)

ventana =Tk()
ventana.title('Reproductor de Musica')
ventana.iconbitmap('icono.ico')
ventana.config(bg='black')
ventana.resizable(0,0)

estilo = ttk.Style()
estilo.theme_use('clam')
estilo.configure("Vertical.TProgressbar", foreground='green2', background='green2',troughcolor='black',
	bordercolor='black',lightcolor='green2', darkcolor='green2')

frame1 = Frame(ventana, bg='black', width=600, height=350)
frame1.grid(column=0,row=0, sticky='nsew')
frame2 = Frame(ventana, bg='black', width=600, height=50)
frame2.grid(column=0,row=1, sticky='nsew')

barra1 = ttk.Progressbar(frame1, orient= 'vertical', length=300,  maximum=300, style="Vertical.TProgressbar")
barra1.grid(column=0,row=0, padx = 1)
barra17 = ttk.Progressbar(frame1, orient= 'vertical', length=300,  maximum=300, style="Vertical.TProgressbar") 


estilo1 = ttk.Style()
estilo1.theme_use('clam')
estilo1.configure("Horizontal.TProgressbar", foreground='red', background='black',troughcolor='#ffffff',
																bordercolor='#ffffff',lightcolor='#ffffff', darkcolor='black')

tiempo = ttk.Progressbar(frame2, orient= 'horizontal', length = 390, mode='determinate',style="Horizontal.TProgressbar")
tiempo.grid(row=0, columnspan=8, padx=5)
texto = Label(frame2, bg='black', fg='#ffffff', width=5)
texto.grid(row=0,column=8)

nombre = Label(frame2, bg='black', fg='#ffffff', width=55)
nombre.grid(column=0, row=1, columnspan=8, padx=5)
cantidad = Label(frame2, bg='black', fg='#ffffff')
cantidad.grid(column=8, row=1)

imagen1  = PhotoImage(file ='carpeta.png')
imagen2  = PhotoImage(file ='play.png')
imagen3  = PhotoImage(file ='pausa.png')
imagen4 = PhotoImage(file ='repetir.png')
imagen5 = PhotoImage(file ='stop.png')
imagen6 = PhotoImage(file ='anterior.png')
imagen7 = PhotoImage(file ='adelante.png')

boton1 = Button(frame2, image= imagen1, bg='black',command= abrir_archivo)
boton1.grid(column=0, row=2, pady=10)
boton2 = Button(frame2, image= imagen2, bg='black', command=iniciar)
boton2.grid(column=1, row=2, pady=10)
boton3 = Button(frame2,image= imagen3, bg='black', command=stop)
boton3.grid(column=2, row=2, pady=10)
boton4 = Button(frame2,image= imagen4, bg='black', command=pausa)
boton4.grid(column=3, row=2, pady=10)
boton5 = Button(frame2, image= imagen5, bg='black',command=continuar)
boton5.grid(column=4, row=2, pady=10)
atras = Button(frame2, image= imagen6, bg='black',command= retroceder)
atras.grid(column=5, row=2, pady=10)
adelante = Button(frame2, image= imagen7, bg='black',command=adelantar)
adelante.grid(column=6, row=2, pady=10)

volumen = ttk.Scale(frame2, to = 10, from_ =0, orient='horizontal',length=90, style= 'Horizontal.TScale')
volumen.grid(column=7, row=2)

style = ttk.Style()
style.configure("Horizontal.TScale", bordercolor='#ffffff', troughcolor='black', background= '#ffffff', 
	foreground='black',lightcolor='black',darkcolor='black')  

nivel = Label(frame2, bg='black', fg='#ffffff', width=3)
nivel.grid(column=8,row=2)

ventana.mainloop()












































