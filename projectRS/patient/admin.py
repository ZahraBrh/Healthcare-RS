from django.contrib import admin
from .models import Patient,SideEffect,ListDrug,ListCondition,ListSideEffect,Review,Wilaya

# Register your models here.
admin.site.register(Patient)
admin.site.register(SideEffect)
admin.site.register(ListCondition)
admin.site.register(ListDrug)
admin.site.register(ListSideEffect)
admin.site.register(Review)
admin.site.register(Wilaya)