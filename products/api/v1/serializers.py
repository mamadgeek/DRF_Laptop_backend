from rest_framework.serializers import  Serializer ,  ModelSerializer , ValidationError
from products.models import LaptopProduct , UserAdmin , Cpu , Ram, Gpu

class LaptopProductSerializers(ModelSerializer):
    class Meta:
        model= LaptopProduct
        exclude=['create_time','update_time']

    def validate_brand(self,brand):
        # if attrs.brand == 'AMD' and attrs.cpu=='core':            
        #     return 'not true' 
        if brand == 'asus':
            raise ValidationError('fuck asus') #{ # "brand": [ "fuck asus"# ],# "model": ["This field is required." # ],
        return brand
    
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

