class Task:

# Task, suborder con posicion a entregar y tipo de product

    def __init__(self,position,type_product) :
        self.position = position
        self.type_product = type_product

    def getPosition(self) :
        return self.position

    def setPosition(self,position) :
        self.position = position

    def setTypeProduct(self,type_product) :
        self.type_product = type_product

    def getTypeProduct(self) :
        return self.type_product
