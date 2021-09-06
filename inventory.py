class Inventory:
    ingredient_vs_quantity = dict()

    def __init__(self, all_ingredients):
        if isinstance(all_ingredients, dict):
            self.ingredient_vs_quantity = all_ingredients

    def clear_inventory(self):
        self.ingredient_vs_quantity = None

    def add_ingredient_to_inventory(self, name, quantity):
        if quantity >= 0:
            self.ingredient_vs_quantity[name] = quantity

    def get_quantity_in_inventory(self, ingredient_name):
        return self.ingredient_vs_quantity.get(ingredient_name, -1)

    def is_inventory_initialized(self):
        if bool(self.ingredient_vs_quantity) and len(self.ingredient_vs_quantity) >= 1:
            return True
        else:
            return False

    def check_and_update(self, beverage):
        """
        method to gather info using passed beverage object and
        based on that update inventory if all necessary quantity is present

        """
        if not self.is_inventory_initialized():
            print("Initialize inventory ... ")
            return False

        status = True

        beverage_name = beverage.get_beverage_name()
        beverage_ingredients_dict = beverage.get_beverage_ingredients()
        remove_quantities_from_inventory = dict()
        for beverage_ingredient in beverage_ingredients_dict:
            quantity_needed_for_bvg = beverage_ingredients_dict.get(beverage_ingredient, -1)
            # quantity_needed_for_bvg = beverage.get_ingredient_quantity(beverage_ingredient)
            quantity_in_inventory = self.get_quantity_in_inventory(beverage_ingredient)

            if quantity_needed_for_bvg is None or quantity_needed_for_bvg == -1:
                # in case inventory has gone dry for a certain ingridient or
                # beverage does not the specific ingredient .ie. None
                continue

            if quantity_in_inventory != -1 and quantity_in_inventory >= quantity_needed_for_bvg:
                # self.ingredient_names[beverage_ingredient] -= quantity_needed_for_bvg
                remove_quantities_from_inventory[beverage_ingredient] = quantity_needed_for_bvg

            elif quantity_in_inventory != -1 and quantity_in_inventory < quantity_needed_for_bvg:
                print("{} cannot be prepared, {} is not sufficient".format(beverage_name, beverage_ingredient))
                status = False
                break
            elif quantity_in_inventory == -1:
                print("{} cannot be prepared, {} is finished".format(beverage_name, beverage_ingredient))
                status = False
                break

        if status:
            # removing here so that in case all ingredients are not available , wont mess up inventory then
            for bev_name in remove_quantities_from_inventory:
                bev_quantity = remove_quantities_from_inventory[bev_name]
                self.ingredient_vs_quantity[bev_name] -= bev_quantity

            print("{} is prepared".format(beverage_name))

        return status
