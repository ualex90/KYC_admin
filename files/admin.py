from django.contrib import admin

from base.servises import get_token
from files.models import File, StatusFile
from files.servises import change_status


@admin.action(description="Принять")
def make_accepted(modeladmin, request, queryset):
    queryset.update(status=StatusFile.ACCEPTED)
    change_status(queryset, StatusFile.ACCEPTED)


@admin.action(description="Отклонить")
def make_rejected(modeladmin, request, queryset):
    queryset.update(status=StatusFile.REJECTED)
    change_status(queryset, StatusFile.REJECTED)


@admin.action(description="На проверке")
def make_under_review(modeladmin, request, queryset):
    queryset.update(status=StatusFile.UNDER_REVIEW)
    change_status(queryset, StatusFile.UNDER_REVIEW)


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'size', 'filename', 'is_public', 'status', 'owner', )
    list_display_links = None
    search_fields = ('owner', 'name', )
    list_filter = ('is_public', 'status', )
    actions = (make_accepted, make_rejected, make_under_review, )
