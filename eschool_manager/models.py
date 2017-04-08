from django.db import models
from polymorphic.models import PolymorphicModel
from django.utils.translation import ugettext as _


class Person(PolymorphicModel):
    first_name = models.CharField(max_length=255, verbose_name=_('Imię'))
    last_name = models.CharField(max_length=255, verbose_name=_('Nazwisko'))
    street = models.CharField(max_length=255, verbose_name=_('Ulica'), blank=True)
    city = models.CharField(max_length=255, verbose_name=_('Miejscowość'), blank=True)
    postal = models.CharField(max_length=255, verbose_name=_('Kod pocztowy'), blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.first_name + " " + self.last_name


class Student(Person):
    class Meta:
        verbose_name = _('Uczeń')
        verbose_name_plural = _('Ucznowie')


class SchoolGrade(models.Model):
    GRADE_CHOICE = (
        (1, 'Niedostateczny'),
        (2, 'Dopuszczający'),
        (3, 'Dostateczny'),
        (4, 'Dobry'),
        (5, 'Bardzo Dobry'),
        (6, 'Celujący'),
    )
    grade = models.IntegerField(_('Ocena'), choices=GRADE_CHOICE)

    student = models.ForeignKey('Student', on_delete=models.CASCADE, verbose_name=_("Uczeń"))
    subject = models.ForeignKey('SchoolSubject', on_delete=models.CASCADE, verbose_name=_('Przedmiot'))

    def __str__(self):
        return "{}, {}, {}".format(self.student, self.subject, self.grade)


class SchoolSubject(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Imię'))

    class Meta:
        verbose_name = _('Przedmiot')
        verbose_name_plural = _('Przedmioty')

    def __str__(self):
        return self.name
