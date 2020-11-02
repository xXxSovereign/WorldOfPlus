class Player:
    def __init__(self, base_inventory, base_equipped):
        # Theses values are all place holders

        self.inventory = base_inventory
        self.equipped = base_equipped

    def add_item(self, item):
        self.inventory.append(item)

    def equip_item(self, equipped_item):
        if equipped_item in self.inventory:
            self.equipped.append(equipped_item)
            self.inventory.remove(equipped_item)


# This stuff is for testing purposes
player1 = Player([], [])
player1.add_item("Wooden Sword")
player1.equip_item("Wooden Sword")
print(player1.inventory)
print(player1.equipped)
