from django.urls import include, path

from levstik.views.home import HomeView, AboutUs
from levstik.views.profile import ProfileView
from levstik.views.register import RegisterView
from levstik.views.winner import CreateWinnerView, EditWinnerView
from levstik.views.winner_profile import WinnerProfileView
from levstik.views.winners import WinnersView


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('', include('django.contrib.auth.urls')),
    path('about-us/', AboutUs.as_view(), name="about_us"),
    path('register/', RegisterView.as_view(), name="register"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('winner/', CreateWinnerView.as_view(), name="create_winner"),
    path('winner/<int:id>/edit/', EditWinnerView.as_view(), name="edit_winner"),
    path('winner/<slug:slug>/', WinnerProfileView.as_view(), name="winner_profile"),
    path('winners/', WinnersView.as_view(), name="winners"),
]
