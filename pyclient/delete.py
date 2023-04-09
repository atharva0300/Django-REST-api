import requests 

product_id = input("What is the product id that you want to use? : ")
try : 
    product_id = int(product_id)

except : 
    product_id = None
    print("Product ID is not valid")



# creating a new endpoint for the api app
endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"

data = {
    'title' : 'Field is done',
    'price' : 00
}

get_response = requests.delete(endpoint , json = data)
# the params is equivalent to -> http://127.0.0.1:8000/api/?abc=123
# we use the delete method to delete the value 

# the get method and the post method requests can also be sent using 
# requests.post() and requests.get() 


 
#print(get_response.json())
# this will give a json object which will have the message

print(get_response.status_code , get_response.status_code == 204)
# 204 status code if the deletion is successful
