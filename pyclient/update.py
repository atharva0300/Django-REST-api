import requests

endpoint = "http://127.0.0.1:8001/api/products/1/update/"

data = {
    'title' : 'Hello Friend',
    'price' : 123.12
}

get_response = requests.put(endpoint , json = data)    # emulate a http get request
# using put method


print()
#print(get_response.text)
print(get_response.json())

# sending json data 
# requests.get(endpoint , json = {'query' : 'Something does here'})
# we pass json data to also receive json data 

# status code 
print(get_response.status_code)