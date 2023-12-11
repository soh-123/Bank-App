from flask import Flask, request, jsonify
import smtplib
from email.message import EmailMessage

app = Flask(__name__)


def send_email_smtp(user_email, pdf_path):
    try:
        msg = EmailMessage()
        msg["Subject"] = "Your Bank Statement"
        msg["From"] = "your-email@example.com"
        msg["To"] = user_email

        with open(pdf_path, "rb") as f:
            file_data = f.read()
            msg.add_attachment(
                file_data, maintype="application", subtype="pdf", filename=pdf_path
            )

        with smtplib.SMTP("localhost", 1025) as server:
            server.send_message(msg)
        
        return None

    except Exception as e:
        return str(e) 
    

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.json
    user_email = data.get("user_email")
    pdf_path = data.get("pdf_path")

    error_message = send_email_smtp(user_email, pdf_path)
    if error_message is None:
        return "Email sent successfully."
    else:
        return jsonify({"error": error_message}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5003)
