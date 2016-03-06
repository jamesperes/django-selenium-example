from django.conf.urls import url
from todos.views import TodoActiveListView


urlpatterns = [
    url(r'^active/$', TodoActiveListView.as_view(), name="active_list"),
    url(r'^completed/$', TodoActiveListView.as_view(), name="completed_list"),
]