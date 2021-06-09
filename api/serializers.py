from django.contrib.auth.models import User
from . models import Notification
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    staff_of = serializers.StringRelatedField()
    class Meta:
        model = User
        fields = ['username', 'email','staff_of']


class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="notification-detail", lookup_field='pk')
    created_on = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = Notification
        fields = ['url','id','title','link','creator','created_on']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['creator'] = UserSerializer(instance.creator).data
        return response