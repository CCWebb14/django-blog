from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
  # Match all empty paths, and make it a named URL home
  path('post/<int:pk>', BlogDetailView.as_view(),
    name='post_detail'),
  path('', BlogListView.as_view(), name='home'),
]
