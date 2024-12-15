from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name= "feed"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",views.home,name="home"),
    path("create-post/",views.create_post,name="create_post"),
    path("delete/<int:id>/",views.delete_post,name="delete_post"),
    path("update/<int:id>/",views.update_post,name="update_post"),
    path("like/<int:id>/",views.like_post,name="like_post"),
    path('post/<int:id>/comment/', views.comment_post, name='comment_post'),
    path("comments/",views.comment_list,name="all comments"),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('profile/edit/<str:username>/', views.profile_edit, name='profile_edit'),
    path('search/', views.search_posts, name='search_posts'),
    # Profile edit page for the logged-in user
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
