import tkinter
import parser

ventana = tkinter.Tk()
ventana.title("Calculadora")
ventana.geometry("300x180")

cajaTexto = tkinter.Entry(ventana, font ="Helvetica 18", width = 22)
cajaTexto.place(x = 10,y = 10)

i = 0

def get_number(n):
    global i
    cajaTexto.insert(i, n)
    i += 1

def get_operation(operator):
    global i
    cajaTexto.insert(i, operator)
    i += 1
    
def clear():
    cajaTexto.delete(0, "end")
    
def calcular():
    estado_actual = cajaTexto.get()
    try:
        exp_matematica = parser.expr(estado_actual).compile()
        resultado = eval(exp_matematica)
        clear()
        cajaTexto.insert(0, resultado)
    except Exception:
        clear()
        cajaTexto.insert(0, "Error")


boton1 = tkinter.Button(
    ventana, text = "1", width = 5, command = lambda:  get_number(1))
boton2 = tkinter.Button(
    ventana, text = "2", width = 5, command = lambda:  get_number(2))
boton3 = tkinter.Button(
    ventana, text = "3", width = 5, command = lambda:  get_number(3))
boton4 = tkinter.Button(
    ventana, text = "4", width = 5, command = lambda:  get_number(4))
boton5 = tkinter.Button(
    ventana, text = "5", width = 5, command = lambda:  get_number(5))
boton6 = tkinter.Button(
    ventana, text = "6", width = 5, command = lambda:  get_number(6))
boton7 = tkinter.Button(
    ventana, text = "7", width = 5, command = lambda:  get_number(7))
boton8 = tkinter.Button(
    ventana, text = "8", width = 5, command = lambda:  get_number(8))
boton9 = tkinter.Button(
    ventana, text = "9", width = 5, command = lambda:  get_number(9))
boton0 = tkinter.Button(
    ventana, text = "0", width = 5, command = lambda:  get_number(0))

botonSuma = tkinter.Button(
    ventana, text = "+", width = 5, command = lambda:  get_operation("+"))
botonResta = tkinter.Button(
    ventana, text = "-", width = 5, command = lambda:  get_operation("-"))
botonMultipli = tkinter.Button(
    ventana, text = "x", width = 5, command = lambda:  get_operation("x"))
botonDiv = tkinter.Button(
    ventana, text = "/", width = 5, command = lambda:  get_operation("/"))

botonResult = tkinter.Button(
    ventana, text = "=", width = 5, command = lambda:  calcular())

botonAC = tkinter.Button(
    ventana, text = "AC", width = 5, comman = lambda: clear())

boton1.place(x = 10,y = 50)
boton2.place(x = 80,y = 50)
boton3.place(x = 150,y = 50)
boton4.place(x = 10,y = 80)
boton5.place(x = 80,y = 80)
boton6.place(x = 150,y = 80)
boton7.place(x = 10,y = 110)
boton8.place(x = 80,y = 110)
boton9.place(x = 150,y = 110)
boton0.place(x = 80,y = 140)

botonResta.place(x = 220,y = 50)
botonSuma.place(x = 220,y = 80)
botonResult.place(x = 220,y =110)
botonMultipli.place(x = 10,y = 140)
botonDiv.place(x = 150,y = 140)

botonAC.place(x = 220,y = 140)

ventana.mainloop()


