from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from landing.models import QPApplication
from dashboard.models import ScoreApplication
from django.shortcuts import get_object_or_404
from . import forms

@login_required
def index(request):
    return render(request, 'dashboard.html', context={})

@login_required
def scoring(request):
    context={
        'qpapplications': QPApplication.objects.all(),
    }
    return render(request, 'scoring.html', context)

@login_required
def score_applicant(request, appid):
    instance = get_object_or_404(QPApplication, id=appid)
    existing = ScoreApplication.objects.filter(scorer_id=request.user.id, application_id=instance.id)
    check_existing = existing and existing.count() > 0

    if request.method == "POST":
        update_form = forms.UpdateQPApplication(request.POST, instance=instance)
        score_form = forms.ScoreApplicationForm(request.POST)

        if score_form.is_valid() and update_form.is_valid():
            post_score = score_form.save(commit=False)
            post_application = update_form.save(commit=False)
            post_score.application_id = instance.id
            post_score.scorer_id = request.user.id
            post_application.num_of_scores = instance.num_of_scores + 1
            post_application.score = post_score.score + instance.score
            post_score.save()
            post_application.save()
            return redirect('scoring')

    else:
        update_form = forms.UpdateQPApplication(instance=instance)
        score_form = forms.ScoreApplicationForm()

    context={
        'applicant': instance,
        'score_form': score_form,
        'update_form': update_form,
        'check_existing': check_existing,
    }

    return render(request, 'score_applicant.html', context)