from flask import Flask, request, jsonify
import csv
from datetime import datetime

app = Flask(__name__)


def filter_transactions(start_date, end_date, user_email):
    transactions = []
    try:
        with open("database_service/transactions.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                transaction_date = datetime.strptime(
                    row["date_of_transaction"], "%Y-%m-%d"
                ).date()
                if (
                    row["user_email"] == user_email
                    and start_date <= transaction_date <= end_date
                ):
                    transactions.append(
                        {
                            "amount": row["amount"],
                            "date_of_transaction": row["date_of_transaction"],
                        }
                    )
    except Exception as e:
        return str(e)

    return transactions


@app.route("/get-transactions", methods=["POST"])
def get_transactions():
    try:
        data = request.json
        user_email = data.get("user_email")
        start_date = datetime.strptime(data.get("start_date"), "%Y-%m-%d").date()
        end_date = datetime.strptime(data.get("end_date"), "%Y-%m-%d").date()

        filtered_transactions = filter_transactions(start_date, end_date, user_email)
        if isinstance(filtered_transactions, list):
            return jsonify(filtered_transactions)
        else:
            return jsonify({"error": filtered_transactions}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)
