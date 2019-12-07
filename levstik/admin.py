from django.contrib import admin
from levstik.models import Winner


@admin.register(Winner)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'description', 'birth_date')
    # list_filter = ('confirmed', 'canceled', 'created', 'updated')
    # raw_id_fields = ('provider', 'customer', 'review')
    readonly_fields = ('created', 'updated')
    search_fields = ('first_name', 'last_name')

