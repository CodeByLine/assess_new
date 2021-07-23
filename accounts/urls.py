from django.urls import path
from .views import SignUpView
from . import views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]

# urlpatterns += [
#     path('bbloggers/', views.AuthorListsView.as_view(), name='bbloggers'),
#     path('bbloggers/<int:pk>', views.AuthorDetailsView.as_view(), name='author-detail')
# ]