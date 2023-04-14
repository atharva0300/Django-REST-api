import requests

endpoint = "http://127.0.0.1:8001/api/"

# post request to the api_view 
# and retrning back the serializer data
get_response = requests.post(endpoint , params = {"abc" : 123} , data = {'title' : 'This is Atharva'})    # emulate a http get request
# using post method


print()
#print(get_response.text)
print(get_response.json())

# sending json data 
# requests.get(endpoint , json = {'query' : 'Something does here'})
# we pass json data to also receive json data 

# status code 
print(get_response.status_code)

get_response = requests.post(endpoint , params = {"abc" : 123} , data = {'someothertitle' : 'This is Atharva'})    # emulate a http get request

print()
#print(get_response.text)
print(get_response.json())

# sending json data 
# requests.get(endpoint , json = {'query' : 'Something does here'})
# we pass json data to also receive json data 

# status code 
print(get_response.status_code)