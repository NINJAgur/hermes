from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")),
    path("chat/", include("apps.chat.urls"))
]

handler400="apps.helpers.views.error400"
handler403="apps.helpers.views.error403"
handler404="apps.helpers.views.error404"
handler500="apps.helpers.views.error500"