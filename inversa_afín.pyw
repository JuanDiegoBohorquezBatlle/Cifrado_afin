from tkinter import *

ABC=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
val_num = {ABC: i for i, ABC in enumerate(ABC)}


#---------------------------Cuerpo-------------------------------#

root=Tk()
root.title("Cifrado Afín")
root.resizable(0,0)

value_b = IntVar()
value_var = IntVar()
text_var = StringVar()
 	
frm=Frame(root, width=500, height=400)
frm.pack(fill="both", expand=1)

#---------------------------Lógica-------------------------------#

def factorizar(n):
    numeros_primos = iter((2, 3, 5, 7, 11, 13, 17, 19, 23, 29))
    numero_primo_actual = next(numeros_primos)
    resultado = []
    cociente = None
    while cociente != 1:
        if n % numero_primo_actual != 0:
            numero_primo_actual = next(numeros_primos)
            continue
        resultado.append(numero_primo_actual)
        n = cociente = n / numero_primo_actual
    return resultado

def cif():
	global value_var, result_a, text_var, val_num, ABC, result_C, value_b
	i = 0
	b = 0
	a = 0
	w = len(ABC)	#Numero de letras en este ABC.
	f = factorizar(value_var.get())
	resultado_C = ''

	if len(f) >= 1:
		a = w % f[0]

		if len(f) >= 2:
			a = w % f[1]

			if len(f) >= 3:
				a = w % f[2]
					
				if len(f) >= 4:
					a = w % f[3]

	if a == 0:
		b = 1
		result_a.config(text="Debe no ser divisible por " + str(w))

	
	if value_var.get() == 0:
		value_var.set(1)

	while b != 1:
		i += 1
		b = value_var.get()*i % w

	if a != 0:
		result_a.config(text=i)
	
		for k in range(len(text_var.get())):
			leter_search = text_var.get()[k]
			valor_asociado = val_num.get(leter_search)
			crypt = valor_asociado*value_var.get()+value_b.get()
			crypt %= w
			element_search = next((ABC for ABC, valor in val_num.items() if valor == crypt), None)
			
			if element_search is not None:
				resultado_C += element_search

		result_C.config(text=resultado_C)

def dcif():
	global value_var, result_a, text_var, val_num, ABC, result_C, value_b
	i = 0
	b = 0
	w = len(ABC)	#Numero de letras en este ABC.
	a = w % value_var.get()
	resultado_C = ''
	
	if a == 0:
		b=1
		result_a.config(text="Debe no ser divisible por " + str(w))
	
	if value_var.get() == 0:
		value_var.set(1)

	while not b==1:
		i += 1
		b = value_var.get()*i % w

	if a != 0:
		result_a.config(text=i)
	
		for k in range(len(text_var.get())):
			leter_search = text_var.get()[k]
			valor_asociado = val_num.get(leter_search)
			crypt = (valor_asociado-value_b.get())*value_var.get()
			crypt %= w
			element_search = next((ABC for ABC, valor in val_num.items() if valor == crypt), None)
			
			if element_search is not None:
				resultado_C += element_search

		result_C.config(text=resultado_C)


#-------------------------Widgets--------------------------------#

bug_solv=Label(frm, 
				text="",
				pady=30).grid(row=0,column=0)	#Soluciona la incompatibilidad del grid y place en "intro".

lbl=Label(frm, 
	text="Escribe la clave de cifrado/descifrado a:").grid(row=1, column=0, 
												sticky="e", 
												padx=15, pady=15)

variable_a=Entry(frm, textvariable=value_var).grid(row=1, column=1, sticky="e", padx=15, pady=15)

variable_b=Entry(frm, textvariable=value_b).grid(row=2, column=1, sticky="e", padx=15, pady=15)

lbl=Label(frm, 
	text="Escribe la clave de cifrado b:").grid(row=2, column=0, 
												sticky="e", 
												padx=15, pady=15)

lbl=Label(frm, 
	text="Escribe la palabra a cifrar/descifrar M/C en minusculas:").grid(row=3, column=0, 
												sticky="e", 
												padx=15, pady=15)

variable_m=Entry(frm, textvariable=text_var).grid(row=3, column=1, sticky="e", padx=15, pady=15)


boton1 = Button(frm, 
					text="Cifrar", 
					padx=15, 
					pady=15, command=cif).grid(row=1, column=2)

boton2 = Button(frm, 
					text="Descifrar", 
					padx=15, 
					pady=15, command=dcif).grid(row=3, column=2)

intro=Label(frm, 
			relief="raised",
			text="""La fórmula debe ser de la forma,\nC=M*a+b, Donde M sera la clave a cifrar""",
			width=35, height=4).place(x=80,y=5)

#---------------------Etiqueta de Resultado----------------------#

rsa=Label(frm, text="inversa de a:").grid(row=4, column=0, sticky="e", padx=15, pady=15)
result_a=Label(frm, text="Esperando...")
result_a.grid(row=4, column=1, padx=15, pady=15)



rsc=Label(frm, text="Mensaje cifrado/descifrado:").grid(row=5, column=0, sticky="e", padx=15, pady=15)
result_C=Label(frm, text="Esperando...")
result_C.grid(row=5, column=1)


root.mainloop()
