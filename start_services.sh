#!/bin/bash

echo "Starting all services..."

# Start API Service
python api_service/app.py &
api_pid=$!

# Start Database Service
python database_service/database.py &
db_pid=$!

# Start PDF Generation Service
python pdf_service/pdf_generator.py &
pdf_pid=$!

# Start Email Service
python email_service/email_sender.py &
email_pid=$!

echo "All services started. Press Ctrl+C to stop."

trap "echo 'Stopping Services...'; kill $api_pid $db_pid $pdf_pid $email_pid" EXIT

# Wait for all services to close
wait $api_pid $db_pid $pdf_pid $email_pid
