import flet as ft
import json


from pages.splashscreens.splash_screen import SplashScreen
from pages.registration.registration_page import RegistrationPage
from pages.registration.components.verification import VerificationPage
from pages.registration.components.confirmation import ConfirmationPage
from pages.onboarding.onboarding_step1 import OnboardingStep1
from pages.onboarding.onboarding_step2 import OnboardingStep2
from pages.onboarding.onboarding_step3 import OnboardingStep3
from pages.homepage.home_page import HomePage
from pages.bookingpage.dinning.coffee.dining_coffee import DiningCoffeePage
from pages.bookingpage.dinning.coffee.coffee_confirmation import CoffeeConfirmation
from pages.bookingpage.dinning.coffee.coffee_loading_screen import CoffeeLoadingScreen
from pages.bookingpage.dinning.brunch.dining_brunch import DiningBrunchPage
from pages.bookingpage.dinning.brunch.brunch_confirmation import BrunchConfirmation
from pages.bookingpage.dinning.brunch.brunch_loading_screen import BrunchLoadingScreen
from pages.bookingpage.dinning.dinner.dining_diner import DiningDinerPage
from pages.bookingpage.dinning.dinner.dinner_confirmation import DinnerConfirmation
from pages.bookingpage.dinning.dinner.dinner_loading_screen import DinnerLoadingScreen
from pages.bookingpage.bars import BarsPage
from pages.bookingpage.experience import ExperiencePage
from pages.profiles.profile_page import ProfilePage
from pages.profiles.components.profile_settings import ProfileSettingsPage
from pages.profiles.components.profile_edit import ProfileEditPage
from pages.messages.messages import MessagesPage
from pages.mybooking.upcoming import UpcomingPage
from pages.mybooking.completed import CompletedPage
from pages.mybooking.cancelled import CancelledPage
from pages.login.login_page import LoginPage
from pages.login.components.forgot_password import ForgotPassword
from pages.login.components.otp import OtpPage
from pages.login.components.reset_password import ResetPasswordPage
from pages.login.components.confirmation_password import ConfirmationPassword
from pages.onboarding_quiz.user_setup import UserSetupPage
from pages.onboarding_quiz.gender import GenderPage
from pages.onboarding_quiz.birthdate import BirthdatePage
from pages.onboarding_quiz.interests import InterestPage
from pages.onboarding_quiz.bio import BioPage
from pages.onboarding_quiz.location import LocationPage
from pages.onboarding_quiz.notification import NotificationPage
from pages.bookingdetails.coffee_booking_details import CoffeeDetails
from pages.bookingdetails.brunch_booking_details import BrunchDetails
from pages.bookingdetails.diner_booking_details import DinerDetails


ROUTES = {
    "/splash": SplashScreen,
    "/registration": RegistrationPage,
    "/verification": VerificationPage,
    "/confirmation": ConfirmationPage,
    "/onboarding1": OnboardingStep1,
    "/onboarding2": OnboardingStep2,
    "/onboarding3": OnboardingStep3,
    "/homepage": HomePage,
    "/coffee": DiningCoffeePage,
    "/coffeeconfirm": CoffeeConfirmation,
    "/coffeeloading": CoffeeLoadingScreen,
    "/brunch": DiningBrunchPage,
    "/brunchconfirm": BrunchConfirmation,
    "/brunchloading": BrunchLoadingScreen,
    "/diner": DiningDinerPage,
    "/dinerconfirm": DinnerConfirmation,
    "/dinerloading": DinnerLoadingScreen,
    "/bars": BarsPage,
    "/experience": ExperiencePage,
    "/profile": ProfilePage,
    "/profile/settings": ProfileSettingsPage,
    "/profile/edit": ProfileEditPage,
    "/messages": MessagesPage,
    "/upcoming": UpcomingPage,
    "/completed": CompletedPage,
    "/cancelled": CancelledPage,
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
    "/coffeedetails": CoffeeDetails,
    "/brunchdetails": BrunchDetails,
    "/dinerdetails": DinerDetails,
}


def get_user_data():
    """
    Reads the user data from the JSON file and returns it as a dictionary.
    """
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
            kwargs["user_id"] = user_data.get("id")

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

    go_to("/login", page)


ft.app(target=main)
