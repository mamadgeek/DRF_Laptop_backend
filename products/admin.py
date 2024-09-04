from django.contrib import admin

# Register your models here.
from .models import LaptopProduct ,Cpu,Gpu,Ram

@admin.register(LaptopProduct)
class LaptopProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Cpu)
class CpuAdmin(admin.ModelAdmin):
    pass


@admin.register(Gpu)
class GpuAdmin(admin.ModelAdmin):
    pass

@admin.register(Ram)
class RamAdmin(admin.ModelAdmin):
    pass