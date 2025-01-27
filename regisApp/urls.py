# In this file you'll write the html files urls paths so views.py can display them
#
#
#
#
# *******************************************************************************

from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordChangeView, ProfilePageView, editProfilePage, CreateProfilePage
from django.contrib.auth import views as auth_views
from . import views

# write paths below.
urlpatterns = [
    
    path('registration/', UserRegisterView.as_view(), name='register'),
    path('editProfile/', UserEditView.as_view(), name='editProfile'),

    # to activate password change page
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/changePassword.html')),

    # to make costume password change
    path('password/', PasswordChangeView.as_view(template_name='registration/changePassword.html')),

    # to make a success page i think
    path('password_success', views.password_success, name="password_success"),

    # Profile page path
    path('<int:pk>/profile', ProfilePageView.as_view(), name="ProfilePage"),

    # Profile edit page path
    path('<int:pk>/profileEditor/', editProfilePage.as_view(), name="profileEditor"),
    
    # Profile Creation page path
    path('profileCreator/', CreateProfilePage.as_view(), name="profileCreator"),

    
    
]