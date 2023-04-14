from rest_framework.authentication import TokenAuthentication as BaseTokenAuth

# importing the token
from rest_framework.authtoken.models import Token


class TokenAuthentication(BaseTokenAuth) : 
    keyword = 'Bearer'