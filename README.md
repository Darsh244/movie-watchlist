# 🎬 Movie Watchlist

A full-stack web application built with Django that allows users to search movies using the JustWatch API and create personalized watchlists. Users can sign up, log in, and manage their own watchlists to keep track of movies they want to watch.

---

## 🚀 Features

- User authentication with secure password login 🔐  
- Search movies via the JustWatch API 🔍  
- Add movies to personalized watchlists 📋  
- Mark movies as watched/unwatched ✔️❌  
- Responsive and user-friendly UI 📱💻  
- Static files served efficiently with WhiteNoise ⚡

---

## 🛠 Technologies Used

**Languages:**  
Python, HTML, CSS, JavaScript

**Frameworks & Libraries:**  
Django, JustWatch API, WhiteNoise, Bootstrap, Axios

**Developer Tools:**  
Git, GitHub, VS Code, PyCharm

---

## 📦 Installation & Setup

1. Clone the repository  
   ```bash
   git clone https://github.com/your-username/movie-watchlist.git
   cd movie-watchlist
   ```

2. Create and activate a virtual environment
    ```bash
    python3 -m venv venv
    source venv/bin/activate    # On Windows: venv\Scripts\activate
    ```

3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables

- Create a .env file in the root directory with your settings, for example:

```
DATABASE_URL=your_database_url_here
SECRET_KEY=your_django_secret_key_here
DEBUG=True
```

5. Run database migrations
    ```bash
    python manage.py migrate
    ```

6. Run the deployment server
    ```bash
    python manage.py runserver
    ```

- Open your browser at http://127.0.0.1:8000 to view the app locally.


## ⚙️ Usage

- Sign up for a new account or log in.
- Search for movies using the search bar.
- Add movies to your watchlist.
- Manage your watchlist by marking movies as watched or removing them.


## 🚀 Deployment

**Deploying on Render.com**
1. Connect your GitHub repository to Render.
2. Create a new Web Service on Render and select your repo.

3. Set the build command to:
```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```
4. Start the start command to:
```bash
gunicorn movie_watchlist.wsgi
```
5. Add environment variables in Render's dashboard:
- DATABASE_URL (your PostgreSQL connection URL)
- SECRET_KEY (your Django secret key)
- DJANGO_SETTINGS_MODULE (movie_watchlist.settings)
- PYTHON_VERSION (the python version)

Your app will live at the URL provided by Render after deployment.



**Running Locally**
You can also run the app locally using the instructions in the Installation & Setup section. This uses SQLite by default unless you configure otherwise.

## 📄 License

This project is licensed under the MIT License.



Developed by Darsh Mishra.

