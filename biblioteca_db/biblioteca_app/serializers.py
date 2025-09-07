from rest_framework import serializers
from .models import Autor, Editorial, Libro, Miembro, Prestamo

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = "__all__"

class LibroSerializer(serializers.ModelSerializer):
    autor = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all())
    editorial = serializers.PrimaryKeyRelatedField(queryset=Editorial.objects.all())
    autor_nombre = serializers.CharField(source='autor.__str__', read_only=True)
    editorial_nombre = serializers.CharField(source='editorial.__str__', read_only=True)

    class Meta:
        model = Libro
        fields = ['id','titulo','resumen','isbn','anio_publicacion','autor','editorial','autor_nombre','editorial_nombre']

class MiembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miembro
        fields = "__all__"

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = "__all__"
