from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['account_id', 'email', 'username', 'password', 'password_confirm', 'first_name', 'last_name', 'role']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    account_id = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        account_id = data.get('account_id')
        password = data.get('password')
        user = User.objects.filter(account_id=account_id).first()
        if user and user.check_password(password):
            return user
        if not user:
            raise AuthenticationFailed('Invalid credentials')
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['account_id', 'email', 'username', 'first_name', 'last_name', 'role']
        read_only_fields = ['account_id', 'email', 'role']