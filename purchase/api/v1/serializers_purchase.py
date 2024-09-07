from rest_framework import serializers 
from purchase.models import CartItem , Order ,  Payment

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['laptop','quantity']
        read_only_fields = ['custumer']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['customer','total_price','items','status']


class  PaymenySerializers(serializers.ModelSerializer):
    class  Meta:
        model = Payment
        fields='__all__'
        
