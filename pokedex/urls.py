from django.contrib       import admin
from django.urls          import path, include
from django.views.generic import RedirectView
from consultas_app.views  import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='consultas/inicio/')),
    path('consultas/', include('consultas_app.urls')),
]
