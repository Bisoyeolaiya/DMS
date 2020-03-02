from django.urls import path
from docRecords import views

app_name = 'docRecords'

urlpatterns = [
    path('entry-list/', views.EntryListView.as_view(), name='list-entry'),
    path('create-entry/', views.EntryCreateView.as_view(), name='create-entry'),
    path('<slug:slug>/', views.EntryDetailView.as_view(),name='entry-detail'),
    path('<slug:slug>/update/', views.EntryUpdateView.as_view(), name='update-entry'),
    path('<slug:slug>/delete/', views.EntryDeleteView.as_view(), name='delete-entry'),
]
