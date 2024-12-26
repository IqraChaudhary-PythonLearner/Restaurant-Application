# Imports
from tkinter import *
import ttkbootstrap
import math
# Making my Main Window
main_window = ttkbootstrap.Window(themename="solar")
main_window.title("5th Avenue - Iqra Chaudhary")
main_window.state("zoomed")
#main_window.resizable(False, False)
# Making my Notebook
notebook = ttkbootstrap.Notebook(main_window)
# My Background Image
main_bg1 = PhotoImage(file="D:\\RestaurantApplication\\black_bg.png")
main_bg2 = PhotoImage(file="D:\\RestaurantApplication\\black_bg2.png")
order_image = PhotoImage(file="D:\\RestaurantApplication\\app_bg.png.png")
popcorn_image = PhotoImage(file="D:\\RestaurantApplication\\popcorn.png")
cheeseburger_image = PhotoImage(file="D:\\RestaurantApplication\\cheeseburger.png")
fries_image = PhotoImage(file="D:\\RestaurantApplication\\fries.png")
coffee_image = PhotoImage(file="D:\\RestaurantApplication\\coffee.png")
drinks_image = PhotoImage(file="D:\\RestaurantApplication\\drinks.png")
pizza_image = PhotoImage(file="D:\\RestaurantApplication\\pizza.png")
hotdog_image = PhotoImage(file="D:\\RestaurantApplication\\hotdog.png")
# Defining the Tabs
about_us_tab = Frame(notebook)
more_info_tab = Frame(notebook)
special_deals_tab = Frame(notebook)
complain_tab = Frame(notebook)
order_tab = Frame(notebook)
# Adding the Background To Each Tab
about_us_canvas = Canvas(about_us_tab, width=1920, height=968)
about_us_canvas.pack(expand=True)
about_us_canvas.create_image(0,0, image=main_bg1, anchor="nw")

more_info_canvas = Canvas(more_info_tab, width=1920, height=968)
more_info_canvas.pack(expand=True)
more_info_canvas.create_image(0,0, image=main_bg1, anchor="nw")

special_deals_canvas = Canvas(special_deals_tab, width=1920, height=968)
special_deals_canvas.pack(expand=True)
special_deals_canvas.create_image(0,0, image=main_bg2, anchor="nw")

order_tab_canvas = Canvas(order_tab, width=1400, height=730)
order_tab_canvas.pack(fill="both", expand=True)
order_tab_canvas.create_image(0,0, image=order_image, anchor="nw")
# Special Deals
# Functions
def save_info():
    with open("D:\\RestaurantApplication\\More Info.txt", "a") as file:
        file.write("Timings: Working Hours: 10 A.M. TO 11 P.M\n")
        file.write("Location: Kingston, New York 12401\n")
        file.write("Working Days: Monday to Saturday\n")
        file.write("Phone Number: +306 881 1994\n")
        file.write("Email: 5thAvenue@gmail.com\n")
        file.write("-------------------------------------------------\n")
    done_label = Label(more_info_canvas, text="Information has been saved", fg="white",bg="#292f42",font=("Lexend", 20, "italic")).place(x=50, y=520)
# Designing the "About Us" Canvas
about_us_label = Label(about_us_canvas, text="Our Story", fg="white",bg="#292f42",font=("Lexend", 50, "bold italic underline")).place(x=2, y=10)
story_line1 = Label(about_us_canvas, text="Welcome to 5th Avenue, where fast food", fg="white",bg="#292f42",font=("Lexend", 19, "italic")).place(x=2, y=110) 
story_line2 = Label(about_us_canvas, text="meets flavor and creativity! Nestled in the heart of", fg="white",bg="#292f42",font=("Lexend", 19, "italic")).place(x=2, y=150) 
story_line3 = Label(about_us_canvas, text="your favorite neighborhood our restaurant is more than just a place", fg="white",bg="#292f42",font=("Lexend", 19, "italic")).place(x=2, y=190) 
story_line4 = Label(about_us_canvas, text="to grab a quick bite. It's a culinary experience designed for those", fg="white",bg="#292f42",font=("Lexend", 19, "italic")).place(x=2, y=230) 
story_line5 = Label(about_us_canvas, text="who appreciate quality without sacrificing convenience. From juicy", fg="white",bg="#292f42",font=("Lexend", 19, "italic")).place(x=2, y=270) 
story_line6 = Label(about_us_canvas, text="burgers to fresh salads go, we promise an unforgettable taste that", fg="white",bg="#292f42",font=("Lexend", 19, "italic")).place(x=2, y=310) 
story_line7 = Label(about_us_canvas, text="keeps you coming back for more. Join us as every item on our", fg="white",bg="#292f42",font=("Lexend", 19, "italic")).place(x=2, y=350) 
story_line8 = Label(about_us_canvas, text="menu tells a story of passion and dedication. Whether you're", fg="white",bg="#292f42",font=("Lexend", 19, "italic")).place(x=2, y=390) 
story_line9 = Label(about_us_canvas, text="dining in with friends or grabbing takeout on the go", fg="white",bg="#292f42",font=("Lexend", 19, "italic")).place(x=2, y=430) 
story_line10 = Label(about_us_canvas, text="we dive into what makes 5th Avenue truly special!", fg="white",bg="#292f42",font=("Lexend", 19, "italic")).place(x=2, y=470) 
# Designing the "More Info" Canvas
more_info_label = Label(more_info_canvas, text="More Info", fg="white",bg="#292f42",font=("Lexend", 60, "bold italic underline")).place(x=2, y=10)
timing_label = Label(more_info_canvas, text="Timings: Working Hours: 10 A.M. TO 11 P.M", fg="white",bg="#292f42",font=("Lexend", 25, "italic")).place(x=2, y=130) 
working_days_label = Label(more_info_canvas, text="Working Days: Monday to Saturday", fg="white",bg="#292f42",font=("Lexend", 25, "italic")).place(x=2, y=180) 
phone_number_label = Label(more_info_canvas, text="Phone Number: +306 881 1994", fg="white",bg="#292f42",font=("Lexend", 25, "italic")).place(x=2, y=230) 
email_label = Label(more_info_canvas, text="Email: 5thAvenue@gmail.com", fg="white",bg="#292f42",font=("Lexend", 25, "italic")).place(x=2, y=280) 
location_label = Label(more_info_canvas, text="Location: Kingston, New York 12401", fg="white",bg="#292f42",font=("Lexend", 25, "italic")).place(x=2, y=330) 
save_info = Button(more_info_canvas, text="Save Info", fg="white",bg="#292f42",font=("Lexend", 30, "italic"), command=save_info).place(x=100, y=400)
fifth_avaenue = Label(more_info_canvas, text="5th Avenue", fg="white",bg="#292f42",font=("Courier New", 55, "bold italic underline")).place(x=5, y=600)
# Designing the "Special Deals" Canvas
special_price = []
happy_new_year_label = Label(special_deals_canvas, text="Happy New Year!", fg="white",bg="#292f42",font=("Lexend", 45, "bold italic ")).place(x=2, y=10)
enjoy_label = Label(special_deals_canvas, text="Enjoy our Special Deals!", fg="white",bg="#292f42",font=("Lexend", 14, "italic")).place(x=2, y=110)

#def submit_display_price():
 #   price = Label(special_deals_canvas, text=f"${special_total}", bg="black", fg="#fedfc0",font=("Arial", 24, "bold")).place(x=275, y=900)
deal_var1 = IntVar()
deal_var2 = IntVar()
deal_var3 = IntVar()
deal_var4 = IntVar()
deal_var5 = IntVar()
deal_var6 = IntVar()
deal_var7 = IntVar()

popcorn_deal = Button(special_deals_canvas, image=popcorn_image, command=None).place(x=2, y=150)
cheeseburger_deal = Button(special_deals_canvas, image=cheeseburger_image, command=None).place(x=210, y=150)
fries_deal = Button(special_deals_canvas, image=fries_image, command=None).place(x=418, y=150)
coffee_deal = Button(special_deals_canvas, image=coffee_image, command=None).place(x=626, y=150)
drinks_deal = Button(special_deals_canvas, image=drinks_image, command=None).place(x=2, y=480)
pizza_deal = Button(special_deals_canvas, image=pizza_image, command=None).place(x=275, y=480)
hotdog_deal = Button(special_deals_canvas, image=hotdog_image, command=None).place(x=545, y=480)

special_orders = []

def calculate_special_total():
    special_total = 0
    if deal_var1.get() == 1:
        special_total += 1.50
        special_orders.append("Popcorn")
    if deal_var1.get() == 0:
        print("Deal_var1 is not clicked.")

    if deal_var2.get() == 1:
        special_total += 1.75
        special_orders.append("Cheeseburger")
    if deal_var2.get() == 0:
        print("Deal_var2 is not clicked.")

    if deal_var3.get() == 1:
        special_total += 3.00
        special_orders.append("Fries")
    if deal_var3.get() == 0:
        print("Deal_var3 is not clicked.")

    if deal_var4.get() == 1:
        special_total += 4.50
        special_orders.append("Coffee")
    if deal_var4.get() == 0:
        print("Deal_var4 is not clicked.")

    if deal_var5.get() == 1:
        special_total += 4.50
        special_orders.append("Drinks")
    if deal_var5.get() == 0:
        print("Deal_var5 is not clicked.")

    if deal_var6.get() == 1:
        special_total += 8.99
        special_orders.append("Pizza")
    if deal_var6.get() == 0:
        print("Deal_var6 is not clicked.")

    if deal_var7.get() == 1:
        special_total += 7.99
        special_orders.append("Hot Dog")
    if deal_var7.get() == 1:
        print("Deal_var7 is not clicked.")


    Label(special_deals_canvas, text=f"You have to pay: ${special_total:.2f}", bg="black", fg="#fedfc0",font=("Arial", 25, "bold")).place(x=200, y=905)
    Label(special_deals_canvas, text="Special Ordered Deals", bg="black", fg="#fedfc0",font=("Arial", 25, "italic bold")).place(x=850, y=170)
    x_value = 850
    y_value = 220
    for special_foods in special_orders:
        Label(special_deals_canvas, text=special_foods, bg="black", fg="#fedfc0",font=("Arial", 20, "italic")).place(x=x_value, y=y_value)
        y_value += 40
    print(special_orders)
    print(special_total)




# Checkboxes
popcorn_checkbox = Checkbutton(special_deals_canvas, text="Popcorn", fg="white",bg="#292f42",font=("Lexend", 14, "italic"), onvalue=1, offvalue=0, variable=deal_var1).place(x=10, y=180)
cheeseburger_checkbox = Checkbutton(special_deals_canvas, text="Cheeseburger", fg="white",bg="#292f42",font=("Lexend", 14, "italic"), onvalue=1, offvalue=0, variable=deal_var2).place(x=215, y=180)
fries_checkbox = Checkbutton(special_deals_canvas, text="Fries", fg="white",bg="#292f42",font=("Lexend", 14, "italic"), onvalue=1, offvalue=0, variable=deal_var3).place(x=430, y=180)
coffee_checkbox = Checkbutton(special_deals_canvas, text="Coffee", fg="white",bg="#292f42",font=("Lexend", 14, "italic"), onvalue=1, offvalue=0, variable=deal_var4).place(x=645, y=180)
drinks_checkbox = Checkbutton(special_deals_canvas, text="Drinks", fg="white",bg="#292f42",font=("Lexend", 20, "italic"), onvalue=1, offvalue=0, variable=deal_var5).place(x=40, y=520)
pizza_checkbox = Checkbutton(special_deals_canvas, text="Pizza", fg="white",bg="#292f42",font=("Lexend", 20, "italic"), onvalue=1, offvalue=0, variable=deal_var6).place(x=300, y=520)
hotdog_checkbox = Checkbutton(special_deals_canvas, text="Hotdog", fg="white",bg="#292f42",font=("Lexend", 20, "italic"), onvalue=1, offvalue=0, variable=deal_var7).place(x=550, y=510)
#popcorn_checkbox = Checkbutton(special_deals_canvas, text="Popcorn", fg="white",bg="#292f42",font=("Lexend", 14, "italic")).place(x=10, y=180)
submit_special_deals = Button(special_deals_canvas, text="Submit", bg="black", fg="#fedfc0",font=("Arial", 25, "bold"), command=calculate_special_total).place(x=2, y=900)

notebook.add(about_us_tab, text="About Us")
notebook.add(more_info_tab, text="More Info")
notebook.add(special_deals_tab, text="Special Deals")
notebook.add(order_tab, text="Order")

notebook.place(x=0, y=0)
#######RESTAURANT ORDER APPLICATION##########
# Variables
food_quantities = []
drink_quantities = []
selected_foods = []
selected_drinks = []
food_prices = []
drink_price = []
# Food and Drinks Labels
#fedfc0_food_label = Label(window, bg="#fedfc0", width=90, height=36).place(x=50, y=110)
#fedfc0_drink_label = Label(window, bg="#fedfc0", width=90, height=36).place(x=720, y=110)
# Restaurant Label
restaurant_label = Label(order_tab_canvas, text="5th Avenue", fg="#fedfc0", bg="black", font=("Lexend", 50, "bold italic")).place(x=720, y=10)
# Food and Drink Menu Text
food_menu_label = Label(order_tab_canvas, text="Food Menu", bg="black", fg="#fedfc0", font=("Arial", 36, "bold")).place(x=225, y=110)
drink_menu_label = Label(order_tab_canvas, text="Drink Menu", bg="black", fg="#fedfc0", font=("Arial", 36, "bold")).place(x=1325, y=110)
# Set image in canvas
# Food Menu Labels
list_of_foods_with_prices = ["Zinger Burger - Rs. 150 Each", "Chicken Shawarma - Rs. 60 Each", "Fajita - Rs. 200 Each", "Pizza - Rs. 1200", "Chicken Nuggets - Rs. 20 Each", "Dehi Bullay - Rs. 50 Each Plate", "Goll Guppay - Rs. 150 Each Plate", "French Fries - Rs. 80 Each Packet", "Pasta - Rs. 150 Each Plate", "Rice - Rs. 170 Each Plate"]
value_of_y = 200
food_number = 1
for items in list_of_foods_with_prices:
    food_label = Label(order_tab_canvas, text=f"{food_number}. {items}", bg="#fedfc0", fg="black", borderwidth=15, height=0, font=("Lexend", 15, "bold italic")).place(x=75, y=value_of_y)
    value_of_y += 65
    food_number += 1
# Drink Menu Labels
list_of_drinks_with_prices = ["Coca-Cola/Pepsi - Rs.150", "Marinda - Rs.120", "Seven-Up/Sprite - Rs.100", "Mango Milkshake - Rs.250", "Chocolate Milkshake - Rs.300", "Pomegrenate Juice - Rs.550", "Banana Milkshake - Rs.250", "Apple Milkshake - Rs.150", "Orange Juice - Rs.170", "Carrot Juice - Rs.90"]
value_of_y = 200
drink_number = 1
for items in list_of_drinks_with_prices:
    food_label = Label(order_tab_canvas, text=f"{drink_number}. {items}", bg="#fedfc0", fg="black", borderwidth=15, height=0,font=("Lexend", 15, " bold italic")).place(x=1120, y=value_of_y)
    value_of_y += 65
    drink_number+= 1
# Foods Text Boxes and Quantity Labels
y_value2 = 200
for foods in range(len(list_of_foods_with_prices)):
    quantity_labels = Label(order_tab_canvas, text="Quantity: ", bg="#fedfc0", fg="black", font=("Arial", 20, "bold")).place(x=560, y=y_value2)
    y_value2 += 65
food_var1 = IntVar()
food_var2 = IntVar()
food_var3 = IntVar()
food_var4 = IntVar()
food_var5 = IntVar()
food_var6 = IntVar()
food_var7 = IntVar()
food_var8 = IntVar()
food_var9 = IntVar()
food_var10 = IntVar()
y_value3 = 200
for x in range(1):
    zinger_textbox = Entry(order_tab_canvas, fg="black", font=("Arial", 20, "bold"), width=7, textvariable=food_var1).place(x=720, y=y_value3)
    y_value3 += 65
    shawarma_textbox = Entry(order_tab_canvas, fg="black", font=("Arial", 20, "bold"), width=7, textvariable=food_var2).place(x=720, y=y_value3)
    y_value3 += 65
    fajita_textbox = Entry(order_tab_canvas, fg="black", font=("Arial", 20, "bold"), width=7, textvariable=food_var3).place(x=720, y=y_value3)
    y_value3 += 65
    pizza_textbox = Entry(order_tab_canvas, fg="black", font=("Arial", 20, "bold"), width=7, textvariable=food_var4).place(x=720, y=y_value3)
    y_value3 += 65
    chicken_nuggets_textbox = Entry(order_tab_canvas, fg="black", font=("Arial", 20, "bold"), width=7, textvariable=food_var5).place(x=720, y=y_value3)
    y_value3 += 65
    zdehi_bullay_textbox = Entry(order_tab_canvas, fg="black", font=("Arial", 20, "bold"), width=7, textvariable=food_var6).place(x=720, y=y_value3)
    y_value3 += 65
    goll_guppay_textbox = Entry(order_tab_canvas, fg="black", font=("Arial", 20, "bold"), width=7, textvariable=food_var7).place(x=720, y=y_value3)
    y_value3 += 65
    frech_fries_textbox = Entry(order_tab_canvas, fg="black", font=("Arial", 20, "bold"), width=7, textvariable=food_var8).place(x=720, y=y_value3)
    y_value3 += 65
    pasta_textbox = Entry(order_tab_canvas, fg="black", font=("Arial", 20, "bold"), width=7, textvariable=food_var9).place(x=720, y=y_value3)
    y_value3 += 65
    rice_textbox = Entry(order_tab_canvas, fg="black", font=("Arial", 20, "bold"), width=7, textvariable=food_var10).place(x=720, y=y_value3)
# Drinks Text Boxes and Quantity Labels
y_value4 = 200
for drinks in range(len(list_of_drinks_with_prices)):
    quantity_labels = Label(order_tab_canvas, text="Quantity: ", bg="#fedfc0", fg="black", height=0,font=("Arial", 20, "bold")).place(x=1550, y=y_value4)
    y_value4 += 65
y_value5 = 200
drink_var1 = IntVar()
drink_var2 = IntVar()
drink_var3 = IntVar()
drink_var4 = IntVar()
drink_var5 = IntVar()
drink_var6 = IntVar()
drink_var7 = IntVar()
drink_var8 = IntVar()
drink_var9 = IntVar()
drink_var10 = IntVar()
y_value3 = 200
for x in range(1):
    coke_textbox = Entry(order_tab_canvas, fg="black", font=("Arial", 20, "bold"), width=7, textvariable=drink_var1).place(x=1709, y=y_value3)
    y_value3 += 65
    marinda_textbox = Entry(order_tab_canvas, fg="black", font=("Arial", 20, "bold"), width=7, textvariable=drink_var2).place(x=1709, y=y_value3)
    y_value3 += 65
    sprite_textbox = Entry(order_tab_canvas, fg="black", font=("Arial", 20, "bold"), width=7, textvariable=drink_var3).place(x=1709, y=y_value3)
    y_value3 += 65
    mango_milkshake_textbox = Entry(order_tab_canvas, fg="black", font=("Arial", 20, "bold"), width=7, textvariable=drink_var4).place(x=1709, y=y_value3)
    y_value3 += 65
    chocolate_milkshake_textbox = Entry(order_tab_canvas, fg="black", font=("Arial", 20, "bold"), width=7, textvariable=drink_var5).place(x=1709, y=y_value3)
    y_value3 += 65
    pomegrenate_juice_textbox = Entry(order_tab_canvas, fg="black", font=("Arial", 20, "bold"), width=7, textvariable=drink_var6).place(x=1709, y=y_value3)
    y_value3 += 65
    banana_milkshake_textbox = Entry(order_tab_canvas, fg="black", font=("Arial", 20, "bold"), width=7, textvariable=drink_var7).place(x=1709, y=y_value3)
    y_value3 += 65
    apple_milkshake_textbox = Entry(order_tab_canvas, fg="black", font=("Arial", 20, "bold"), width=7, textvariable=drink_var8).place(x=1709, y=y_value3)
    y_value3 += 65
    orange_juice_textbox = Entry(order_tab_canvas, fg="black", font=("Arial", 20, "bold"), width=7, textvariable=drink_var9).place(x=1709, y=y_value3)
    y_value3 += 65
    carrot_juice_textbox = Entry(order_tab_canvas, fg="black", font=("Arial", 20, "bold"), width=7, textvariable=drink_var10).place(x=1709, y=y_value3)
# Functions
def submit_button():
    global cart_window
    global total_price_of_foods
    global total_price_of_drinks
    cart_window = Tk()
    cart_window.title("Reciept - Your Cart")
    cart_window.geometry("550x600")
    cart_window.config(bg="#002b36")
    cart_window.resizable(False, False)
    # Food, Drink, Bill, and Receipt Labels
    food_label2 = Label(cart_window, text="Foods", fg="#fedfc0", bg="black", font=("Arial", 23, "bold")).place(x=10, y=80)
    drink_label2 = Label(cart_window, text="Drinks", fg="#fedfc0", bg="black", font=("Arial", 23, "bold")).place(x=250, y=80)
    reciept_label = Label(cart_window, text="Reciept🧾", fg="#fedfc0", bg="black", font=("Arial", 30, "bold")).place(x=180, y=10)
    total_bill_label = Label(cart_window, text="Your Total Bill: ", bg="black", fg="#fedfc0",font=("Arial", 25, "bold italic")).place(x=10, y=480)
    
# Food Displaying
    def food_quatity1():
        zinger_quantity = food_var1.get()
        food_quantities.append(zinger_quantity)
        selected_foods.append(f"Zinger x{zinger_quantity}")
        if zinger_quantity == 0:
            food_quantities.remove(zinger_quantity)
            selected_foods.remove(f"Zinger x{zinger_quantity}")
        else:
            food_quantities.append(zinger_quantity)
            selected_foods.append(f"Zinger x{zinger_quantity}")
        set(selected_foods)
        set(food_quantities)
    food_quatity1()
    def food_quatity2():
        shawarma_quantity = food_var2.get()
        food_quantities.append(shawarma_quantity)
        selected_foods.append(f"Chicken Shawarma x{shawarma_quantity}")
        if shawarma_quantity == 0:
            food_quantities.remove(shawarma_quantity)
            selected_foods.remove(f"Chicken Shawarma x{shawarma_quantity}")
        else:
            food_quantities.append(shawarma_quantity)
            selected_foods.append(f"Chicken Shawarma x{shawarma_quantity}")
        set(selected_foods)
        set(food_quantities)
    food_quatity2()
    def food_quatity3():
        fajita_quantity = food_var3.get()
        food_quantities.append(fajita_quantity)
        selected_foods.append(f"Fajita x{fajita_quantity}")
        if fajita_quantity == 0:
            food_quantities.remove(fajita_quantity)
            selected_foods.remove(f"Fajita x{fajita_quantity}")
        else:
            food_quantities.append(fajita_quantity)
            selected_foods.append(f"Fajita x{fajita_quantity}")
        set(selected_foods)
        set(food_quantities)
    food_quatity3()
    def food_quatity4():
         pizza_quantity = food_var3.get()
         food_quantities.append(pizza_quantity)
         selected_foods.append(f"Pizza x{pizza_quantity}")
         if pizza_quantity == 0:
            food_quantities.remove(pizza_quantity)
            selected_foods.remove(f"Pizza x{pizza_quantity}")
         else:
            food_quantities.append(pizza_quantity)
            selected_foods.append(f"Pizza x{pizza_quantity}")
         set(selected_foods)
         set(food_quantities)
    food_quatity4()         
    def food_quatity5():
         chicken_nuggets_quantity = food_var5.get()
         food_quantities.append(chicken_nuggets_quantity)
         selected_foods.append(f"Chicken Nuggets x{chicken_nuggets_quantity}")
         if chicken_nuggets_quantity == 0:
            food_quantities.remove(chicken_nuggets_quantity)
            selected_foods.remove(f"Chicken Nuggets x{chicken_nuggets_quantity}")
         else:
            food_quantities.append(chicken_nuggets_quantity)
            selected_foods.append(f"Chicken Nuggets x{chicken_nuggets_quantity}")
         set(selected_foods)
         set(food_quantities)
    food_quatity5()
    def food_quatity6():
         dehi_bullay_quantity = food_var6.get()
         food_quantities.append(dehi_bullay_quantity)
         selected_foods.append(f"Dehi Bullay x{dehi_bullay_quantity}")
         if dehi_bullay_quantity == 0:
            food_quantities.remove(dehi_bullay_quantity)
            selected_foods.remove(f"Dehi Bullay x{dehi_bullay_quantity}")
         else:
            food_quantities.append(dehi_bullay_quantity)
            selected_foods.append(f"Dehi Bullay x{dehi_bullay_quantity}")
         set(selected_foods)
         set(food_quantities)
    food_quatity6()
    def food_quatity7():
         goll_guppay_quantity = food_var7.get()
         food_quantities.append(goll_guppay_quantity)
         selected_foods.append(f"Goll Guppay x{goll_guppay_quantity}")
         if goll_guppay_quantity == 0:
            food_quantities.remove(goll_guppay_quantity)
            selected_foods.remove(f"Goll Guppay x{goll_guppay_quantity}")
         else:
            food_quantities.append(goll_guppay_quantity)
            selected_foods.append(f"Goll Guppay x{goll_guppay_quantity}")
         set(selected_foods)
         set(food_quantities)
    food_quatity7()
    def food_quatity8():
         french_fries_quantity = food_var8.get()
         food_quantities.append(french_fries_quantity)
         selected_foods.append(f"French Fries x{french_fries_quantity}")
         if french_fries_quantity == 0:
            food_quantities.remove(french_fries_quantity)
            selected_foods.remove(f"French Fries x{french_fries_quantity}")
         else:
            food_quantities.append(french_fries_quantity)
            selected_foods.append(f"French Fries x{french_fries_quantity}")
         set(selected_foods)
         set(food_quantities)
    food_quatity8()
    def food_quatity9():
         pasta_quantity = food_var9.get()
         food_quantities.append(pasta_quantity)
         selected_foods.append(f"Pasta x{pasta_quantity}")
         if pasta_quantity == 0:
            food_quantities.remove(pasta_quantity)
            selected_foods.remove(f"Pasta x{pasta_quantity}")
         else:
            food_quantities.append(pasta_quantity)
            selected_foods.append(f"Pasta x{pasta_quantity}")
         set(selected_foods)
         set(food_quantities)
    food_quatity9()
    def food_quatity10():
         rice_quantity = food_var10.get()
         food_quantities.append(rice_quantity)
         selected_foods.append(f"Rice x{rice_quantity}")
         if rice_quantity == 0:
            food_quantities.remove(rice_quantity)
            selected_foods.remove(f"Rice x{rice_quantity}")
         else:
            food_quantities.append(rice_quantity)
            selected_foods.append(f"Rice x{rice_quantity}")
         set(selected_foods)
         set(food_quantities)
    food_quatity10()
    # Drink Displaying
    def drink_quantity1():
        coke_quantity = drink_var1.get()
        drink_quantities.append(coke_quantity)
        selected_drinks.append(f"Pepsi/Coke x{coke_quantity}")
        if coke_quantity == 0:
           drink_quantities.remove(coke_quantity)
           selected_drinks.remove(f"Pepsi/Coke x{coke_quantity}")
        else:
           drink_quantities.append(coke_quantity)
           selected_drinks.append(f"Pepsi/Coke x{coke_quantity}")
        set(selected_drinks)
        set(drink_quantities)
    drink_quantity1()
    def drink_quantity2():
        marinda_quantity = drink_var2.get()
        drink_quantities.append(marinda_quantity)
        selected_drinks.append(f"Marinda x{marinda_quantity}")
        if marinda_quantity == 0:
           drink_quantities.remove(marinda_quantity)
           selected_drinks.remove(f"Marinda x{marinda_quantity}")
        else:
           drink_quantities.append(marinda_quantity)
           selected_drinks.append(f"Marinda x{marinda_quantity}")
        set(selected_drinks)
        set(drink_quantities)
    drink_quantity2()
    def drink_quantity3():
        sprite_quantity = drink_var3.get()
        drink_quantities.append(sprite_quantity)
        selected_drinks.append(f"Sprite/7-Up x{sprite_quantity}")
        if sprite_quantity == 0:
           drink_quantities.remove(sprite_quantity)
           selected_drinks.remove(f"Sprite/7-Up x{sprite_quantity}")
        else:
           drink_quantities.append(sprite_quantity)
           selected_drinks.append(f"Sprite/7-Up x{sprite_quantity}")
        set(selected_drinks)
        set(drink_quantities)
    drink_quantity3()
    def drink_quantity4():
        mango_milkshake_quantity = drink_var4.get()
        drink_quantities.append(mango_milkshake_quantity)
        selected_drinks.append(f"Mango Milkshake x{mango_milkshake_quantity}")
        if mango_milkshake_quantity == 0:
           drink_quantities.remove(mango_milkshake_quantity)
           selected_drinks.remove(f"Mango Milkshake x{mango_milkshake_quantity}")
        else:
           drink_quantities.append(mango_milkshake_quantity)
           selected_drinks.append(f"Mango Milkshake x{mango_milkshake_quantity}")
        set(selected_drinks)
        set(drink_quantities)
    drink_quantity4()
    def drink_quantity5():
        chocolate_milkshake_quantity = drink_var5.get()
        drink_quantities.append(chocolate_milkshake_quantity)
        selected_drinks.append(f"Chocolate Milkshake x{chocolate_milkshake_quantity}")
        if chocolate_milkshake_quantity == 0:
           drink_quantities.remove(chocolate_milkshake_quantity)
           selected_drinks.remove(f"Chocolate Milkshake x{chocolate_milkshake_quantity}")
        else:
           drink_quantities.append(chocolate_milkshake_quantity)
           selected_drinks.append(f"Chocolate Milkshake x{chocolate_milkshake_quantity}")
        set(selected_drinks)
        set(drink_quantities)
    drink_quantity5()
    def drink_quantity6():
        pomegrenate_juice_quantity = drink_var6.get()
        drink_quantities.append(pomegrenate_juice_quantity)
        selected_drinks.append(f"Pomegrenate Juice x{pomegrenate_juice_quantity}")
        if pomegrenate_juice_quantity == 0:
           drink_quantities.remove(pomegrenate_juice_quantity)
           selected_drinks.remove(f"Pomegrenate Juice x{pomegrenate_juice_quantity}")
        else:
           drink_quantities.append(pomegrenate_juice_quantity)
           selected_drinks.append(f"Pomegrenate Juice x{pomegrenate_juice_quantity}")
        set(selected_drinks)
        set(drink_quantities)
    drink_quantity6()
    def drink_quantity7():
        banana_milkshake_quantity = drink_var7.get()
        drink_quantities.append(banana_milkshake_quantity)
        selected_drinks.append(f"Banana Milkshake x{banana_milkshake_quantity}")
        if banana_milkshake_quantity == 0:
           drink_quantities.remove(banana_milkshake_quantity)
           selected_drinks.remove(f"Banana Milkshake x{banana_milkshake_quantity}")
        else:
           drink_quantities.append(banana_milkshake_quantity)
           selected_drinks.append(f"Banana Milkshake x{banana_milkshake_quantity}")
        set(selected_drinks)
        set(drink_quantities)
    drink_quantity7()
    def drink_quantity8():
        apple_milkshake_quantity = drink_var8.get()
        drink_quantities.append(apple_milkshake_quantity)
        selected_drinks.append(f"Apple Milkshake x{apple_milkshake_quantity}")
        if apple_milkshake_quantity == 0:
           drink_quantities.remove(apple_milkshake_quantity)
           selected_drinks.remove(f"Apple Milkshake x{apple_milkshake_quantity}")
        else:
           drink_quantities.append(apple_milkshake_quantity)
           selected_drinks.append(f"Apple Milkshake x{apple_milkshake_quantity}")
        set(selected_drinks)
        set(drink_quantities)
    drink_quantity8()
    def drink_quantity9():
        orange_juice_quantity = drink_var9.get()
        drink_quantities.append(orange_juice_quantity)
        selected_drinks.append(f"Orange Juice x{orange_juice_quantity}")
        if orange_juice_quantity == 0:
           drink_quantities.remove(orange_juice_quantity)
           selected_drinks.remove(f"Orange Juice x{orange_juice_quantity}")
        else:
           drink_quantities.append(orange_juice_quantity)
           selected_drinks.append(f"Orange Juice x{orange_juice_quantity}")
        set(selected_drinks)
        set(drink_quantities)
    drink_quantity9()
    def drink_quantity10():
        carrot_juice_quantity = drink_var10.get()
        drink_quantities.append(carrot_juice_quantity)
        selected_drinks.append(f"Carrot Juice x{carrot_juice_quantity}")
        if carrot_juice_quantity == 0:
           drink_quantities.remove(carrot_juice_quantity)
           selected_drinks.remove(f"Carrot Juice x{carrot_juice_quantity}")
        else:
           drink_quantities.append(carrot_juice_quantity)
           selected_drinks.append(f"Carrot Juice x{carrot_juice_quantity}")
        set(selected_drinks)
        set(drink_quantities)
    drink_quantity10()
    # Food Items Side
    x_value = 10
    y_value = 120
    index = -1
    for items in set(selected_foods):
        Label(cart_window, text=items, bg="black", fg="#fedfc0",font=("Arial", 14, "italic")).place(x=x_value, y=y_value)
        y_value += 30
    # Drink Item Side
    x_value = 250
    y_value = 120
    index2 = -1
    for items in set(selected_drinks):
        Label(cart_window, text=items, bg="black", fg="#fedfc0",font=("Arial", 14, "italic")).place(x=x_value, y=y_value)
        y_value += 30
    # Total Price of Food
    total_price_of_foods = 0
    if f"Zinger x{food_var1.get()}" in selected_foods:
        total_price_of_foods += int(food_var1.get()) * 150
        food_prices.append(total_price_of_foods)
    if f"Chicken Shawarma x{food_var2.get()}" in selected_foods:
        total_price_of_foods += int(food_var2.get()) * 60
        food_prices.append(total_price_of_foods)
    if f"Fajita x{food_var3.get()}" in selected_foods:
        total_price_of_foods += int(food_var3.get()) * 200
        food_prices.append(total_price_of_foods)
    if f"Pizza x{food_var4.get()}" in selected_foods:
        total_price_of_foods += int(food_var4.get()) * 1200
        food_prices.append(total_price_of_foods)
    if f"Chicken Nuggets x{food_var5.get()}" in selected_foods:
        total_price_of_foods += int(food_var5.get()) * 20
        food_prices.append(total_price_of_foods)
    if f"Dehi Bullay x{food_var6.get()}" in selected_foods:
        total_price_of_foods += int(food_var6.get()) * 50
        food_prices.append(total_price_of_foods)
    if f"Goll Guppay x{food_var7.get()}" in selected_foods:
        total_price_of_foods += int(food_var7.get()) * 150
        food_prices.append(total_price_of_foods)
    if f"French Fries x{food_var8.get()}" in selected_foods:
        total_price_of_foods += int(food_var8.get()) * 80
        food_prices.append(total_price_of_foods)
    if f"Pasta x{food_var9.get()}" in selected_foods:
        total_price_of_foods += int(food_var9.get()) * 150
        food_prices.append(total_price_of_foods)
    if f"Rice x{food_var10.get()}" in selected_foods:
        total_price_of_foods += int(food_var10.get()) * 170
        food_prices.append(total_price_of_foods)
    # Tfotal Price of Drinks
    # list_of_drinks_with_prices = ["Coca-Cola/Pepsi - Rs.150", "Marinda - Rs.120", "Seven-Up/Sprite - Rs.100", "Mango Milkshake - Rs.250", "Chocolate Milkshake - Rs.300", "Pomegrenate Juice - Rs.550", "Banana Milkshake - Rs.250", "Apple Milkshake - Rs.150", "Orange Juice - Rs.170", "Carrot Juice - Rs.90"]
    total_price_of_drinks = 0
    if f"Pepsi/Coke x{drink_var1.get()}" in selected_drinks:
        total_price_of_drinks += int(drink_var1.get()) * 150
        food_prices.append(total_price_of_drinks)
    if f"Marinda x{drink_var2.get()}" in selected_drinks:
        total_price_of_drinks += int(drink_var2.get()) * 120
        food_prices.append(total_price_of_drinks)
    if f"Sprite/7-Up x{drink_var3.get()}" in selected_drinks:
        total_price_of_drinks += int(drink_var3.get()) * 100
        food_prices.append(total_price_of_drinks)
    if f"Mango Milkshake x{drink_var4.get()}" in selected_drinks:
        total_price_of_drinks += int(drink_var4.get()) * 250
        food_prices.append(total_price_of_drinks)
    if f"Chocolate Milkshake x{drink_var5.get()}" in selected_drinks:
        total_price_of_drinks += int(drink_var5.get()) * 300
        food_prices.append(total_price_of_drinks)
    if f"Pomegrenate Juice x{drink_var6.get()}" in selected_drinks:
        total_price_of_drinks += int(drink_var6.get()) * 550
        food_prices.append(total_price_of_drinks)
    if f"Banana Milkshake x{drink_var7.get()}" in selected_drinks:
        total_price_of_drinks += int(drink_var7.get()) * 250
        food_prices.append(total_price_of_drinks)
    if f"Apple Milkshake x{drink_var8.get()}" in selected_drinks:
        total_price_of_drinks += int(drink_var8.get()) * 150
        food_prices.append(total_price_of_drinks)
    if f"Orange Juice x{drink_var9.get()}" in selected_drinks:
        total_price_of_drinks += int(drink_var9.get()) * 170
        food_prices.append(total_price_of_drinks)
    if f"Carrot Juice x{drink_var10.get()}" in selected_drinks:
        total_price_of_drinks += int(drink_var10.get()) * 90
        food_prices.append(total_price_of_drinks)
    Label(cart_window, text=f"Rs.{total_price_of_foods + total_price_of_drinks}", bg="black", fg="#fedfc0",font=("Arial", 23, "italic")).place(x=200, y=540)
    def save_reciept():
        global total_price_of_foods
        global total_price_of_drinks
        global cart_window
        text1="FOODS AND DRINKS SELECTED:\n"
        text4 = f"FOOD BILL: Rs.{total_price_of_foods}\n"
        text5 = f"DRINK BILL: Rs.{total_price_of_drinks}\n"
        text6 = f"YOUR TOTAL BILL IS: Rs.{total_price_of_foods + total_price_of_drinks}\n"
        text7 = "------------------------------------------\n"
        with open("D:\\RestaurantApplication\\Reciepts.txt", "w") as file:
            file.write(text1)
            for selected_f in set(selected_foods):
                file.write(selected_f + "\n")
            for selected_d in set(selected_drinks):
                file.write(selected_d + "\n")
            file.write(text4)
            file.write(text5)
            file.write(text6)
            file.write(text7)
    save_reciept = Button(cart_window, text="Save Receipt", bg="black", fg="#fedfc0",font=("Arial", 25, "bold"), activebackground="black", activeforeground="#fedfc0", borderwidth=5, command=save_reciept).place(x=10, y=400)
    exit_or_quit = Button(cart_window, text="X", bg="black", fg="#fedfc0",font=("Arial", 25, "bold"), activebackground="red", activeforeground="#fedfc0", borderwidth=5, command=quit).place(x=320, y=400)

    print(f"Selected Foods: {selected_foods}")
    print(f"Food Quantities: {food_quantities}")
    print(f"Drinks Quantities: {selected_drinks}")
    print(f"Selected Drinks: {drink_quantities}")
    print(f"The total price for the food is Rs.{total_price_of_foods}")
    print(f"The total price for the drinks is Rs.{total_price_of_drinks}")
    print(f"Your total bill is {total_price_of_foods + total_price_of_drinks}")

    # list_of_foods_with_prices = ["Zinger Burger - Rs. 150 Each", "Chicken Shawarma - Rs. 60 Each", "Fajita - Rs. 200 Each", "Pizza - Rs. 1200", "Chicken Nuggets - Rs. 20 Each", "Dehi Bullay - Rs. 50 Each Plate", "Goll Guppay - Rs. 150 Each Plate", "French Fries - Rs. 80 Each Packet", "Pasta - Rs. 150 Each Plate", "Rice - Rs. 170 Each Plate"]
        #total_price_label = Label(cart_window, text=f"Rs. {total_price_of_food_and_drinks}", bg="black", fg="#fedfc0",font=("Arial", 20, "italic")).place(x=50, y=500)
# Submit Button
submit_btn = Button(order_tab_canvas, text="Submit", bg="black", fg="#fedfc0",font=("Arial", 25, "bold"), activebackground="black", activeforeground="#fedfc0", borderwidth=0, command=submit_button).place(x=880, y=880)
order_tab_canvas.mainloop()


main_window.mainloop()





"""about_us_button = customtkinter.CTkButton(order_tab_canvas, text="About Us", command=about_us_page).place(x=0, y=0)
more_info_button = customtkinter.CTkButton(order_tab_canvas, text="More Info").place(x=140, y=0)
special_deals_button = customtkinter.CTkButton(order_tab_canvas, text="Special Deals").place(x=280, y=0)
complains_button = customtkinter.CTkButton(order_tab_canvas, text="Report").place(x=420, y=0)
order_button = customtkinter.CTkButton(order_tab_canvas, text="Order").place(x=560, y=0)
quit_button = customtkinter.CTkButton(order_tab_canvas, text="Quit", command=quit).place(x=700, y=0)"""
"""notebook = ttk.Notebook(order_tab_canvas)

about_us_tab = Frame(notebook)
more_info_tab = Frame(notebook)
special_deals_tab = Frame(notebook)
complain_tab = Frame(notebook)
order_tab = Frame(notebook)

notebook.add(about_us_tab, text="About Us")
notebook.add(more_info_tab, text="More Info")
notebook.add(special_deals_tab, text="Special Deals")
notebook.add(complain_tab, text="Report")
notebook.add(order_tab, text="Order")

notebook.place(x=0, y=0)"""