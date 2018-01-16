from django.db import models


class Competency(models.Model):
    """Models Technical Competency."""

    technology = models.CharField(max_length=100)
    used_from_date = models.DateField()
    used_to_date = models.DateField(null=True, blank=True)

    def __str__(self):
        readable_used_from_date = "{:%B %Y}".format(self.used_from_date)
        if(self.used_to_date):
            readable_used_to_date = "{:%B %Y}".format(self.used_to_date)
            return "Used {0} from {1} to {2}".format(
                self.technology, readable_used_from_date,
                readable_used_to_date)
        else:
            return "Using {0} from {1}".format(self.technology,
                                               readable_used_from_date)
