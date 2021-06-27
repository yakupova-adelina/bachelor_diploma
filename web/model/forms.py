from django import forms


class ObservationForm(forms.Form):
    admission_condition = forms.ChoiceField(
        label="Условие поступления",
        choices=(("1", "БВИ"), ("2", "Общий конкурс"), ("3", "Льгота"),
                 ("4", "Контракт"), ("5", "Грант"), ("6", "Целевое")),
        widget=forms.Select(attrs={"display": "table-cell"})
    )
    exam_math = forms.IntegerField(
        label="ЕГЭ по математике",
        widget=forms.NumberInput(attrs={"display": "table-cell"})
    )
    exam_inf = forms.IntegerField(
        label="ЕГЭ по информатике",
        widget=forms.NumberInput(attrs={"display": "table-cell"})
    )
    exam_rus = forms.IntegerField(
        label="ЕГЭ по русскому языку",
        widget=forms.NumberInput(attrs={"display": "table-cell"})
    )
    individual_achievements = forms.FloatField(
        label="ИД",
        widget=forms.NumberInput(attrs={"display": "table-cell"})
    )
    student_mark_math = forms.FloatField(
        label="Оценка по математике от студента",
        widget=forms.NumberInput(attrs={"display": "table-cell"})
    )
    student_mark_inf = forms.FloatField(
        label="Оценка по информатике от студента",
        widget=forms.NumberInput(attrs={"display": "table-cell"})
    )
    math_olymp_100 = forms.BooleanField(
        label="Есть 100 баллов по математике за олимпиаду",
        required=False,
        widget=forms.CheckboxInput(attrs={"display": "table-cell"})
    )
    inf_olymp_100 = forms.BooleanField(
        label="Есть 100 баллов по информатике за олимпиаду",
        required=False,
        widget=forms.CheckboxInput(attrs={"display": "table-cell"})
    )
    math_olymp_bvi = forms.BooleanField(
        label="Есть БВИ по математике",
        required=False,
        widget=forms.CheckboxInput(attrs={"display": "table-cell"})
    )
    inf_olymp_bvi = forms.BooleanField(
        label="Есть БВИ по информатике",
        required=False,
        widget=forms.CheckboxInput(attrs={"display": "table-cell"})
    )
