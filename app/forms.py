# from django import forms
# def check_for_a(value):
#         if value[0].lower()=='a':
#             raise forms.ValidationError('Not Start with a')
        
# class StudentForm(forms.Form):
#     Sname=forms.CharField(max_length=100,validators=[check_for_a])
#     Sage=forms.IntegerField()
#     Email=forms.EmailField(validators=[check_for_a,validators.ma])
#     Email=forms.EmailField()
#     Re_Enter_Email=forms.EmailField()
#     botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)

#     def clean(self):
#          e=self.cleaned_data['Email']
#          r=self.cleaned_data['Re_Enter_Email']
#          if e!=r:
#             raise forms.ValidationError('Not matched')
         
#     def clean_botcatcher(self):
#         bot=self.cleaned_data['botcatcher']
#         if len(bot)>0:
#              raise forms.ValidationError()
        

from django import forms

from django.core import validators
def check_for_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('name started with a')

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a])
    name=forms.CharField(max_length=100,validators=[check_for_a,validators.MaxLengthValidator(5)])
    age=forms.IntegerField()
    email=forms.EmailField()
    re_enter_email=forms.EmailField()
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)

    mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['re_enter_email']