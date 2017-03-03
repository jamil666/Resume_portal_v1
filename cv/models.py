from django.db import models
from cv_portal import settings

# Create your models here.

LanguageChoice = (

    ('Fluent', 'Fluent'),
    ('Good', 'Good'),
    ('Bad', 'Bad'),

                )


class Profile(models.Model):
    def __str__(self):
        FullName = self.FirstName + " " + self.LastName
        return FullName



    # Account information

    FirstName = models.CharField(max_length=200, null=False)
    LastName = models.CharField(max_length=200, null=False)
    Password = models.CharField(max_length=50, null=False)
    Username = models.CharField(max_length=200, null=False, blank=True, unique=True)
    Date = models.DateTimeField('date published', blank=True)

    # User info

    Position = models.CharField(max_length=200, null=True, blank=True)
    Address = models.CharField(max_length=255, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Tel = models.CharField(max_length=100, null=True, blank=True)
    Photo = models.FileField(blank=True, upload_to="cv/static/images/profile_photos/")
    PhotoName = models.CharField(max_length=50, null=True, blank=True)
    LinkedIn = models.CharField(max_length=255, null=True, blank=True)

    # Education info

    Date_01 = models.CharField(max_length=100, null=True, blank=True)
    Study_Place_1 = models.CharField(max_length=200, null=True, blank=True)
    Degree_1 = models.CharField(max_length=200, null=True, blank=True)

    Date_02 = models.CharField(max_length=100, null=True, blank=True)
    Study_Place_2 = models.CharField(max_length=200, null=True, blank=True)
    Degree_2 = models.CharField(max_length=200, null=True, blank=True)

    Date_03 = models.CharField(max_length=100, null=True, blank=True)
    Study_Place_3 = models.CharField(max_length=200, null=True, blank=True)
    Degree_3 = models.CharField(max_length=200, null=True, blank=True)

    Date_04 = models.CharField(max_length=100, null=True, blank=True)
    Study_Place_4 = models.CharField(max_length=200, null=True, blank=True)
    Degree_4 = models.CharField(max_length=200, null=True, blank=True)

    # Work Experience

    WorkDate1 = models.CharField(max_length=100, blank=True)
    Work1 = models.CharField(max_length=100, blank=True)
    Position1 = models.CharField(max_length=200, blank=True)

    WorkDate2 = models.CharField(max_length=100, blank=True)
    Work2 = models.CharField(max_length=100, blank=True)
    Position2 = models.CharField(max_length=200, blank=True)

    WorkDate3 = models.CharField(max_length=100, blank=True)
    Work3 = models.CharField(max_length=100, blank=True)
    Position3 = models.CharField(max_length=200, blank=True)

    WorkDate4 = models.CharField(max_length=100, blank=True)
    Work4 = models.CharField(max_length=100, blank=True)
    Position4 = models.CharField(max_length=200, blank=True)

    WorkDate5 = models.CharField(max_length=100, blank=True)
    Work5 = models.CharField(max_length=100, blank=True)
    Position5 = models.CharField(max_length=200, blank=True)

    WorkDate6 = models.CharField(max_length=100, blank=True)
    Work6 = models.CharField(max_length=100, blank=True)
    Position6 = models.CharField(max_length=200, blank=True)

    # Skills

    Skill_1 = models.CharField(max_length=255, blank=True)
    Skill_2 = models.CharField(max_length=255, blank=True)
    Skill_3 = models.CharField(max_length=255, blank=True)
    Skill_4 = models.CharField(max_length=255, blank=True)
    Skill_5 = models.CharField(max_length=255, blank=True)
    Skill_6 = models.CharField(max_length=255, blank=True)
    Skill_7 = models.CharField(max_length=255, blank=True)
    Skill_8 = models.CharField(max_length=255, blank=True)
    Skill_9 = models.CharField(max_length=255, blank=True)
    Skill_10 = models.CharField(max_length=255, blank=True)
    Skill_11 = models.CharField(max_length=255, blank=True)
    Skill_12 = models.CharField(max_length=255, blank=True)
    Skill_13 = models.CharField(max_length=255, blank=True)
    Skill_14 = models.CharField(max_length=255, blank=True)
    Skill_15 = models.CharField(max_length=255, blank=True)
    Skill_16 = models.CharField(max_length=255, blank=True)
    Skill_17 = models.CharField(max_length=255, blank=True)
    Skill_18 = models.CharField(max_length=255, blank=True)
    Skill_19 = models.CharField(max_length=255, blank=True)
    Skill_20 = models.CharField(max_length=255, blank=True)
    Skill_21 = models.CharField(max_length=255, blank=True)
    Skill_22 = models.CharField(max_length=255, blank=True)
    Skill_23 = models.CharField(max_length=255, blank=True)
    Skill_24 = models.CharField(max_length=255, blank=True)
    Skill_25 = models.CharField(max_length=255, blank=True)
    Skill_26 = models.CharField(max_length=255, blank=True)
    Skill_27 = models.CharField(max_length=255, blank=True)
    Skill_28 = models.CharField(max_length=255, blank=True)
    Skill_29 = models.CharField(max_length=255, blank=True)
    Skill_30 = models.CharField(max_length=255, blank=True)

    # Languages

    Language_1 = models.CharField(max_length=100, blank=True)
    Language_1_Quality = models.CharField(max_length=255, blank=True, choices=LanguageChoice)
    Language_2 = models.CharField(max_length=100, blank=True)
    Language_2_Quality = models.CharField(max_length=255, blank=True, choices=LanguageChoice)
    Language_3 = models.CharField(max_length=100, blank=True)
    Language_3_Quality = models.CharField(max_length=255, blank=True, choices=LanguageChoice)
    Language_4 = models.CharField(max_length=100, blank=True)
    Language_4_Quality = models.CharField(max_length=255, blank=True, choices=LanguageChoice)
    Language_5 = models.CharField(max_length=100, blank=True)
    Language_5_Quality = models.CharField(max_length=255, blank=True, choices=LanguageChoice)

    # Certificates

    Certificate_1 = models.CharField(max_length=200, blank=True)
    Certificate_2 = models.CharField(max_length=200, blank=True)
    Certificate_3 = models.CharField(max_length=200, blank=True)
    Certificate_4 = models.CharField(max_length=200, blank=True)
    Certificate_5 = models.CharField(max_length=200, blank=True)
    Certificate_6 = models.CharField(max_length=200, blank=True)
    Certificate_7 = models.CharField(max_length=200, blank=True)
    Certificate_8 = models.CharField(max_length=200, blank=True)
    Certificate_9 = models.CharField(max_length=200, blank=True)
    Certificate_10 = models.CharField(max_length=200, blank=True)


