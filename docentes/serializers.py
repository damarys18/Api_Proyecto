from rest_framework import serializers

from docentes.models import Docente, Institucion, Materia


class DocenteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Docente
        fields = ('url','id', 'nombre', 'apellido', 'cedula', 'sexo', 'email', 'fecha_de_nacimiento', 'celular', 'activo', 'institucion', 'materia')

class InstitucionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Institucion
        fields = ('url', 'nombre', 'direccion', 'numero')

class MateriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materia
        fields = ('url', 'nombre', 'horas', 'institucion')