from django import forms

from .models import Selecao

class SelecaoForm(forms.ModelForm):
	class Meta:
		model = Selecao