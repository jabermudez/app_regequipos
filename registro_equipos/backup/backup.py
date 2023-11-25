import os
import shutil
import smtplib
from email.message import EmailMessage
import schedule
import time

def backup_database(db_path, backup_path):
    
    # Copia el archivo de la base de datos a una nueva ubicación
    shutil.copyfile(db_path, backup_path)    
    print("Copia de seguridad realizada con éxito.")
    

def send_backup_email(backup_path, sender_email, receiver_email, email_password):
    msg = EmailMessage()
    msg['Subject'] = 'Copia de seguridad de la base de datos'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content('Encuentra adjunto la copia de seguridad de la base de datos.')

    # Adjunta el archivo
    with open(backup_path, 'rb') as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename='backup.db')

    # Envía el correo electrónico
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, email_password)
        smtp.send_message(msg)

    print("Correo electrónico enviado con éxito.")

def schedule_backup_tasks():
    # Ajusta estas rutas según tu configuración
    
    CURRENT_DIR = os.path.dirname(__file__)
    db_path = os.path.normpath(os.path.join(CURRENT_DIR, "../database/usuarios.db"))
    backup_path = os.path.join(CURRENT_DIR, "../backup/backup.db")
       
        
    sender_email = 'sia.serviciostic@gmail.com'
    receiver_email = 'sia.serviciostic@outlook.com'
    email_password = 'Machu2023.'

    # Programa las tareas
    #schedule.every().day.at("22:52").do(backup_database, db_path=db_path, backup_path=backup_path)
    #schedule.every().day.at("22:53").do(send_backup_email, backup_path=backup_path, sender_email=sender_email, receiver_email=receiver_email, email_password=email_password)
    backup_database(db_path, backup_path)
    send_backup_email(backup_path=backup_path, sender_email=sender_email, receiver_email=receiver_email, email_password=email_password)
   
    global running
    running = True

    while running:
        # código del while
    
        running = False # para terminar


