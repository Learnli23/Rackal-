from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static
urlpatterns = [
          path('',views.home,name='home'),
          path('New',views.gallery,name='New'),
          path('Men',views.Men,name='Men'),
          path('Women',views.Women,name='Women'),
          path('Accessories',views.Accessories,name='Accessories'),
          path('Collections',views.Collections,name='Collections'),  
          path('Store',views.Store,name='Store'), 
          path('Bags_ and_Leather_goods',views.Bags_and_Leather_goods,name='Bags_ and_Leather_goods'), 
          #blog urls
          path('blog_list', views.blog_list, name='blog_list'),
          path('post/<int:post_id>/', views.blog_detail, name='blog_detail'),
          path('post/<int:post_id>/like/', views.like_post, name='like_post'),
          path('post/<int:post_id>/dislike/', views.dislike_post, name='dislike_post'),
          path('create_blog',views.create_blog,name='create_blog'),
          path('delete_post/<post_id>',views.delete_post, name='delete_post'),
          path('edit_post/<post_id>',views.edit_post, name='edit_post'),
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)

 

 