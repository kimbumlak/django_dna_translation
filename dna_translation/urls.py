from django.contrib import admin
from django.urls import path
from translation.views import home_view, result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('result', result, name="result")
    #path('result', result)
    #path('results', HomeView.as_view()),
    #path('results', HomeView.as_view()),
]


from django.conf import settings
from django.conf.urls import include, url  # For django versions before 2.0
from django.urls import include, path  # For django versions from 2.0 and up

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns