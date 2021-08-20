from django.contrib import admin
from . models import Cards,Category,AddNewCode
# Register your models here.
admin.site.register(Category)
admin.site.register(Cards)
admin.site.register(AddNewCode)