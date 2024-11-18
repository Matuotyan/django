from django.urls import path
from .views import job_list, apply_for_job,register,job_detail,base,application_confirmation

urlpatterns = [
    path('',base,name='base'),
    path('job_list/', job_list, name='job_list'),
    path('apply/<int:job_id>/', apply_for_job, name='apply_for_job'),
    path('register/', register, name='register'),  # 会員登録のURL
    path('detail/<int:job_id>/', job_detail, name='job_detail'),
    path('application_confirmation/', application_confirmation, name='application_confirmation'),
]


