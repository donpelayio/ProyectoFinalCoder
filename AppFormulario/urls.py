from django.urls import path
from AppFormulario import views


urlpatterns = [
    path('',views.inicio,name="inicio"),
    path('principiante/',views.principiante,name="principiante"),
    path('intermedio/',views.intermedio,name="intermedio"),
    path('avanzado/',views.avanzado,name="avanzado"),
    path('profesional/',views.profesional,name="profesional"),
    #url de la busqueda de alumnos principiantes
    path('busquedaPrincipiante/',views.busquedaPrincipiante,name="busquedaPrincipiante"),
    path('buscar/',views.buscar, name='buscarPrincipiante'),
    path('leerPrincipiantes/',views.leerPrincipiantes, name='leerPrincipiantes'),
    path('eliminarPrincipiante/<principiante_nombre>/',views.eliminarPrincipiante, name='eliminarPrincipiante'),
    path('editarPrincipiante/<principiante_nombre>/',views.editarPrincipiante, name='editarPrincipiante'),
    path('intermedio/lista',views.IntermedioListView.as_view(),name="ListaIntermedio"),
    path('intermedio/nuevo',views.IntermedioCreateView.as_view(),name="NuevoIntermedio"),
    path('intermedio/<pk>',views.IntermedioDetailView.as_view(),name="DetalleIntermedio"),
    path('intermedio/<pk>/editar',views.IntermedioUpdateView.as_view(),name="EditarIntermedio"),
    path('intermedio/<pk>/borrar',views.IntermedioDeleteView.as_view(),name="BorrarIntermedio"),
    path('login', views.login_request, name = 'Login'),

]