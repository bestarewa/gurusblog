from django.urls import path
from .views import all_post, postView, addComment

app_name = 'blog'

urlpatterns = [
    
    path('add-comment', addComment, name='add-comment'),
    path('<slug>/', postView, name='post-details'),
    path('', all_post, name='home'),
]
