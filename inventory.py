class Inventory:
    ingredient_vs_quantity = dict()

    def __init__(self, all_ingredients):
        # Why this check
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
        # Again this check seems weird
        if not self.is_inventory_initialized():
            print("Initialize inventory ... ")
            return False

        status = True

        beverage_name = beverage.get_beverage_name()
        # DOn't use ds name in the variable name. Bad practice
        beverage_ingredients_dict = beverage.get_beverage_ingredients()
        remove_quantities_from_inventory = dict()
        for beverage_ingredient in beverage_ingredients_dict:
            quantity_needed_for_bvg = beverage_ingredients_dict.get(beverage_ingredient, -1) # Incredients should not be None atal. If it is, I think just raise an Error.
            # Also raise an error if it is 0. Also I think this check can be part of the initialization process for CoffeeMaker

            quantity_needed_for_bvg = beverage.get_ingredient_quantity(beverage_ingredient)
            quantity_in_inventory = self.get_quantity_in_inventory(beverage_ingredient)

            # Why would this be ever None. Don't check for continue statement.
            if quantity_needed_for_bvg is None or quantity_needed_for_bvg == -1:
                # in case inventory has gone dry for a certain ingridient or
                # beverage does not the specific ingredient .ie. None
                continue

            # First check doesn't make sense
            if quantity_in_inventory != -1 and quantity_in_inventory >= quantity_needed_for_bvg:
                # self.ingredient_names[beverage_ingredient] -= quantity_needed_for_bvg
                remove_quantities_from_inventory[beverage_ingredient] = quantity_needed_for_bvg
            # Also I think it is a good idea to create public APIs for making all these checks and should be done in the beverage Class.
            # If you do that then I think You won't even need all these braek statements
            elif quantity_in_inventory != -1 and quantity_in_inventory < quantity_needed_for_bvg:
                print("{} cannot be prepared, {} is not sufficient".format(beverage_name, beverage_ingredient))
                status = False
                break
            elif quantity_in_inventory == -1:
                print("{} cannot be prepared, {} is finished".format(beverage_name, beverage_ingredient))
                status = False
                break

        # This looks good as this is something like Transaction. If we use a DB for inventory then we could have had a txn commit here.
        if status:
            # removing here so that in case all ingredients are not available , wont mess up inventory then
            for bev_name in remove_quantities_from_inventory:
                bev_quantity = remove_quantities_from_inventory[bev_name]
                self.ingredient_vs_quantity[bev_name] -= bev_quantity
            # Inventory class should not care about if the drink is made or not
            print("{} is prepared".format(beverage_name))

        return status
