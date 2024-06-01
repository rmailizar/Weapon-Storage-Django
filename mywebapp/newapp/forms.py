# forms.py
from django import forms

class StokForm(forms.Form):
    jumlah_perubahan = forms.IntegerField(label='Jumlah Perubahan')

class KurangiStokForm(StokForm):
    pass

class TambahStokForm(StokForm):
    pass
