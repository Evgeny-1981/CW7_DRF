from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Регистрация пользователей в админке."""

    list_display = ("id", "email", "is_active", "password", "telegram_id", "avatar", "phone_number")
    list_filter = ("email",)
    search_fields = ("email",)
