from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Car, User, Part

admin.site.register(Part)



class UserAdmin(BaseUserAdmin):
    ordering=["id"]
    list_display = ['email','role']
    fieldsets = (
        (None, {"fields": ("email", "password","role")}),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser")}
        ),
        ("Important dates", {"fields": ("last_login",)})
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2","role")
        }),
    )


class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'car_model', 'is_repaired', 'is_finished']
    list_editable = ['is_repaired', 'is_finished']
    actions = ['enable_is_repaired', 'disable_is_repaired',
               'enable_is_finished', 'disable_is_finished']

    def enable_is_repaired(self, request, queryset):
        for qs in queryset:
            qs.is_repaired = True
            qs.save()

    def disable_is_repaired(self, request, queryset):
        for qs in queryset:
            qs.is_repaired = False
            qs.save()

    def enable_is_finished(self, request, queryset):
        for qs in queryset:
            qs.is_finished = True
            qs.save()

    def disable_is_finished(self, request, queryset):
        for qs in queryset:
            qs.is_finished = False
            qs.is_repaired = False
            qs.save()


admin.site.register(Car, CarAdmin)
admin.site.register(User, UserAdmin)

