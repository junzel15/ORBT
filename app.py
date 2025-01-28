import flet as ft
import json


from splashscreens.splash_screen import SplashScreen
from registration.registration_page import RegistrationPage
from registration.components.verification import VerificationPage
from registration.components.confirmation import ConfirmationPage
from onboarding.onboarding_step1 import OnboardingStep1
from onboarding.onboarding_step2 import OnboardingStep2
from onboarding.onboarding_step3 import OnboardingStep3
from homepage.home_page import HomePage
from homepage.tabs.dining_coffee import DiningCoffeePage
from homepage.tabs.dining_brunch import DiningBrunchPage
from homepage.tabs.dining_diner import DiningDinerPage
from homepage.components.bars import BarsPage
from homepage.components.experience import ExperiencePage
from profiles.profile_page import ProfilePage
from profiles.components.profile_settings import ProfileSettingsPage
from profiles.components.profile_edit import ProfileEditPage
from messages.messages import MessagesPage
from bookingpage.upcoming import UpcomingPage
from bookingpage.completed import CompletedPage
from bookingpage.cancelled import CancelledPage
from login.login_page import LoginPage
from onboarding_quiz.user_setup import UserSetupPage
from onboarding_quiz.gender import GenderPage
from onboarding_quiz.birthday import BirthdayPage
from onboarding_quiz.interests import InterestPage
from onboarding_quiz.about_me import AboutMePage
from onboarding_quiz.location import LocationPage
from onboarding_quiz.notification import NotificationPage


ROUTES = {
    "/splash": SplashScreen,
    "/registration": RegistrationPage,
    "/verification": VerificationPage,
    "/confirmation": ConfirmationPage,
    "/onboarding1": OnboardingStep1,
    "/onboarding2": OnboardingStep2,
    "/onboarding3": OnboardingStep3,
    "/homepage": HomePage,
    "/dining/coffee": DiningCoffeePage,
    "/dining/brunch": DiningBrunchPage,
    "/dining/diner": DiningDinerPage,
    "/bars": BarsPage,
    "/experience": ExperiencePage,
    "/profile": ProfilePage,
    "/profile/settings": ProfileSettingsPage,
    "/profile/edit": ProfileEditPage,
    "/messages": MessagesPage,
    "/bookings/upcoming": UpcomingPage,
    "/bookings/completed": CompletedPage,
    "/bookings/cancelled": CancelledPage,
    "/login": LoginPage,
    "/usersetup": UserSetupPage,
    "/gender": GenderPage,
    "/birthday": BirthdayPage,
    "/interest": InterestPage,
    "/aboutme": AboutMePage,
    "/location": LocationPage,
    "/notification": NotificationPage,
}


def get_user_data():
    """
    Reads the user data from the JSON file and returns it as a dictionary.
    """
    try:
        with open("users.json", "r") as file:
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
