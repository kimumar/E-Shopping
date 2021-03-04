from django.contrib import admin

# Register your models here.
from . models import Category, Product, Images

class CategoryAdmin(admin.ModelAdmin):
    list_display= ['id','title', 'parent','status','image' ]
    list_filter= ['status']
    prepopulated_fields = {'slug': ('title',)}


class ProductImageInline(admin.TabularInline):
    model= Images
    extra = 2

class ProductAdmin(admin.ModelAdmin):
    list_display= ['id','title', 'category','status','image',
                     'available','brand', 'code', 'points', 'banner', 'slug', 'bestseller',
                        'topseller', 'trending', 'featured', 'new', 'latest']
    list_filter= ['category']
    list_display_links = ('title', 'category','status','image')
    readonly_fields= ('image_tag',)
    inlines= [ProductImageInline]
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['bestseller', 'topseller', 'trending', 'featured', 'new', 'latest']






admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images)