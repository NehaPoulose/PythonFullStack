from .import views
from django.urls import path

urlpatterns = [

    path('',views.basic,name = 'Home'),
    path('delete/<int:task_id>/',views.delete,name = 'Delete'),
    path('update/<int:id>/',views.update,name = 'Update'),
    path('clsgenlist/',views.Task_list.as_view(),name = 'GenericListView'),
    path('clsgendetail/<int:pk>/',views.Task_detail.as_view(),name = 'GenericDetailView'),
    path('clsgenupdate/<int:pk>/',views.Task_Update.as_view(),name = 'GenericUpdateView'),
    path('clsgendelete/<int:pk>/',views.Task_delete.as_view(),name = 'GenericDeleteView'),
]
