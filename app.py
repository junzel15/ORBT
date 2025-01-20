import flet as ft
from splashscreens.splash_screen import SplashScreen
from registration.registration_page import RegistrationPage
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


def go_to(route, page):
    if route == "/booking":
        page.views.clear()

    view = None
    if route == "/splash":
        view = SplashScreen(page, lambda r: go_to(r, page))
    elif route == "/onboarding1":
        view = OnboardingStep1(page, lambda r: go_to(r, page))
    elif route == "/onboarding2":
        view = OnboardingStep2(page, lambda r: go_to(r, page))
    elif route == "/onboarding3":
        view = OnboardingStep3(page, lambda r: go_to(r, page))
    elif route == "/registration":
        view = RegistrationPage(page, lambda r: go_to(r, page))
    elif route == "/booking":
        booking_page = BookingPage(page, lambda r: go_to(r, page))
        view = booking_page.render()
    elif route == "/dining/coffee":
        dining_page = DiningCoffeePage(page, lambda r: go_to(r, page))
        view = dining_page.render()
    elif route == "/dining/brunch":
        dining_page = DiningBrunchPage(page, lambda r: go_to(r, page))
        view = dining_page.render()
    elif route == "/dining/diner":
        dining_page = DiningDinerPage(page, lambda r: go_to(r, page))
        view = dining_page.render()
    elif route == "/bars":
        bars_page = BarsPage(page, lambda r: go_to(r, page))
        view = bars_page.render()
    elif route == "/experience":
        experience_page = ExperiencePage(page, lambda r: go_to(r, page))
        view = experience_page.render()
    elif route == "/profile":
        profile_page = ProfilePage(page, lambda r: go_to(r, page))
        view = profile_page.render()
    elif route == "/profile/settings":
        profile_settings_page = ProfileSettingsPage(page, lambda r: go_to(r, page))
        view = profile_settings_page.render()
    elif route == "/profile/edit":
        profile_edit_page = ProfileEditPage(page, lambda r: go_to(r, page))
        view = profile_edit_page.render()
    elif route == "/messages":
        messages_page = MessagesPage(page, lambda r: go_to(r, page))
        view = messages_page.render()
    elif route == "/bookings/upcoming":
        upcoming_page = UpcomingPage(page, lambda r: go_to(r, page))
        view = upcoming_page.render()
    elif route == "/bookings/completed":
        completed_page = CompletedPage(page, lambda r: go_to(r, page))
        view = completed_page.render()
    elif route == "/bookings/cancelled":
        cancelled_page = CancelledPage(page, lambda r: go_to(r, page))
        view = cancelled_page.render()
    else:
        print(f"Unknown route: {route}")

    if view:
        if (
            len(page.views) == 0
            or not hasattr(page.views[-1], "route")
            or page.views[-1].route != route
        ):
            page.views.append(view)
        else:
            page.views.pop()

        if hasattr(view, "route"):
            page.go(view.route)
        else:
            print("Error: View does not have a 'route' attribute.")

        page.update()


def main(page: ft.Page):
    page.on_route_change = lambda _: go_to(page.route, page)
    go_to("/booking", page)


ft.app(target=main)
