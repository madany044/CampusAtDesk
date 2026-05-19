import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")

DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")

# Database Configuration
DATABASE_URI = "mysql+pymysql://25EMRITCS051:8SeFCC%2Ai%25fZmNRvE@157.173.221.22:3308/25EMRITCS051"

UPLOAD_FOLDER = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    "uploads",
    "resumes"
)

ALLOWED_RESUME_EXTENSIONS = {"pdf", "doc", "docx"}