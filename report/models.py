from django.db import models


class DateTimeModel(models.Model):
    Prev_Start = models.DateTimeField()
    Prev_End = models.DateTimeField()
    Curr_Start = models.DateTimeField()
    Curr_End = models.DateTimeField()
