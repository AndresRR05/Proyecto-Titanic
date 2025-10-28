from django.urls import path
from .views import PredictView, IndexView

# Este es el nombre del conjunto de URLs de nuestra app.
# Lo usaremos en el archivo de URLs principal.
app_name = 'predictor'

urlpatterns = [
    path('', IndexView.as_view(), name='index'), # <-- NUEVA: Ruta para la página principal
    path('predict/', PredictView.as_view(), name='predict'), # <-- Ruta para la API
]