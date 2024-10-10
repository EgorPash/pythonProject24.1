from rest_framework.permissions import BasePermission

class IsModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Модераторы').exists()

class IsOwner(BasePermission):
    """
    Allows access only to the owner of the object.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user  # Предполагается, что поле 'owner' добавлено в модели