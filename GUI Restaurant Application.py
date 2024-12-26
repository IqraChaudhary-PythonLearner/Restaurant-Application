import time
import tkinter
from tkinter import *
# Main Page
main_window = Tk()
main_window.title("5th Avenue - Home Page")
main_window.geometry("1025x682+50+50")
main_window.resizable(False, False)
#main_window.resizable(False, False)
# Define image
main_bg1 = PhotoImage(file="D:\\RestaurantApplication\\black_bg.png")
# Create a canvas
my_main_canvas1 = Canvas(main_window, width=850, height=250)
my_main_canvas1.pack(fill="both", expand=True)
my_main_canvas1.create_image(0,0, image=main_bg1, anchor="nw")
# Menu Label
grey_frame = Frame(my_main_canvas1, height=50, width=1025,bg="#292f42").place(x=0, y=0)

"""# Function
# Location Function
def location():
    location_window = Tk()
    location_window.title("Where Can You Find Us?")
    location_window.geometry("400x200+100+100")
    location_window.config(bg="#292f42")
    location_window.resizable(False, False)
    location_title_label = Label(location_window, text="Location", fg="white",bg="#292f42",font=("Lexend", 45, "bold italic")).place(x=70, y=10)
    location_label = Label(location_window, text="Kingston, New York 12401", fg="white",bg="#292f42",font=("Lexend", 22, "italic")).place(x=20, y=100)  
    location_window.mainloop()
def about_us():
    about_us_window = Tk()
    about_us_window.title("5th Avenue - About Us  ")
    about_us_window.geometry("825x600+100+100")
    about_us_window.config(bg="#292f42")
    about_us_window.resizable(False, False)
    scroll_bar = Scrollbar(about_us_window) 
    scroll_bar.pack(side = RIGHT, fill=Y ) 
    about_us_label = Label(about_us_window, text="Our Story", fg="white",bg="#292f42",font=("Lexend", 45, "bold italic underline")).place(x=250, y=10)
    story_line1 = Label(about_us_window, text="Welcome to 5th Avenue, where fast food meets flavor and creativity! Nestled in the heart", fg="white",bg="#292f42",font=("Lexend", 14, "italic")).place(x=13, y=80) 
    story_line1 = Label(about_us_window, text="of your favorite neighborhood our restaurant is more than just a place to grab a quick bite.", fg="white",bg="#292f42",font=("Lexend", 14, "italic")).place(x=13, y=105) 
    story_line1 = Label(about_us_window, text="It's a culinary experience designed for those who appreciate quality without sacrificing", fg="white",bg="#292f42",font=("Lexend", 14, "italic")).place(x=13, y=130) 
    story_line1 = Label(about_us_window, text="convenience. From juicy burgers to fresh salads, every item on our menu tells a story of", fg="white",bg="#292f42",font=("Lexend", 14, "italic")).place(x=13, y=155) 
    story_line1 = Label(about_us_window, text="passion and dedication. Whether you're dining in with friends or grabbing takeout on the", fg="white",bg="#292f42",font=("Lexend", 14, "italic")).place(x=13, y=180) 
    story_line1 = Label(about_us_window, text="go, we promise an unforgettable taste that keeps you coming back for more. Join us as ", fg="white",bg="#292f42",font=("Lexend", 14, "italic")).place(x=13, y=205) 
    story_line1 = Label(about_us_window, text="we dive into what makes 5th Avenue truly special!", fg="white",bg="#292f42",font=("Lexend", 14, "italic")).place(x=10, y=230) 
    about_us_window.mainloop()
def report_something():
    report_window = Tk()
    report_window.title("5th Avenue - Report Something")
    report_window.geometry("650x270+50+50")
    report_window.resizable(False, False)
    report_window.config(bg="#292f42")
    report_something_label = Label(report_window, text="Report Something", fg="white",bg="#292f42",font=("Lexend", 45, "bold italic underline")).place(x=70, y=10)
    sorry_label = Label(report_window, text="We're sorry if we have some issues.😓", fg="white",bg="#292f42",font=("Lexend", 15, "italic")).place(x=15, y=90)
    sorry_label = Label(report_window, text="We will improve next time. What did you have issues with?🌸", fg="white",bg="#292f42",font=("Lexend", 15, "italic")).place(x=15, y=120)
    text_box = Entry(report_window, fg="white",bg="#292f42",font=("Lexend", 20, "italic"), width=40, textvariable=complaint).place(x=15, y=150)
    complaint = StringVar()
    def send_complain():
        with open("D:\\RestaurantApplication\\Complains.txt", "a") as file:
            file.write(f"{str(complaint.get())} \n")
            file.write("---------------------------------------------------------------------------------\n")
            file.close()

        print(f"complain entered: {complaint.get()}")
    send_btn = Button(report_window, text="Send Complain", fg="white",bg="#292f42",font=("Lexend", 20, "italic bold"), borderwidth=0, cursor="hand2", activebackground="#292f42", activeforeground="white", command=send_complain).place(x=235, y=210)

    report_window.mainloop()"""
def RestaurantApplication():
    window = tkinter.Tk()

    window.title("Restaurant Application - Iqra Chaudhary")
    window.geometry("1400x730+40+40")
    window.config(bg="black")
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
    # Define image
    bg1 = PhotoImage(file="D:\\RestaurantApplication\\app_bg.png.png", master=window)

    # Create a canvas
    my_canvas = Canvas(window, width=1400, height=730)
    my_canvas.pack(fill="both", expand=True)
    my_canvas.create_image(0,0, image=bg1, anchor="nw")

    # Restaurant Label
    restaurant_label = Label(my_canvas, text="Restaurant", fg="#fedfc0", bg="black", font=("Lexend", 50, "bold italic")).place(x=550, y=10)
    # Food and Drink Menu Text
    food_menu_label = Label(my_canvas, text="Food Menu", bg="black", fg="#fedfc0", font=("Arial", 30, "bold")).place(x=265, y=70)
    drink_menu_label = Label(my_canvas, text="Drinks Menu", bg="black", fg="#fedfc0", font=("Arial", 30, "bold")).place(x=930, y=70)
    # Set image in canvas


    # Food Menu Labels
    list_of_foods_with_prices = ["Zinger Burger - Rs. 150 Each", "Chicken Shawarma - Rs. 60 Each", "Fajita - Rs. 200 Each", "Pizza - Rs. 1200", "Chicken Nuggets - Rs. 20 Each", "Dehi Bullay - Rs. 50 Each Plate", "Goll Guppay - Rs. 150 Each Plate", "French Fries - Rs. 80 Each Packet", "Pasta - Rs. 150 Each Plate", "Rice - Rs. 170 Each Plate"]
    value_of_y = 130
    food_number = 1
    for items in list_of_foods_with_prices:
        food_label = Label(my_canvas, text=f"{food_number}. {items}", bg="#fedfc0", fg="black", borderwidth=15, height=0, font=("Lexend", 11, "bold italic")).place(x=120, y=value_of_y)
        value_of_y += 53
        food_number += 1
    # Drink Menu Labels
    list_of_drinks_with_prices = ["Coca-Cola/Pepsi - Rs.150", "Marinda - Rs.120", "Seven-Up/Sprite - Rs.100", "Mango Milkshake - Rs.250", "Chocolate Milkshake - Rs.300", "Pomegrenate Juice - Rs.550", "Banana Milkshake - Rs.250", "Apple Milkshake - Rs.150", "Orange Juice - Rs.170", "Carrot Juice - Rs.90"]
    value_of_y = 130
    drink_number = 1
    for items in list_of_drinks_with_prices:
        food_label = Label(my_canvas, text=f"{drink_number}. {items}", bg="#fedfc0", fg="black", borderwidth=15, height=0,font=("Lexend", 11, " bold italic")).place(x=800, y=value_of_y)
        value_of_y += 53
        drink_number+= 1

    # Foods Text Boxes and Quantity Labels
    y_value2 = 140
    for foods in range(len(list_of_foods_with_prices)):
        quantity_labels = Label(my_canvas, text="Quantity: ", bg="#fedfc0", fg="black", font=("Arial", 14, "bold")).place(x=430, y=y_value2)
        y_value2 += 53
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
    y_value3 = 140
    for x in range(1):
        zinger_textbox = Entry(my_canvas, fg="black", font=("Arial", 12, "bold"), width=7, textvariable=food_var1).place(x=530, y=y_value3)
        y_value3 += 54
        shawarma_textbox = Entry(my_canvas, fg="black", font=("Arial", 12, "bold"), width=7, textvariable=food_var2).place(x=530, y=y_value3)
        y_value3 += 54
        fajita_textbox = Entry(my_canvas, fg="black", font=("Arial", 12, "bold"), width=7, textvariable=food_var3).place(x=530, y=y_value3)
        y_value3 += 54
        pizza_textbox = Entry(my_canvas, fg="black", font=("Arial", 12, "bold"), width=7, textvariable=food_var4).place(x=530, y=y_value3)
        y_value3 += 54
        chicken_nuggets_textbox = Entry(my_canvas, fg="black", font=("Arial", 12, "bold"), width=7, textvariable=food_var5).place(x=530, y=y_value3)
        y_value3 += 54
        zdehi_bullay_textbox = Entry(my_canvas, fg="black", font=("Arial", 12, "bold"), width=7, textvariable=food_var6).place(x=530, y=y_value3)
        y_value3 += 54
        goll_guppay_textbox = Entry(my_canvas, fg="black", font=("Arial", 12, "bold"), width=7, textvariable=food_var7).place(x=530, y=y_value3)
        y_value3 += 54
        frech_fries_textbox = Entry(my_canvas, fg="black", font=("Arial", 12, "bold"), width=7, textvariable=food_var8).place(x=530, y=y_value3)
        y_value3 += 54
        pasta_textbox = Entry(my_canvas, fg="black", font=("Arial", 12, "bold"), width=7, textvariable=food_var9).place(x=530, y=y_value3)
        y_value3 += 54
        rice_textbox = Entry(my_canvas, fg="black", font=("Arial", 12, "bold"), width=7, textvariable=food_var10).place(x=530, y=y_value3)

    # Drinks Text Boxes and Quantity Labels
    y_value4 = 140
    for drinks in range(len(list_of_drinks_with_prices)):
        quantity_labels = Label(my_canvas, text="Quantity: ", bg="#fedfc0", fg="black", height=0,font=("Arial", 14, "bold")).place(x=1070, y=y_value4)
        y_value4 += 54
    y_value5 = 192
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
    y_value3 = 140
    for x in range(1):
        coke_textbox = Entry(my_canvas, fg="black", font=("Arial", 12, "bold"), width=7, textvariable=drink_var1).place(x=1170, y=y_value3)
        y_value3 += 54
        marinda_textbox = Entry(my_canvas, fg="black", font=("Arial", 12, "bold"), width=7, textvariable=drink_var2).place(x=1170, y=y_value3)
        y_value3 += 54
        sprite_textbox = Entry(my_canvas, fg="black", font=("Arial", 12, "bold"), width=7, textvariable=drink_var3).place(x=1170, y=y_value3)
        y_value3 += 54
        mango_milkshake_textbox = Entry(my_canvas, fg="black", font=("Arial", 12, "bold"), width=7, textvariable=drink_var4).place(x=1170, y=y_value3)
        y_value3 += 54
        chocolate_milkshake_textbox = Entry(my_canvas, fg="black", font=("Arial", 12, "bold"), width=7, textvariable=drink_var5).place(x=1170, y=y_value3)
        y_value3 += 54
        pomegrenate_juice_textbox = Entry(my_canvas, fg="black", font=("Arial", 12, "bold"), width=7, textvariable=drink_var6).place(x=1170, y=y_value3)
        y_value3 += 54
        banana_milkshake_textbox = Entry(my_canvas, fg="black", font=("Arial", 12, "bold"), width=7, textvariable=drink_var7).place(x=1170, y=y_value3)
        y_value3 += 54
        apple_milkshake_textbox = Entry(my_canvas, fg="black", font=("Arial", 12, "bold"), width=7, textvariable=drink_var8).place(x=1170, y=y_value3)
        y_value3 += 54
        orange_juice_textbox = Entry(my_canvas, fg="black", font=("Arial", 12, "bold"), width=7, textvariable=drink_var9).place(x=1170, y=y_value3)
        y_value3 += 54
        carrot_juice_textbox = Entry(my_canvas, fg="black", font=("Arial", 12, "bold"), width=7, textvariable=drink_var10).place(x=1170, y=y_value3)

    # Functions
    def submit_button():
        global cart_window
        cart_window = Tk()
        cart_window.title("Reciept - Your Cart")
        cart_window.geometry("550x600")
        cart_window.config(bg="black")
        cart_window.resizable(False, False)
        # Food, Drink, Bill, and Receipt Labels
        food_label2 = Label(cart_window, text="Foods", fg="#fedfc0", bg="black", font=("Arial", 23, "bold")).place(x=10, y=80)
        drink_label2 = Label(cart_window, text="Drinks", fg="#fedfc0", bg="black", font=("Arial", 23, "bold")).place(x=250, y=80)
        reciept_label = Label(cart_window, text="Reciept🧾", fg="#fedfc0", bg="black", font=("Arial", 30, "bold")).place(x=180, y=10)
        total_bill_label = Label(cart_window, text="Your Total Bill: ", bg="black", fg="#fedfc0",font=("Arial", 25, "bold italic")).place(x=10, y=480)
        show_price = Button(cart_window, text="Show Bill", bg="black", fg="#fedfc0",font=("Arial", 25, "bold"), activebackground="black", activeforeground="#fedfc0", borderwidth=5, command=calculate_total).place(x=10, y=400)
    # Food Displaying
        def food_quatity1():
            zinger_quantity = food_var1.get()
            food_quantities.append(zinger_quantity)
            selected_foods.append("Zinger")
            if zinger_quantity == 0:
                food_quantities.remove(zinger_quantity)
                selected_foods.remove("Zinger")
            else:
                food_quantities.append(zinger_quantity)
                selected_foods.append("Zinger")
            set(selected_foods)
            set(food_quantities)
        food_quatity1()
        def food_quatity2():
            shawarma_quantity = food_var2.get()
            food_quantities.append(shawarma_quantity)
            selected_foods.append("Chicken Shawarma")
            if shawarma_quantity == 0:
                food_quantities.remove(shawarma_quantity)
                selected_foods.remove("Chicken Shawarma")
            else:
                food_quantities.append(shawarma_quantity)
                selected_foods.append("Chicken Shawarma")
            set(selected_foods)
            set(food_quantities)
        food_quatity2()
        def food_quatity3():
            fajita_quantity = food_var3.get()
            food_quantities.append(fajita_quantity)
            selected_foods.append("Fajita")
            if fajita_quantity == 0:
                food_quantities.remove(fajita_quantity)
                selected_foods.remove("Fajita")
            else:
                food_quantities.append(fajita_quantity)
                selected_foods.append("Fajita")
            set(selected_foods)
            set(food_quantities)
        food_quatity3()
        def food_quatity4():
             pizza_quantity = food_var3.get()
             food_quantities.append(pizza_quantity)
             selected_foods.append("Pizza")
             if pizza_quantity == 0:
                food_quantities.remove(pizza_quantity)
                selected_foods.remove("Pizza")
             else:
                food_quantities.append(pizza_quantity)
                selected_foods.append("Pizza")
             set(selected_foods)
             set(food_quantities)
        food_quatity3()         
        def food_quatity5():
             chicken_nuggets_quantity = food_var5.get()
             food_quantities.append(chicken_nuggets_quantity)
             selected_foods.append("Chicken Nuggets")
             if chicken_nuggets_quantity == 0:
                food_quantities.remove(chicken_nuggets_quantity)
                selected_foods.remove("Chicken Nuggets")
             else:
                food_quantities.append(chicken_nuggets_quantity)
                selected_foods.append("Chicken Nuggets")
             set(selected_foods)
             set(food_quantities)
        food_quatity5()
        def food_quatity6():
             dehi_bullay_quantity = food_var6.get()
             food_quantities.append(dehi_bullay_quantity)
             selected_foods.append("Dehi Bullay")
             if dehi_bullay_quantity == 0:
                food_quantities.remove(dehi_bullay_quantity)
                selected_foods.remove("Dehi Bullay")
             else:
                food_quantities.append(dehi_bullay_quantity)
                selected_foods.append("Dehi Bullay")
             set(selected_foods)
             set(food_quantities)
        food_quatity6()
        def food_quatity7():
             goll_guppay_quantity = food_var7.get()
             food_quantities.append(goll_guppay_quantity)
             selected_foods.append("Goll Guppay")
             if goll_guppay_quantity == 0:
                food_quantities.remove(goll_guppay_quantity)
                selected_foods.remove("Goll Guppay")
             else:
                food_quantities.append(goll_guppay_quantity)
                selected_foods.append("Goll Guppay")
             set(selected_foods)
             set(food_quantities)
        food_quatity7()
        def food_quatity8():
             french_fries_quantity = food_var8.get()
             food_quantities.append(french_fries_quantity)
             selected_foods.append("French Fries")
             if french_fries_quantity == 0:
                food_quantities.remove(french_fries_quantity)
                selected_foods.remove("French Fries")
             else:
                food_quantities.append(french_fries_quantity)
                selected_foods.append("French Fries")
             set(selected_foods)
             set(food_quantities)
        food_quatity8()
        def food_quatity9():
             pasta_quantity = food_var9.get()
             food_quantities.append(pasta_quantity)
             selected_foods.append("Pasta")
             if pasta_quantity == 0:
                food_quantities.remove(pasta_quantity)
                selected_foods.remove("Pasta")
             else:
                food_quantities.append(pasta_quantity)
                selected_foods.append("Pasta")
             set(selected_foods)
             set(food_quantities)
        food_quatity9()
        def food_quatity10():
             rice_quantity = food_var10.get()
             food_quantities.append(rice_quantity)
             selected_foods.append("Rice")
             if rice_quantity == 0:
                food_quantities.remove(rice_quantity)
                selected_foods.remove("Rice")
             else:
                food_quantities.append(rice_quantity)
                selected_foods.append("Rice")
             set(selected_foods)
             set(food_quantities)
        food_quatity10()
    # Drink Displaying
        def drink_quantity1():
            coke_quantity = drink_var1.get()
            drink_quantities.append(coke_quantity)
            selected_drinks.append("Pepsi/Coke")
            if coke_quantity == 0:
               drink_quantities.remove(coke_quantity)
               selected_drinks.remove("Pepsi/Coke")
            else:
               drink_quantities.append(coke_quantity)
               selected_drinks.append("Pepsi/Coke")
            set(selected_drinks)
            set(drink_quantities)
        drink_quantity1()

        def drink_quantity2():
            marinda_quantity = drink_var2.get()
            drink_quantities.append(marinda_quantity)
            selected_drinks.append("Marinda")
            if marinda_quantity == 0:
               drink_quantities.remove(marinda_quantity)
               selected_drinks.remove("Marinda")
            else:
               drink_quantities.append(marinda_quantity)
               selected_drinks.append("Marinda")
            set(selected_drinks)
            set(drink_quantities)
        drink_quantity2()
        def drink_quantity3():
            sprite_quantity = drink_var3.get()
            drink_quantities.append(sprite_quantity)
            selected_drinks.append("Sprite/7-Up")
            if sprite_quantity == 0:
               drink_quantities.remove(sprite_quantity)
               selected_drinks.remove("Sprite/7-Up")
            else:
               drink_quantities.append(sprite_quantity)
               selected_drinks.append("Sprite/7-Up")
            set(selected_drinks)
            set(drink_quantities)

        drink_quantity3()
        def drink_quantity4():
            mango_milkshake_quantity = drink_var4.get()
            drink_quantities.append(mango_milkshake_quantity)
            selected_drinks.append("Mango Milkshake")
            if mango_milkshake_quantity == 0:
               drink_quantities.remove(mango_milkshake_quantity)
               selected_drinks.remove("Mango Milkshake")
            else:
               drink_quantities.append(mango_milkshake_quantity)
               selected_drinks.append("Mango Milkshake")
            set(selected_drinks)
            set(drink_quantities)

        drink_quantity4()
        def drink_quantity5():
            chocolate_milkshake_quantity = drink_var5.get()
            drink_quantities.append(chocolate_milkshake_quantity)
            selected_drinks.append("Chocolate Milkshake")
            if chocolate_milkshake_quantity == 0:
               drink_quantities.remove(chocolate_milkshake_quantity)
               selected_drinks.remove("Chocolate Milkshake")
            else:
               drink_quantities.append(chocolate_milkshake_quantity)
               selected_drinks.append("Chocolate Milkshake")
            set(selected_drinks)
            set(drink_quantities)

        drink_quantity5()
        def drink_quantity6():
            pomegrenate_juice_quantity = drink_var6.get()
            drink_quantities.append(pomegrenate_juice_quantity)
            selected_drinks.append("Pomegrenate Juice")
            if pomegrenate_juice_quantity == 0:
               drink_quantities.remove(pomegrenate_juice_quantity)
               selected_drinks.remove("Pomegrenate Juice")
            else:
               drink_quantities.append(pomegrenate_juice_quantity)
               selected_drinks.append("Pomegrenate Juice")
            set(selected_drinks)
            set(drink_quantities)

        drink_quantity6()
        def drink_quantity7():
            banana_milkshake_quantity = drink_var7.get()
            drink_quantities.append(banana_milkshake_quantity)
            selected_drinks.append("Banana Milkshake")
            if banana_milkshake_quantity == 0:
               drink_quantities.remove(banana_milkshake_quantity)
               selected_drinks.remove("Banana Milkshake")
            else:
               drink_quantities.append(banana_milkshake_quantity)
               selected_drinks.append("Banana Milkshake")
            set(selected_drinks)
            set(drink_quantities)

        drink_quantity7()
        def drink_quantity8():
            apple_milkshake_quantity = drink_var8.get()
            drink_quantities.append(apple_milkshake_quantity)
            selected_drinks.append("Apple Milkshake")
            if apple_milkshake_quantity == 0:
               drink_quantities.remove(apple_milkshake_quantity)
               selected_drinks.remove("Apple Milkshake")
            else:
               drink_quantities.append(apple_milkshake_quantity)
               selected_drinks.append("Apple Milkshake")
            set(selected_drinks)
            set(drink_quantities)

        drink_quantity8()
        def drink_quantity9():
            orange_juice_quantity = drink_var9.get()
            drink_quantities.append(orange_juice_quantity)
            selected_drinks.append("Orange Juice")
            if orange_juice_quantity == 0:
               drink_quantities.remove(orange_juice_quantity)
               selected_drinks.remove("Orange Juice")
            else:
               drink_quantities.append(orange_juice_quantity)
               selected_drinks.append("Orange Juice")
            set(selected_drinks)
            set(drink_quantities)

        drink_quantity9()
        def drink_quantity10():
            carrot_juice_quantity = drink_var10.get()
            drink_quantities.append(carrot_juice_quantity)
            selected_drinks.append("Carrot Juice")
            if carrot_juice_quantity == 0:
               drink_quantities.remove(carrot_juice_quantity)
               selected_drinks.remove("Carrot Juice")
            else:
               drink_quantities.append(carrot_juice_quantity)
               selected_drinks.append("Carrot Juice")
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
        cart_window.mainloop()
    def calculate_total():
        # Total Price of Food
        total_price_of_foods = 0
        if "Zinger" in selected_foods:
            total_price_of_foods += int(food_var1.get()) * 150
            food_prices.append(total_price_of_foods)

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
        print(f"Selected Foods: {selected_foods}")
        print(f"Food Quantities: {food_quantities}")
        print(f"Drinks Quantities: {selected_drinks}")
        print(f"Selected Drinks: {drink_quantities}")
        print(f"The total price for the food is Rs.{total_price_of_foods}")
        print(f"The total price for the drinks is Rs.{total_price_of_drinks}")
        print(f"Your total bill is {total_price_of_foods + total_price_of_drinks}")
        total_price_label = Label(cart_window, text=f"Rs.{total_price_of_foods + total_price_of_drinks}", bg="black", fg="#fedfc0",font=("Arial", 23, "italic")).place(x=200, y=540)
        def save_reciept():
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
            Goodbye = Tk()
            Goodbye.title("")
        save_reciept = Button(cart_window, text="Save Receipt", bg="black", fg="#fedfc0",font=("Arial", 25, "bold"), activebackground="black", activeforeground="#fedfc0", borderwidth=5, command=save_reciept).place(x=200, y=400)

        # list_of_foods_with_prices = ["Zinger Burger - Rs. 150 Each", "Chicken Shawarma - Rs. 60 Each", "Fajita - Rs. 200 Each", "Pizza - Rs. 1200", "Chicken Nuggets - Rs. 20 Each", "Dehi Bullay - Rs. 50 Each Plate", "Goll Guppay - Rs. 150 Each Plate", "French Fries - Rs. 80 Each Packet", "Pasta - Rs. 150 Each Plate", "Rice - Rs. 170 Each Plate"]
            #total_price_label = Label(cart_window, text=f"Rs. {total_price_of_food_and_drinks}", bg="black", fg="#fedfc0",font=("Arial", 20, "italic")).place(x=50, y=500)
    # Submit Button
    submit_btn = Button(window, text="Submit", bg="black", fg="#fedfc0",font=("Arial", 25, "bold"), activebackground="black", activeforeground="#fedfc0", borderwidth=0, command=submit_button).place(x=630, y=650)
    window.mainloop()

# Main Page Text
#main_page_text = Label(my_main_canvas1, text="Home Page", fg="#d0c8b4",bg="#292f42",font=("Lexend", 45, "bold italic")).place(x=20, y=25)
#welcome_message = Label(my_main_canvas1, text="Welcome!😊😊 Click one of the below👇", fg="#d0c8b4",bg="#292f42",font=("Lexend", 19, "bold italic")).place(x=20, y=125)
working_hours = Label(my_main_canvas1, text="Working Hours: 10 A.M. TO 11 P.M.", font=("Lexend", 19, "italic"), fg="#d0c8b4",bg="#292f42").place(x=20, y=585)
phone_number = Label(my_main_canvas1, text="Phone Number: +306 881 1994", font=("Lexend", 19, "italic"), fg="#d0c8b4",bg="#292f42").place(x=20, y=620)
# Different Page Frames
location_page = Frame(my_main_canvas1).place(x=0, y=0)
about_us_page = Frame(my_main_canvas1).place(x=0, y=0)
more_info_page = Frame(my_main_canvas1).place(x=0, y=0)
special_deals_page = Frame(my_main_canvas1).place(x=0, y=0)
complains_page = Frame(my_main_canvas1).place(x=0, y=0)
order_something_page = Frame(my_main_canvas1).place(x=0, y=0)
close_quit_page = Frame(my_main_canvas1).place(x=0, y=0)
# Labels and Functions
# Location Label
location_title_label = Label(location_page, text="Location", fg="white",bg="#292f42",font=("Lexend", 45, "bold italic")).place(x=20, y=50)
location_label = Label(location_page, text="Kingston, New York 12401", fg="white",bg="#292f42",font=("Lexend", 22, "italic")).place(x=20, y=150)
# About Us
about_us_label = Label(about_us_page, text="Our Story", fg="white",bg="#292f42",font=("Lexend", 45, "bold italic underline")).place(x=250, y=10)
story_line1 = Label(about_us_page, text="Welcome to 5th Avenue, where fast food meets flavor and creativity! Nestled in the heart", fg="white",bg="#292f42",font=("Lexend", 14, "italic")).place(x=13, y=80)
story_line1 = Label(about_us_page, text="of your favorite neighborhood our restaurant is more than just a place to grab a quick bite.", fg="white",bg="#292f42",font=("Lexend", 14, "italic")).place(x=13, y=105)
story_line1 = Label(about_us_page, text="It's a culinary experience designed for those who appreciate quality without sacrificing", fg="white",bg="#292f42",font=("Lexend", 14, "italic")).place(x=13, y=130) 
story_line1 = Label(about_us_page, text="convenience. From juicy burgers to fresh salads, every item on our menu tells a story of", fg="white",bg="#292f42",font=("Lexend", 14, "italic")).place(x=13, y=155)
story_line1 = Label(about_us_page, text="passion and dedication. Whether you're dining in with friends or grabbing takeout on the", fg="white",bg="#292f42",font=("Lexend", 14, "italic")).place(x=13, y=180) 
story_line1 = Label(about_us_page, text="go, we promise an unforgettable taste that keeps you coming back for more. Join us as ", fg="white",bg="#292f42",font=("Lexend", 14, "italic")).place(x=13, y=205)
story_line1 = Label(about_us_page, text="we dive into what makes 5th Avenue truly special!", fg="white",bg="#292f42",font=("Lexend", 14, "italic")).place(x=10, y=230) 
# Buttons
location = Button(my_main_canvas1, text="Location", font=("Lexend", 19, "italic underline"), fg="white",bg="#292f42", borderwidth=0, activeforeground="white", activebackground="#292f42", cursor="hand2", command= lambda: location_page.tkraise()).place(x=10, y=0)
about_us_button = Button(my_main_canvas1, text="About Us", font=("Lexend", 19, "italic underline"), fg="white",bg="#292f42", borderwidth=0, activeforeground="white", activebackground="#292f42", cursor="hand2", command= lambda: about_us_page.tkraise()).place(x=145, y=0)
more_information = Button(my_main_canvas1, text="More Info", font=("Lexend", 19, "italic underline"), fg="white",bg="#292f42", borderwidth=0, activeforeground="white", activebackground="#292f42", cursor="hand2").place(x=285, y=0)
special_deals = Button(my_main_canvas1, text="Special Deals", font=("Lexend", 19, "italic underline"), fg="white",bg="#292f42", borderwidth=0, activeforeground="white", activebackground="#292f42", cursor="hand2").place(x=430, y=0)
complains = Button(my_main_canvas1, text="Report", font=("Lexend", 19, "italic underline"), fg="white",bg="#292f42", borderwidth=0, activeforeground="white", activebackground="#292f42", cursor="hand2").place(x=625, y=0)
order_something = Button(my_main_canvas1, text="Order", font=("Lexend", 19, "italic underline"), fg="white",bg="#292f42", borderwidth=0, activeforeground="white", activebackground="#292f42", cursor="hand2", command=RestaurantApplication).place(x=735, y=0)
close_quit = Button(my_main_canvas1, text="Quit", font=("Lexend", 19, "italic underline"), fg="white",bg="#292f42", borderwidth=0, activeforeground="white", activebackground="#292f42", cursor="hand2", command=quit).place(x=840, y=0)

main_window.mainloop()
