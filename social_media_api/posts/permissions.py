from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
	def get_object_permission(self, request, view, obj):
		if request.user == obj.author
			return True
		else:
			return False