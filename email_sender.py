import csv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, To

# Load the dynamic template id
template_id = "dynamic_template_id_from_send_grid"

# Load your SendGrid API key
sg = SendGridAPIClient('your_send_grid_api_key')

# Function to send email
def send_email(to_email, to_name):
    to = To(email=to_email, name=to_name)  # Correctly create a To object with name
    message = Mail(
        from_email='no-reply@example.com',  # Replace with your email
        to_emails=to,
    )
    message.dynamic_template_data = {
        'name': to_name  # Assuming your template uses this variable
    }
    message.template_id = template_id
    try:
        response = sg.send(message)
        print(f"Email to {to_email} sent successfully.")
    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {e}")

# Read the CSV and send emails
with open('emails.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if your CSV has one
    for row in reader:
        email, name = row  # Adjust this based on your CSV structure
        send_email(email, name)
