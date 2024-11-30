articles = {"1": ['schuhe', 100], "2": ['iphone', 1000], "3": ['ipad', 800], "4": ['airpods', 300], "5": ['kugelschreiber', 2]}
prices = {1: '100', 2: '1000', 3: '800', 4: '300', 5: '2'}

order_number = 1
shopping_cart = ['1']

class Shopping:

    def __init__(self, available, fill):
        self.available = available
        self.fill = fill

    # Funktion listet die verfügbaren Artikel auf
    def available():
        print("-------- Available --------")
        for key, value in articles.items():
            print(f"{key} - {value[0]:15}{value[1]:10.2f} €")
        print("---------- END -----------")


    # Funktion füllt Einkaufswagen nach User Input
    def fill():
        print()
        print("--Fill cart with available items--")
        active_shop = True
        exit = "q"
        complete = "c"
        current_order = []
        while active_shop:
            order = input("Enter article no. you want to add (q to quit - c to complete): ")
            if order in articles.keys():
                shopping_cart.append(order)
                for key in shopping_cart:
                    pass
                current_order.append(articles.get(key)[0])
                print(f"Current order: {current_order}")
            elif order == complete:
                print("Thank you for choosing us!")
                for order in shopping_cart:
                    pass
                print(f"Your order: {current_order}", end=",")
                active_shop = False
            elif order == exit:
                print("See you next time.")
                shopping_cart.clear()
                active_shop = False
            else:
                print("Invalid input.")

def main():
    Shopping.available()
    Shopping.fill()

if __name__ == '__main__':
    main()
