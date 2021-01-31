from django.contrib import admin
from django.urls import path, include
from home.views import home
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from post.sitemaps import PostSitemap
from post.feeds import LatestPostsFeed
from search.views import search
from account.views import login, logout, registration

from django.contrib.auth import views as auth_views
sitemaps = {'post':PostSitemap}

urlpatterns = [
    path('trumbowyg/', include('trumbowyg.urls')),
    path('admin/', admin.site.urls),
    path('post/', include('post.urls', namespace='post')),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    path('feed/', LatestPostsFeed(), name='feed_post'),
    path('search/', search, name='search'),
    
    path('profile/', include('account.urls', namespace='account')),
    path('story/', include('story.urls', namespace='story')),

    # path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('registration/', registration, name='registration'),

    path('password/change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password/change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password/reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('confirm/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='confirm_reset'),
    path('confirm/reset/done/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_complete'),

    path('', home, name='home'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
