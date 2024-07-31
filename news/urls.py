from django.urls import path

from.views import(
    HomeView,ContactView,NewsDetailView
)



urlpatterns = [
    path('',view=HomeView.as_view(),name='home_page'),
    path('contact/',view=ContactView.as_view(),name='contact_page'),
    path('news-detail',view=NewsDetailView.as_view(),name='news_deetil_page')
]

