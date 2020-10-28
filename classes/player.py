class Player:
    def __init__(self):
        # Theses values are all place holders

        self.inventory = []

    def add_item(self, inventory):
        self.inventory.append(inventory)


player1 = Player()
player1.add_item("Wooden Sword")
print(player1.inventory)
