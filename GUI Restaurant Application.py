import tkinter
from tkinter import *

window = tkinter.Tk()

window.title("Restaurant Application")
window.geometry("1400x730")
window.config(bg="#181444")
# Variables
food_quantities = []
drink_quantities = []
selected_foods = []
selected_drinks = []
food_prices = []
drink_price = []

# Restaurant Label
restaurant_label = Label(window, text="Restaurant", fg="white", bg="#181444", font=("Arial", 50, "bold")).place(x=550, y=10)

# Food and Drinks Labels
white_food_label = Label(window, bg="white", width=90, height=36).place(x=50, y=110)
white_drink_label = Label(window, bg="white", width=90, height=36).place(x=720, y=110)

# Food and Drink Menu Text
food_menu_label = Label(window, text="Food Menu", bg="white", fg="#181444", font=("Arial", 30, "bold")).place(x=265, y=125)
drink_menu_label = Label(window, text="Drinks Menu", bg="white", fg="#181444", font=("Arial", 30, "bold")).place(x=930, y=125)

# Food Menu Labels
list_of_foods_with_prices = ["Zinger Burger - Rs. 150 Each", "Chicken Shawarma - Rs. 60 Each", "Fajita - Rs. 200 Each", "Pizza - Rs. 1200", "Chicken Nuggets - Rs. 20 Each", "Dehi Bullay - Rs. 50 Each Plate", "Goll Guppay - Rs. 150 Each Plate", "French Fries - Rs. 80 Each Packet", "Pasta - Rs. 150 Each Plate", "Rice - Rs. 170 Each Plate"]
value_of_y = 180
food_number = 1
for items in list_of_foods_with_prices:
    food_label = Label(window, text=f"{food_number}. {items}", bg="white", fg="#181444", borderwidth=15, font=("Arial", 14, "italic")).place(x=50, y=value_of_y)
    value_of_y += 40
    food_number += 1
# Drink Menu Labels
list_of_drinks_with_prices = ["Coca-Cola/Pepsi - Rs.150", "Marinda - Rs.120", "Seven-Up/Sprite - Rs.100", "Mango Milkshake - Rs.250", "Chocolate Milkshake - Rs.300", "Pomegrenate Juice - Rs.550", "Banana Milkshake - Rs.250", "Apple Milkshake - Rs.150", "Orange Juice - Rs.170", "Carrot Juice - Rs.90"]
value_of_y = 180
drink_number = 1
for items in list_of_drinks_with_prices:
    food_label = Label(window, text=f"{drink_number}. {items}", bg="white", fg="#181444", borderwidth=15, font=("Arial", 14, "italic")).place(x=725, y=value_of_y)
    value_of_y += 40
    drink_number+= 1

# Foods Text Boxes and Quantity Labels
y_value2 = 185
for foods in range(len(list_of_foods_with_prices)):
    quantity_labels = Label(window, text="Quantity: ", bg="white", fg="#181444", font=("Arial", 14, "bold")).place(x=430, y=y_value2)
    y_value2 += 40
food_var1 = StringVar()
food_var2 = StringVar()
food_var3 = StringVar()
food_var4 = StringVar()
food_var5 = StringVar()
food_var6 = StringVar()
food_var7 = StringVar()
food_var8 = StringVar()
food_var9 = StringVar()
food_var10 = StringVar()
y_value3 = 192
for x in range(1):
    zinger_textbox = Entry(window, fg="#181444", font=("Arial", 12, "bold"), width=7, textvariable=food_var1).place(x=520, y=y_value3)
    y_value3 += 40
    shawarma_textbox = Entry(window, fg="#181444", font=("Arial", 12, "bold"), width=7, textvariable=food_var2).place(x=520, y=y_value3)
    y_value3 += 40
    fajita_textbox = Entry(window, fg="#181444", font=("Arial", 12, "bold"), width=7, textvariable=food_var3).place(x=520, y=y_value3)
    y_value3 += 40
    pizza_textbox = Entry(window, fg="#181444", font=("Arial", 12, "bold"), width=7, textvariable=food_var4).place(x=520, y=y_value3)
    y_value3 += 40
    chicken_nuggets_textbox = Entry(window, fg="#181444", font=("Arial", 12, "bold"), width=7, textvariable=food_var5).place(x=520, y=y_value3)
    y_value3 += 40
    zdehi_bullay_textbox = Entry(window, fg="#181444", font=("Arial", 12, "bold"), width=7, textvariable=food_var6).place(x=520, y=y_value3)
    y_value3 += 40
    goll_guppay_textbox = Entry(window, fg="#181444", font=("Arial", 12, "bold"), width=7, textvariable=food_var7).place(x=520, y=y_value3)
    y_value3 += 40
    frech_fries_textbox = Entry(window, fg="#181444", font=("Arial", 12, "bold"), width=7, textvariable=food_var8).place(x=520, y=y_value3)
    y_value3 += 40
    pasta_textbox = Entry(window, fg="#181444", font=("Arial", 12, "bold"), width=7, textvariable=food_var9).place(x=520, y=y_value3)
    y_value3 += 40
    rice_textbox = Entry(window, fg="#181444", font=("Arial", 12, "bold"), width=7, textvariable=food_var10).place(x=520, y=y_value3)

# Drinks Text Boxes and Quantity Labels
y_value4 = 185
for drinks in range(len(list_of_drinks_with_prices)):
    quantity_labels = Label(window, text="Quantity: ", bg="white", fg="#181444", font=("Arial", 14, "bold")).place(x=1080, y=y_value4)
    y_value4 += 40
y_value5 = 192
drink_var1 = StringVar()
drink_var2 = StringVar()
drink_var3 = StringVar()
drink_var4 = StringVar()
drink_var5 = StringVar()
drink_var6 = StringVar()
drink_var7 = StringVar()
drink_var8 = StringVar()
drink_var9 = StringVar()
drink_var10 = StringVar()
y_value3 = 192
for x in range(1):
    coke_textbox = Entry(window, fg="#181444", font=("Arial", 12, "bold"), width=7, textvariable=drink_var1).place(x=1170, y=y_value3)
    y_value3 += 40
    marinda_textbox = Entry(window, fg="#181444", font=("Arial", 12, "bold"), width=7, textvariable=drink_var2).place(x=1170, y=y_value3)
    y_value3 += 40
    sprite_textbox = Entry(window, fg="#181444", font=("Arial", 12, "bold"), width=7, textvariable=drink_var3).place(x=1170, y=y_value3)
    y_value3 += 40
    mango_milkshake_textbox = Entry(window, fg="#181444", font=("Arial", 12, "bold"), width=7, textvariable=drink_var4).place(x=1170, y=y_value3)
    y_value3 += 40
    chocolate_milkshake_textbox = Entry(window, fg="#181444", font=("Arial", 12, "bold"), width=7, textvariable=drink_var5).place(x=1170, y=y_value3)
    y_value3 += 40
    pomegrenate_juice_textbox = Entry(window, fg="#181444", font=("Arial", 12, "bold"), width=7, textvariable=drink_var6).place(x=1170, y=y_value3)
    y_value3 += 40
    banana_milkshake_textbox = Entry(window, fg="#181444", font=("Arial", 12, "bold"), width=7, textvariable=drink_var7).place(x=1170, y=y_value3)
    y_value3 += 40
    apple_milkshake_textbox = Entry(window, fg="#181444", font=("Arial", 12, "bold"), width=7, textvariable=drink_var8).place(x=1170, y=y_value3)
    y_value3 += 40
    orange_juice_textbox = Entry(window, fg="#181444", font=("Arial", 12, "bold"), width=7, textvariable=drink_var9).place(x=1170, y=y_value3)
    y_value3 += 40
    carrot_juice_textbox = Entry(window, fg="#181444", font=("Arial", 12, "bold"), width=7, textvariable=drink_var10).place(x=1170, y=y_value3)
# VarChars
check_var1 = IntVar()
check_var2 = IntVar()
check_var3 = IntVar()
check_var4 = IntVar()
check_var5 = IntVar()
check_var6 = IntVar()
check_var7 = IntVar()
check_var8 = IntVar()
check_var9 = IntVar()
check_var10 = IntVar()
foods_to_append = ["Zinger", "Shawarma", "Fajita", "Pizza", "Chicken Nuggets", "Dehi Bullay", "Goll Guppay", "French Fries", "Pasta", "Rice"]
var_char_list = [check_var1, check_var2, check_var3, check_var4, check_var5, check_var6, check_var7, check_var8, check_var9, check_var10]
# Functions
def food1():
        if check_var1.get()==1: 
            selected_foods.append("Zinger")
        else:
            print("  ")
def food2():
        if check_var2.get()==1: 
            selected_foods.append("Chicken Shawarma")
        else:
            print("  ")
def food3():
        if check_var3.get()==1: 
            selected_foods.append("Fajita")
        else:
            print("  ")
def food4():
        if check_var4.get()==1: 
            selected_foods.append("Pizza")
        else:
            print("  ")
def food5():
        if check_var5.get()==1: 
            selected_foods.append("Chicken Nuggets")
        else:
            print("  ")
def food6():
        if check_var6.get()==1: 
            selected_foods.append("Dehi Bullay")
        else:
            print("  ")
def food7():
        if check_var7.get()==1: 
            selected_foods.append("Goll Guppay")
        else:
            print("  ")
def food8():
        if check_var8.get()==1: 
            selected_foods.append("French Fries")
        else:
            print("  ")
def food9():
        if check_var9.get()==1: 
            selected_foods.append("Pasta")
        else:
            print("  ")
def food10():
        if check_var10.get()==1: 
            selected_foods.append("Rice")
        else:
            print("  ")
# Food Variables
zinger_checkbox = Checkbutton(window, bg="white", variable=check_var1,font=(15), onvalue=1, offvalue=0, command=food1).place(x=400, y=185)
chicken_shawarma_checkbox = Checkbutton(window, bg="white", variable=check_var2,font=(15), onvalue=1, offvalue=0, command=food2).place(x=400, y=225)
fajita_checkbox = Checkbutton(window, bg="white", variable=check_var3,font=(15), onvalue=1, offvalue=0, command=food3).place(x=400, y=265)
pizza_checkbox = Checkbutton(window, bg="white", variable=check_var4,font=(15), onvalue=1, offvalue=0, command=food4).place(x=400, y=305)
chicken_nuggets_checkbox = Checkbutton(window, bg="white", variable=check_var5,font=(15), onvalue=1, offvalue=0, command=food5).place(x=400, y=345)
dehi_bullay_checkbox = Checkbutton(window, bg="white", variable=check_var6,font=(15), onvalue=1, offvalue=0, command=food6).place(x=400, y=390)
goll_guppay_checkbox = Checkbutton(window, bg="white", variable=check_var7,font=(15), onvalue=1, offvalue=0, command=food7).place(x=400, y=430)
french_fries_checkbox = Checkbutton(window, bg="white", variable=check_var8,font=(15), onvalue=1, offvalue=0, command=food8).place(x=400, y=470)
pasta_checkbox = Checkbutton(window, bg="white", variable=check_var9,font=(15), onvalue=1, offvalue=0, command=food9).place(x=400, y=510)
rice_checkbox = Checkbutton(window, bg="white", variable=check_var10,font=(15), onvalue=1, offvalue=0, command=food10).place(x=400, y=550)
# VarChars
check_var11 = IntVar()
check_var12 = IntVar()
check_var13 = IntVar()
check_var14 = IntVar()
check_var15 = IntVar()
check_var16 = IntVar()
check_var17 = IntVar()
check_var18 = IntVar()
check_var19 = IntVar()
check_var20 = IntVar()
# Functions
def drink11():
        if check_var11.get()==1: 
            selected_drinks.append("Pepsi/Coke")
        else:
            print("  ")
def drink12():
        if check_var12.get()==1: 
            selected_drinks.append("Marinda")
        else:
            print("  ")
def drink13():
        if check_var13.get()==1: 
            selected_drinks.append("Sprite/7-Up")
        else:
            print("  ")
def drink14():
        if check_var14.get()==1: 
            selected_drinks.append("Mango Milkshake")
        else:
            print("  ")
def drink15():
        if check_var15.get()==1: 
            selected_drinks.append("Chocolate Milkshake")
        else:
            print("  ")
def drink16():
        if check_var16.get()==1: 
            selected_drinks.append("Pomegrenate Juice")
        else:
            print("  ")
def drink17():
        if check_var17.get()==1: 
            selected_drinks.append("Banana Milkshake")
        else:
            print("  ")
def drink18():
        if check_var18.get()==1: 
            selected_drinks.append("Apple Milkshake")
        else:
            print("  ")
def drink19():
        if check_var19.get()==1: 
            selected_drinks.append("Orange Juice")
        else:
            print("  ")
def drink20():
        if check_var20.get()==1: 
            selected_drinks.append("Carrot Juice")
        else:
            print("  ")
# Drink CheckBoxes
coke_checkbox = Checkbutton(window, bg="white", variable=check_var11,font=(15), onvalue=1, offvalue=0, command=drink11).place(x=1050, y=185)
marinda_shawarma_checkbox = Checkbutton(window, bg="white", variable=check_var12,font=(15), onvalue=1, offvalue=0, command=drink12).place(x=1050, y=225)
sprite_checkbox = Checkbutton(window, bg="white", variable=check_var13,font=(15), onvalue=1, offvalue=0, command=drink13).place(x=1050, y=265)
mango_milkshake_checkbox = Checkbutton(window, bg="white", variable=check_var14,font=(15), onvalue=1, offvalue=0, command=drink14).place(x=1050, y=305)
chocolate_milkshake_checkbox = Checkbutton(window, bg="white", variable=check_var15,font=(15), onvalue=1, offvalue=0, command=drink15).place(x=1050, y=345)
pomegrenate_juice_checkbox = Checkbutton(window, bg="white", variable=check_var16,font=(15), onvalue=1, offvalue=0, command=drink16).place(x=1050, y=390)
banana_milkshake_checkbox = Checkbutton(window, bg="white", variable=check_var17,font=(15), onvalue=1, offvalue=0, command=drink17).place(x=1050, y=430)
apple_milkshake_checkbox = Checkbutton(window, bg="white", variable=check_var18,font=(15), onvalue=1, offvalue=0, command=drink18).place(x=1050, y=470)
orange_juice_checkbox = Checkbutton(window, bg="white", variable=check_var19,font=(15), onvalue=1, offvalue=0, command=drink19).place(x=1050, y=510)
carrot_juice_checkbox = Checkbutton(window, bg="white", variable=check_var20,font=(15), onvalue=1, offvalue=0, command=drink20).place(x=1050, y=550)
    # Retriving Quantities for Foods
def food_quatity1():
     zinger_quantity = food_var1.get()
     food_quantities.append(zinger_quantity)
     if zinger_quantity == "":
        food_quantities.remove(zinger_quantity)
        set(food_quantities)
     else:
        pass
food_quatity1()
def food_quatity2():
     shawrama_quantity = food_var2.get()
     food_quantities.append(shawrama_quantity)
     if shawrama_quantity == "":
        food_quantities.remove(shawrama_quantity)
        set(food_quantities)
     else:
        pass
food_quatity2()
def food_quatity3():
     fajita_quantity = food_var3.get()
     food_quantities.append(fajita_quantity)
     if fajita_quantity == "":
        food_quantities.remove(fajita_quantity)
        set(food_quantities)
     else:
        pass
food_quatity3()
def food_quatity4():
     pizza_quantity = food_var4.get()
     food_quantities.append(pizza_quantity)
     if pizza_quantity == "":
        food_quantities.remove(pizza_quantity)
        set(food_quantities)
     else:
        pass
food_quatity4()
def food_quatity5():
     chicken_nuggets_quantity = food_var5.get()
     food_quantities.append(chicken_nuggets_quantity)
     if chicken_nuggets_quantity == "":
        food_quantities.remove(chicken_nuggets_quantity)
        set(food_quantities)
     else:
        pass
food_quatity5()
def food_quatity6():
     dehi_bullay_quantity = food_var6.get()
     food_quantities.append(dehi_bullay_quantity)
     if dehi_bullay_quantity == "":
        food_quantities.remove(dehi_bullay_quantity)
        set(food_quantities)
     else:
        pass
food_quatity6()
def food_quatity7():
     goll_guppay_quantity = food_var7.get()
     food_quantities.append(goll_guppay_quantity)
     if goll_guppay_quantity == "":
        food_quantities.remove(goll_guppay_quantity)
        set(food_quantities)
     else:
        pass
food_quatity7()
def food_quatity8():
     french_fries_quantity = food_var8.get()
     food_quantities.append(french_fries_quantity)
     if french_fries_quantity == "":
        food_quantities.remove(french_fries_quantity)
        set(food_quantities)
     else:
        pass
food_quatity8()
def food_quatity9():
     pasta_quantity = food_var9.get()
     food_quantities.append(pasta_quantity)
     if pasta_quantity == "":
        food_quantities.remove(pasta_quantity)
        set(food_quantities)
     else:
        pass
food_quatity9()
def food_quatity10():
     rice_quantity = food_var10.get()
     food_quantities.append(rice_quantity)
     if rice_quantity == "":
        food_quantities.remove(rice_quantity)
        set(food_quantities)
     else:
        pass
food_quatity10()
# Retriving Quantities for Drinks
def drink_quantity1():
     coke_quantity = drink_var1.get()
     drink_quantities.append(coke_quantity)
     if coke_quantity == "":
         drink_quantities.remove(coke_quantity)
         set(drink_quantities)             
     else:
         pass
drink_quantity1()
def drink_quantity2():
     marinda_quantity = drink_var2.get()
     drink_quantities.append(marinda_quantity)
     if marinda_quantity == "":
         drink_quantities.remove(marinda_quantity)
         set(drink_quantities)
     else:
         pass
drink_quantity2()
def drink_quantity3():
     sprite_quantity = drink_var3.get()
     drink_quantities.append(sprite_quantity)
     if sprite_quantity == "":
         drink_quantities.remove(sprite_quantity)
         set(drink_quantities)
     else:
         pass
drink_quantity3()
def drink_quantity4():
     mango_milkshake_quantity = drink_var4.get()
     drink_quantities.append(mango_milkshake_quantity)
     if mango_milkshake_quantity == "":
         drink_quantities.remove(mango_milkshake_quantity)
         set(drink_quantities)
     else:
         pass
drink_quantity4()
def drink_quantity5():
     chocolate_milkshake_quantity = drink_var5.get()
     drink_quantities.append(chocolate_milkshake_quantity)
     if chocolate_milkshake_quantity == "":
         drink_quantities.remove(chocolate_milkshake_quantity)
         set(drink_quantities)
     else:
         pass
drink_quantity5()
def drink_quantity6():
     pomegrenate_juice_quantity = drink_var6.get()
     drink_quantities.append(pomegrenate_juice_quantity)
     if pomegrenate_juice_quantity == "":
         drink_quantities.remove(pomegrenate_juice_quantity)
         set(drink_quantities)
     else:
         pass
drink_quantity6()
def drink_quantity7():
     banana_milkshake_quantity = drink_var7.get()
     drink_quantities.append(banana_milkshake_quantity)
     if banana_milkshake_quantity == "":
         drink_quantities.remove(banana_milkshake_quantity)
         set(drink_quantities)
     else:
         pass
drink_quantity7()
def drink_quantity8():
     apple_milkshake_quantity = drink_var8.get()
     drink_quantities.append(apple_milkshake_quantity)
     if apple_milkshake_quantity == "":
         drink_quantities.remove(apple_milkshake_quantity)
         set(drink_quantities)
     else:
         pass
drink_quantity8()
def drink_quantity9():
     orange_juice_quantity = drink_var9.get()
     drink_quantities.append(orange_juice_quantity)
     if orange_juice_quantity == "":
         drink_quantities.remove(orange_juice_quantity)
         set(drink_quantities)
     else:
         pass
drink_quantity9()
def drink_quantity10():
     carrot_juice_quantity = drink_var10.get()
     drink_quantities.append(carrot_juice_quantity)
     if carrot_juice_quantity == "":
         drink_quantities.remove(carrot_juice_quantity)
         set(drink_quantities)
     else:
         pass
drink_quantity10()
print(selected_foods)
print(selected_drinks)
print(food_quantities)
print(drink_quantities)
# Functions
def submit_button():
    global cart_window
    cart_window = Tk()
    cart_window.title("Reciept - Your Cart")
    cart_window.geometry("550x600")
    cart_window.config(bg="#181444")
    cart_window.resizable(False, False)
    # Food, Drink, Bill, and Receipt Labels
    food_label2 = Label(cart_window, text="Foods", fg="white", bg="#181444", font=("Arial", 23, "bold")).place(x=10, y=80)
    drink_label2 = Label(cart_window, text="Drinks", fg="white", bg="#181444", font=("Arial", 23, "bold")).place(x=250, y=80)
    reciept_label = Label(cart_window, text="Reciept🧾", fg="white", bg="#181444", font=("Arial", 30, "bold")).place(x=180, y=10)
    total_bill_label = Label(cart_window, text="Your Total Bill: ", bg="#181444", fg="white",font=("Arial", 25, "bold italic")).place(x=10, y=480)
    show_price = Button(cart_window, text="Show Bill", bg="#181444", fg="white",font=("Arial", 25, "bold"), activebackground="#181444", activeforeground="white", borderwidth=5, command=calculate_total).place(x=10, y=400)
    # Food Items Side
    x_value = 10
    y_value = 120
    index = -1
    for items in selected_foods:
        foods_to_print = Label(cart_window, text=items, bg="#181444", fg="white",font=("Arial", 14, "italic")).place(x=x_value, y=y_value)
        y_value += 30
    # Drink Item Side
    x_value = 250
    y_value = 120
    index2 = -1
    for items in selected_drinks:
        foods_to_print = Label(cart_window, text=items, bg="#181444", fg="white",font=("Arial", 14, "italic")).place(x=x_value, y=y_value)
        y_value += 30
    cart_window.mainloop()
def calculate_total():
    # Total Price of Food
    total_price_of_foods = 0
    if "Zinger" in selected_foods:
        total_price_of_foods += int(food_var1.get()) * 150
        food_prices.append(total_price_of_foods)
    print(food_prices)
    if "Chicken Shawarma" in selected_foods:
        total_price_of_foods += int(food_var2.get()) * 60
        food_prices.append(total_price_of_foods)
    
    if "Fajita" in selected_foods:
        total_price_of_foods += int(food_var3.get()) * 200
        food_prices.append(total_price_of_foods)
    
    if "Pizza" in selected_foods:
        total_price_of_foods += int(food_var4.get()) * 1200
        food_prices.append(total_price_of_foods)
    
    if "Chicken Nuggets" in selected_foods:
        total_price_of_foods += int(food_var5.get()) * 20
        food_prices.append(total_price_of_foods)
    
    if "Dehi Bullay" in selected_foods:
        total_price_of_foods += int(food_var6.get()) * 50
        food_prices.append(total_price_of_foods)
    
    if "Goll Guppay" in selected_foods:
        total_price_of_foods += int(food_var7.get()) * 150
        food_prices.append(total_price_of_foods)
    
    if "French Fries" in selected_foods:
        total_price_of_foods += int(food_var8.get()) * 80
        food_prices.append(total_price_of_foods)
    
    if "Pasta" in selected_foods:
        total_price_of_foods += int(food_var9.get()) * 150
        food_prices.append(total_price_of_foods)
    
    if "Rice" in selected_foods:
        total_price_of_foods += int(food_var10.get()) * 170
        food_prices.append(total_price_of_foods)
    
    print(f"The total price for the food is Rs.{total_price_of_foods}")
    # Total Price of Drinks
    # list_of_drinks_with_prices = ["Coca-Cola/Pepsi - Rs.150", "Marinda - Rs.120", "Seven-Up/Sprite - Rs.100", "Mango Milkshake - Rs.250", "Chocolate Milkshake - Rs.300", "Pomegrenate Juice - Rs.550", "Banana Milkshake - Rs.250", "Apple Milkshake - Rs.150", "Orange Juice - Rs.170", "Carrot Juice - Rs.90"]
    total_price_of_drinks = 0
    if "Pepsi/Coke" in selected_drinks:
        total_price_of_drinks += int(drink_var1.get()) * 150
        food_prices.append(total_price_of_drinks)
    if "Marinda" in selected_drinks:
        total_price_of_drinks += int(drink_var2.get()) * 120
        food_prices.append(total_price_of_drinks)
    
    if "Sprite/7-Up" in selected_drinks:
        total_price_of_drinks += int(drink_var3.get()) * 100
        food_prices.append(total_price_of_drinks)
    
    if "Mango Milkshake" in selected_drinks:
        total_price_of_drinks += int(drink_var4.get()) * 250
        food_prices.append(total_price_of_drinks)
    
    if "Chocolate Milkshake" in selected_drinks:
        total_price_of_drinks += int(drink_var5.get()) * 300
        food_prices.append(total_price_of_drinks)
    
    if "Pomegrenate Juice" in selected_drinks:
        total_price_of_drinks += int(drink_var6.get()) * 550
        food_prices.append(total_price_of_drinks)
    
    if "Banana Milkshake" in selected_drinks:
        total_price_of_drinks += int(drink_var7.get()) * 250
        food_prices.append(total_price_of_drinks)
    
    if "Apple Milkshake" in selected_drinks:
        total_price_of_drinks += int(drink_var8.get()) * 150
        food_prices.append(total_price_of_drinks)
    
    if "Orange Juice" in selected_drinks:
        total_price_of_drinks += int(drink_var9.get()) * 170
        food_prices.append(total_price_of_drinks)
    
    if "Carrot Juice" in selected_drinks:
        total_price_of_drinks += int(drink_var10.get()) * 90
        food_prices.append(total_price_of_drinks)
    print(f"The total price for the drinks is Rs.{total_price_of_drinks}")
    print(f"Your total bill is {total_price_of_foods + total_price_of_drinks}")
    total_price_label = Label(cart_window, text=f"Rs.{total_price_of_foods + total_price_of_drinks}", bg="#181444", fg="white",font=("Arial", 23, "italic")).place(x=200, y=540)

    
    # list_of_foods_with_prices = ["Zinger Burger - Rs. 150 Each", "Chicken Shawarma - Rs. 60 Each", "Fajita - Rs. 200 Each", "Pizza - Rs. 1200", "Chicken Nuggets - Rs. 20 Each", "Dehi Bullay - Rs. 50 Each Plate", "Goll Guppay - Rs. 150 Each Plate", "French Fries - Rs. 80 Each Packet", "Pasta - Rs. 150 Each Plate", "Rice - Rs. 170 Each Plate"]
        #total_price_label = Label(cart_window, text=f"Rs. {total_price_of_food_and_drinks}", bg="#181444", fg="white",font=("Arial", 20, "italic")).place(x=50, y=500)
# Submit Button
submit_btn = Button(window, text="Submit", bg="#181444", fg="white",font=("Arial", 25, "bold"), activebackground="#181444", activeforeground="white", borderwidth=5, command=submit_button).place(x=630, y=660)
window.mainloop()

