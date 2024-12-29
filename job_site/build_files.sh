curl -O https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install -r requirements.txt
python3.9 manage.py collectstatic