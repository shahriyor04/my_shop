from django.urls import path, include

urlpatterns = [
    path('user/', include('user.urls')),
    path('product/', include('prodct.urls')),
    path('clent/', include('clent.urls')),

]
