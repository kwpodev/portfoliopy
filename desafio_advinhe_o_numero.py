import tkinter as tk
import random

numero_sorteado = random.randint(1,10)
tentativas = 0

def verificar_palpite():
    global tentativas

    try: 
        palpite = int(entrada.get())
        tentativas += 1

        if palpite < 1 or palpite > 10:
            resultado["text"] = "⚠️ Digite um número entre 1 e 10."
        elif palpite < numero_sorteado:
            resultado["text"] = "🔻 Muito baixo. Tente novamente."
        elif palpite > numero_sorteado:
            resultado["text"] = "🔺 Muito alto. Tente novamente."
        else:
            resultado["text"] = f"✅ Acertou! Tentativas: {tentativas}"
            botao["state"] = "disabled"
    except ValueError:
        resultado["text"] = "⚠️ Digite apenas números."

    # Criar janela
janela = tk.Tk()
janela.title("Jogo: Adivinhe o Número")
janela.geometry("300x200")

# Instruções
instrucoes = tk.Label(janela, text="Adivinhe um número entre 1 e 10")
instrucoes.pack(pady=10)

# Campo de entrada
entrada = tk.Entry(janela)
entrada.pack()

# Botão
botao = tk.Button(janela, text="Verificar", command=verificar_palpite)
botao.pack(pady=5)

# Resultado / Dicas
resultado = tk.Label(janela, text="")
resultado.pack(pady=10)

# Inicia a interface
janela.mainloop()





