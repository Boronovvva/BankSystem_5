from rest_framework import serializers

from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('id','username','phone','age','balance','wallet_address','created_at')
        extra_kwargs = {
            'wallet_address' : {'write_only' : True}
        }