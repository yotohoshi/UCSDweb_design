#!bin/bash

# install Django
pip3 install django

# install nltk
pip3 install nltk

# install overrides
pip3 install overrides

# run python import nltk and run nltk.download('stopwords')

# change migration script to executable
chmod +x ./migrationreset.sh

# migrate django database
python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py shell<generato.py
python3 manage.py shell<generate.py

# now run python3 manage.py runserver
