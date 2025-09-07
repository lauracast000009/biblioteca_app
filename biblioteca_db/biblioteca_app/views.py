from rest_framework import generics, filters
from django_filters import rest_framework as dj_filters
from .models import Autor, Editorial, Libro, Miembro, Prestamo
from .serializers import AutorSerializer, EditorialSerializer, LibroSerializer, MiembroSerializer, PrestamoSerializer

# ------- FILTROS ---------
class LibroFilter(dj_filters.FilterSet):
    autor = dj_filters.NumberFilter(field_name='autor')
    editorial = dj_filters.NumberFilter(field_name='editorial')
    autor_nombre = dj_filters.CharFilter(field_name='autor__nombre', lookup_expr='icontains')
    editorial_nombre = dj_filters.CharFilter(field_name='editorial__nombre', lookup_expr='icontains')

    class Meta:
        model = Libro
        fields = ['autor', 'editorial', 'autor_nombre', 'editorial_nombre']

class PrestamoFilter(dj_filters.FilterSet):
    fecha_prestamo = dj_filters.DateFilter(field_name='fecha_prestamo')
    miembro = dj_filters.NumberFilter(field_name='miembro')

    class Meta:
        model = Prestamo
        fields = ['fecha_prestamo', 'miembro']


# ------- AUTORES ---------
class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filter_backends = [dj_filters.DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nombre', 'apellido']

class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


# ------- EDITORIALES ---------
class EditorialList(generics.ListCreateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
    filter_backends = [dj_filters.DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nombre']

class EditorialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer


# ------- LIBROS ---------
class LibroList(generics.ListCreateAPIView):
    queryset = Libro.objects.select_related('autor', 'editorial').all()
    serializer_class = LibroSerializer
    filter_backends = [dj_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = LibroFilter
    search_fields = ['titulo', 'isbn', 'autor__nombre', 'autor__apellido', 'editorial__nombre']
    ordering_fields = ['anio_publicacion', 'titulo']

class LibroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


# ------- MIEMBROS ---------
class MiembroList(generics.ListCreateAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer
    filter_backends = [dj_filters.DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nombre', 'apellido', 'email']

class MiembroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer


# ------- PRÉSTAMOS ---------
class PrestamoList(generics.ListCreateAPIView):
    queryset = Prestamo.objects.select_related('libro', 'miembro').all()
    serializer_class = PrestamoSerializer
    filter_backends = [dj_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PrestamoFilter
    search_fields = ['libro__titulo', 'miembro__nombre', 'miembro__apellido']
    ordering_fields = ['fecha_prestamo', 'fecha_devolucion']

class PrestamoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
