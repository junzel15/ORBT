import flet as ft
from splash_screen_pages.splash_screen import SplashScreen
from registration.registration_page import RegistrationPage
from onboarding_pages.onboarding_step1 import OnboardingStep1
from onboarding_pages.onboarding_step2 import OnboardingStep2
from onboarding_pages.onboarding_step3 import OnboardingStep3
from home_page_booking.booking_page import BookingPage
from home_page_booking.tabs.dining_coffee import DiningCoffeePage
from home_page_booking.tabs.dining_brunch import DiningBrunchPage
from home_page_booking.tabs.dining_diner import DiningDinerPage
from home_page_booking.components.bars import BarsPage
from home_page_booking.components.experience import ExperiencePage


def main(page: ft.Page):
    def go_to(route):
        page.views.clear()
        view = None

        if route == "/splash":
            view = SplashScreen(page, go_to)
        elif route == "/onboarding1":
            view = OnboardingStep1(page, go_to)
        elif route == "/onboarding2":
            view = OnboardingStep2(page, go_to)
        elif route == "/onboarding3":
            view = OnboardingStep3(page, go_to)
        elif route == "/registration":
            view = RegistrationPage(page, go_to)
        if route == "/booking":
            booking_page = BookingPage(page, go_to)
            view = booking_page.render()
        elif route == "/dining/coffee":
            dining_page = DiningCoffeePage(page, go_to)
            view = dining_page.render()
        elif route == "/dining/brunch":
            dining_page = DiningBrunchPage(page, go_to)
            view = dining_page.render()
        elif route == "/dining/diner":
            dining_page = DiningDinerPage(page, go_to)
            view = dining_page.render()
        elif route == "/bars":
            bars_page = BarsPage(page, go_to)
            view = bars_page.render()
        elif route == "/experience":
            experience_page = ExperiencePage(page, go_to)
            view = experience_page.render()
        else:
            print(f"Unknown route: {route}")

        if view:
            page.views.append(view)
            page.update()

    page.on_route_change = lambda _: go_to(page.route)
    go_to("/booking")


ft.app(target=main)
