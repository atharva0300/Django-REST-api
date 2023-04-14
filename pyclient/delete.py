import requests



product_id = input("What is the product id : ")

endpoint = f"http://127.0.0.1:8001/api/products/{product_id}/destroy/"

try : 
    product_id = int(product_id)
except : 
    product_id = None
    print("Product id is not valid")



get_response = requests.delete(endpoint)    # emulate a http get request
# using delete method


print()
#print(get_response.text)
print(get_response.status_code , get_response.status_code==204)
