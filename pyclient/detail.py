import requests 

# creating a new endpoint for the api app
endpoint = "http://127.0.0.1:8000/api/products/1/"

get_response = requests.get(endpoint , params = {"product_id" : 123})
# the params is equivalent to -> http://127.0.0.1:8000/api/?abc=123

# the get method and the post method requests can also be sent using 
# requests.post() and requests.get() 



print(get_response.json())
# this will give a json object which will have the message