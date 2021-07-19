from django.urls import path
from .views import SignUpView, AuthorListView, AuthorDetailView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]