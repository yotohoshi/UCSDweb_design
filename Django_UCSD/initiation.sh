echo "Install Django and Dependencies"
# install Django
pip install django

# install nltk
pip install nltk

# install overrides
pip install overrides

# run python import nltk and run nltk.download('stopwords')
python install_nltk.py
#python -c 'import nltk; import nltk; nltk.download('stopwords')'

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
python manage.py makemigrations
echo "Finished migrations"
echo "Migrate"
python manage.py migrate
echo "Finished Migrate"

# migrate django database

# input yes while encounter with command line
echo "Flushing database"
python manage.py flush
echo "Finished flushing"

echo "Make migrations"
python manage.py makemigrations
echo "Finished migrations"

echo "Migrate"
python manage.py migrate
echo "Finished Migrate"

echo "RUN generato.py then generate.py"
python manage.py shell < generato.py
python manage.py shell < generate.py
echo "Finished generato and generate"
# now run python manage.py runserver
