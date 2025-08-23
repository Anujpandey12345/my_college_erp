from django.db import models

class ProjectAccounts(models.Model):
    Projectname = models.CharField(max_length=20)
    projectExpense = models.IntegerField()

    def __str__(self):
        return self.Projectname
