from tkinter import *
from data import narudzbine, info
from backend import ajmo

prozorce = Tk()
prozorce.title("Market bot")
prozorce.config(bg="lightblue")
prozorce.geometry("600x600")

naslov = Label(prozorce, text="Market Bot - Place Your Order", font=("Arial", 20, "bold"), bg="lightblue")
naslov.pack(pady=20)

narudzbina_label = Label(prozorce, text="What you want to order:", font=("Arial", 14), bg="lightblue")
narudzbina_label.pack(pady=10)

narudzbina_entry = Entry(prozorce, font=("Arial", 14))
narudzbina_entry.pack(pady=5)

kolicina_label = Label(prozorce, text="Quantity:", font=("Arial", 14), bg="lightblue")
kolicina_label.pack(pady=10)

kolicina_spinbox = Spinbox(prozorce, from_=1, to=100, font=("Arial", 14), width=5)
kolicina_spinbox.pack(pady=5)

def add_to_cart():
    info(narudzbina_entry, kolicina_spinbox)
    narudzbina_entry.delete(0, END)
    kolicina_spinbox.delete(0, END)
    kolicina_spinbox.insert(0, "1")
    print("Added to cart!")

def order_now():
    if narudzbine:
        ajmo()
    else:
        print("Cart is empty!")

add_btn = Button(prozorce, text="Add to Cart", font=("Arial", 14), command=add_to_cart)
add_btn.pack(pady=10)

order_btn = Button(prozorce, text="Order / Checkout", font=("Arial", 14), command=order_now)
order_btn.pack(pady=20)

prozorce.mainloop()
