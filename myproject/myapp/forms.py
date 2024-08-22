from wtforms import SubmitField
from .models import Data
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column

class Mydata(forms.ModelForm):
    class Meta:
        model=Data
        fields='__all__'
def __init__(self,*args,**kwargs):
    super(Mydata,self).__init__(*args,**kwargs)
    self.fields['mobile'].widget.attrs.update({'style':'width:150px;'})
    self.fields['keyboard'].widget.attrs.update({'style':'width:150px;'})
    self.fields['monitor'].widget.attrs.update({'style':'width:150px;'})

    self.helper = FormHelper(self)
    self.helper.layout = Layout(
        Row(
             Column('mobile',css_class='form-group col-md-4 mb-0'),
             Column('keyboard',css_class='form-group col-md-4 mb-0'),
             Column('monitor',css_class='form-group col-md-4 mb-0'),
         ),
         SubmitField('submit','submit')
    )
