from django.contrib import admin

from . models import Setting, ContactMessage, Client, Slider
# Register your models here.

class SettingAdmin(admin.ModelAdmin):
     list_display=('id', 'title', 'company','status','icon','logo')


class ClientAdmin(admin.ModelAdmin):
     list_display= ['id','title','clients']
     
class SliderAdmin(admin.ModelAdmin):
     list_display= ['id','title','slide','slides']

class ContactMessageAdmin(admin.ModelAdmin):
    list_display=('name','email', 'subject','message','status', 'note','updated_at')
    readonly_fields = ('name', 'subject','email', 'message', 'ip')
    list_filter= ['status']
    list_display_links = ('status','name','note')
    search_fields = ('name','email', 'subject','message','status', 'note','updated_at')
    list_per_page = 25

    
admin.site.register(Setting, SettingAdmin) 
admin.site.register(Client, ClientAdmin)  
admin.site.register(Slider,SliderAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
    
   
