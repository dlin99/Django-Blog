from django.urls import path

from . import views

app_name = 'comments'
urlpatterns = [

    path('<int:pk>/', views.comment_thread, name='thread'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='comment-delete'),

]
