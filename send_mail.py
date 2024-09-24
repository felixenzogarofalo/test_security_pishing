import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Función para enviar correo
def send_email(to_email):
    from_email = "egarofalosalas221@gmail.com"  # Tu correo de Gmail
    subject = "Prueba de phishing"
    
    # Plantilla HTML del mensaje con el correo dinámicamente insertado
    html_template = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Correo de Phishing de Prueba</title>
    </head>
    <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" width="600" style="background-color: #ffffff; padding: 20px;">
        <tr>
          <td style="text-align: center;">
            <h2>¡Atención! Ha llegado un nuevo mensaje importante</h2>
            <p>Parece que hay una oferta exclusiva esperando por ti. Haz clic en el botón a continuación para aprovecharla antes de que se acabe.</p>
            <p style="color: red;">Este es un mensaje de prueba para verificar tu conocimiento sobre correos electrónicos de phishing.</p>
            <!-- El parámetro {{email}} es reemplazado dinámicamente -->
            <a href="http://127.0.0.1:5000/click?email={}" style="background-color: #007bff; color: #ffffff; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Haz clic aquí</a>
            <p style="font-size: 12px; color: #888888;">Si no solicitaste esta oferta, por favor ignora este mensaje.</p>
          </td>
        </tr>
      </table>
    </body>
    </html>
    """.format(to_email)  # Inserta el correo electrónico en el enlace

    # Crear el mensaje MIME
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Convertir HTML a MIMEText
    msg.attach(MIMEText(html_template, 'html'))

    # Conectar al servidor SMTP de Gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Usar TLS
    # Utilizar la contraseña de aplicación generada
    server.login(from_email, "pcheqkqwucirznwq")

    # Enviar el correo
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

# Llamar a la función para enviar un correo a un destinatario
send_email("felixenzogarofalo@gmail.com")
