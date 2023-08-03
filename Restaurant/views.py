from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import viewsets, status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer, UserSerializer
from django.contrib.auth.models import User

# Create your views here.


def sayHello(request):
    return HttpResponse("Hello")


def index(request):
    return render(request, "index.html", {})


class BookingView(APIView):
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)


class MenuView(APIView):
    def get(self, request):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)  # serialization

    def post(self, request):
        serializer = MenuSerializer(data=request.data)  # incoming post fields

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data}
            )  # deserialization


class UserView(viewsets.ViewSet):
    Users = User.objects.all()
    serializer = UserSerializer(Users, many=True)
    permission_classes = [IsAuthenticated]

    def list(self, request):
        return Response(serializer.data, status.HTTP_200_OK)

    def create(self, request):
        return Response({"message": "Creating a book"}, status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        return Response({"message": "Updating a book"}, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        return Response({"message": "Displaying a book"}, status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        return Response({"message": "Partially updating a book"}, status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        return Response({"message": "Deleting a book"}, status.HTTP_200_OK)


class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)

    def list(self, request):
        return Response(serializer, status.HTTP_200_OK)
