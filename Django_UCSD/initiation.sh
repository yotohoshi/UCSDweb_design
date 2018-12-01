#!bin/bash

# install Django
pip install django


# install nltk
pip install nltk


# install overrides
pip install overrides


# run python import nltk and run nltk.download('stopwords')

# change migration script to executable
chmod +x ./migrationreset.sh

# migrate django database
python manage.py makemigrations


python manage.py migrate


python manage.py shell<generato.py
python manage.py shell<generate.py

# now run python manage.py runserver
