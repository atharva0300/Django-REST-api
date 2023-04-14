from rest_framework import permissions

# creating custom permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions) : 
    perms_map = {
        'GET' : ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS' : [],
        'HEAD' : [],
        'POST' : ['%(app_label)s.add_%(model_name)s'],
        'PUT' : ['%(app_label)s.change_%(model_name)s'],
        'PATCH' : ['%(app_label)s.change_%(model_name)s'],
        'DELETE' : ['%(app_label)s.change_%(model_name)s'],

    }


    def has_permission(self , request , view) :
        user = request.user
        if request.user.is_staff : 
            if user.has_perm("products.add_product") : # "app_name.verb_model_name"
                return True
            
            if user.has_perm("products.delete_product") : 
                return True
            
            if user.has_perm("products.change_product") : 
                return True
            
            if user.has_perm("products.view_product") : 
                return True
            

            return False 
        
        print(user.get_all_permissions())
        return False 
    
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user