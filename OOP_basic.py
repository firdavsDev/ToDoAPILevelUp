class Pizza:
    def __init__(self, toppings):
        self.toppings = list(toppings)

    def __str__(self):
        return f"Pizza({self.toppings})"

    def add_topping(self, topping):
        self.toppings.append(topping)

    def remove_topping(self, topping):
        if topping in self.toppings:
            self.toppings.remove(topping)

    ## Class methods to create specific types of pizzas
    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomatoes"])

    @classmethod
    def prosciutto(cls):
        return cls(["mozzarella", "tomatoes", "ham"])

    @staticmethod
    def get_size_in_inches(size):
        """Returns the diameter in inches for common pizza sizes."""
        size_map = {
            "small": 8,
            "medium": 12,
            "large": 16,
        }

        return size_map.get(size, "Unknown size")


if __name__ == "__main__":
    pizza = Pizza(["pepperoni", "mushrooms", "green peppers"])
    # print(pizza)  # Output: Pizza(['pepperoni', 'mushrooms', 'green peppers'])

    # pizza.add_topping("extra cheese")
    # print(
    #     pizza
    # )  # Output: Pizza(['pepperoni', 'mushrooms', 'green peppers', 'extra cheese'])

    # pizza.remove_topping("mushrooms")
    # print(pizza)  # Output: Pizza(['pepperoni', 'green peppers', 'extra cheese'])

    # margherita = Pizza(["mozzarella", "tomatoes"])
    margherita = Pizza.margherita()  # Output: Pizza(['mozzarella', 'tomatoes'])
    print(margherita)
    print(Pizza.get_size_in_inches("medium"))  # Output: 12
    prosciutto = Pizza.prosciutto()  # Output: Pizza(['mozzarella', 'tomatoes', 'ham'])
    print(prosciutto)
