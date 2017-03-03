from django.forms import ModelForm
from .models import Profile
from django import forms

class LoginForm(ModelForm):

    Password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile

        fields = ['Username', 'Password', 'FirstName', 'LastName', ]



class CVForm(ModelForm):
    #Photo = forms.ImageField(allow_empty_file=True)

    class Meta:
        model = Profile

        fields = ['Position', 'Address', 'Email', 'Tel', 'LinkedIn', 'Photo',
                    'Date_01', 'Study_Place_1', 'Degree_1',
                    'Date_02', 'Study_Place_2', 'Degree_2',
                    'Date_03', 'Study_Place_3', 'Degree_3',
                    'Date_04', 'Study_Place_4', 'Degree_4',
                    'WorkDate1', 'Work1', 'Position1',
                    'WorkDate2', 'Work2', 'Position2',
                    'WorkDate3', 'Work3', 'Position3',
                    'WorkDate4', 'Work4', 'Position4',
                    'WorkDate5', 'Work5', 'Position5',
                    'WorkDate6', 'Work6', 'Position6',
                    'Skill_1', 'Skill_2', 'Skill_3', 'Skill_4', 'Skill_5', 'Skill_6',
                    'Skill_7', 'Skill_8', 'Skill_9', 'Skill_10', 'Skill_11', 'Skill_12',
                    'Skill_13', 'Skill_14', 'Skill_15', 'Skill_16', 'Skill_17', 'Skill_18',
                    'Skill_19', 'Skill_20', 'Skill_21', 'Skill_22', 'Skill_23', 'Skill_24',
                    'Skill_25', 'Skill_26', 'Skill_27', 'Skill_28', 'Skill_29', 'Skill_30',
                    'Language_1', 'Language_2', 'Language_3', 'Language_4', 'Language_5',
                    'Certificate_1', 'Certificate_2', 'Certificate_3', 'Certificate_4', 'Certificate_5',
                    'Certificate_6', 'Certificate_7', 'Certificate_8', 'Certificate_9', 'Certificate_10' ]