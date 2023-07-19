from airflow.models import DAG
from datetime import datetime
from datetime import timedelta
from airflow.operators.python_operator import PythonOperator
import requests
from bs4 import BeautifulSoup
from os.path import expanduser
import os


default_args = {
    'owner': 'Ivan',
    'depends_on_past': False,
    'email': ['ivan@theaicore.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'start_date': datetime(2020, 1, 1), # If you set a datetime previous to the curernt date, it will try to backfill
    'retry_delay': timedelta(minutes=5),
    'end_date': datetime(2022, 1, 1),
}

def get_ul(url: str):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.find('ul')

def write_file(li: str, file_dir: str):
    with open(file_dir, 'a') as f:
        f.write(li)
        f.write('\n')

home = expanduser("~")
desktop_dir = os.path.join(home, 'Desktop/test_2.txt')

with DAG(dag_id='test_python',
         default_args=default_args,
         schedule_interval='*/1 1 * * *',
         catchup=False,
         tags=['test']
         ) as dag:

    def get_today_events(ti, url: str, file_dir: str):
        ul_soup = get_ul(url)
        for li in ul_soup.find_all('li'):
            write_file(li.text, file_dir)

    date_task = PythonOperator(
        task_id='write_events',
        python_callable=get_today_events,
        op_kwargs={'url': 'https://en.wikipedia.org/wiki/Wikipedia:On_this_day/Today', 
                   'file_dir': desktop_dir})
    
