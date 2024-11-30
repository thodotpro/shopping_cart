articles = {1: ['schuhe', 100], 2: ['iphone', 1000], 3: ['ipad', 800], 4: ['airpods', 300], 5: ['kugelschreiber', 2]}
prices = {1: '100', 2: '1000', 3: '800', 4: '300', 5: '2'}

order_number = 1
shopping_cart = []

class shopping:

    def __init__(self):
        self.article = articles
        self.shopping_cart = cart
        self.fill_cart = fill

    # Funktion listet die verfügbaren Artikel auf
    def available():
        print("-------- Available --------")
        for key, value in articles.items():
            print(f"{key} - {value[0]:15}{value[1]:10.2f} €")
        print("---------- END -----------")


    # Eingabefehler funktionieren noch nicht ganz. Value Error mit int und str
    def fill_cart():
        print()
        print("--Fill cart with available items--")
        active_shop = True
        exit = "q"
        complete = "c"
        while active_shop:
            order = input("Enter article no. you want to add (q to quit - c to complete): ")
            if order == exit.lower():
                print("See you next time.")
                shopping_cart.clear()
                active_shop = False
            elif order == complete.lower():
                print("Thank you for choosing us!")
                print(f"Your order: {shopping_cart}")
                active_shop = False
            elif int(order) in articles.keys():
                shopping_cart.append(int(order))
                print(f"Current order: {shopping_cart}")
            elif int(order) not in articles.keys():
                print("Invalid input.")
            elif order not in articles.values():
                print("Invalid input.")
            else:
                print("Invalid input.")


shopping.available()
shopping.fill_cart()
