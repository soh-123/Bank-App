from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route("/generate-statement", methods=["POST"])
def generate_statement():
    try:
        data = request.json
        user_email = data.get("user_email")
        start_date = data.get("start_date")
        end_date = data.get("end_date")

        # Call the Database Service
        transactions = requests.post(
            "http://localhost:5001/get-transactions",
            json={
                "user_email": user_email,
                "start_date": start_date,
                "end_date": end_date,
            },
        ).json()

        # Call the PDF Generation Service
        pdf_path = requests.post(
            "http://localhost:5002/generate-pdf", json=transactions
        ).text

        # Call the Email Service
        email_response = requests.post(
            "http://localhost:5003/send-email",
            json={"user_email": user_email, "pdf_path": pdf_path},
        ).text

        return jsonify(
            {
                "message": "Statement generated and emailed successfully.",
                "email_response": email_response,
            }
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
