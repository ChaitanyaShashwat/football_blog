from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from football_blog import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$',views.home,name='home_page'),
    url(r'^admin/', admin.site.urls),
    url(r'^about',views.about,name='about'),
    url(r'^joinus',views.join,name='joinus'),
    url(r'^articles/',include('articles.urls')),
    url(r'^accounts/',include('accounts.urls'))
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
