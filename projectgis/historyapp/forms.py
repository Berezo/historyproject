from django.contrib.gis import forms
from .models import WojnaTrzydziestoletnia, PowstanieStyczniowe, PowstanieListopadowe, RewolucjaAmerykanska

class LoginForm(forms.Form):
    loginClass = forms.TextInput(attrs={'class': 'form-control'})
    passwordClass = forms.PasswordInput(attrs={'class': 'form-control'})
    login = forms.CharField(widget=loginClass, label='Login', max_length=50, required=True)
    password = forms.CharField(widget=passwordClass, label='Password', max_length=50, required=True)

class RegisterForm(forms.Form):
    loginClass = forms.TextInput(attrs={'class': 'form-control'})
    passwordClass = forms.PasswordInput(attrs={'class': 'form-control'})
    login = forms.CharField(widget=loginClass, label='Login', max_length=50, required=True)
    email = forms.CharField(widget=loginClass, label='Email', max_length=50, required=True)
    password = forms.CharField(widget=passwordClass, label='Password', max_length=50, required=True)

class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if type(self.fields[field]) == type(forms.DateField()):
                self.fields[field].widget.input_type = 'date'
            
            if field != 'typ':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })
            else:
                self.fields[field].widget.attrs.update({
                    'class': 'form-select'
                })

class WojnaTrzydziestoletniaForm(BootstrapModelForm):
    nazwa = forms.CharField(max_length=80, required=True)
    geometry = forms.PointField(required=False, widget=forms.OSMWidget(attrs={'map_width': 1300, 'map_height': 500, 'template_name': 'gis/openlayers-osm.html', 'default_lat': 50.89, 'default_lon': 10.88, 'default_zoom': 6}))

    class Meta:
        model = WojnaTrzydziestoletnia
        fields = ["nazwa", "typ", "data", "okres", "opis", "str_kon_1", "str_kon_2", "dowod_1", "dowod_2", "zwyciestwo", "geometry",]

class PowstanieStycznioweForm(BootstrapModelForm):
    nazwa = forms.CharField(max_length=80, required=True)
    geometry = forms.PointField(required=False, widget=forms.OSMWidget(attrs={'map_width': 1300, 'map_height': 500, 'template_name': 'gis/openlayers-osm.html', 'default_lat': 50.89, 'default_lon': 10.88, 'default_zoom': 6}))

    class Meta:
        model = PowstanieStyczniowe
        fields = ["nazwa", "typ", "data", "okres", "opis", "str_kon_1", "str_kon_2", "dowod_1", "dowod_2", "zwyciestwo", "geometry",]

class PowstanieListopadoweForm(BootstrapModelForm):
    nazwa = forms.CharField(max_length=80, required=True)
    geometry = forms.PointField(required=False, widget=forms.OSMWidget(attrs={'map_width': 1300, 'map_height': 500, 'template_name': 'gis/openlayers-osm.html', 'default_lat': 50.89, 'default_lon': 10.88, 'default_zoom': 6}))

    class Meta:
        model = PowstanieListopadowe
        fields = ["nazwa", "typ", "data", "okres", "opis", "str_kon_1", "str_kon_2", "dowod_1", "dowod_2", "zwyciestwo", "geometry",]

class RewolucjaAmerykanskaForm(BootstrapModelForm):
    nazwa = forms.CharField(max_length=80, required=True)
    geometry = forms.PointField(required=False, widget=forms.OSMWidget(attrs={'map_width': 1300, 'map_height': 500, 'template_name': 'gis/openlayers-osm.html', 'default_lat': 50.89, 'default_lon': 10.88, 'default_zoom': 6}))

    class Meta:
        model = RewolucjaAmerykanska
        fields = ["nazwa", "typ", "data", "okres", "opis", "str_kon_1", "str_kon_2", "dowod_1", "dowod_2", "zwyciestwo", "geometry",]
