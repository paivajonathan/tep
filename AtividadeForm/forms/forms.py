from django import forms


class CustomDateInput(forms.DateInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {})
        kwargs['attrs'].update({
            'type': 'date',
        })
        super().__init__(*args, **kwargs)


class MyForm(forms.Form):
    choices = (
        ('S', 'Student'),
        ('T', 'Teacher')
    )

    name = forms.CharField()
    role = forms.ChoiceField(choices=choices)
    date_birth = forms.DateField(widget=CustomDateInput())
    document = forms.FileField(required=False)

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if len(name) < 3:
            raise forms.ValidationError('Name must have at least 3 characters.')
        
        return name
