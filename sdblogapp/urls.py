from django.urls import path
from . import views
# from django.views.generic import DeleteView
from .views import NewPostView
from .views import NewCategoryView, SearchView
from sdblogapp.views import *
from .views import home, NewPostView, updatepost, deletepost, DetailArticle, landingpage, NotificationListView, HalfDetailPageView, Plan, UpdateUserRoleView, StaffDashboard, AuthorPost, AllTables, DeleteUser, UpdateUserView, LegalPage, success, contact, EditPrimeRole, PrivacyPolicy, payment_success, logout_views, check_for_new_posts, posttable, posttabledelete, emaildashboard, notify, EmailListView, DeleteSubscriptionView, CategoryListView, CategoryDeleteView



urlpatterns = [
    # path('', landingpage.as_view(), name='landingpage'),
    path('home/', home, name='home'),
    path('', landingpage, name='landingpage'),
    path('email-list/', EmailListView.as_view(), name='email_list'),
    path('email-list/<int:subscription_id>/delete/', DeleteSubscriptionView.as_view(), name='delete_subscription'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<slug:category_slug>/delete/', CategoryDeleteView.as_view(), name='delete_category'),
    path('posttable/', posttable, name='posttable'),
    path('notification/', NotificationListView.as_view(), name='notification'),  # Define URL pattern for notification
    path('notify/', notify, name='notify'),    
    path('posttableupdate/<int:post_id>/', posttableupdate, name='posttableupdate'),
    path('posttabledelete/<int:post_id>/', posttabledelete, name='posttabledelete'),
    path('emaildashboard/', emaildashboard, name='emaildashboard'),
    path('logout/', logout_views, name = 'logout_views'),
    path('contact/', contact, name='contact'),
    path('check_for_new_posts/', check_for_new_posts, name='check_for_new_posts'),
    path('check_for_new_posts/', check_for_new_posts, name='check_for_new_posts'),

    path('success/', success, name='success'),
    path('privacypolicy/', PrivacyPolicy, name='PrivacyPolicy'),
    path('staff-dashboard/', StaffDashboard.as_view(),name='StaffDashboard'),
    path('admin-dashboard/', AdminDashboard.as_view(),name='AdminDashboard'),
    path('alltable/', AllTables.as_view(), name='all_tables'),
    path('update-user/<int:pk>/', UpdateUserView.as_view(), name='update_user'),
    path('delete-user/<int:pk>/', DeleteUser.as_view(), name='delete_user'),
    path('legalpage/', LegalPage.as_view(), name='LegalPage'),
    path('subscribe-newsletter/', views.subscribe_newsletter, name='subscribe_newsletter'),


    path('authorpost/', AuthorPost.as_view(),name='AuthorPost'),
    path('EditPrimeRole/', EditPrimeRole, name='EditPrimeRole'),
    path('editrole/', UpdateUserRoleView.as_view(), name='update-user-role'),
    path('half/', HalfDetailPageView.as_view(), name='half_detail'),
    path('plan/', Plan, name='Plan'),
    path('payment/', payment, name='payment'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('payment_success/', payment_success, name='payment_success'),

    # path('home/', home.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search'),
    # path('newpost/', newpost.as_view(), name='newpost'),
    # path('<str:cat>/', CategoryPageView.as_view(), name='category'),
    path('newpost/', NewPostView.as_view(), name='newpost'),
    path('edit/<slug:slug>', updatepost.as_view(), name='updatepost'),
    path('deletepost/<slug:slug>/', deletepost.as_view(), name='deletepost'),
    path('newcategory/', NewCategoryView.as_view(), name='newcategory'),
    path('<cat>/<slug>/', DetailArticle.as_view(), name='detail-article'),
    path('<str:cat>/', views.categorypage, name='category'),

]
