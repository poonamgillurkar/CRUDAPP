from . import views
from django.urls import path
'''
urlpatterns = [
    path('',views.PageView.as_view(),name='POST_DELETE.html'),
    path('',views.PageView.as_view(),name='POST_FORM.html'),
    path('',views.PageView.as_view(),name='POST_LIST.html'),

]
'''
urlpatterns = [
    path('delete/',views.delete,name='delete'),
    path('form/',views.form,name='form'),
    path('list/',views.list,name='list'),
]