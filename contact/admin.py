from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'category', 'show', # Campos que aparecerão
    ordering = '-id', # Campo que a lista será automaticamente ordenada
    # list_filter = 'created_date', # Adiciona um filtro a lista
    search_fields = 'id', 'first_name', 'last_name', 'phone', 'category__name', # Campos que você pode pesquisar
    list_per_pages = 10 # Itens por página
    list_max_show_all = 50 # Máximo de itens por página
    list_editable = 'phone', 'show', # Itens editáveis da lista
    list_display_links = 'id', 'first_name' # Itens clicaveis da lista

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name', # Campos que aparecerão
    ordering = '-id', # Campo que a lista será automaticamente ordenada
    
    

    
