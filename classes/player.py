class Player:
    def __init__(self, base_inventory):
        # Theses values are all place holders

        self.inventory = base_inventory

    def add_item(self, item):
        self.inventory.append(item)


player1 = Player([])
player1.add_item("Wooden Sword")
print(player1.inventory)
