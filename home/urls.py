from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # HTML Views
    path('', views.login_page, name='home'),               # default is login page
    path('index/', views.index, name='index'),
    path('login/', views.login_page, name='login'),        # HTML form login
    path('logout/', views.logout_view, name='logout'),     # logout user
    path('register/',views.register_page,name ='register'),
    path('browse-books/', views.browse_books_page, name='browse_book'), 
    path('add-to-cart-page/', views.add_to_cart_page, name='add_cart'),
    # path('checkout/', views.checkout_cart, name='checkout'),
    path('save-for-later/', views.save_later, name='save-for-later'),
    # path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),


    # API Endpoints
    path('api/login/', views.login_user, name='api_login'),         # POST with JSON (username, password)
    path('api/register/', views.register_user_api, name='api_register'), # POST with JSON (username, password)
#    homepage
    path('api/browse-books/', views.browse_books, name='api_browse_books'),
    path('api/cart/add/', views.add_to_cart, name='add_to_cart'),
    # path('api/cart/checkout/', views.checkout_cart, name='checkout_cart'),
    path('api/save_for_later/', views.save_for_later, name='save_for_later'),
    
    
]