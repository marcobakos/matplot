class Menu:
    """
    Create a Menu Object
    """
    def __init__(self, name, items, start_time, end_time):
        """
        Args :
        :param name: (str) - menu Name
        :param items: (dic) - Dictionary with ("purchase item": price)
        :param start_time: (int) - Time when it is open - Format 24 hs - ex. 10am = 1000
        :param end_time: (int) - Time when it is close - Format 24 hs - ex. 11pm = 2300
        """
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        """
        Print the object
        :return: "Menu - {mn}, available from {st} to {et}."
        """
        self.representative_string = "Menu - {mn}, available from {st} to {et}.".\
            format(mn=self.name,
                   st=self.start_time,
                   et=self.end_time
                   )
        return self.representative_string

    def calculate_bill(self, purchased_items):
        """
        Calculate the bill
        :param purchased_items: (list) - List of Purchase items
        :return: (float) - Total value of the Bill
        """
        self.purchased_items = purchased_items
        total_price = 0
        for item in self.purchased_items:
            total_price += self.items[item]
        return total_price

    def print_menu(self):
        """
        Print Menu Items
        :return: (tuple) - purchase item , $ price
        """
        offer = self.items.items()
        for k, v in offer:
                print("Item --> ", k, " - $", v)


class Franchise:
    """
    Create a Franchise Object
    """
    def __init__(self, address, menus):
        """
        Args :
        :param address: (str) - Place address
        :param menus: (list) - List of Menus Object
        """
        self.address = address
        self.menus = menus

    def __repr__(self):
        """
        Print the Place Address
        :return: (str) - Place Address
        """
        return "Franchise Address - {fa}.".format(fa=self.address)

    def available_menus(self, time):
        """
        Check if the specific Menu is available in that time between start-time and end-time
        :param time: (int) - Format 24 hs - ex. 10am = 1000
        :return: (list) - With the Menu Names
        """
        available_menu = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menu.append(menu)
        return available_menu


class Business:
    """
    Create a Business Object
    """
    def __init__(self, name, franchises):
        """
        Args :
        :param name: (str) - Place Name
        :param franchises: (list) - list of Franchise Object
        """
        self.name = name
        self.franchises = franchises


"""
Execution
"""

brunch = Menu("brunch", {
    'pancakes': 7.50,
    'waffles': 9.00,
    'burger': 11.00,
    'home fries': 4.50,
    'coffee': 1.50,
    'espresso': 3.00,
    'tea': 1.00,
    'mimosa': 10.50,
    'orange juice': 3.50
    }, 1100, 1600)


print("Print brunch_menu -->", brunch.print_menu())

early_bird = Menu("Early-bird Dinners", {
    'salumeria plate': 8.00,
    'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50,
    'espresso': 3.00,
    }, 1500, 1800)

dinner = Menu("Dinner", {
    'crostini with eggplant caponata': 13.00,
    'ceaser salad': 16.00,
    'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 2.00, 'espresso': 3.00,
    }, 1700, 2300)

kids = Menu("Kids", {
    'chicken nuggets': 6.50,
    'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00
    }, 1100, 2100)

print("Print brunch --> ", brunch)

bill = brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
print("Print bill --> ", str(bill))

bill2 = early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])
print("Print bill --> ",str(bill2))


flasship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])

print("The flasship_store --> ", flasship_store )

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

print("The new_installment --> ", new_installment)

print("Print flasship store --> ", flasship_store.available_menus(1700))

basta = Business("Basta Fazoolin' with my Heart", [flasship_store, new_installment])

# Arepas

arepas_items = {
    'arepa pabellon': 7.00,
    'pernil arepa': 8.50,
    'guayanes arepa': 8.00,
    'jamon arepa': 7.50
    }


arepas_menu = Menu("Take a' Arepa", arepas_items, 1000, 2000)


arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu, kids])


arepas = Business("Take a' Arepa", [arepas_place])

print("Arepas information --> ", arepas.franchises[0].menus[0])


print("Print Arepas --> ", arepas_menu.items.






