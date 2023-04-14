import requests

endpoint = "http://127.0.0.1:8001/api/products/1/"

get_response = requests.get(endpoint , params = {"abc" : 123} , json = {"name" : "Atharva"})    # emulate a http get request
# using get method


print()
#print(get_response.text)
print(get_response.json())

# sending json data 
# requests.get(endpoint , json = {'query' : 'Something does here'})
# we pass json data to also receive json data 

# status code 
print(get_response.status_code)