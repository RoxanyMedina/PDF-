import tkinter as tk
from tkinter import ttk, messagebox, mainloop
from fpdf import FPDF

def gerar_pdf():
    cliente = entrada_cliente.get()
    servico = combo_servico.get()
    valor = float(entrada_valor.get())

    if not cliente or not servico or not valor:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return

    try:
        pdf = FPDF()
        pdf.add_page() # Criando a página PDF é nesta linha
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt= "ORDEM DE SERVIÇO", ln=1, align="C")
        pdf.ln(10)

        pdf.cell(200, 10, txt=f"Cliente: {cliente}", ln=1)
        pdf.cell(200, 10, txt=f"Servoço: {servico}", ln=1)
        pdf.cell(200, 10, txt=f"Valor: R$ {valor}", ln=1)

        pdf.output("ordem_de_servico.pdf")
        messagebox.showinfo("Sucesso", "PDF gerado com sucesso!")

    except Exception as e:
        # Se ocorrer qualquer erro, ele exibe a mensagem de erro
        messagebox.showerror("Erro", f"Erro ao gerar PDF: {e}")

janela = tk.Tk()
janela.title("Gerador de Ordem de Serviço")
janela.geometry("350x220")

# Cliente Label e campo de entrada Entry
tk.Label(janela, text="Cliente: ").grid(row=0, column=0, padx=10, pady=10)
entrada_cliente = tk.Entry(janela, width=30)
entrada_cliente.grid(row=0, column=1, padx=10, pady=10)


# Serviço

tk.Label(janela, text="Serviço: ").grid(row=1, column=0, padx=10, pady=10)

#Criando uma lista para o Combobox que são os serviços
servicos = [
    "Formatação de Computador",
    "Instalação do Rwindows",
    "Manutenção de Rede",
    "Criação de site",
    "Suporte Técnico"
]
combo_servico = ttk.Combobox(janela, width=26, values=servicos, state="readonly")
combo_servico.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

# Criação do Label e campo Valor

tk.Label(janela, text="Valores: ").grid(row=2, column=0, padx=10, pady=10)
entrada_valor = tk.Entry(janela, width=30)
entrada_valor.grid(row=2, column=1, padx=10, pady=10)


#===== BOTÃO: GERAR PDF =====

botao_pdf = tk.Button(janela, text="Gerar PDF", command=gerar_pdf, bg="green", fg="white")
botao_pdf.grid(row=3, column=1, columnspan=2, padx=10, pady=10)



janela.mainloop()