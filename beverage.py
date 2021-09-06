class Beverage:
    def __init__(self, beverage_name, all_ingredients):
        self.beverage_name = beverage_name
        # No need of this check again
        # Another thing is your whole code revolves around the coffeeMAke not knowing what drinks to make. But here you are creating a dependency, which I think is bad
        if isinstance(all_ingredients, dict):
            self.ingredients = dict()
            self.ingredients["hot_water"] = all_ingredients.get("hot_water")
            self.ingredients["hot_milk"] = all_ingredients.get("hot_milk")
            self.ingredients["ginger_syrup"] = all_ingredients.get("ginger_syrup")
            self.ingredients["sugar_syrup"] = all_ingredients.get("sugar_syrup")
            self.ingredients["tea_leaves_syrup"] = all_ingredients.get("tea_leaves_syrup")
            self.ingredients["green_mixture"] = all_ingredients.get("green_mixture")
        else:
            print("Received ingredients are not in dict format")

    def add_ingredient(self, name, quantity):
        if quantity >= 0:
            self.ingredients[name] = quantity

    def get_ingredient_quantity(self, name):
        return self.ingredients.get(name, -1)

    def remove_ingredient(self, name):
        del self.ingredients[name]

    def get_beverage_name(self):
        return self.beverage_name

    def get_beverage_ingredients(self):
        return self.ingredients
