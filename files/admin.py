from django.contrib import admin

from files.models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'size', 'filename', 'is_public', 'status', 'owner', )
    list_display_links = ('name', )
    search_fields = ('owner', 'name', )
    list_filter = ('is_public', 'status', )
    list_editable = ('status', )
