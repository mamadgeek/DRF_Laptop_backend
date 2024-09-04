from rest_framework.response import  Response
from rest_framework.decorators import api_view
from rest_framework.request import Request
from products.models import LaptopProduct , UserAdmin , Cpu,Ram,Gpu 
from .serializers import LaptopProductSerializers , CpuSerializer,RamSerializer, GpuSerializer,AdminSerializer
from rest_framework import status
# showing laptops here 
from django.db.models import  Q ,  F , Avg , Sum , Count
from rest_framework.permissions import  BasePermission
from rest_framework.views import APIView
from rest_framework import generics , mixins
from rest_framework import viewsets
from general_class_functions.drf_functions import query_parametrs_filtering_generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# همه را نشون بده 
# فیللتر کنه 
# دستکاری بشه  و بوجود بیاد
# خرید بشه و از دیتا بیس کم بشه
# به درگاه وصل بشه
# هرچیزی که برای یه فروشگاه بک اند کار میفرسته به فرانت  یا  ادمین ها اضافه میکنن و دستکاری میکنن
# مقایسه بشن باهم 
# بازه ها چگونه باید تعریف بشن برای نمونه بازه زمانی یا بازه پولی یا ... که فرانت بازه بده و ما فیلتر کنیم
# https://www.digikala.com/search/category-all-in-pc/?has_selling_stock=1&price%5Bmax%5D=818236519&price%5Bmin%5D=290221160&sort=7
# چطور تغیرات را برای ما نشون نمیده ولی برای دسترسی دارها نشون میده


class CpuView(generics.ListAPIView):
    queryset=Cpu.objects.filter()
    serializer_class=CpuSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]


class RamView(generics.ListAPIView):
    queryset=Ram.objects.filter()
    serializer_class=RamSerializer


class GpuView(generics.ListAPIView):
    queryset=Gpu.objects.filter()
    serializer_class=GpuSerializer
    # pagination_class = PageNumberPagination  # This line ensures the use of the specified pagination class
    def paginate_queryset(self, queryset):
        return super().paginate_queryset(queryset)
    

class UsersView(generics.ListAPIView):
    queryset=UserAdmin.objects.filter()
    serializer_class=AdminSerializer



# see the details manupulate them by admin or responsibeler 

# seeling in database

# viewsets-router

class Laptpsviewset(viewsets.ModelViewSet):
    queryset=LaptopProduct.objects.filter()
    serializer_class = LaptopProductSerializers
    # pagination_class = PageNumberPagination  # This pagination class will be applied to the filtered results. first filters and the pagination http://127.0.0.1:8000/laptops/?brand=Generic&page=2
    
    def get_queryset(self): 
        # filter by querparameters due to exclude this bellow list
        exclude_fields={'id','update_time','create_time','images','description'}
        query_fields = [field.name for field in LaptopProduct._meta.get_fields()
                         if field.name not in exclude_fields]
        queryset =query_parametrs_filtering_generics(self,query_fields,LaptopProduct) 
        return queryset 
    


    

# # generic api view
# class showing_laptops(generics.ListCreateAPIView):
#     # queryset=LaptopProduct.objects.filter() # if witout get_queryset it is needed 
#     serializer_class=LaptopProductSerializers 
#     def get_queryset(self): 
#         # filter by querparameters due to exclude this bellow list
#         exclude_fields={'id','update_time','create_time','images','description'}
#         query_fields = [field.name for field in LaptopProduct._meta.get_fields()
#                          if field.name not in exclude_fields]
#         return query_parametrs_filtering_generics(self,query_fields,LaptopProduct)



# class laptop_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=LaptopProduct.objects.filter()
#     serializer_class=LaptopProductSerializers






# mixins
# class showing_laptops(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=LaptopProduct.objects.filter()  
#     serializer_class = LaptopProductSerializers
#     def get_queryset(self): 
#         # filter by querparameters due to 
#         exclude_fields={'id','update_time','create_time','images','description'}
#         query_fields = [field.name for field in LaptopProduct._meta.get_fields() if field.name not in exclude_fields] # cpu ram ..
#         filtering=Q() 
#         for field in query_fields: 
#             value = self.request.query_params.get(field)  # self.request is the diffrence from @ and apiview #y700 #lenovo
#             if value:  
#                 filtering &=(Q(**{field:value})) #(AND: ('brand', 'lenovo'), ('model', 'y700'))
#         return  LaptopProduct.objects.filter(filtering)
    
#     def get(self,request:Request):
#         return self.list(request)

#     def post(self,request:Request):
#         return self.create(request)


# class laptop_detail(mixins.RetrieveModelMixin,
#                     mixins.CreateModelMixin,
#                     mixins.DestroyModelMixin ,
#                     mixins.UpdateModelMixin,
#                     generics.GenericAPIView
#                      ): 
    
#     queryset=LaptopProduct.objects.filter()
#     serializer_class=LaptopProductSerializers

#     def get(self,request:Request,pk:int):
#         return self.retrieve(request,pk)

#     def put(self,request:Request,pk:int):
#         return self.update(request,pk)
    

#     def delete(self,request:Request,pk:int):
#         return self.destroy(request,pk)











# from drf_spectacular.utils import extend_schema
# # apiview
# class showing_laptops(APIView):
#     @extend_schema(
#     request=LaptopProductSerializers,
#     responses={200: LaptopProductSerializers},
#     )
#     def get(self, request:Request):
#         exclude_fields=['id','update_time','create_time','images','description']
#         query_fields = [field.name for field in LaptopProduct._meta.get_fields() if field.name not in exclude_fields]
#         filtering=Q() 
#         for field in query_fields: 
#             value = request.query_params.get(field)  #y700 #lenovo
#             if value:  
#                 filtering &=(Q(**{field:value})) #(AND: ('brand', 'lenovo'), ('model', 'y700'))
#         laptops=LaptopProduct.objects.filter(filtering)  
#         serialized_laptops=LaptopProductSerializers(laptops,many=True)
#         return Response(serialized_laptops.data,status=status.HTTP_200_OK)
#     def post(self,request:Request):
#         serialized=LaptopProductSerializers(data=request.data)
#         if serialized.is_valid():
#             serialized.save() 
#             return Response(serialized.data,status=status.HTTP_201_CREATED)
#         return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)


# class laptop_detail(APIView):
#     def get_obj(self,the_id:int):
#         try:    
#             laptop_detail=LaptopProduct.objects.get(id=the_id)
#             return laptop_detail
#         except LaptopProduct.DoesNotExist:
#             return Response(None,status=status.HTTP_204_NO_CONTENT)
        
#     def get(self,request:Request,the_id:int):
#         laptop_detail=self.get_obj(the_id=the_id)
#         serialized=LaptopProductSerializers(laptop_detail)
#         return Response(serialized.data,status=status.HTTP_200_OK)

#     def put(self,request:Request,the_id:int):
#         laptop_detail=self.get_obj(the_id=the_id) 
#         serialized=LaptopProductSerializers(laptop_detail,request.data)
#         if serialized.is_valid():
#             serialized.save()
#             print('accepted update')
#             return Response (serialized.data,status=status.HTTP_202_ACCEPTED)
#         return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    

#     def delete (self,request:Request,the_id:int):
#         laptop_detail=self.get_obj(the_id=the_id) 
#         laptop_detail.delete()
#         return Response(f"{laptop_detail.id} is deleted",status=status.HTTP_204_NO_CONTENT)
    




#function base
# # filter only some query parameters which is not in the below list 
# @api_view(['GET','POST'])
# def showing_laptops(request: Request):
#     print(request.method)
#     if request.method== 'GET': 
#         # this filtering is only for filtering on query params not showing
#         exclude_fields=['id','update_time','create_time','images','description']
#         query_fields = [field.name for field in LaptopProduct._meta.get_fields() if field.name not in exclude_fields]
#         filtering=Q() 
#         for field in query_fields: 
#             value = request.query_params.get(field)  #y700 #lenovo
#             if value:  
#                 filtering &=(Q(**{field:value})) #(AND: ('brand', 'lenovo'), ('model', 'y700'))
#         laptops=LaptopProduct.objects.filter(filtering)  
#         serialized_laptops=LaptopProductSerializers(laptops,many=True)
#         return Response(serialized_laptops.data,status=status.HTTP_200_OK)
    
#     elif request.method =='POST':
#         serializer=LaptopProductSerializers(data=request.data)
#         if serializer.is_valid():  
#             serializer.save() 
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        



# {
#     "brand": "asus",
#     "model": "gl 552",
#     "series": "g",
#     "cpu": "core i 7 5400h",
#     "ram": "64",
#     "price": "27000000",
#     "images": "",
#     "usage": "general",
#     "description": ""
# }



# @api_view(['GET','PUT','DELETE'])
# def laptop_detail(request: Request ,the_id:int ):
#     try:    
#         laptop_detail=LaptopProduct.objects.get(id=the_id)
#     except LaptopProduct.DoesNotExist:
#         return Response(None,status=status.HTTP_204_NO_CONTENT)
    
#     if request.method == 'GET':
#         serialized=LaptopProductSerializers(laptop_detail)
#         return Response(serialized.data,status=status.HTTP_200_OK)
    
#     elif request.method == 'PUT':
#         serialized=LaptopProductSerializers(laptop_detail,request.data)
#         if serialized.is_valid():
#             serialized.save()
#             print('accepted update')
#             return Response (serialized.data,status=status.HTTP_202_ACCEPTED)
#         return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         laptop_detail.delete()
#         return Response('delete ok',status=status.HTTP_204_NO_CONTENT)
    






# @api_view(['GET'])
# def showing_laptops(request: Request):
#     exclude_fields=['id','update_time','create_time','images','description']
#     query_fields = [field.name for field in LaptopProduct._meta.get_fields() if field.name not in exclude_fields]

#     the_brand = request.query_params.get('brand')  #lenovo
#     print(the_brand)

#     laptops=LaptopProduct.objects.filter()
#     if the_brand :
#         laptops=laptops.filter(brand=the_brand)
#     serialized_laptops=LaptopProductSerializers(laptops,many=True)
#     return Response(serialized_laptops.data,status=status.HTTP_200_OK)












