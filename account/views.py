from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .forms import RegistrationForm, UserEditForm
from .models import UserBase
from .token import account_activation_token


@login_required
def dashboard(request):
    """renders dashboard.html file

    Args:
        request (object)
    """
    return render(request, "account/user/dashboard.html")


def account_register(request):
    """method to register the user and send them email of
    activation token

    Args:
        request (obhect)

    Returns:
        [HttpResponse]: renders different html pages on the bases of
                        various conditions.
    """

    if request.method == "POST":
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data["email"]
            user.set_password(registerForm.cleaned_data["password"])
            user.is_active = False
            user.save()
            # setup email
            current_site = get_current_site(request)
            subject = "Activate your Account"
            message = render_to_string(
                "account/registration/account_activation_email.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": account_activation_token.make_token(user),
                },
            )
            user.email_user(subject=subject, message=message)
            return HttpResponse("register user and activate user")

    else:
        registerForm = RegistrationForm()
    return render(request, "account/registration/register.html", {"form": registerForm})


def account_activate(request, uidb64, token):
    """method to activate account and login the user

    Args:
        request (object):
        uidb64 (string): dentifier that marks that particular record as unique
        token (string):

    Returns: renders or re-directs to appropriate page.
    """
    print("active......................................")
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except Exception as err:
        print(err)
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("account:dashboard")
    else:
        return render(request, "account/registration/activation_invalid.html")


@login_required
def account_edit_details(request):
    """method to update the username"""

    if request.method == "POST":
        userForm = UserEditForm(instance=request.user, data=request.POST)
        if userForm.is_valid():
            userForm.save()

    else:
        userForm = UserEditForm(instance=request.user)

    return render(request, "account/user/edit_detail.html", {"form": userForm})


@login_required
def delete_user(request):
    "delete the user account by making it not active in db"
    user = UserBase.objects.get(user_name=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect("account:delete_confirmation")
