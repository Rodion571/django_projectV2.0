from django.contrib import admin
from .models import Category, Dish, Event, Chef, ChefCategory, Gallery, Contact, Reservation, FooterItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible', 'sort', 'created_at', 'updated_at')
    list_editable = ('is_visible', 'sort')
    list_filter = ('is_visible', 'created_at', 'updated_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'name', 'ingredients', 'price', 'weight', 'photo', 'is_visible', 'sort', 'category', 'updated_at')
    list_editable = ('name', 'ingredients', 'price', 'weight', 'photo', 'is_visible', 'sort', 'category')
    list_filter = ('is_visible', 'created_at', 'updated_at', 'category')
    date_hierarchy = 'created_at'

@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'title', 'sort', 'is_visible', 'description', 'photo', 'price','date_and_time' ,'created_at', 'updated_at')
    list_editable = ('title', 'sort', 'is_visible', 'description', 'photo', 'price', 'date_and_time')
    list_filter = ('is_visible',)
    date_hierarchy = 'created_at'

@admin.register(ChefCategory)
class ChefCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible', 'created_at', 'updated_at')
    list_editable =  ('is_visible', )
    list_filter = ('is_visible', )
    date_hierarchy = 'created_at'

@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ('created_at' ,'first_name', 'last_name', 'photo', 'chef_category', 'updated_at')
    list_editable = ('first_name', 'last_name', 'photo', 'chef_category')
    date_hierarchy = 'created_at'

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'is_visible', 'photo', 'position', 'updated_at')
    list_editable = ('is_visible', 'photo', 'position')
    list_filter = ('is_visible', 'position')
    date_hierarchy ='created_at'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('item_title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('item_title',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'date', 'time', 'people', 'is_processed', 'created_at', 'updated_at')
    list_editable = ('is_processed',)
    list_filter = ('is_processed', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'phone')
    date_hierarchy = 'created_at'

@admin.register(FooterItem)
class FooterItemAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'item_title', 'item_description', 'item_icon', 'item_slug', 'item_follow_link', 'item_follow_name', 'updated_at')
    list_editable = ('item_title', 'item_description', 'item_icon', 'item_slug', 'item_follow_link', 'item_follow_name')
    list_filter = ('created_at', 'updated_at', 'item_title', 'item_description')
    search_fields = ('item_title', 'item_description')
    date_hierarchy = 'created_at'