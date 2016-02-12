class Product:

    def __init__(self,type_id,weight):
        self.type_id = type_id
        self.max_weight = weight

    def getTypeId(self):
        return self.type_id

    def setTypeId(self,type_id):
        self.type_id = type_id

    def getWeight(self):
        return self.weight

    def setWeight(self,weight):
        self.weight = weight
