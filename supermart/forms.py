from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy, gettext as _
from django.contrib.auth import password_validation
from .models import Customer, CancledOrders, ReturnOrders


class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
                "autocomplete": "off",
                "onfocus": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Password'",
            }
        ),
    )
    password2 = forms.CharField(
        required=True,
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirm Password",
                "autocomplete": "off",
                "onfocus": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Confirm Password'",
            }
        ),
    )
    email = forms.CharField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email Address",
                "autocomplete": "off",
                "onfocus": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Email Address'",
                "onclick": "clearFields()",
            }
        ),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {"email": "Email Address"}
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Username",
                    "autocomplete": "off",
                    "onfocus": "this.placeholder = ''",
                    "onblur": "this.placeholder = 'Username'",
                    "onclick": "clearFields()",
                }
            )
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "class": "form-control",
                "placeholder": "Username",
                "autocomplete": "off",
                "onfocus": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Username'",
            }
        )
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "form-control",
                "placeholder": "Password",
                "autocomplete": "off",
                "onfocus": "this.placeholder = ''",
                "onblur": "this.placeholder = 'Password'",
            }
        ),
    )


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "class": "form-control",
                "placeholder": "Enter Your Old Password"
            }
        ),
    )
    new_password1 = forms.CharField(
        label=_("New Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password",
                   "class": "form-control", "placeholder": "Enter Your New Password"}
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("Confirm New Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control",
                   "placeholder": "Confirm Your New Password"}
        ),
    )


class MyPasswordResetForm(PasswordResetForm):
    email = forms.CharField(
        required=True,
        label=_("Email"),
        widget=forms.EmailInput(
            attrs={"class": "form-control", "autocomplete": "email",
                   "placeholder": "Enter your valid email address"}
        ),
    )


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password",
                   "class": "form-control", "placeholder": "Enter Your New Password"}
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("Confirm New Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control",
                   "placeholder": "Confirm Your New Password"}
        ),
    )


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "fname",
            "lname",
            "phone",
            "addone",
            "addtwo",
            "city",
            "state",
            "zipcode",
        ]
        widgets = {
            "fname": forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name",
                                            "autocomplete": "off", }),
            "lname": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name",
                                            "autocomplete": "off", }),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone",
                                            "autocomplete": "off", }),
            "addone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Address Line One",
                                             "autocomplete": "off", }),
            "addtwo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Address Line Two",
                                             "autocomplete": "off", }),
            "city": forms.TextInput(attrs={"class": "form-control", "placeholder": "City Name",
                                           "autocomplete": "off", }),
            "state": forms.Select(attrs={"class": "country_select"}),
            "zipcode": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Zip Code/Postal Code", "autocomplete": "off", }),
        }


class CancledOrdersForm(forms.ModelForm):
    class Meta:
        model = CancledOrders
        fields = [
            "reason",
            "bank_name",
            "bank_acc",
            "bank_ifsc",
            "holder_name",
            "upi_id",
        ]
        labels = {
            "reason": "Cancle Product Reason",
            "bank_name": "Bank Name",
            "bank_acc": "Bank Account Number",
            "bank_ifsc": "Bank IFSC Number",
            "holder_name": "Account Holder Name",
            "upi_id": "Upi Id",
        }
        widgets = {
            "reason": forms.Select(attrs={"class": "form-control", "required": "true"}),
            "bank_name": forms.Select(
                attrs={"class": "form-control", "required": "true"}
            ),
            "bank_acc": forms.TextInput(
                attrs={"class": "form-control", "required": "true"}
            ),
            "bank_ifsc": forms.TextInput(
                attrs={"class": "form-control", "required": "true"}
            ),
            "holder_name": forms.TextInput(
                attrs={"class": "form-control", "required": "true"}
            ),
            "upi_id": forms.TextInput(
                attrs={"class": "form-control", "required": "true"}
            ),
        }


class ReturnOrdersForm(forms.ModelForm):
    class Meta:
        model = ReturnOrders
        fields = [
            "rreason",
            "bank_name",
            "bank_acc",
            "bank_ifsc",
            "holder_name",
            "upi_id",
        ]
        labels = {
            "rreason": "Return Product Reason",
            "bank_name": "Bank Name",
            "bank_acc": "Bank Account Number",
            "bank_ifsc": "Bank IFSC Number",
            "holder_name": "Account Holder Name",
            "upi_id": "Upi Id",
        }
        widgets = {
            "rreason": forms.Select(attrs={"class": "form-control"}),
            "bank_name": forms.Select(attrs={"class": "form-control"}),
            "bank_acc": forms.TextInput(attrs={"class": "form-control"}),
            "bank_ifsc": forms.TextInput(attrs={"class": "form-control"}),
            "holder_name": forms.TextInput(attrs={"class": "form-control"}),
            "upi_id": forms.TextInput(attrs={"class": "form-control"}),
        }
