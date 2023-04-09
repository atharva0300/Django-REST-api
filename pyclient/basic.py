import requests 


# creating an endpoint for the API client 
endpoint = "https://httpbin.org/"
# this is a url  ( an endpoint )

# using the api in the requests library
# getting a get request 
# API -> application programming interface 
# using the file is a form of using an API 
# these are not hte REST api 

# a REST API is a web based API
# it will use an HTTP request
get_response = requests.get(endpoint)  # emulate a http GET request 

# a response will be received 
# print(get_response.text)   # print the raw test response
# printing the text attribute of the get_response

# A regular HTTP request will give -> html 
# A REST API request ( http ) request will give -> JSON 

# javascript object notatoin is quite similar ( but not the same ) as the Python Dictionary

print(get_response.text)


endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint)

print(get_response.json())

print()
print()


get_response = requests.get(endpoint , json = {'query' : 'Hello World'})
# sends the query to the endpoint 
# get's hte reponse of the endpoint 

print(get_response.json())

# getting the status code 
print(get_response.status_code)

# for a page that does not exists 
# the status code returned is 404 
get_response  = requests.get('https://a.com')
print(get_response.status_code)