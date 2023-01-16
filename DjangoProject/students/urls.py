from django.urls import path
from . import views


app_name = 'students'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('dailyclinicrecords/', views.dailyclinicrecords, name='dailyclinicrecords'),
    path('add', views.add, name='add'),
    path('dailyclinicrecords/addvisitor/', views.addvisitor, name='addvisitor'),
    path('dailyclinicrecords/addvisitor/processaddvisitor', views.processaddvisitor, name='processaddvisitor'),
    path('<int:student_id>/edit/', views.edit, name='edit'),
    path('<int:student_id>/processedit/', views.processedit, name='processedit'),
    path('search', views.search, name='search'),
    path('processadd', views.processadd, name='processadd'),
    path('<int:student_id>/detail/', views.detail, name='detail'),
    path('detail/<int:data_id>', views.addstudentrecord, name='addstudentrecord'),
    path('<int:student_id>/delete/', views.delete, name='delete')
]
