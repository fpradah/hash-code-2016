class Order:

# Order contenedora de los products
    def __init__(self,deliver) :
        self.products = []
        self.deliver = deliver

# Lista de products
    def getProducts(self) :
        return self.products

    def setProducts(self,products) :
        self.products = products

# Agregamos un product a la orden
    def addProduct(self,product) :
        self.products.append(product)

# Deliver (Cliente al que entregamos)
    def getDeliver(self) :
        return self.deliver

    def setDeliver(self,deliver) :
        self.deliver = deliver
