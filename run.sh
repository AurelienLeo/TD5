pip3 install pandas
pip3 install virtualenv
virtualenv virtual1
pip freeze > virtual1/requirements.txt
pip install -r virtual1/requirements.txt
source virtual1/scripts/activate
virtual1/bin/activate
python3 main.py
