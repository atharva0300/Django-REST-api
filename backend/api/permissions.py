from rest_framework import permissions
# importing the permissions library from the rest_framework

# creating a custom permissions over here


class IsStaffEditorPermission(permissions.DjangoModelPermissions) :

    perms_map = {
    'GET': ['%(app_label)s.view_%(model_name)s'],
    'OPTIONS': [],
    'HEAD': [],
    'POST': ['%(app_label)s.add_%(model_name)s'],
    'PUT': ['%(app_label)s.change_%(model_name)s'],
    'PATCH': ['%(app_label)s.change_%(model_name)s'],
    'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


    """
    def has_permssion(self , request , view) : 
        if not request.user.is_staff :
            return False    
        return super().has_permission(request , view)
    
        
    """

    
    """

    def has_permission(self, request, view):
        user = request.user
        if request.user.is_staff : 
            # if the user is staff , then 
            if user.has_perm('products.view_product') : 
                return True

            if user.has_perm('products.change_product') : 
                return True
            
            if user.has_perm('products.add_product') : 
                return True
            
            if user.has_perm('products.delete_product') : 
                return True
            
            return False
        
        # printing the user permissions 
        print(user.get_all_permissions())
        return False
    
    """
    
    """ 
    
    def has_object_permission(self, request, view, obj):
    
        return obj.owner==request.user
    
    """