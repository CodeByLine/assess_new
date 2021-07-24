from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('blogs/', views.PostListView.as_view(), name='blogs'),

    path('blog/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='post-update'),
    # path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post-delete'),
]


urlpatterns += [
    path('bloggers/', views.AuthorListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail')
]