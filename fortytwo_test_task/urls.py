from django.conf.urls import include, url

from django.contrib import admin
import loginsys
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('loginsys.urls')),	
]
