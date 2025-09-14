# Footsteps Sneakers

An online sneaker store with a shopping cart, basic analytics, and an admin panel for managing products.

## Technologies

- Python 3.x
- Django 5.1.7
- PostgreSQL
- Docker / docker-compose
- Key libraries:
  - asgiref==3.9.1
  - django-environ==0.12.0
  - environ==1.0
  - pillow==11.3.0
  - psycopg2-binary==2.9.10
  - sqlparse==0.5.3

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd footstepsneakers

2.	Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3.	Install dependencies:
pip install -r requirements.txt

4.	Set up PostgreSQL database:
	•	Create a database and user.
	•	Configure .env file:

POSTGRES_DB=<your_db_name>
POSTGRES_USER=<your_db_user>
POSTGRES_PASSWORD=<your_db_password>
POSTGRES_HOST=localhost
POSTGRES_PORT=5433 (or another)

5.	Apply migrations:
python manage.py migrate

6.	Create a superuser:
python manage.py createsuperuser

7.	Run the project:
python manage.py runserver

To run with Docker:
<directory> docker compose up -d
# This will start containers for Django and PostgreSQL. Redis is not used.

Features
	•	Browse product catalog
	•	Add/remove products from the cart
	•	Calculate total cart value
	•	Basic analytics for views and orders
	•	Django admin panel for managing products and users

