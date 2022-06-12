from rest_framework.permissions import IsAuthenticated


class IsAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) \
               and request.user.role == 'admin'


class IsReception(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view)\
               and request.user.role == 'reception'


class IsTechnician(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view)\
               and request.user.role == 'technician'


class IsInspector(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) \
               and request.user.role == 'inspector'
