import tkinter as tk
from tkinter import messagebox, filedialog
import random
#vlw ryan
LIMITE_TOTAL = 100

PRODUTOS = {
    
    "Temaki": {"preco": 25, "max": 15, "cat": "Sushi & Sashimi"},
    "Sushi Combo": {"preco": 65, "max": 10, "cat": "Sushi & Sashimi"},
    "Sashimi": {"preco": 45, "max": 12, "cat": "Sushi & Sashimi"},
    "Yakissoba": {"preco": 38, "max": 15, "cat": "Sushi & Sashimi"},
    "Gyoza": {"preco": 22, "max": 20, "cat": "Sushi & Sashimi"},
    
    
    "Saquê": {"preco": 18, "max": 30, "cat": "Bebidas"},
    "Chá Verde": {"preco": 8, "max": 40, "cat": "Bebidas"},
    "Refrigerante": {"preco": 6, "max": 50, "cat": "Bebidas"},
    "Suco de Laranja": {"preco": 9, "max": 35, "cat": "Bebidas"},
    "Água Mineral": {"preco": 5, "max": 60, "cat": "Bebidas"},
    
    
    "Mochi": {"preco": 12, "max": 25, "cat": "Sobremesas"},
    "Hot Roll Doce": {"preco": 16, "max": 20, "cat": "Sobremesas"},
    "Sorvete Matcha": {"preco": 14, "max": 20, "cat": "Sobremesas"},
    "Tempurá Sorvete": {"preco": 22, "max": 15, "cat": "Sobremesas"},
    "Salada de Frutas": {"preco": 10, "max": 25, "cat": "Sobremesas"},
}

class Sakura:
    def __init__(self):
        self.qtd = {p: 0 for p in PRODUTOS}
        self.labels_qtd = {}
        self.tela_inicial()

    def tela_inicial(self):
        self.splash = tk.Tk()
        self.splash.title("Restaurante Sakura")
        

        self.splash.attributes('-fullscreen', True)
        self.splash.configure(bg="#8B0000")

        canvas = tk.Canvas(self.splash, bg="#8B0000", highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        self.splash.update()
        largura = self.splash.winfo_width()
        altura = self.splash.winfo_height()

        pétalas_base = [
            (40,40), (90,70), (140,50), (560,50), (610,80), (650,40),
            (250,90), (320,70), (430,80), (50,180), (70,240), (40,320),
            (620,180), (590,260), (630,340), (270,240), (380,250), (470,220),
            (120,370), (220,390), (350,400), (480,390), (580,370)
        ]
        #p
        for px, py in pétalas_base:
            for fator_x in [0.1, 0.5, 0.8]:
                x = int(px + (largura * fator_x) - 300)
                y = int(py * (altura / 450))
                if 0 < x < largura and 0 < y < altura:
                    canvas.create_oval(x, y, x+18, y+12, fill="#FFC0CB", outline="")
                    canvas.create_oval(x+10, y-5, x+28, y+7, fill="#FFD1DC", outline="")

        canvas.create_text(largura // 2, altura // 2 - 50, text="✿ Restaurante SAKURA",
                           fill="white", font=("Georgia", 40, "bold"))

        
        canvas.create_text(largura // 2, altura // 2 + 50, text="A carregar o sistema...",
                           fill="gold", font=("Arial", 14, "italic"))

        self.splash.after(6000, self.abrir)
        self.splash.mainloop()

    def abrir(self):
        self.splash.destroy()

        self.root = tk.Tk()
        self.root.title("Restaurante Sakura")
        
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg="firebrick4")
        
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        self.criar_interface()
        self.root.mainloop()

    def criar_produto(self, pai, nome):
        box = tk.Frame(pai, bg="firebrick4")
        box.pack(fill="x", pady=4, padx=5)
        box.columnconfigure(0, weight=1)

        info = PRODUTOS[nome]

        tk.Label(
            box,
            text=f"{nome}\nR$ {info['preco']} | Max.{info['max']}",
            bg="firebrick4",
            fg="white",
            justify="left",
            font=("Arial", 10, "bold")
        ).grid(row=0, column=0, sticky="w", padx=2)

        btn_container = tk.Frame(box, bg="firebrick4")
        btn_container.grid(row=0, column=1, sticky="e")

        tk.Button(btn_container, text="-", width=3, bg="red", fg="white", font=("Arial", 9, "bold"),
                  command=lambda: self.alterar(nome, -1)).pack(side="left", padx=5)

        lbl = tk.Label(btn_container, text="0", width=4, bg="white", font=("Arial", 10, "bold"))
        lbl.pack(side="left", padx=5)

        tk.Button(btn_container, text="+", width=3, bg="green", fg="white", font=("Arial", 9, "bold"),
                  command=lambda: self.alterar(nome, 1)).pack(side="left", padx=5)

        self.labels_qtd[nome] = lbl

    def alterar(self, nome, valor):
        atual = self.qtd[nome]
        limite = PRODUTOS[nome]["max"]
        novo = atual + valor

        if novo < 0:
            return
        if novo > limite:
            messagebox.showwarning("Limite", f"{nome}: máximo {limite}")
            return

        self.qtd[nome] = novo
        self.labels_qtd[nome].config(text=str(novo))
        self.atualizar_total()

    def criar_interface(self):

        f2 = tk.LabelFrame(self.root, text="Sushi & Sashimi", bg="firebrick4", fg="gold", font=("Arial", 11, "bold"))
        f2.place(relx=0.02, rely=0.12, relwidth=0.23, relheight=0.38)

        f3 = tk.LabelFrame(self.root, text="Bebidas", bg="firebrick4", fg="gold", font=("Arial", 11, "bold"))
        f3.place(relx=0.27, rely=0.12, relwidth=0.23, relheight=0.38)

        f4 = tk.LabelFrame(self.root, text="Sobremesas", bg="firebrick4", fg="gold", font=("Arial", 11, "bold"))
        f4.place(relx=0.52, rely=0.12, relwidth=0.23, relheight=0.38)

        for p in PRODUTOS:
            cat = PRODUTOS[p]["cat"]
            if cat == "Sushi & Sashimi":
                self.criar_produto(f2, p)
            elif cat == "Bebidas":
                self.criar_produto(f3, p)
            else:
                self.criar_produto(f4, p)

        
        f5 = tk.LabelFrame(self.root, text="Ações", bg="firebrick4", fg="gold", font=("Arial", 11, "bold"))
        f5.place(relx=0.02, rely=0.53, relwidth=0.73, relheight=0.13)

        
        tk.Button(f5, text="Gerar Recibo", bg="green", fg="white", font=("Arial", 10, "bold"),
                  command=self.recibo).place(relx=.04, rely=.2, relwidth=.20, relheight=.6)
        tk.Button(f5, text="Salvar Recibo", bg="green", fg="white", font=("Arial", 10, "bold"),
                  command=self.salvar).place(relx=.28, rely=.2, relwidth=.20, relheight=.6)
        tk.Button(f5, text="Limpar Campos", bg="orange", fg="white", font=("Arial", 10, "bold"),
                  command=self.limpar).place(relx=.52, rely=.2, relwidth=.20, relheight=.6)
        tk.Button(f5, text="Sair (ESC)", bg="red", fg="white", font=("Arial", 10, "bold"),
                  command=self.root.destroy).place(relx=.76, rely=.2, relwidth=.20, relheight=.6)

        
        f6 = tk.LabelFrame(self.root, text="🛒 Resumo do Pedido", bg="firebrick4", fg="gold", font=("Arial", 11, "bold"))
        f6.place(relx=0.02, rely=0.68, relwidth=0.73, relheight=0.26)

        self.total_lbl = tk.Label(f6, text="TOTAL: R$ 0,00", bg="firebrick4", fg="gold", font=("Arial", 16, "bold"))
        self.total_lbl.pack(pady=4)

        self.sushi_lbl = tk.Label(f6, text="🍣 Sushi & Sashimi: 0", bg="firebrick4", fg="white", font=("Arial", 10))
        self.sushi_lbl.pack(pady=1)

        self.bebidas_lbl = tk.Label(f6, text="🥤 Bebidas: 0", bg="firebrick4", fg="white", font=("Arial", 10))
        self.bebidas_lbl.pack(pady=1)

        self.doces_lbl = tk.Label(f6, text="🍰 Sobremesas: 0", bg="firebrick4", fg="white", font=("Arial", 10))
        self.doces_lbl.pack(pady=1)

        self.itens_lbl = tk.Label(f6, text="📦 Itens: 0/100", bg="firebrick4", fg="white", font=("Arial", 10, "bold"))
        self.itens_lbl.pack(pady=3)

        
        f7 = tk.Frame(self.root, bd=3, relief="groove")
        f7.place(relx=0.77, rely=0.12, relwidth=0.21, relheight=0.82)

        tk.Label(f7, text="Nota Fiscal", font=("Arial", 12, "bold")).pack(fill="x", pady=5)
        self.txt = tk.Text(f7, font=("Courier New", 11))
        self.txt.pack(fill="both", expand=True, padx=4, pady=4)

    def atualizar_total(self):
        itens = sum(self.qtd.values())
        total = sum(self.qtd[p]*PRODUTOS[p]["preco"] for p in PRODUTOS)
        self.total_lbl.config(text=f"TOTAL: R$ {total:.2f}")
        self.itens_lbl.config(text=f"📦 Itens: {itens}/{LIMITE_TOTAL}")

        sushi = sum(self.qtd[p] for p in PRODUTOS if PRODUTOS[p]["cat"]=="Sushi & Sashimi")
        bebidas = sum(self.qtd[p] for p in PRODUTOS if PRODUTOS[p]["cat"]=="Bebidas")
        doces = sum(self.qtd[p] for p in PRODUTOS if PRODUTOS[p]["cat"]=="Sobremesas")

        self.sushi_lbl.config(text=f"🍣 Sushi & Sashimi: {sushi}")
        self.bebidas_lbl.config(text=f"🥤 Bebidas: {bebidas}")
        self.doces_lbl.config(text=f"🍰 Sobremesas: {doces}")

    def recibo(self):
        total = sum(self.qtd[p]*PRODUTOS[p]["preco"] for p in PRODUTOS)
        if total == 0:
            messagebox.showwarning("Aviso", "Adicione itens ao pedido.")
            return

        self.txt.delete("1.0", "end")
        self.txt.insert("end", "RESTAURANTE SAKURA\n\n")
        self.txt.insert("end", f"Pedido Nº: {random.randint(1000,9999)}\n\n")

        for p in PRODUTOS:
            if self.qtd[p]:
                self.txt.insert("end", f"{p:<18}{self.qtd[p]}\n")

        self.txt.insert("end", f"\nTOTAL: R$ {total:.2f}")

    def salvar(self):
        arq = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")])
        if arq:
            with open(arq, "w", encoding="utf-8") as f:
                f.write(self.txt.get("1.0", "end"))
            messagebox.showinfo("Sucesso", "Recibo salvo com sucesso!")

    def limpar(self):
        for p in self.qtd:
            self.qtd[p] = 0
            self.labels_qtd[p].config(text="0")
        self.txt.delete("1.0", "end")
        self.atualizar_total()

if __name__ == "__main__":
    Sakura()
