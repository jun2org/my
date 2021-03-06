from django.contrib import admin

from apps.domains.library.book.models import LibraryBook
from lib.base.admin import BaseModelAdmin


class LibraryBookAdmin(BaseModelAdmin):
    fieldsets = (
        (None, {'fields': ('id', 'user',)}),
        ('소유 정보', {'fields': ('own_status', 'own_date',)}),
        ('소유 정보', {'fields': ('read_status', 'read_date',)}),
        ('Related dates', {'fields': ('created', 'last_modified',)}),
    )
    readonly_fields = ('id', 'user', 'book', 'created', 'last_modified',)
    list_display = (
        'user', 'book', 'own_status', 'own_date', 'read_status', 'read_date', 'last_modified',
    )
    search_fields = ('book', 'user',)


admin.site.register(LibraryBook, LibraryBookAdmin)
