from django.urls import path
from .views import (
    lead_list, lead_detail, lead_create, lead_update, lead_delete,
    LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView,
    AssignAgentView
)

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),  #name 정해주기 전 프로젝트의 urls.py에서 namespace 정해줘야하는 듯
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'), #int 적어줘야 pk가 정수인걸 알아서 뒤에 url오류 안남
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name='assign-agent'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
]