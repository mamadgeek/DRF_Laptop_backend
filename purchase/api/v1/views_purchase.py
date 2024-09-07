
from purchase.models import CartItem,Order
from .serializers_purchase import CartItemSerializer , OrderSerializer , Payment
from rest_framework import viewsets ,  generics
from products.models import UserAdmin
from rest_framework.response import Response
from rest_framework import status



class CartItemView(viewsets.ModelViewSet):
    # queryset=CartItem.objects.filter()
    serializer_class=CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(custumer=self.request.user)  # Filter cart items for the current user

    def perform_create(self, serializer):
        print(self.request.data) #{'laptop': 7003, 'quantity': 2}
        serializer.save(custumer=self.request.user)

class OrderView(viewsets.ModelViewSet):
    # queryset=Order.objects.filter()
    serializer_class=OrderSerializer
    
    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user,)
    
    def create(self, request, *args, **kwargs):
        print(request.body)  # Check if raw data is coming through
        print(request.data)  # Check the parsed data
        return super().create(request, *args, **kwargs)


    def perform_create(self, serializer):
        # print(self.request.data)
         #{'id': 4,
        #  'total_price': '464968724.0000',
        #  'status': 'pending',
        #  'created_at': '2024-09-06T20:43:57.446292Z',
        #  'customer': 2,
        #  'items': []}
        cart_items = CartItem.objects.filter(custumer=self.request.user)   #<QuerySet [<CartItem: MSI - pro - APPLE M1 Pro - RTX 3080 - 8GB - 2 - by mamad>, <CartItem: Acer - Unknown - APPLE M1 Pro - RTX 3080 - 8GB - 1 - by mamad>]>
        if not cart_items.exists():
            return Response({"detail": "Cart is empty."}, status=status.HTTP_400_BAD_REQUEST)

        total_price = sum([item.laptop.price * item.quantity for item in cart_items])

        order =serializer.save(customer=self.request.user, total_price=total_price)
        order.items.set(cart_items) 
        cart_items.delete() 

        return order 
    
