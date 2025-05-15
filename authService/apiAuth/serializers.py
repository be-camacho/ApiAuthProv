from rest_framework import serializers
from django.contrib.auth.hashers import check_password # Importo la funcion check_password para verificar la contraseña con hash
from .models import User


class UserSerializer(serializers.ModelSerializer): # creo un serializer para recibir los datos a consultar en la base de datos
    username = serializers.CharField() #declaro que recibire un username
    password = serializers.CharField() #declaro que recibire un password

    def validar(self, data): #hago una funcion para validar los datos
        username=data.get('username') 
        password=data.get('password')
        try: #intento obtener el usuario de la base de datos
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("Usuario o contraseña incorrectos")
        if not check_password(password, user.password): #se usa una if not para verificar si la contraseña no es correcta devido a que la contraseña se guarda en hash
            raise serializers.ValidationError("Usuario o contraseña incorrectos")
        if user.rol.lower() == 'p': #verifico que el rol del usuario sea proveedor
            return { #retorno el id del proveedor para su futuro uso y el rol del usuario
                "idprov": user.idproveedor,
                "rol": user.rol
            }
        else:
            return { #retorno el el rol del usuario para su futuro uso
                "rol": user.rol
            }