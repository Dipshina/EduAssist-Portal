from django.shortcuts import redirect
from apps.account.models import UserProfile
from .forms import LoginForm, RegisterForm
from django.contrib.auth import get_user_model
from django.views.generic import FormView

User = get_user_model()

class LoginView(FormView):
    form_class = LoginForm
    template_name = "account/login.html"


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'account/register.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            password = form.cleaned_data.pop("password")
            confirm_password = form.cleaned_data.pop("confirm_password")

            if password != confirm_password:
                return redirect("user_register")

            # Pop UserProfile-specific fields
            phone = form.cleaned_data.pop("phone")
            address = form.cleaned_data.pop("address")
            date_of_birth = form.cleaned_data.pop("date_of_birth")
            school_college = form.cleaned_data.pop("school_college")
            major = form.cleaned_data.pop("major")
            year_of_study = form.cleaned_data.pop("year_of_study")
            graduation_year = form.cleaned_data.pop("graduation_year")
            bio = form.cleaned_data.pop("bio")

            # Create the User instance
            user = User.objects.create(is_active=True, **form.cleaned_data)
            user.set_password(password)
            user.save()

            # Create the UserProfile instance
            UserProfile.objects.create(
                user=user,
                address=address,
                phone=phone,
                date_of_birth=date_of_birth,
                school_college=school_college,
                major=major,
                year_of_study=year_of_study,
                graduation_year=graduation_year,
                bio=bio
            )

            return redirect("home")
        else:
            return self.form_invalid(form)
