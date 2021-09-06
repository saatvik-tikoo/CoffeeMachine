from inventory import Inventory
from beverage import Beverage


class CoffeeMachine:
    # request_q = list() # can be used to queue up pending reuqests

    inventory = Inventory(None)  # static inventory manager object variable
    machine_in_use = 0  # static variable to keep track of num of coffee machines in use concurrently

    def __init__(self, num_of_machines):
        self.total_num_of_machines = num_of_machines

    def initialize_inventory(self, ingredients):
        self.inventory = Inventory(ingredients)

    def make_beverage(self, beverage_name, beverage_ingredients):
        """
        method to call inventory object and update if all beverage ingredients are present
        """
        beverage = Beverage(beverage_name, beverage_ingredients)
        # I think the bevarage should be called only if all the ingredients are available evr fail here it self.
        # I think beverage should depend on the inventory and should internally call thsi function
        status = self.inventory.check_and_update(beverage)
        return status

    def request_beverage(self, bvg_name, bvg_ingredients_data):
        """
        method to check if the passed beverage name is present in inventory
        and if its ingredients are present in necessary quantity
        """
        was_beverage_made = False
        # Why this first check. I think these checks should not be done as it should be a part of contract between the coffeeMaker and the Client

        # Idaelly if you have a separate Client that would have taken care of the number of machines in use. Also if Our CoffeeMaker is taking care of this,
        # We should not even reach this places just to fail everything. That should have happend initially in the main file itself, where we chack the sanity
        if isinstance(bvg_ingredients_data, dict) and self.machine_in_use <= self.total_num_of_machines:
            self.machine_in_use += 1
            was_beverage_made = self.make_beverage(bvg_name, bvg_ingredients_data)
            self.machine_in_use -= 1
        else:
            print("Request cannot be processed yet")
        return was_beverage_made
