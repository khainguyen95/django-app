from django.conf.urls import url
from cow import views
urlpatterns=[
    url(r'^$',views.user_list),
    url(r'^(?P<pk>[0-9]+)/$',views.user_detail)
]