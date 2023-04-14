# importing the custom permissions 
from .permissions import IsStaffEditorPermission

# importing DRF permissions 
from rest_framework import permissions

class StaffEditorPermissionMixin() : 
    permission_classes = [permissions.IsAdminUser , IsStaffEditorPermission]
    # adding the IsAdminUser permission and Custom made staff editor permission to the permission classes 
    # this mixin will be imported in the views.py of products 
    # and pass this to the parameters list of the classes in the views ( Class views )



