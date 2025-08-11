from tkinter import *
from tkinter import messagebox
from data import narudzbine, info
from backend import ajmo, close_browser

prozorce = Tk()
prozorce.title("Market Bot")
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

def dodaj_u_korpu():
    proizvod = narudzbina_entry.get().strip()
    kolicina = kolicina_spinbox.get().strip()
    
    if not proizvod:
        messagebox.showwarning("Warning", "Please enter a product name!")
        return
    
    if not kolicina or int(kolicina) < 1:
        messagebox.showwarning("Warning", "Please enter a valid quantity!")
        return
        
    info(narudzbina_entry, kolicina_spinbox)
    narudzbina_entry.delete(0, END)
    kolicina_spinbox.delete(0, END)
    kolicina_spinbox.insert(0, "1")
    messagebox.showinfo("Success", f"Added {proizvod} (quantity: {kolicina}) to cart!")

def poruci_sada():
    if narudzbine:
        try:
            ajmo()
            messagebox.showinfo("Success", "Order placed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to place order: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Cart is empty! Add some items first.")

def ocisti_korpu():
    if narudzbine:
        narudzbine.clear()
        messagebox.showinfo("Info", "Cart cleared!")
    else:
        messagebox.showinfo("Info", "Cart is already empty!")

def prikazi_korpu():
    if narudzbine:
        sadrzaj_korpe = "Current Cart:\n\n"
        for proizvod, kolicina in narudzbine.items():
            sadrzaj_korpe += f"• {proizvod}: {kolicina}\n"
        messagebox.showinfo("Cart Contents", sadrzaj_korpe)
    else:
        messagebox.showinfo("Cart Contents", "Cart is empty!")

def izadji_iz_aplikacije():
    rezultat = messagebox.askyesno("Quit", "Are you sure you want to quit?\nThis will close the browser and exit the application.")
    if rezultat:
        close_browser()
        prozorce.quit()
        prozorce.destroy()

add_btn = Button(prozorce, text="Add to Cart", font=("Arial", 14), command=dodaj_u_korpu, bg="lightgreen")
add_btn.pack(pady=10)

buttons_frame = Frame(prozorce, bg="lightblue")
buttons_frame.pack(pady=20)

show_cart_btn = Button(buttons_frame, text="Show Cart", font=("Arial", 12), command=prikazi_korpu, bg="lightyellow")
show_cart_btn.pack(side=LEFT, padx=5)

clear_cart_btn = Button(buttons_frame, text="Clear Cart", font=("Arial", 12), command=ocisti_korpu, bg="orange")
clear_cart_btn.pack(side=LEFT, padx=5)

order_btn = Button(prozorce, text="Order / Checkout", font=("Arial", 14), command=poruci_sada, bg="lightcoral")
order_btn.pack(pady=20)

quit_btn = Button(prozorce, text="Quit Application", font=("Arial", 12), command=izadji_iz_aplikacije, bg="red", fg="white")
quit_btn.pack(pady=10)

prozorce.protocol("WM_DELETE_WINDOW", izadji_iz_aplikacije)

prozorce.mainloop()
