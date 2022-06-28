import datetime

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

MAX_NAME_LENGTH = 100
MIN_DATE_OF_BIRTH = datetime.date(1900, 1, 1)


# ISO/IEC 5218 gender
class GenderChoices(models.IntegerChoices):
    NOT_KNOWN = 0, _("not known")
    MALE = 1, _("male")
    FEMALE = 2, _("female")
    NOT_APPLICABLE = 9, _("not applicable")


class Person(models.Model):
    first_name: str = models.CharField(max_length=MAX_NAME_LENGTH, verbose_name=_("first name"))
    last_name: str = models.CharField(max_length=MAX_NAME_LENGTH, verbose_name=_("last name"))
    gender: str = models.IntegerField(
        choices=GenderChoices.choices, default=GenderChoices.NOT_KNOWN, verbose_name=_("gender")
    )
    date_of_birth: datetime.date = models.DateField(
        blank=True, null=True, validators=[MinValueValidator(MIN_DATE_OF_BIRTH)], verbose_name=_("date of birth")
    )

    class Meta:
        ordering = ("last_name", "first_name", "date_of_birth", "id")
        verbose_name = _("person")
        verbose_name_plural = _("persons")
