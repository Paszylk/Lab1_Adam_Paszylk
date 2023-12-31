from django.contrib import admin
from django.urls import path, include
from crud_blog_web.views import test_response
from crud_blog_web.views import all_articles

def moja_metoda(request):
    # Tutaj można umieścić kod przetwarzający żądanie, jeśli jest to konieczne
    return render(request, 'articles.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_response),
    path('crud-blog/', include("crud_blog_web.urls")),
    path('templates/', all_articles),
]