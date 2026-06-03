from tkinter import *
from tkinter import filedialog, messagebox
import time

root = Tk()
root.geometry('1400x600')
root.resizable(0, 0)
root.title('Restaurante Sakura')

#oi

vtemaki = IntVar()
vsushicombo = IntVar()
vsashimi = IntVar()
vsake = IntVar()
vcha_verde = IntVar()
vrefri = IntVar()
vmochi = IntVar()
vhot_doce = IntVar()
vsorvete_matcha = IntVar()

custototal = StringVar()
totaldocomida = StringVar()
totaldobebida = StringVar()
totaldoces1 = StringVar()


def quit():
    root.quit()

def limpar():
    vtemaki.set(0)
    vsushicombo.set(0)
    vsashimi.set(0)
    vsake.set(0)
    vcha_verde.set(0)
    vrefri.set(0)
    vmochi.set(0)
    vhot_doce.set(0)
    vsorvete_matcha.set(0)
    custototal.set("")
    totaldocomida.set("")
    totaldobebida.set("")
    totaldoces1.set("")
    txt.delete('1.0', END)

def totalapp():
    item_comida1 = vtemaki.get()
    item_comida2 = vsushicombo.get()
    item_comida3 = vsashimi.get()
    item_bebida1 = vsake.get()
    item_bebida2 = vcha_verde.get()
    item_bebida3 = vrefri.get()
    item_doce1 = vmochi.get()
    item_doce2 = vhot_doce.get()
    item_doce3 = vsorvete_matcha.get()

    precotemaki, precosushicombo, precosashimi = 25.0, 65.0, 45.0
    precosake, precocha_verde, precorefri = 18.0, 8.0, 6.0
    precomochi, precohot_doce, precosorvete = 12.0, 16.0, 14.0

    totalcomida = (precotemaki * item_comida1) + (precosushicombo * item_comida2) + (precosashimi * item_comida3)
    totabebidas = (precocha_verde * item_bebida2) + (precosake * item_bebida1) + (precorefri * item_bebida3)
    totaldoces = (precomochi * item_doce1) + (precohot_doce * item_doce2) + (precosorvete * item_doce3)

    totaldetudo = round(totalcomida + totabebidas + totaldoces, 2)

    custototal.set(f"R$ {totaldetudo:.2f}")
    totaldocomida.set(f"R$ {totalcomida:.2f}")
    totaldobebida.set(f"R$ {totabebidas:.2f}")
    totaldoces1.set(f"R$ {totaldoces:.2f}")

def bill_area():
    txt.delete('1.0', END)
    date = time.strftime('%d/%m/%Y')
    hora = time.strftime('%H:%M:%S')

    txt.insert(END, "        Restaurante Sakura \n") 
    txt.insert(END, "\n====================================")
    txt.insert(END, f"\n Hora: {hora}       Data: {date} ")
    txt.insert(END, "\n====================================")
    txt.insert(END, "\nProduto          Qtd       Preço")
    txt.insert(END, "\n====================================")

    precotemaki, precosushicombo, precosashimi = 25.0, 65.0, 45.0
    precosake, precocha_verde, precorefri = 18.0, 8.0, 6.0
    precomochi, precohot_doce, precosorvete = 12.0, 16.0, 14.0

    if vtemaki.get() != 0: txt.insert(END, f"\nTemaki           {vtemaki.get()}         R$ {vtemaki.get() * precotemaki:.2f}")
    if vsushicombo.get() != 0: txt.insert(END, f"\nSushi Combo      {vsushicombo.get()}         R$ {vsushicombo.get() * precosushicombo:.2f}")
    if vsashimi.get() != 0: txt.insert(END, f"\nSashimi          {vsashimi.get()}         R$ {vsashimi.get() * precosashimi:.2f}")
    if vsake.get() != 0: txt.insert(END, f"\nSake             {vsake.get()}         R$ {vsake.get() * precosake:.2f}")
    if vcha_verde.get() != 0: txt.insert(END, f"\nChá Verde        {vcha_verde.get()}         R$ {vcha_verde.get() * precocha_verde:.2f}")
    if vrefri.get() != 0: txt.insert(END, f"\nRefrigerante     {vrefri.get()}         R$ {vrefri.get() * precorefri:.2f}")
    if vmochi.get() != 0: txt.insert(END, f"\nMochi            {vmochi.get()}         R$ {vmochi.get() * precomochi:.2f}")
    if vhot_doce.get() != 0: txt.insert(END, f"\nHot Roll Doce    {vhot_doce.get()}         R$ {vhot_doce.get() * precohot_doce:.2f}")
    if vsorvete_matcha.get() != 0: txt.insert(END, f"\nSorvete Matcha   {vsorvete_matcha.get()}         R$ {vsorvete_matcha.get() * precosorvete:.2f}")

    total_geral = (vtemaki.get() * precotemaki + vsushicombo.get() * precosushicombo + vsashimi.get() * precosashimi + vsake.get() * precosake + vcha_verde.get() * precocha_verde + vrefri.get() * precorefri + vmochi.get() * precomochi + vhot_doce.get() * precohot_doce + vsorvete_matcha.get() * precosorvete)

    txt.insert(END, "\n====================================")
    txt.insert(END, f"\n Total Geral :                  R$ {total_geral:.2f}")

def save():
    if txt.get(1.0, END).strip() == "": return
    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if url is None: return
    url.write(txt.get(1.0, END))
    url.close()
    messagebox.showinfo('Informação', 'Consulta de Mesa salva com sucesso!')


titulo = Label(root, text="Restaurante Sakura", font=('arial', 22, 'bold'),
              bg='firebrick4', fg="#d4af37", bd=12, relief=GROOVE) 
titulo.place(relx=0.38, rely=0.03)


F2 = LabelFrame(text='Sushi & Sashimi', bd=10, relief=GROOVE, bg="firebrick4", fg="gold", font=("times new roman", 13, "bold"))
F2.place(x=15, y=100, width=325, height=250)

F3 = LabelFrame(text='Bebidas', bd=10, relief=GROOVE, bg="firebrick4", fg="gold", font=("times new roman", 13, "bold"))
F3.place(x=350, y=100, width=325, height=250)

F4 = LabelFrame(text='Sobremesas', bd=10, relief=GROOVE, bg="firebrick4", fg="gold", font=("times new roman", 13, "bold"))
F4.place(x=680, y=100, width=325, height=250)

F5 = LabelFrame(text='Ações', bd=10, relief=GROOVE, bg="firebrick4", fg="gold", font=("times new roman", 13, "bold"))
F5.place(x=15, y=350, width=990, height=90)

F6 = LabelFrame(text='Resumo Financeiro', bd=10, relief=GROOVE, bg="firebrick4", fg="gold", font=("times new roman", 13, "bold"))
F6.place(x=15, y=435, width=990, height=160)

F7 = Label(root, bd=10, relief=GROOVE)
F7.place(x=1050, y=100, width=325, height=480)

bill_title = Label(F7, text="Nota Fiscal", font=("Lucida", 13, "bold"), bd=7, relief=GROOVE)
bill_title.pack(fill=X)

scroll_y = Scrollbar(F7, orient=VERTICAL)
txt = Text(F7, yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=txt.yview)
txt.pack(fill=BOTH, expand=1)


Label(F2, text='Temaki', font=('arial', 14, 'bold'), bg='firebrick4', fg='white').place(relx=0.05, rely=0.2)
Entry(F2, font=('arial', 12, 'bold'), bd=5, width=6, textvariable=vtemaki, justify='center').place(relx=0.6, rely=0.2)
Label(F2, text='Sushi Combo', font=('arial', 14, 'bold'), bg='firebrick4', fg='white').place(relx=0.05, rely=0.45)
Entry(F2, font=('arial', 12, 'bold'), bd=5, width=6, textvariable=vsushicombo, justify='center').place(relx=0.6, rely=0.45)
Label(F2, text='Sashimi', font=('arial', 14, 'bold'), bg='firebrick4', fg='white').place(relx=0.05, rely=0.7)
Entry(F2, font=('arial', 12, 'bold'), bd=5, width=6, textvariable=vsashimi, justify='center').place(relx=0.6, rely=0.7)

Label(F3, text='Sake Dose', font=('arial', 14, 'bold'), bg='firebrick4', fg='white').place(relx=0.05, rely=0.2)
Entry(F3, font=('arial', 12, 'bold'), bd=5, width=6, textvariable=vsake, justify='center').place(relx=0.6, rely=0.2)
Label(F3, text='Chá Verde', font=('arial', 14, 'bold'), bg='firebrick4', fg='white').place(relx=0.05, rely=0.45)
Entry(F3, font=('arial', 12, 'bold'), bd=5, width=6, textvariable=vcha_verde, justify='center').place(relx=0.6, rely=0.45)
Label(F3, text='Refrigerante', font=('arial', 14, 'bold'), bg='firebrick4', fg='white').place(relx=0.05, rely=0.7)
Entry(F3, font=('arial', 12, 'bold'), bd=5, width=6, textvariable=vrefri, justify='center').place(relx=0.6, rely=0.7)

Label(F4, text='Mochi (Unid)', font=('arial', 14, 'bold'), bg='firebrick4', fg='white').place(relx=0.05, rely=0.2)
Entry(F4, font=('arial', 12, 'bold'), bd=5, width=6, textvariable=vmochi, justify='center').place(relx=0.6, rely=0.2)
Label(F4, text='Hot Roll Doce', font=('arial', 14, 'bold'), bg='firebrick4', fg='white').place(relx=0.05, rely=0.45)
Entry(F4, font=('arial', 12, 'bold'), bd=5, width=6, textvariable=vhot_doce, justify='center').place(relx=0.6, rely=0.45)
Label(F4, text='Sorvete Matcha', font=('arial', 14, 'bold'), bg='firebrick4', fg='white').place(relx=0.05, rely=0.7)
Entry(F4, font=('arial', 12, 'bold'), bd=5, width=6, textvariable=vsorvete_matcha, justify='center').place(relx=0.6, rely=0.7)

Button(F5, text='Calcular Total', font=('arial', 12, 'bold'), fg='white', bg='green', bd=3, command=totalapp).place(relx=0.03, rely=0.15, relwidth=0.16)
Button(F5, text='Gerar Recibo', font=('arial', 12, 'bold'), fg='white', bg='green', bd=3, command=bill_area).place(relx=0.23, rely=0.15, relwidth=0.16)
Button(F5, text='Salvar Recibo', font=('arial', 12, 'bold'), fg='white', bg='green', bd=3, command=save).place(relx=0.43, rely=0.15, relwidth=0.16)
Button(F5, text='Limpar Campos', font=('arial', 12, 'bold'), fg='white', bg='orange', bd=3, command=limpar).place(relx=0.63, rely=0.15, relwidth=0.16)
Button(F5, text='Sair', font=('arial', 12, 'bold'), fg='white', bg='red', bd=3, command=quit).place(relx=0.83, rely=0.15, relwidth=0.15)


Label(F6, text="TOTAL DA CONTA:", font=("Arial", 12, "bold"), bg='firebrick4', fg='gold').place(relx=0.05, rely=0.4)
Label(F6, textvariable=custototal, font=("Arial", 14, "bold"), fg="green").place(relx=0.3, rely=0.38, relwidth=0.15)
Label(F6, text="Sushi:", bg='firebrick4', fg='white').place(relx=0.55, rely=0.15)
Label(F6, textvariable=totaldocomida).place(relx=0.7, rely=0.15, relwidth=0.12)
Label(F6, text="Bebidas:", bg='firebrick4', fg='white').place(relx=0.55, rely=0.45)
Label(F6, textvariable=totaldobebida).place(relx=0.7, rely=0.45, relwidth=0.12)
Label(F6, text="Doces:", bg='firebrick4', fg='white').place(relx=0.55, rely=0.75)
Label(F6, textvariable=totaldoces1).place(relx=0.7, rely=0.75, relwidth=0.12)

root.config(bg='firebrick4')
root.mainloop()