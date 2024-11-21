from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(('blog.urls', 'blog',))),  # Add namespace here
    path('', lambda request: redirect('blog:csv_to_excel')),  # Redirect root URL to your upload page
]
