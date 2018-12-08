echo "Install Django and Dependencies"
# install Django
pip3 install django

# install nltk
pip3 install nltk

# install overrides
pip3 install overrides

# run python import nltk and run nltk.download('stopwords')
# python3 -c 'import nltk; nltk.download('stopwords')'
python3 install_nltk.py

echo "Finish installation"

# Pre-set

# change migration script to executable
chmod +x ./migrationreset.sh
echo "Changed migrationreset.sh to executable"
# reset migration
./migrationreset.sh
echo "Executed migration reset"
# migrate django database
echo "Make migrations"
python3 manage.py makemigrations
echo "Finished migrations"
echo "Migrate"
python3 manage.py migrate
echo "Finished Migrate"

# migrate django database

# input yes while encounter with command line
echo "Flushing database"
python3 manage.py flush
echo "Finished flushing"

echo "Make migrations"
python3 manage.py makemigrations
echo "Finished migrations"

echo "Migrate"
python3 manage.py migrate
echo "Finished Migrate"

echo "RUN generato.py then generate.py"
python3 manage.py shell < generato.py
python3 manage.py shell < generate.py
echo "Finished generato and generate"
# now run python manage.py runserver
