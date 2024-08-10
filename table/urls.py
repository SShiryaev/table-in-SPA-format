from table.apps import TableConfig
from rest_framework.routers import DefaultRouter
from table.views import TableViewSet

app_name = TableConfig.name

router = DefaultRouter()
router.register(r'table', TableViewSet, basename='table')

urlpatterns = [

] + router.urls
