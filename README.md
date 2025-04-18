# BlogSphere

**BlogSphere** is a minimalistic blog platform built with Django. It allows users to log in, create blog posts, and view posts created by others. With a user-friendly design and straightforward functionality, BlogSphere aims to provide a seamless experience for users who want to share their thoughts and ideas.

---

## Features

- **User Authentication**: Secure login functionality for users.
- **Create Blog Posts**: Logged-in users can create blog posts.
- **View Blog Posts**: Users can view posts created by others.
- **Responsive Design**: The platform is optimized for both desktop and mobile devices.
- **Minimalistic Interface**: Simple and clean user interface.

---

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite 
- **Authentication**: Django’s built-in authentication system
---

## Setup & Installation

Follow these steps to get the project running locally:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/BlogSphere.git
   cd BlogSphere
   ```

2. **Create a virtual environment** (optional, but recommended):

   ```bash
   python3 -m venv env
   source env/bin/activate  # For Windows: env\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations** to set up the database:

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

7. Open your browser and go to `http://127.0.0.1:8000/` to view the app.
