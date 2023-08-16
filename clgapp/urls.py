from django.urls import path
from .import views

urlpatterns = [
   path('',views.home,name='home'),
   path('adminpanel',views.adminpanel,name='adminpanel'),
   path('add_course',views.add_course,name='add_course'),
   path('add_student',views.add_student,name='add_student'),
   path('signup',views.signup,name='signup'),
   path('courseadd',views.courseadd,name='courseadd'),
   path('std_add',views.std_add,name='std_add'),
   path('showstd_details',views.showstd_details,name='showstd_details'),
   path('edit/<int:pk>',views.edit,name='edit'),
   path('edit_details/<int:pk>',views.edit_details,name='edit_details'),
   path('delete/<int:pk>',views.delete,name='delete'),
   path('reg',views.reg,name='reg'),
   path('adminlogin',views.adminlogin,name='adminlogin'),
   path('showtchr',views.showtchr,name='showtchr'),
   path('delete_th/<int:pk>',views.delete_th,name='delete_th'),
   path('th_edit',views.th_edit,name='th_edit'),
   path('edit_details1/<int:pk>',views.edit_details1,name='edit_details1'),
   path('profile',views.profile,name='profile'),
   path('logout1',views.logout1,name='logout1'),
   path('th_home',views.th_home,name='th_home')
   

   
]