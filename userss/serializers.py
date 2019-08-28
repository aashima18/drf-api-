from rest_framework import serializers
from userss.models import User,Item
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields = ('username','first_name', 'last_name', 'email','password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    username=serializers.CharField(write_only=True)
    password=serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username','password')    

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('title', 'description','user_s')    
  
