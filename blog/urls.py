from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('blogs/', views.PostListView.as_view(), name='blogs'),
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    path('blog/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('blog/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]

urlpatterns += [
    path('blog/<int:pk>/', views.post_detail, name='post_detail'),
    # path('blog/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
]

urlpatterns += [ 
    # path('blog/<int:pk>/comment/create', views.CommentCreateView.as_view(), name='comment-create'),
    # path('comment/<int:pk>', views.CommentDetailView.as_view, name='comment_detail'),
]


urlpatterns += [
    path('bloggers/', views.AuthorListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail')
]