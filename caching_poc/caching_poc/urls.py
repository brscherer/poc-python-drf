from django.urls import include, path
from rest_framework import routers

from .views import TodoListApiView, TodoDetailApiView

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('todos/', TodoListApiView.as_view()),
    path('todos/<int:todo_id>/', TodoDetailApiView.as_view()),

]