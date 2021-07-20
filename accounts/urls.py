from django.urls import path
from .views import SignUpView, AuthorListView, AuthorDetailView
from . import views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]

# urlpatterns += [
#     path('bbloggers/', views.AuthorListView.as_view(), name='bbloggers'),
#     path('bbloggers/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail')
# ]