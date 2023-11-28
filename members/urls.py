from django.urls import path
from .views import TeamMemberListView, TeamMemberCreateView, TeamMemberUpdateView, TeamMemberDeleteView

urlpatterns = [
    path('', TeamMemberListView.as_view(), name='team-list'),    
    path('add/', TeamMemberCreateView.as_view(), name='team-add'),
    path('<int:pk>/edit/', TeamMemberUpdateView.as_view(), name='team-update'),
    path('<int:pk>/delete/', TeamMemberDeleteView.as_view(), name='team-delete'),
]