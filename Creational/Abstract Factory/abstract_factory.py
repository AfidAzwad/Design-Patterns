class Chair:
    def sit_on(self):
        pass

class Table:
    def place_item(self):
        pass

class Sofa:
    def lie_on(self):
        pass

#Concrete Products
class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on a Victorian Chair"

class VictorianTable(Table):
    def place_item(self):
        return "Placing an item on a Victorian Table"

class VictorianSofa(Sofa):
    def lie_on(self):
        return "Lie on a Victorian Sofa"

class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a Modern Chair"

class ModernTable(Table):
    def place_item(self):
        return "Placing an item on a Modern Table"

class ModernSofa(Sofa):
    def lie_on(self):
        return "Lie on a Modern Sofa"

# Abstract Factory Interface
class FurnitureFactory:
    def create_chair(self):
        pass

    def create_table(self):
        pass

    def create_sofa(self):
        pass

# Concrete Factory for Victorian Furniture
class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return VictorianChair()

    def create_table(self):
        return VictorianTable()

    def create_sofa(self):
        return VictorianSofa()

# Concrete Factory for Modern Furniture
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_table(self):
        return ModernTable()

    def create_sofa(self):
        return ModernSofa()

# Client Code
def create_furniture(factory: FurnitureFactory):
    chair = factory.create_chair()
    table = factory.create_table()
    sofa = factory.create_sofa()

    print(chair.sit_on())
    print(table.place_item())
    print(sofa.lie_on())


victoria_factory = VictorianFurnitureFactory()
create_furniture(victoria_factory)

