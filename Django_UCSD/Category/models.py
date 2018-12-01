from django.db import models

# Create your models here.
CATEGORYKEYWORDS = (
    ('S', 'Software'),
    ('E', 'Engineering'),
    ('H', 'Hardware'),
    ('EM', 'Embedded'),
    ('A', 'Aerospace'),
    ('AR', 'Art'),
    ('B', 'Business'),
    ('M', 'Math'),
    ('AC', 'Accounting'),
    ('PHY', 'Physics'),
    ('COMM', 'Communication'),
    ('C', 'Computer'),
    ('SC', 'Science'),
    ('MUS', 'Music'),
    ('BIO', 'Biology'),
    ('BE', 'BioEngineering'),
    ('CHEM', 'Chemistry'),
    ('ELE', 'Electrical'),
    ('BC', 'BioChemistry'),
    ('L', 'Laborer')
)



class Category(models.Model):
    category_name = models.CharField(primary_key=True, max_length=100, choices=CATEGORYKEYWORDS)

    def __str__(self):
        return self.category_name
