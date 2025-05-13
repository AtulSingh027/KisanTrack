set -o errexit  

pip install -r requirements.txt
python KisanTrack/manage.py collectstatic --noinput
python KisanTrack/manage.py migrate