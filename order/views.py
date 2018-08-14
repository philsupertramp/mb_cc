from rest_framework import mixins
from rest_framework import generics

from .models import Order, Customer
from .serializer import OrderSerializer


class OrderList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    """
    Lists all orders, or create a new one
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        customer_name = request.data.get("customer_name", None)
        new_customer_name = customer_name if customer_name is not None else "unknown"
        Customer.objects.get_or_create(full_name=new_customer_name)
        return self.create(request, *args, **kwargs)


class OrderDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    """
    Retrieve, delete or update order
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        customer_name = request.data.get("customer_name", None)
        new_customer_name = customer_name if customer_name is not None else "unknown"
        Customer.objects.get_or_create(full_name=new_customer_name)
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
