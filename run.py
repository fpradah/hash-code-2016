import sys
import Product
import Order
import Task

def cargaMercancia(drone) :
    # Recorremos la lista de todos las orders"""
    for order in orders:
        products = order.getProducts()
        # Recorremos todos los products de la order
        for product in products:
            if drone.addProduct(product) is False :
                return False
            else :
                type_product = product.getTypeId()
                deliver = order.getDeliver()
                position = deliver.getPosition()
                task = Task.Task(position,type_product)
                drone.addTask(task)
    return True

# Cargamos todos los drones
for drone in drones :
    ordenes_completas = cargaMercancia(drone)
    products = []
    drone.setProducts(products)
    if ordenes_completas is True :
        break

# Repartir mercancia
