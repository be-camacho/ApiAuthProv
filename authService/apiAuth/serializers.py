from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from .models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validar(self, data):
        username=data.get('username')
        password=data.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("Usuario o contraseña incorrectos")
        if not check_password(password, user.password):
            raise serializers.ValidationError("Usuario o contraseña incorrectos")
        return {
            "idprov": user.idproveedor,
            "rol": user.rol
        }