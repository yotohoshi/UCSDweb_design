from django.db import models

# Create your models here.
OFFER_POSITION = (
    ('S', 'Software'),
    ('E', 'Engineering'),
    ('H', 'Hardware'),
    ('EM', 'Embedded'),
    ('A', 'Aerospace'),
    ('AR', 'Art'),
    ('B', 'Business'),
    ('M', 'Math'),
    ('AC', 'Accounting'),
    ('Phy', 'Physics'),
    ('COMM', 'Communication'),
    ('C', 'Computer'),
    ('S', 'Science'),
    ('MUS', 'Music'),
    ('BIO', 'Biology'),
    ('BIOL', 'Biological'),
    ('BE', 'BioEngineering'),
    ('Che', 'Chemistry'),
    ('ELE', 'Electrical'),
    ('BC', 'BioChemistry'),

)


class Category(models.Model):
    category = models.CharField(max_length=100, choices=OFFER_POSITION, null=True, blank=True)
    def __str__(self):
        return self.category