from django.urls import path
from django.conf.urls.static import static
from . import views
from fullpageweb import settings

urlpatterns = [
    # http://127.0.0.1:8000/
    path('', views.pagelist, name='pagelist'),

    path('photo', views.photo, name='photo'),
    path('photo_post', views.photo_post, name='photo_post'),

    path('show_food', views.show_food, name='show_food'),

    path('get_data', views.get_data, name='get_data'),
    path('get_data1', views.get_data1, name='get_data1'),
    path('get_num', views.get_num, name='get_num'),

    path('price_pre', views.price_pre, name='price_pre'),

]
urlpatterns += static('/upload/', document_root=settings.MEDIA_ROOT)