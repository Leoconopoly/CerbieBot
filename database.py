import firebase_admin
import os
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

# Initialize Firebase Admin SDK
cred = credentials.Certificate("C:\\Users\\leoco\\Documents\\CerbieBot\\cerbiebot-firebase-adminsdk-5afo3-2d5b25d8d2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def add_reminder(user_id, reminder_content, timestamp):
    reminders = db.collection('reminders')
    reminders.add({
        'user_id': user_id,
        'reminder_content': reminder_content,
        'timestamp': timestamp
    })

def get_reminders(user_id):
    return db.collection('reminders').where('user_id', '==', user_id).stream()

def add_task(user_id, task_content):
    tasks = db.collection('tasks')
    tasks.add({
        'user_id': user_id,
        'task_content': task_content,
        'is_completed': False
    })

def get_tasks(user_id):
    return db.collection('tasks').where('user_id', '==', user_id).stream()

