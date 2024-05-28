# import necessary packages 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


SMTP_USER = 'partners@agenciademarketingdigital.org'
SMTP_PASS = 'WEqcbUDV'
SMTP_HOST = 'mail.agenciademarketingdigital.org'
SMTP_PORT = 587


subject = input('Ingrese el asunto del correo: ')
from_email = input('Ingrese el email desde donde quiere se envie el correo: ')
to_email = input('Ingrese a quien le sera enviado el correo: ')


# Crear mensaje
msg = MIMEMultipart('alternative')
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject

html_content = """




"""


# Adjuntar el contenido HTML al mensaje
msg.attach(MIMEText(html_content, 'html'))

# Enviar el correo
try:
    server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
    server.starttls()
    server.login(SMTP_USER, SMTP_PASS)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()
    print("Correo enviado exitosamente")
except Exception as e:
    print(f"Error al enviar el correo: {e}")