from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json

    sender_email = 'your_email@gmail.com'
    sender_password = 'your_email_password'
    receiver_email = data['to']
    subject = data['subject']
    message = data['message']

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)

    return jsonify({'status': 'Email sent successfully'})

if __name__ == '__main__':
    app.run(debug=True)
