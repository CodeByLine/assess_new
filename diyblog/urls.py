
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('blog/', include('blog.urls')),
]

urlpatterns += [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

# urlpatterns += [
#     path('bloggers/', views.AuthorListView.as_view(), name='bloggers'),
#     path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail')
# ]