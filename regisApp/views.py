from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from bis_app.models import Profile
from .forms import SignUpForm, EditProfileForm
from django.views.generic import DetailView

# Create your views here.


# Password change page.
class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')
    # success_url = reverse_lazy('login')

# To create a password change success page I think.
def password_success(request):
    return render(request, 'registration/password_success.html', {})


# User registration form
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


# Edit user info.
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'editProfile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class ProfilePageView(DetailView):
    model = Profile
    template_name = "templates/user_profile.html"

    def get_context_data(self, *args, **kwargs ):
        users_profile = Profile.objects.all()
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])  
        context["page_user"] = page_user
        return context
