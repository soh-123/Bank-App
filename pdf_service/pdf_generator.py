from flask import Flask, request, jsonify, send_file
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.pagesizes import letter
import os

app = Flask(__name__)


@app.route("/generate-pdf", methods=["POST"])
def generate_pdf():
    try:
        transactions = request.json

        if not isinstance(transactions, list):
            return jsonify({"error": "Invalid input. Expected a list of transactions in JSON format."}), 400

        if not transactions:
            return jsonify({"error": "No transactions provided."}), 400
        
        file_name = "statement.pdf"

        doc = SimpleDocTemplate(file_name, pagesize=letter)
        elements = [Paragraph(f"Transaction: {t}") for t in transactions]
        doc.build(elements)

        return file_name
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5002)
