from django.urls import include, path

from levstik.views.home import HomeView, AboutUs
from levstik.views.profile import ProfileView
from levstik.views.register import RegisterView
# from levstik.views.dashboard import DashboardView
from levstik.views.winner import CreateWinnerView
# from levstik.views.provider_public_profile import ProviderPublicProfileView
from levstik.views.winners import WinnersView


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('', include('django.contrib.auth.urls')),
    path('about-us/', AboutUs.as_view(), name="about_us"),
    path('register/', RegisterView.as_view(), name="register"),
    path('profile/', ProfileView.as_view(), name="profile"),
    # path('request-provider-status/', RequestProviderStatusView.as_view(), name="request_provider_status"),
    # path('dashboard/', DashboardView.as_view(), name="dashboard"),
    path('winner/', CreateWinnerView.as_view(), name="create_winner"),
    # path('winner/<slug:slug>/', WinnerPublicProfileView.as_view(), name="public_profile"),
    path('winners/', WinnersView.as_view(), name="winners"),
]
