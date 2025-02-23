# Import the database engine from our database setup
from app.database import engine
import os

# Retrieve the database URL to confirm it's correctly set
database_url = os.getenv("DATABASE_URL")

# Print the database URL to verify it's being read properly
print(f"🔍 DATABASE_URL: {database_url}")

try:
    # Attempt to connect to the PostgreSQL database
    with engine.connect() as connection:
        print("✅ Database connection successful!")
except Exception as e:
    # Print an error message if the connection fails
    print(f"❌ Database connection failed: {e}")
