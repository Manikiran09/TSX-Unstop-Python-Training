import os
from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Database config (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Mail config
app.config.update(
    MAIL_SERVER='manikiran649@gmail.com',               # ✅ FIXED: Correct mail server
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),   # e.g., your_email@gmail.com
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD')    # App Password or real password (not recommended)
)

# Initialize extensions
db = SQLAlchemy(app)
mail = Mail(app)

# Database model
class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message_body = request.form['message']

        # Save to DB
        new_msg = ContactMessage(name=name, email=email, message=message_body)
        db.session.add(new_msg)
        db.session.commit()

        # Try sending email
        try:
            msg = Message(
                subject=f'New message from {name}',
                sender=app.config['MAIL_USERNAME'],
                recipients=[app.config['MAIL_USERNAME']],
                body=f"From: {name} <{email}>\n\n{message_body}"
            )
            mail.send(msg)
            flash('Message sent successfully!', 'success')
        except Exception as e:
            print(f"Email send error: {e}")
            flash('Message saved but failed to send email.', 'warning')

        return redirect(url_for('contact'))

    return render_template('contact.html')

@app.route('/messages')
def messages():
    # Note: Add authentication in real-world apps
    all_messages = ContactMessage.query.order_by(ContactMessage.id.desc()).all()
    return render_template('messages.html', messages=all_messages)

# Main entry
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
