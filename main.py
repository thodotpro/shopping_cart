article = {1: ['schuhe', 100], 2: ['iphone', 1000], 3: ['ipad', 800], 4: ['airpods', 300], 5: ['kugelschreiber', 2]}


order_number = 1
shopping_cart = []


class shopping:

    def __init__(self):
        self.article = article
        self.shopping_cart = cart
        self.fill_cart = fill

    def available():
        print("-------- Available --------")
        for key, value in article.items():
            print(f"{key} - {value[0]:15}{value[1]:10.2f} €")
        print("---------- END -----------")

    # Bug
    def fill_cart(**kwargs):
        print()
        print("--Fill cart with available items--")
        active_shop = True
        exit = "q"
        complete = "c"
        while active_shop:
            order = input("Enter article you want to add (q to quit/c to complete): ")
            if int(order) in article.keys():
                shopping_cart.append(order)
            elif order not in article.keys():
                print("Invalid value!")
            elif order == exit.lower():
                shopping_cart.clear()
                active_shop = False
            elif order == complete.lower():
                active_shop = False

        print(shopping_cart)



shopping.available()
shopping.fill_cart()
