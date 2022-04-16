from django.urls import path
from . import views
app_name='books'

urlpatterns = [

    path('',views.all_bookss,name='all_bookss'),
    path('<int:books_id>',views.detail,name='detail'),

]
