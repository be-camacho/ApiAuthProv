from rest_framework import serializers
from django.contrib.auth.hashers import check_password # Importo la funcion check_password para verificar la contraseña con hash
from .models import Usuario


class UserSerializer(serializers.ModelSerializer): # creo un serializer para recibir los datos a consultar en la base de datos
    username = serializers.CharField() #declaro que recibire un username
    password = serializers.CharField() #declaro que recibire un password

    class Meta:
        model = Usuario #indico el modelo a usar
        fields = ['username', 'password'] #indico los campos a recibir
        
    def validate(self, data): #hago una funcion para validar los datos
        username=data.get('username') 
        password=data.get('password')
        try: #intento obtener el usuario de la base de datos
            user = Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            raise serializers.ValidationError("Usuario o contraseña incorrectos")
        if not check_password(password, user.password): #se usa una if not para verificar si la contraseña no es correcta devido a que la contraseña se guarda en hash
            raise serializers.ValidationError("Usuario o contraseña incorrectos")
        
        response_data = { #siempre retorno el rol
            "rol": user.rol
        }

        if user.rol.lower() == 'p': #si el rol es proveedor añado el idproveedor al response_data
            response_data["id"] = user.idproveedor 
        
        return response_data