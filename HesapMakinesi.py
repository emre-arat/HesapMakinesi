import tkinter

window = tkinter.Tk()
window.title("Hesap Makinesi")
kutu = tkinter.Entry()
kutu.place(x=10,y=0)
kutu2 = tkinter.Entry()
kutu2.place(x=10,y=25)

def topla():
    kutu2_value = int(kutu2.get())
    kutu_value = int(kutu.get())
    sonuç = kutu_value + kutu2_value
    sonuç_metin = tkinter.Label(text=sonuç)
    sonuç_metin.place(x=10,y=80)
    print(sonuç)
def çıkar():
    kutu2_value = int(kutu2.get())
    kutu_value = int(kutu.get())
    sonuç = kutu_value - kutu2_value
    sonuç_metin = tkinter.Label(text=sonuç)
    sonuç_metin.place(x=10,y=80)
    print(sonuç)
def çarp():
    kutu2_value = int(kutu2.get())
    kutu_value = int(kutu.get())
    sonuç = kutu_value * kutu2_value
    sonuç_metin = tkinter.Label(text=sonuç)
    sonuç_metin.place(x=10,y=80)
    print(sonuç)
def böl():
    kutu2_value = int(kutu2.get())
    kutu_value = int(kutu.get())
    sonuç = kutu_value / kutu2_value
    sonuç_metin = tkinter.Label(text=sonuç)
    sonuç_metin.place(x=10,y=80)
    print(sonuç)

def işlem():
    button = tkinter.Button(text="topla",command=topla)
    button.place(x=0,y=50)
    button = tkinter.Button(text="çıkar",command=çıkar)
    button.place(x=50,y=50)
    button = tkinter.Button(text="çarp",command=çarp)
    button.place(x=100,y=50)
    button = tkinter.Button(text="böl",command=böl)
    button.place(x=150,y=50)
işlem()
window.mainloop()