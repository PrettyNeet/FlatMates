from mainapp import db, app

# Ensure the app context is pushed
app.app_context().push()

# Create the database tables
db.create_all()

print("Database tables created successfully.")
