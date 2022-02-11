from django.contrib import admin

from .models import Employee, Store, Visit


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Employee, EmployeeAdmin)


class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'employee')
    list_display_links = ('id', 'employee')
    search_fields = ('name',)


admin.site.register(Store, StoreAdmin)


class VisitAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    fields = ('date', 'store', 'latitude', 'longitude')
    list_display = ('id', 'date', 'store', 'latitude', 'longitude', )
    list_display_links = ('id', 'date')
    search_fields = ['store__name', 'store__employee__name']


admin.site.register(Visit, VisitAdmin)