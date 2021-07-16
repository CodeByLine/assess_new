from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('blogs/', views.PostListView.as_view(), name='blogs'),

    path('blog/<int:pk>', views.PostDetailView.as_view(), name='post-detail')
    # path('blog/create/', views.AuthorCreate.as_view(), name='post-create'),
#     # path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
#     # path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]

urlpatterns += [
    path('bloggers/', views.AuthorListView.as_view(), name='bloggers'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail')

#     # path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    # path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    # path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]