import smtplib
from email.mime.text import MIMEText

try:
    from flask import Flask, request, jsonify, render_template_string
    FLASK_AVAILABLE = True
    app = Flask(__name__)
except Exception:  # Flask not installed
    FLASK_AVAILABLE = False
    Flask = None
    request = None
    jsonify = None
    render_template_string = None
    app = None

# Configuration for SMTP server
SMTP_SERVER = 'localhost'
SMTP_PORT = 25
SENDER_EMAIL = 'no-reply@example.com'

def send_email(recipient_email):
    """Send a simple email with the text 'Hi'."""
    msg = MIMEText('Hi')
    msg['Subject'] = 'Hello'
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient_email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.sendmail(SENDER_EMAIL, [recipient_email], msg.as_string())

if FLASK_AVAILABLE:
    INDEX_HTML = """
    <!doctype html>
    <title>Email Sender</title>
    <h1>Send Email</h1>
    <form action="/send" method="post">
      <input type="email" name="email" placeholder="Email" required>
      <input type="submit" value="Send">
    </form>
    """

    @app.route('/')
    def index():
        """Display a simple form to collect the user's email."""
        return render_template_string(INDEX_HTML)

    @app.route('/send', methods=['POST'])
    def send():
        """Endpoint to send an email to the provided address."""
        recipient = None
        if request.is_json:
            data = request.get_json(silent=True) or {}
            recipient = data.get('email')
        else:
            recipient = request.form.get('email')

        if not recipient:
            return jsonify({'error': 'email is required'}), 400
        try:
            send_email(recipient)
            return jsonify({'status': 'sent'}), 200
        except Exception as exc:
            return jsonify({'error': str(exc)}), 500

if __name__ == '__main__':
    if not FLASK_AVAILABLE:
        raise RuntimeError('Flask is required to run the web server')
    app.run(host='0.0.0.0', port=5000)
