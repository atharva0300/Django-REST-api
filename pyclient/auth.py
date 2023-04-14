import requests
from getpass import getpass


endpoint = "http://127.0.0.1:8001/api/auth/"

# getting the username  
username = input("What is your username : ")

password =getpass("What is the password : ")

# the response of the authentication of the token 
auth_response = requests.post(endpoint , json = {'username' : username , 'password' : password})    # emulate a http get request
# using post method

if auth_response.status_code==200 : 


    print()
    #print(get_response.text)
    print(auth_response.json())

    # sending json data 
    # requests.get(endpoint , json = {'query' : 'Something does here'})
    # we pass json data to also receive json data 

    # status code 
    print(auth_response.status_code)

    # success, then
    token = auth_response.json()['token']
    # obtaining the token from the auth_response json object


    headers = {
        'Authorization' : f"Bearer {token}"
    }
    # passing the token to the headers
    # with this auth token we will perform the list operation

    endpoint = "http://127.0.0.1:8001/api/products/"

    get_response = requests.get(endpoint, headers=headers)
    # providing the modified headers which contains the auth token in the get request 


    print(get_response.json())


else : 
    print()
    #print(get_response.text)
    print(auth_response.json())

    # sending json data 
    # requests.get(endpoint , json = {'query' : 'Something does here'})
    # we pass json data to also receive json data 

    # status code 
    print(auth_response.status_code)

