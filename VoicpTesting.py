from vosk import Model, KaldiRecognizer
import pyaudio
import json
import pyautogui
import os
from tkinter import* 
from PIL import ImageTk, Image
import win32gui
it=Tk()#interfaz
canvas1=Canvas(it,width=330,height=210)
tagname='event'

buttonAccionImageIndex = 0#contador para las imagenes
textoAccionTextIndex=0
barraAcciónImageIndex =0
def enter():
    canvas1.config(cursor="hand2")

def leave():
    canvas1.config(cursor= "")


numeros_dict = {
    "cero": 0,
    "uno": 1,
    "dos": 2,
    "tres": 3,
    "cuatro": 4,
    "cinco": 5,
    "seis": 6,
    "siete": 7,
    "ocho": 8,
    "nueve": 9,
    "diez": 10,
    "once": 11,
    "doce": 12,
    "trece": 13,
    "catorce": 14,
    "quince": 15,
    "dieciséis": 16,
    "diecisiete": 17,
    "dieciocho": 18,
    "diecinueve": 19,
    "veinte": 20,
    "veintiuno": 21,
    "veintidós": 22,
    "veintitrés": 23,
    "veinticuatro": 24,
    "veinticinco": 25,
    "veintiséis": 26,
    "veintisiete": 27,
    "veintiocho": 28,
    "veintinueve": 29,
    "treinta": 30,
    "treinta y uno": 31,
    "treinta y dos": 32,
    "treinta y tres": 33,
    "treinta y cuatro": 34,
    "treinta y cinco": 35,
    "treinta y seis": 36,
    "treinta y siete": 37,
    "treinta y ocho": 38,
    "treinta y nueve": 39,
    "cuarenta": 40,
    "cuarenta y uno": 41,
    "cuarenta y dos": 42,
    "cuarenta y tres": 43,
    "cuarenta y cuatro": 44,
    "cuarenta y cinco": 45,
    "cuarenta y seis": 46,
    "cuarenta y siete": 47,
    "cuarenta y ocho": 48,
    "cuarenta y nueve": 49,
    "cincuenta": 50,
    "cincuenta y uno": 51,
    "cincuenta y dos": 52,
    "cincuenta y tres": 53,
    "cincuenta y cuatro": 54,
    "cincuenta y cinco": 55,
    "cincuenta y seis": 56,
    "cincuenta y siete": 57,
    "cincuenta y ocho": 58,
    "cincuenta y nueve": 59,
    "sesenta": 60,
    "sesenta y uno": 61,
    "sesenta y dos": 62,
    "sesenta y tres": 63,
    "sesenta y cuatro": 64,
    "sesenta y cinco": 65,
    "sesenta y seis": 66,
    "sesenta y siete": 67,
    "sesenta y ocho": 68,
    "sesenta y nueve": 69,
    "setenta": 70,
    "setenta y uno": 71,
    "setenta y dos": 72,
    "setenta y tres": 73,
    "setenta y cuatro": 74,
    "setenta y cinco": 75,
    "setenta y seis": 76,
    "setenta y siete": 77,
    "setenta y ocho": 78,
    "setenta y nueve": 79,
    "ochenta": 80,
    "ochenta y uno": 81,
    "ochenta y dos": 82,
    "ochenta y tres": 83,
    "ochenta y cuatro": 84,
    "ochenta y cinco": 85,
    "ochenta y seis": 86,
    "ochenta y siete": 87,
    "ochenta y ocho": 88,
    "ochenta y nueve": 89,
    "noventa": 90,
    "noventa y uno": 91,
    "noventa y dos": 92,
    "noventa y tres": 93,
    "noventa y cuatro": 94,
    "noventa y cinco": 95,
    "noventa y seis": 96,
    "noventa y siete": 97,
    "noventa y ocho": 98,
    "noventa y nueve": 99,   "cien": 100
}
def cerrar(event):
    os._exit(0)
    
variables_dict = {}
funciones_set = {}
model = Model(r"vosk-model-small-es-0.42")
recognizer = KaldiRecognizer(model, 16000)

# Configuración del micrófono
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

def capture_audio():
    audio_buffer = b""
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if len(data) == 0:
            break
        audio_buffer += data
        if recognizer.AcceptWaveform(data):
            resultado = recognizer.Result()
            resultado_json = json.loads(resultado)
            if "text" in resultado_json:
                texto_dictado = resultado_json["text"]
                print("Texto dictado:", texto_dictado)
                return texto_dictado

def CreateFunc():
    # Solicitar el nombre de la función al usuario
    print("Por favor, dicta el nombre de la función:")
    nombre_funcion = capture_audio()
    #se guarda la funcion en el diccionario
    funciones_set[nombre_funcion] = nombre_funcion
    # Generar la estructura de la función con el nombre dictado
    pyautogui.write(f"def {nombre_funcion}():")
    pyautogui.press('enter')

def CallFunc():
    print("Por favor, dicta el nombre de la función:")
    nombre_funcion = capture_audio()
    funciones_mencionadas = [v for v in funciones_set if v in nombre_funcion]
    if funciones_mencionadas:
        for funcion in funciones_mencionadas:
            funcion_name = funciones_set[funcion]
            #{mostrar:mostrar}
            funcionFinal=funcion_name
    pyautogui.write(f"{funcionFinal}()")
    pyautogui.press('enter')
    



def variable():
    # Solicitar el nombre de la variable al usuario
    print("Por favor, dicta el nombre de la variable:")
    nombre_variable = capture_audio()
    # Imprimir el nombre de la variable
    print("Por favor, dicta el valor de la variable:")
    valor_variable = capture_audio()
    if valor_variable in numeros_dict:
        valor_entero = numeros_dict[valor_variable]
        pyautogui.write(f'{nombre_variable} = {valor_entero}')
    else:
        pyautogui.write(f'{nombre_variable} = "{valor_variable}"')
    variables_dict[nombre_variable] = valor_variable
    pyautogui.press('enter')

def CicloFor():

    print("Por favor, dicta la variable inicial :")
    texto_dictado = capture_audio()
    variables_mencionadas = [v for v in variables_dict if v in texto_dictado]
    # Tecla la sintaxis del ciclo for en Python
    if variables_mencionadas:
        # Si se mencionan variables, imprimir cada una de ellas
        for variable in variables_mencionadas:
            valor_variable = variables_dict[variable]
            variable1=variable

    print("Porfavor, dicra la variable final ")
    texto_dictado = capture_audio()
    variables_mencionadas = [v for v in variables_dict if v in texto_dictado]
    if variables_mencionadas:
        # Si se mencionan variables, imprimir cada una de ellas
        for variable in variables_mencionadas:
            valor_variable = variables_dict[variable]
            variable2=variable
    
    pyautogui.write(f'for {variable1} in range ({variable2}):')
    pyautogui.press('enter')

def Imprimir():
    # Dicta el texto para imprimir
    print("Por favor, dicta el texto a imprimir:")
    texto_dictado = capture_audio()


    # Verificar si hay variables mencionadas en el texto dictado
    variables_mencionadas = [v for v in variables_dict if v in texto_dictado]
    
    if variables_mencionadas:
        # Si se mencionan variables, imprimir cada una de ellas
        for variable in variables_mencionadas:
            valor_variable = variables_dict[variable]
            pyautogui.write(f'print({variable})')
            pyautogui.press('enter')
    else:
        # Si no se mencionan variables, imprimir el texto tal cual
        pyautogui.write(f'print("{texto_dictado}")')
    pyautogui.press('enter')

def Compilar():
    pyautogui.hotkey('ctrl', 's')
    pyautogui.hotkey('ctrl', 'alt', 'n')
    pyautogui.press('enter')

def GuardarDocumento():
    pyautogui.hotkey('ctrl', 's')
    pyautogui.press('enter')

#BotonRojo=PhotoImage(file="BotonRojo.png")
def cambiarImagen():
    global buttonAccionImageIndex
    buttonAccionImageIndex = (buttonAccionImageIndex + 1) % len(buttonAccionImages)
    canvas1.itemconfig(buttonAccion, image=buttonAccionImages[buttonAccionImageIndex])
    global textoAccionTextIndex
    textoAccionTextIndex=(textoAccionTextIndex +1)%len(texto)
    canvas1.itemconfig(textoAccion, text= texto[textoAccionTextIndex])
    
    global barraAcciónImageIndex
    barraAcciónImageIndex=(barraAcciónImageIndex+1)%len(barraAccionImages)
    canvas1.itemconfig(barra_window2,image=barraAccionImages[barraAcciónImageIndex])
    it.update()

def renaudar(event):
    global control
    cambiarImagen()
    control=True
    run()

def pausa(event):
    global control
    control=False
    
    cambiarImagen()
def pausa2():
    global control
    control=False
    cambiarImagen
def run():
    global control
    intento=0
    os.system('cls')
    while control: #
        
        
        canvas1.tag_bind(buttonAccion,"<Button-1>",pausa)
        it.update()
        #print(control) #para depurar para ver si funciona 
        if control==False:
            break

        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            valorVoice = recognizer.Result()
            valorVoice = json.loads(valorVoice)  # Guardando data que se introduce
            #print(valorVoice,intento) # para depurar el codigo
            if valorVoice['text'] == '': #si no hay nada 
                intento+=1
                
            if intento==3:
                cambiarImagen()
                break   
            if "crear función" in valorVoice['text'] or "crear funcion" in valorVoice['text']:
                print("funcion")
                intento=0
                CreateFunc()
            elif "guardar documento" in valorVoice['text'] or "guardar" in valorVoice['text']:
                print("Guardando documento")
                intento=0
                GuardarDocumento()
            elif "llamar" in valorVoice['text'] or "llama" in valorVoice['text']:
                print("llamando funcion")
                intento=0
                CallFunc()
            elif "en primer" in valorVoice['text'] or "imprimir" in valorVoice['text'] or "imprime" in valorVoice['text']:
                print("Imprimiendo")
                intento=0
                Imprimir()
            elif "variable" in valorVoice['text']:
                print("Variable")
                intento=0
                variable()
            elif "en pila" in valorVoice['text'] or "compila" in valorVoice['text'] or "compilar" in valorVoice['text']:
                print("compilando")
                intento=0
                Compilar()
            elif "for" in valorVoice['text'] or "ciclo for" in valorVoice['text'] or "ciclo para" in valorVoice['text']:
                print("Generando ciclo")
                intento=0
                CicloFor()
            elif "sierra" in valorVoice['text'] or "cierra" in valorVoice['text']  or "cerrar" in valorVoice['text']:
                print("Cerrando Programa")
                os._exit(0)
                
            elif "pausa" in valorVoice['text'] or "pausar" in valorVoice ['text']:
                cambiarImagen()
                break
            elif"enter " in valorVoice['text'] or "ente" in valorVoice['text']:
                pyautogui.press('enter')
            elif"arriba" in valorVoice['text'] or "arribas" in valorVoice['text']:
                pyautogui.press('up')
            elif"abajo" in valorVoice['text'] or "abajos" in valorVoice['text']:
                pyautogui.press('down')
            elif"salir" in valorVoice['text'] or "sal" in valorVoice['text']:
                pyautogui.hotkey('shift', 'tab')
            


    VentanaPrincipal()





def VentanaPrincipal():
    
    it.attributes('-alpha',0.85)#para hacer la ventana semitransparente
    it.geometry('+1450+750')
    it.minsize(330, 210)
    it.maxsize(330,  501)
    it.overrideredirect(True)
    it.resizable(0,1)#para que no se pueda redimenzionar en ninguna dimensión 
    it.attributes('-topmost',True)# para que no se cierre la ventana, ni se minimize al hacer click en otra función  

    canvas1.place(x=-1,y=-1)
    img=Image.open("FondoLargo.png")
    resized_image=img.resize((330,210))
    bgImage=ImageTk.PhotoImage(resized_image)
    #bg=canvas1.create_image(0,0,image=bgImage,anchor=NW)
    canvas1.create_image(0,0,image=bgImage,anchor="nw")


    global buttonAccionImages
    buttonAccionImages = [
        ImageTk.PhotoImage(Image.open("cirulo.png")),
        ImageTk.PhotoImage(Image.open("BotonRojo.png"))
    ]
    global buttonAccion
    global barraAccionImages
    barraAccionImages=[
        ImageTk.PhotoImage(Image.open("Mesa_de_trabajo_15.png")),
        ImageTk.PhotoImage(Image.open("Mesa_de_trabajo_7.png"))
    ]
    global barra_window2

    #bboton de pausa
    boton_pausa=Image.open("pausa.png")
    boton_pausaTk=ImageTk.PhotoImage(boton_pausa)

    
    #botonAcción
    buttonAccion = canvas1.create_image(165, 90, image=buttonAccionImages[0], tag=tagname)
    
    #boton cerrar
    botonCerrar=Image.open("Mesa_de_trabajo_5.png")
    BotonCerrarTk=ImageTk.PhotoImage(botonCerrar)
    #buttonCerrar=Button(it, text="Quit", command=it.destroy,activebackground= "red")#boton para cerrar 
    #button1_window1 = canvas1.create_window(300,0,anchor="nw",window=buttonCerrar)#Coordenadas en x y , nw nortwest 

    barra_window2=canvas1.create_image(40,180,anchor="nw",image=barraAccionImages[0],tag=tagname)
    
    global texto
    texto = ["SILENCIADO","ESCUCHANDO"]     
    global textoAccion
    textoAccion=canvas1.create_text(171,169, text=texto[0],font=("Helvetica",16),fill="white")
    buttonPause = canvas1.create_image(30, 30, image=boton_pausaTk, tag=tagname) #coordenadas de boton de pausa 19, 15
    botonCerrarCanvas=canvas1.create_image(300,30,image=BotonCerrarTk,tag=tagname)

    #coordenadas de boton de ampliar(283,15)
    canvas1.tag_bind(tagname,"<Enter>",lambda event: enter())
    canvas1.tag_bind(tagname,"<Leave>",lambda event: leave())
    canvas1.tag_bind(buttonAccion,"<Button-1>",renaudar)
    canvas1.tag_bind(botonCerrarCanvas,"<Button-1>",cerrar)
    
    it.mainloop()

    
if __name__ == '__main__':
    VentanaPrincipal()
