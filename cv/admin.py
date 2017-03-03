from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):

    search_fields = ('FirstName', 'LastName', 'Username', 'Password', 'Date', 'Position', 'Address', 'Email', 'Tel', 'Photo', 'LinkedIn',
                     'Date_01', 'Study_Place_1', 'Degree_1', 'Date_02', 'Study_Place_2', 'Degree_2', 'Date_03', 'Study_Place_3', 'Degree_3',
                     'Date_04', 'Study_Place_4', 'Degree_4',
                     'Skill_1', 'Skill_2', 'Skill_3', 'Skill_4', 'Skill_5', 'Skill_6', 'Skill_7', 'Skill_8', 'Skill_9', 'Skill_10', 'Skill_11', 'Skill_12', 'Skill_13', 'Skill_14', 'Skill_15', 'Skill_16',
                     'Skill_17', 'Skill_18', 'Skill_19', 'Skill_20', 'Skill_21', 'Skill_22', 'Skill_23', 'Skill_24', 'Skill_25',
                     'Skill_26', 'Skill_27', 'Skill_28', 'Skill_29', 'Skill_30',
                     'Language_1', 'Language_2', 'Language_3', 'Language_4', 'Language_5',
                     'Certificate_1', 'Certificate_2', 'Certificate_3', 'Certificate_4', 'Certificate_5', 'Certificate_6',
                     'Certificate_7', 'Certificate_8', 'Certificate_9', 'Certificate_10')

    list_display = ('FirstName', 'LastName', 'Username', 'Date')

    fieldsets = (

        ('Account Info', {'fields':
                            ('FirstName',
                             'LastName',
                             'Username',
                             'Password',
                             'Date')}),

        ('Profile Info', {'fields':
                            ('Position', 'Address', 'Email', 'Tel', 'Photo', 'LinkedIn')}),

        ('Education Info', {'fields':
                              ('Date_01', 'Study_Place_1', 'Degree_1',
                               'Date_02', 'Study_Place_2', 'Degree_2',
                               'Date_03', 'Study_Place_3', 'Degree_3',
                               'Date_04', 'Study_Place_4', 'Degree_4')}),

        ('Work Experience Info', {'fields':
                                ('WorkDate1', 'Work1', 'Position1',
                                'WorkDate2', 'Work2', 'Position2',
                                'WorkDate3', 'Work3', 'Position3',
                                'WorkDate4', 'Work4', 'Position4',
                                'WorkDate5', 'Work5', 'Position5',
                                'WorkDate6', 'Work6', 'Position6')}),

        ('Skills Info', {'fields':
                              ('Skill_1', 'Skill_2', 'Skill_3', 'Skill_4', 'Skill_5', 'Skill_6', 'Skill_7', 'Skill_8',
                               'Skill_9', 'Skill_10', 'Skill_11', 'Skill_12', 'Skill_13', 'Skill_14', 'Skill_15',
                               'Skill_16', 'Skill_17', 'Skill_18', 'Skill_19', 'Skill_20', 'Skill_21', 'Skill_22',
                               'Skill_23', 'Skill_24', 'Skill_25', 'Skill_26', 'Skill_27', 'Skill_28', 'Skill_29', 'Skill_30')}),

        ('Language Info', {'fields':
                               ('Language_1', 'Language_1_Quality',
                                'Language_2', 'Language_2_Quality',
                                'Language_3', 'Language_3_Quality',
                                'Language_4', 'Language_4_Quality',
                                'Language_5', 'Language_5_Quality',)}),

        ('Certificates Info', {'fields':
                              ('Certificate_1', 'Certificate_2', 'Certificate_3', 'Certificate_4', 'Certificate_5',
                               'Certificate_6', 'Certificate_7', 'Certificate_8', 'Certificate_9', 'Certificate_10')}),

    )


admin.site.register(Profile, ProfileAdmin)