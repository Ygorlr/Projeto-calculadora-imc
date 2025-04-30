import customtkinter as ctk

def calculo(num1, num2):
    return num1 / (num2**2)

def status(situacao, resultado):
    if resultado < 18.5:
        situacao = "Abaixo do Normal"
    elif resultado >= 18.6 and resultado <= 24.9:
        situacao = "Normal"
    elif resultado >= 25.0 and resultado <= 29.9:
        situacao = "Sobrepeso"
    elif resultado >= 30.0 and resultado <= 34.9:
        situacao = "Obesidade grau I"
    elif resultado >= 35.0 and resultado <= 39.9:
        situacao = "Obesidade grau II"
    elif resultado >= 40.0:
        situacao = "Obesidade grau III"

    return situacao

def botao_pronto():

    try:
        num1 = float(en_peso.get())
        num2 = float(en_altura.get())
        situacao = ''
        resultado = calculo(num1, num2)
        resultado1 = status(situacao, resultado)
        la_resultado.configure(text=f"Resultado: {resultado:.2f}\n Situação: {resultado1}")
    except ValueError:
        la_resultado.configure(text="Entrada inválida.\nDigite números.")

app = ctk.CTk()
app.geometry("300x300")
app.title("Calculadora IMC - Indice de massa corporal")

# Frame geral
root = ctk.CTkFrame(app)
root.pack(pady=10, padx=10, ipady=30, ipadx=30, fill="both")

# Label de peso
la_peso = ctk.CTkLabel(root, text="Seu peso é:", font=("Arial", 18))
la_peso.pack(pady=5, padx=5)

en_peso = ctk.CTkEntry(root, placeholder_text="exemplo: 77.5")
en_peso.pack(pady=5, padx=5)

# Label de altura
la_altura = ctk.CTkLabel(root, text="Sua altura é:", font=("Arial", 18))
la_altura.pack(pady=5, padx=5)

en_altura = ctk.CTkEntry(root, placeholder_text="exemplo: 1.70")
en_altura.pack(pady=5, padx=5)

btn_pronto = ctk.CTkButton(root, text="CALCULAR", font=("Arial", 17, "bold"), 
                           command=lambda:botao_pronto())
btn_pronto.pack(pady=5, padx=5)

# Label resultado
la_resultado = ctk.CTkLabel(root, text="resultado: ", font=("Arial", 22))
la_resultado.pack()

app.mainloop()