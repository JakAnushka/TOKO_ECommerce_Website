from django.contrib import admin
from TOKO_Main.models import Contact,Product,Order,OrderItem

class OrderItemTubleinline(admin.TabularInline):
    model = OrderItem
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTubleinline]



# Register your models here.
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)

