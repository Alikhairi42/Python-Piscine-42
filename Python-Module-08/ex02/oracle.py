
import os
import sys
from dotenv import load_dotenv


def main():
    load_dotenv()

    matrix_name = os.getenv("MATRIX_MODE")
    database_url = os.getenv("DATABASE_URL")

    if matrix_name is None:
        print("Error: MATRIX_NAME is missing from .env")
        sys.exit(1)

    if database_url is None:
        print("Error: DATABASE_URL is missing from .env")
        sys.exit(1)

    print(f"Matrix name: {matrix_name}")
    print("Configuration loaded successfully!")


if __name__ == "__main__":
    main()
