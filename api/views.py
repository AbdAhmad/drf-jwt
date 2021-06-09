from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User
from . models import Notification
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, NotificationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from . permissions import IsOwner

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]


@permission_classes((permissions.IsAuthenticated,)) # This decorator to be used with APIView
class NotificationListView(APIView):
    """
    List of all Available Notifications
    """
    def get_queryset(self, request):
        if request.user.is_superuser:
            queryset = Notification.objects.all().order_by('-created_on')
        else:
            queryset = Notification.objects.filter(creator=request.user).order_by('-created_on')
        return queryset

    def get(self, request, format=None):
        queryset = self.get_queryset(request)
        serializer = NotificationSerializer(queryset, many=True,context={'request': request})
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = NotificationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(creator=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((permissions.IsAuthenticated,)) # This decorator to be used with APIView
class NotificationDetailView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk, request):
        try:
            obj = Notification.objects.get(pk=pk)
            if obj.creator == request.user or request.user.is_superuser:
                return obj
            raise Http404
        except Notification.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk, request)
        serializer = NotificationSerializer(snippet, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk, request)
        serializer = NotificationSerializer(snippet, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk, request)
        snippet.delete()
        return Response(data="object deleted successfully", status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)