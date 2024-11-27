from app import db, app  # Replace 'your_flask_file' with the name of your file (without .py)

with app.app_context():
    db.create_all()
    print("Database and table created successfully.")
