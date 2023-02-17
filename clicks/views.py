from django.shortcuts import render
from django.http import JsonResponse
from .forms import ClickForm
from .models import Click

def clicks_view(request):
    click = Click.objects.all()
    form = None
    
    if request.is_ajax():
        clicks = 0
        if len(click) == 0:
            click = Click()
            click.clicks = request.GET['clicks']
            clicks = request.GET['clicks']
            clisk.save()
        else:
            click_old = Click.objects.get(pk=1)
            click_old.clicks += request.GET['clicks']
            clicks = click_old.clicks
            click_old.save()
        return JsonResponse({'clicks': clicks})
    else:
        form = ClickForm(request.GET)
        if form.is_valid():
            
            print(f'length of clicks is {len(click)}')
            if len(click) == 0:
                form.save()
            else:
                click_new = form.save(commit=False)
                click_old = Click.objects.get(pk=1)
                click_old.clicks += click_new.clicks
                click_old.save()
                
        form = ClickForm()
        
        click = Click.objects.get(pk=1)
        
    context = {'form': form, 'clicks': click.clicks}
    return render(request, 'clicks/index.html', context)
