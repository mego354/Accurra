# Accurra - Django Web Application

A modern Django web application with Egyptian timezone support and Arabic-English slang-friendly content.

## 🚀 Live Demo
[Visit the Website](https://mego354.github.io/Accurra/)

## Features

- 🕐 **Egyptian Timezone Support** - Real-time display of Cairo time
- 🌍 **Bilingual Support** - Arabic-English slang-friendly content
- 🎨 **Modern UI** - Bootstrap 5.3.2 with custom styling
- ⚡ **3D Animations** - Three.js powered background effects
- 📱 **Responsive Design** - Mobile-first approach
- 🔧 **Django Best Practices** - Proper project structure and configuration

## Project Structure

```
Accurra/
├── Accurra/               # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── main/                   # Main application
│   ├── __init__.py
│   ├── apps.py
│   ├── views.py
│   ├── urls.py
│   └── context_processors.py
├── templates/              # HTML templates
│   ├── base.html
│   └── main/
│       └── home.html
├── static/                 # Static files
│   ├── css/
│   ├── js/
│   └── fonts/
├── manage.py
├── requirements.txt
└── README.md
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Accurra
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your settings
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Visit the application**
   Open your browser and go to `http://127.0.0.1:8000/`

## Configuration

### Timezone Settings
The application is configured to use Egyptian timezone (`Africa/Cairo`). The current time is displayed in the top-right corner and updates in real-time.

### Language Support
The application supports Arabic-English slang with a friendly, professional tone. Content is designed to be accessible and engaging.

### Static Files
All static files (Bootstrap, FontAwesome, Three.js) are served locally without CDN dependencies for better performance and reliability.

## Dependencies

- Django 4.2.7
- pytz 2023.3 (Timezone support)
- Pillow 10.1.0 (Image processing)
- python-decouple 3.8 (Environment variables)
- django-extensions 3.2.3 (Development tools)
- whitenoise 6.6.0 (Static file serving)

## Development

### Running Tests
```bash
python manage.py test
```

### Collecting Static Files
```bash
python manage.py collectstatic
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## Deployment

1. Set `DEBUG=False` in production
2. Configure proper database (PostgreSQL recommended)
3. Set up proper email backend
4. Configure static file serving
5. Set up proper logging

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please contact:
- Email: contact@accurra.com
- WhatsApp: +201026004642
- GitHub: https://github.com/mego354

---

**Accurra** - Building the future, one flex at a time. 🇪🇬
