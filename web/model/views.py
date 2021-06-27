import pickle
import numpy as np
from django.shortcuts import render
from .forms import ObservationForm


def get_observation(request):
    if request.method == 'POST':
        form = ObservationForm(request.POST)
        if form.is_valid():
            with open("/usr/src/pca", 'rb') as file:
                pca = pickle.load(file)
            with open("/usr/src/logreg", 'rb') as file:
                logreg = pickle.load(file)
            good_admission_conditions = ["БВИ", "ОК", "Грант"]
            is_good = int(form.cleaned_data.get("admission_condition") in
                          good_admission_conditions)
            observation = np.array([
                form.cleaned_data.get("exam_math"),
                form.cleaned_data.get("exam_inf"),
                form.cleaned_data.get("exam_rus"),
                form.cleaned_data.get("individual_achievements"),
                form.cleaned_data.get("student_mark_math"),
                form.cleaned_data.get("student_mark_inf"),
                form.cleaned_data.get("math_olymp_100"),
                form.cleaned_data.get("inf_olymp_100"),
                form.cleaned_data.get("math_olymp_bvi"),
                form.cleaned_data.get("inf_olymp_bvi"),
                is_good
            ])
            proba = logreg.predict(pca.transform([observation]))
            answer = "Отчислят" if proba[0] else "Не отчислят"
            return render(request, 'model/answer.html',
                          {'proba': answer})

    else:
        form = ObservationForm()

    return render(request, 'model/index.html', {'form': form})
