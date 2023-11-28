from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import TeamMember
from .forms import TeamMemberForm

class TeamMemberListView(ListView):
    model = TeamMember
    template_name = 'member_list.html'

class TeamMemberCreateView(CreateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'member_add.html'
    success_url = reverse_lazy('team-list')

class TeamMemberUpdateView(UpdateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'member_edit.html'
    success_url = reverse_lazy('team-list') 

class TeamMemberDeleteView(DeleteView):
    model = TeamMember
    success_url = reverse_lazy('team-list')