from django.contrib import admin

from . import models


class SchoolGradeInline(admin.TabularInline):
    model = models.SchoolGrade

@admin.register(models.Student)
class StudentAadmin(admin.ModelAdmin):
    inlines = [ SchoolGradeInline ]

admin.site.register(models.SchoolSubject)