from flask import Flask, request, render_template, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Función para registrar el clic en la base de datos
def log_click(email):
    conn = sqlite3.connect('clicks.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS clicks
                      (email TEXT, timestamp TEXT)''')
    cursor.execute("INSERT INTO clicks (email, timestamp) VALUES (?, ?)", 
                   (email, datetime.now()))
    conn.commit()
    conn.close()

# Página principal de phishing (el enlace desde el correo apunta aquí)
@app.route('/click')
def click():
    email = request.args.get('email')
    if email:
        log_click(email)  # Registrar el clic en la base de datos
    return redirect('/thank-you')  # Redirigir a una página de agradecimiento

# Página de agradecimiento después de hacer clic
@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

# Página de información sobre phishing
@app.route('/phishing-info')
def phishing_info():
    return render_template('phishing_warning.html')

# Mostrar los registros de la base de datos
@app.route('/registros')
def registros():
    conn = sqlite3.connect('clicks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clicks")
    rows = cursor.fetchall()  # Obtener todos los registros de la tabla
    conn.close()
    return render_template('registros.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
