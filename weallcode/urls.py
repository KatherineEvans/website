from django.conf.urls import include
from django.urls import path
from django.views.generic import RedirectView

from .views import (
    CreditsView,
    GetInvolvedView,
    HomeView,
    OurStoryView,
    PrivacyView,
    ProgramsSummerCampsView,
    ProgramsView,
    TeamView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='weallcode-home'),
    path('our-story/', OurStoryView.as_view(), name='weallcode-our-story'),
    path('programs/', include([
        path('', ProgramsView.as_view(), name='weallcode-programs'),
        path('summer-camps/', ProgramsSummerCampsView.as_view(), name='weallcode-programs-summer-camps'),
    ])),
    path('team/', TeamView.as_view(), name='weallcode-team'),
    path('get-involved/', GetInvolvedView.as_view(), name='weallcode-get-involved'),
    path('privacy/', PrivacyView.as_view(), name='weallcode-privacy'),
    path('credits/', CreditsView.as_view(), name='weallcode-credits'),

    # Redirect /summer-camps/ to /programs/summer-camps/
    path('summer-camps/', RedirectView.as_view(pattern_name='weallcode-programs-summer-camps')),
]
