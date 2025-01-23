import flet as ft


from splashscreens.splash_screen import SplashScreen
from registration.registration_page import RegistrationPage
from registration.components.verification import verification
from onboarding.onboarding_step1 import OnboardingStep1
from onboarding.onboarding_step2 import OnboardingStep2
from onboarding.onboarding_step3 import OnboardingStep3
from homepage.booking_page import BookingPage
from homepage.tabs.dining_coffee import DiningCoffeePage
from homepage.tabs.dining_brunch import DiningBrunchPage
from homepage.tabs.dining_diner import DiningDinerPage
from homepage.components.bars import BarsPage
from homepage.components.experience import ExperiencePage
from profiles.profile import ProfilePage
from profiles.profile_settings import ProfileSettingsPage
from profiles.profile_edit import ProfileEditPage
from messages.messages import MessagesPage
from bookingpage.upcoming import UpcomingPage
from bookingpage.completed import CompletedPage
from bookingpage.cancelled import CancelledPage
from login.login_page import LoginPage


ROUTES = {
    "/splash": SplashScreen,
    "/registration": RegistrationPage,
    "/verification": lambda page, phone_number: verification(
        "Verification", phone_number
    ),
    "/onboarding1": OnboardingStep1,
    "/onboarding2": OnboardingStep2,
    "/onboarding3": OnboardingStep3,
    "/booking": BookingPage,
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
}


user_name = None


def go_to(route, page, **kwargs):
    global user_name
    if "user_name" in kwargs:
        user_name = kwargs["user_name"]

    print(f"Navigating to {route} with kwargs: {kwargs}")
    view_class = ROUTES[route]
    if route == "/booking":
        view_instance = view_class(page, go_to, user_name=user_name)
    else:
        view_instance = view_class(page, go_to)
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
