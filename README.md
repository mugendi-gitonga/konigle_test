
1.Create a virtual environment and activate it.
    - python -m venv venv
    - source venv/Scripts/activate

1.Install all requirements
    - pip install -r requirements.txt

2.Make migrations and migrate
    - python manage.py makemigrations
    - python manage.py migrate

3.Run the local server
    - python manage.py runserver

4.To subscribe emails, go to localhost:8000, add an email in the widget's input box and click subscribe.
    - If the email does not exist, it will be added to the DB and its subscription status will be True
    - If the email exists, its subscription status will be changes to false

5.To acces the dashboard based on the figma design, go to localhost:8000/dashboard

6.To run the celery task, open a new terminal, activate the virtual environment and run the comman below. For the command to run, Erlang(https://www.erlang.org/downloads) and RabbitMQ(https://www.rabbitmq.com/) have to be installed. 
    - celery -A konigle_test worker -l INFO    ---> Mac and Ubuntu
    - celery -A konigle_test worker -l INFO --pool=solo  ---> Windows


7.to run the schedule, open a new terminal, activate the virtual environment and run the comman below. It has been designed to run every 10 seconds for test purposes but the crontab config stated in 'c' below will run it on Monday and Wednesday of every week.

    a) Start celery:
        - celery -A konigle_test worker -l INFO    ---> Mac and Ubuntu
        - celery -A konigle_test worker -l INFO --pool=solo  ---> Windows
    
    b)Start the celery scheduler:
        - celery -A konigle_test beat -l INFO

    c)Crontab config for every Monday and Wednesday. Replace the schedule field content located under 'app.conf.beat_schedule' in the `celery.py` file with the config below. The `celery.py` file is located in the project folder where `settings.py` file is located.
        
        - crontab(0, 0, day_of_week='mon,wed')