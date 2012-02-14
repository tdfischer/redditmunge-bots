from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from django.db import models
from models import Bot

urlpatterns = patterns('bots.views',
    url(r'^$',
        ListView.as_view(
            queryset=Bot.objects.order_by('username'),
            context_object_name='bot_list',
            template_name='bots/index.html')),
    url(r'^details/(?P<slug>.+)$',
        DetailView.as_view(
            model=Bot,
            slug_field='username',
            template_name='bots/detail.html'),
        name='bot_details'),
    url(r'^edit/(?P<name>.+)$', 'edit', name='edit_bot'),
    url(r'^new$', 'new', name='new_bot'),
)
