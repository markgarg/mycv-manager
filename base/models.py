from django.db import models


class Competency(models.Model):
    """Models Technical Competency."""

    name = models.CharField(max_length=100, unique=True)
    used_from_date = models.DateField()
    used_to_date = models.DateField(null=True, blank=True)
    primary = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Competencies'

    def __str__(self):
        """Representation."""
        readable_used_from_date = "{:%B %Y}".format(self.used_from_date)
        if(self.used_to_date):
            readable_used_to_date = "{:%B %Y}".format(self.used_to_date)
            return "Used {0} from {1} to {2}".format(
                self.name, readable_used_from_date,
                readable_used_to_date)
        else:
            return "Using {0} from {1}".format(self.name,
                                               readable_used_from_date)

    # def get_absolute_url(self):
    #     """Unique URL for the competency."""
    #     from django.urls import reverse
    #     return reverse('', args=[self.name])

    # def save(self, *args, **kwargs):
    #     """Override save."""
    #     if(self.used_to_date):
    #         self.days_used = self.days_between(self.used_from_date,
    #                                            self.used_to_date)
    #     super().save(*args, **kwargs)

    # def days_between(self, from_date, to_date):
    #     """Calculate days between from_date and to_date.

    #     To be extended later for months/years between.
    #     """
    #     return to_date - from_date
