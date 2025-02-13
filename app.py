from flask import Flask, render_template_string
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'iris.macharia@student.moringaschool.com' 
app.config['MAIL_PASSWORD'] = 'xgzk cggh sjkz hpni'  
app.config['MAIL_DEFAULT_SENDER'] = 'iris.macharia@student.moringaschool.com' 

mail = Mail(app)

@app.route('/send-email')
def send_email():
    msg = Message('Hello from Flask', recipients=['kokymash@gmail.com'])
    msg.body = 'This is a test email sent from a Flask web application!'
    mail.send(msg)
    return 'Email sent!'

if __name__ == '__main__':
    app.run(debug=True)
