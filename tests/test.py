def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"]
    
    print("total",total)
    return total

# funcion de pruebas

def test_calculate_total_with_empty_list():
    # con assert debe dar verdadera la prueba
    # paso la lista vacia a la funcion
  
    assert calculate_total([]) == 0

def test_calculate_total_with_single_product():
    products =[
        {
            "name": "Notebook", "price":5
        }
    ]
    assert calculate_total(products) == 5

def test_calculate_total_with_multiple_prodcut():
    products =[
        {
            "name": "Notebook", "price":5
        },
        {
            "name": "Server ", "price":10
        },
        {
            "name": "Notebook 2", "price":5
        }
    ]
    assert calculate_total(products) == 20

if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_prodcut()

