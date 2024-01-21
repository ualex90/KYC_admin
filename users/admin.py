from django.contrib import admin

from users.models import User


@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'surname', 'date_joined', 'last_login', 'is_active', 'is_superuser')
    # поиск
    search_fields = ('email', 'first_name', 'last_name', 'surname')
    list_filter = ('is_active', 'is_superuser', 'is_staff')
