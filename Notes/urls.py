from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Admin's Site"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('to-dos/', user_views.todo, name='to-dos'),
    path('add-todo/', user_views.add_todo, name='add-todo'),
    path('delete-todo/<int:id>/', user_views.delete_todo, name='delete-todo'),
    path('notes/', user_views.notes, name='notes'),
    path('delete-notes/<int:docid>/', user_views.delete_note, name='delete-note'),
    path('change-status/<int:id>/<str:status>/', user_views.change_todo, name='change-status'),
    path('',include('home.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
