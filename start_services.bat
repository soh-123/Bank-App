@echo off
echo Starting all services...

start /B python api_service\app.py
start /B python database_service\database.py
start /B python pdf_service\pdf_generator.py
start /B python email_service\email_sender.py

echo All services started. Close this window to stop all services.
pause
