from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'arcade.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'games.views.base_template', name='base_template'),
    url(r'^register/$', 'games.views.register', name='register'),
    url(r'^profile/$', 'games.views.profile', name='profile'),
    url(r'^memory/$', 'games.views.memory', name='memory'),
    url(r'^snake/$', 'games.views.snake', name='snake'),
    url(r'^paint/$', 'games.views.paint', name='paint'),
    url(r'^allpoke/$', 'pok.views.all_pokemon', name='all_poke'),
    url(r'^pokemon/$', 'pok.views.pokemon', name='pokemon'),
    url(r'^new_pokemon/$', 'pok.views.new_pokemon', name='new_pokemon'),
    url(r'^new_team/$', 'pok.views.new_team', name='new_team'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)
