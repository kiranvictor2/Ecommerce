from django.contrib import admin

from .models import Userper, datarow, datas, person, person1,cart

# Register your models here.
admin.site.register(person)
admin.site.register(person1)
admin.site.register(datas)
admin.site.register(Userper)
admin.site.register(datarow)
admin.site.register(cart)