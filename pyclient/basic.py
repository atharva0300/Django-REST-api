import requests
# importing requests library to deal with API requests 

endpoint = "https://www.google.com/"
# an endpoint is a url which makes a request to the remote server 
# the endpoint will return something -> either a source ( html document ), a api response etc 
# this is not an api endpoint at all

endpoint = "https://httpbin.org/anything"
# this is an api endpoint because it returns a json object and not a html page 
# this endpoint will echo back anything which i send to it


# API -> application programming interface 
# requests.get()  # this uses an api 
# REST API -> a web api 

# the api uses HTTP request. The python request does the http request for us

# new endpoint for django
endpoint = "http://127.0.0.1:8001/api/"

get_response = requests.get(endpoint , params = {"abc" : 123} , json = {"name" : "Atharva"})    # emulate a http get request
# passing the params to the api endpoint

#print(get_response.text)    # displaying the body of the response ( the text )

# HTTP request -> returns a http document 
# REST API ->  returns json object 
# JSON -> javascript object notation
print()
#print(get_response.text)
print(get_response.json())

# sending json data 
# requests.get(endpoint , json = {'query' : 'Something does here'})
# we pass json data to also receive json data 

# status code 
print(get_response.status_code)