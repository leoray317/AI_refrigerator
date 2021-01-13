from django.urls import path
from django.conf.urls.static import static
from . import views
from fullpageweb import settings

# start with blog
urlpatterns = [
    # http://127.0.0.1:8000/
    path('', views.pagelist, name='pagelist'),
    path('get', views.get, name='get'),
    path('add', views.add, name='add'),
    path('text', views.text, name='text'),
    path('photo', views.photo, name='photo'),
    path('photo_post', views.photo_post, name='photo_post'),

    path('web_img_url', views.web_img_url, name='web_img_url'),
    path('web_video_url', views.web_video_url, name='web_video_url'),
    path('show_food', views.show_food, name='show_food'),


    path('get_data', views.get_data, name='get_data'),
    path('get_data1', views.get_data1, name='get_data1'),
]
urlpatterns += static('/upload/', document_root=settings.MEDIA_ROOT)