print("hello welcome to MC Donalds")
order_count = int(input("how many order you want "))
# menu = " menu = burger , french fries , pepsi , cococola , chicken nuggets"
# print(menu)
burger = "select any burger: Big Mac Quarter Pounder with Cheese. Double Quarter Pounder with Cheese.Quarter Pounder with Cheese Deluxe. McDouble Quarter Pounder with Cheese Bacon. Cheeseburger. Double Cheeseburger."
print(burger)

french_fries = "select any french fries: Piri-Piri Fries. Mexican Cheesy Fries. American Cream and Onion Fries. Classic Salted Fries."
print(french_fries)

pepsi = "select any pepsi: Pepsi. Diet Pepsi. Pepsi Zero Sugar. Pepsi Wild Cherry. Diet Pepsi Wild Cherry. Pepsi Real Lime. Diet Pepsi Lime. Caffeine Free Pepsi."
print("pepsi")

coca_cola = "select any coca cola: Coca-Cola Cherry. Coca-Cola Cherry Vanilla. Coca-Cola Vanilla. Coca-Cola Cherry Zero Sugar. Coca-Cola Cherry Vanilla Zero Sugar. Coca-Cola Vanilla Zero Sugar. "
print("coca-cola")

chicken_nuggets = "select any chicken nuggets: the bell, the bow-tie, the ball and the boot. "
print(chicken_nuggets)



price = 0 
while order_count > 0:
    order = input("may i know your order ")
    if order == "burger":
        print("order placed")
        price+=100
        order_count -= 1
        continue

    if order == "french fries":
        print("order placed")
        price+=80
        order_count -= 1
        continue

    if order == "pepsi":
        print("oeder placed")
        price+=80
        order_count -= 1
        continue

    if order == "coca cola":
        print("order placed")
        price+=80
        order_count -= 1
        continue

    if order == "chicken nuggets":
        print("order placed")
        price+=100
        order_count -= 1
        continue

print("total price = " ,+ price)