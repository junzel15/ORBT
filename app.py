import flet as ft
import json
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from pages.splashscreens.splash_screen import SplashScreen
from pages.registration.registration_page import RegistrationPage
from pages.registration.components.verification import VerificationPage
from pages.registration.components.confirmation import ConfirmationPage
from pages.landingpage.onboarding_step1 import OnboardingStep1
from pages.landingpage.onboarding_step2 import OnboardingStep2
from pages.landingpage.onboarding_step3 import OnboardingStep3
from pages.homepage.home_page import HomePage
from pages.mybookings.booking_options.dining import DiningPage
from pages.mybookings.booking_options.bars import BarsPage
from pages.mybookings.booking_options.experience import ExperiencePage
from pages.profiles.profile_page import ProfilePage
from pages.profiles.components.profile_settings import ProfileSettingsPage
from pages.profiles.components.profile_edit import ProfileEditPage
from pages.messages.messages import MessagesPage
from pages.login.login_page import LoginPage
from pages.login.components.forgot_password import ForgotPassword
from pages.login.components.otp import OtpPage
from pages.login.components.reset_password import ResetPasswordPage
from pages.login.components.confirmation_password import ConfirmationPassword
from pages.personal_information.user_setup import UserSetupPage
from pages.personal_information.gender import GenderPage
from pages.personal_information.birthdate import BirthdatePage
from pages.personal_information.interests import InterestPage
from pages.personal_information.bio import BioPage
from features.location import LocationPage
from features.notification import NotificationPage
from pages.mybookings.bookingdetails.booking_details import BookingDetails
from pages.mybookings.booking_options.shared.loading_screen import LoadingScreen
from pages.mybookings.booking_options.shared.booking_confirmation import (
    ConfirmationScreen,
)
from pages.mybookings.booking_navbar.bookings import Bookings
from pages.mybookings.booking_navbar.components import BookingCard, Tabs, FilterModal
from pages.mybookings.booking_navbar.helpers import filter_bookings


ROUTES = {
    "/splash": SplashScreen,
    "/registration": RegistrationPage,
    "/verification": VerificationPage,
    "/confirmation": ConfirmationPage,
    "/onboarding1": OnboardingStep1,
    "/onboarding2": OnboardingStep2,
    "/onboarding3": OnboardingStep3,
    "/homepage": HomePage,
    "/diner": DiningPage,
    "/bars": BarsPage,
    "/experience": ExperiencePage,
    "/profile": ProfilePage,
    "/profile/settings": ProfileSettingsPage,
    "/profile/edit": ProfileEditPage,
    "/messages": MessagesPage,
    "/login": LoginPage,
    "/forgotpassword": ForgotPassword,
    "/otp": OtpPage,
    "/resetpassword": ResetPasswordPage,
    "/confirmationpassword": ConfirmationPassword,
    "/usersetup": UserSetupPage,
    "/gender": GenderPage,
    "/birthdate": BirthdatePage,
    "/interest": InterestPage,
    "/bio": BioPage,
    "/location": LocationPage,
    "/notification": NotificationPage,
    "/bookingdetails": BookingDetails,
    "/loadingscreen": LoadingScreen,
    "/bookingconfirmation": ConfirmationScreen,
    "/bookings": Bookings,
    "/components": (BookingCard, Tabs, FilterModal),
    "/filters": filter_bookings,
}


def get_user_data():
    try:
        with open("json/users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: user_data.json not found!")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON!")
        return []


user_data = None


def go_to(route, page, **kwargs):
    global user_data

    if not user_data:
        user_data_list = get_user_data()
        user_data = user_data_list[0] if user_data_list else {}

    print(f"Navigating to {route} with kwargs: {kwargs}")

    view_class = ROUTES[route]

    if hasattr(view_class, "__init__"):
        init_params = view_class.__init__.__code__.co_varnames
        if "user" in init_params:
            kwargs["user"] = user_data
        if "user_id" in init_params:
            kwargs["user_id"] = user_data.get("uuid")

    view_instance = view_class(page, go_to, **kwargs)

    view = view_instance.render() if hasattr(view_instance, "render") else view_instance

    if not hasattr(view, "route"):
        view = ft.View(route=route, controls=[view])

    if not page.views or page.views[-1].route != route:
        page.views.append(view)

    page.go(view.route)
    page.update()


def main(page: ft.Page):

    page.on_route_change = lambda _: go_to(page.route, page)

    go_to("/bookings", page)


ft.app(target=main)
