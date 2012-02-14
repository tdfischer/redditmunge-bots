from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from models import Bot
from forms import BotForm

def new(request):
    if request.method == 'POST':
        form = BotForm(request.POST)
        if form.is_valid():
            bot = Bot(**form.cleaned_data)
            bot.save()
            return HttpResponseRedirect(bot.get_absolute_url())
    else:
        form = BotForm()
    return render_to_response('bots/new.html', {'form': form}, context_instance=RequestContext(request))

def edit(request, name):
    pass
