from django.contrib import admin
from django.urls import include, path
from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
]

urlpatterns = [
    path('encuesta/', include('encuesta.urls')),
    path('admin/', admin.site.urls),
]
from . import views

urlpatterns = [
    # ex: localhost:8080/polls/
    path('', views.index, name='index'),
    # ex: localhost:8080/polls/5/
    path('<int:pregunta_id>/', views.detalle, name='detail'),
    # ex: localhost:8080/polls/5/results/
    path('<int:pregunta_id>/results/', views.resultados, name='results'),
    # ex: localhost:8080/polls/5/vote/
    path('<int:pregunta_id>/vote/', views.votar, name='vote'),
]
