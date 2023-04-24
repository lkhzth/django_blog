
from django.contrib import admin
from django.urls import path, include

import single_pages

urlpatterns = [
    path('', include('single_pages.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))
]
