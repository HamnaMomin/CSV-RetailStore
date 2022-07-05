# Upload RetailStore CSV File
This project is all about Upload and persist pricing feeds from retail stores using csv file.
Search for pricing records using various criteria and be able to edit/save changes to any record.

**Steps for set up -**
1-Create Virtual environment in any directory -Here I have created ApiEnv
python -m venv CsvEnv

2-Activate virtual environment you have created using below command
CsvEnv/Scripts/activate

3-Install the packages according to the configuration file requirements.txt using below command
pip install -r requirements.txt

4- Go to RetailStoreCsv project directory and create superuser to see data in admin panel
python manage.py createsuperuser username

5-start your server 
python manage.py runserver

6-Go to urls specified in urls.py file to check functionality.
