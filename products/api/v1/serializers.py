from rest_framework.serializers import  Serializer ,  ModelSerializer
from products.models import LaptopProduct , UserAdmin , Cpu , Ram, Gpu

class LaptopProductSerializers(ModelSerializer):
    class Meta:
        model= LaptopProduct
        exclude=['create_time','update_time'] 

class CpuSerializer(ModelSerializer):
    class Meta:
        model=Cpu
        fields='__all__'

class RamSerializer(ModelSerializer):
    ram_laptops=LaptopProductSerializers(read_only=True,many=True)
    class Meta:
        model=Ram
        fields='__all__'

class GpuSerializer(ModelSerializer):
    gpu_laptops=LaptopProductSerializers(read_only=True,many=True)
    class Meta:
        model=Gpu
        fields='__all__'

class AdminSerializer(ModelSerializer):
    user_admin_laptops=LaptopProductSerializers(read_only=True,many=True)
    class Meta:
        model=UserAdmin
        fields='__all__'

