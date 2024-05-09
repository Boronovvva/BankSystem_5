from rest_framework import serializers

from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'age', 'email','phone', 'balance','created_at', 'password', 'password_confirm', 'wallet_address')
        extra_kwargs = {
            'password': {'write_only': True},
            'password_confirm': {'write_only': True},
            'wallet_address': {'read_only': True},
            'balance': {'read_only': True}
        }
        
    def create(self, validated_data):
         print(validated_data)
         user = User.objects.create(
            wallet_address=validated_data['wallet_address']
        )
         user.set_password(validated_data['created_at'])
         user.save()
         return user
    
    def validate(self, attrs):
        print(attrs)
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password':'Пароли отличаются'})
        if len(attrs['password']) < 8:
            raise serializers.ValidationError({'password':'Длина пароля меньше 8 символов'})
        return attrs