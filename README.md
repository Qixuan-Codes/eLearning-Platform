# eLearning Platform

The eLearning platform is a web-based application designed to facilitate online learning by providing features such as user authentication, course management, real-time communication via chat rooms, and more. Built using **Django**, **Django REST Framework**, and **Channels**, the application supports both synchronous and asynchronous features.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Guide](#setup-guide)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Contributing](#contributing)

## Features
- User authentication and authorization (students, teachers)
- Course management for teachers
- Enrollment and feedback system for students
- Real-time course chat rooms
- Responsive design for mobile and desktop
- Secure communication with HTTPS

## Technologies Used

### Backend
- **Django 4.2.9**: Web framework for backend development
- **Django REST Framework 3.14.0**: For building RESTful APIs
- **Django Channels 4.0.0**: Adds asynchronous support for handling WebSockets (real-time communication)
- **Channels-Redis 4.2.0**: Redis for asynchronous task management

### Frontend
- **HTML** / **JavaScript**: For the user interface
- **Django-Bootstrap-v5**: For responsive design and front-end styling
- **Django-Widget-Tweaks**: For custom Bootstrap form integration

### Other Tools
- **Uvicorn 0.27.1**: ASGI server for handling asynchronous tasks
- **Whitenoise 6.6.0**: Simplifies static file serving
- **Redis**: Used for managing WebSocket connections in chat rooms and notifications
- **Pillow 10.2.0**: For handling image processing (e.g., profile pictures, uploads)

## Setup Guide

### Development Environment
- **Operating System**: Windows OS
- **Python Version**: 3.11.4
- **IDE**: Visual Studio Code
- **Additional Tools**:
- Redis Server: Utilized within Ubuntu (Windows Subsystem for Linux)
- Uvicorn: Employed as an ASGI server for running the application

### Installation

1. Clone the repository:
```
git clone https://github.com/Qixuan-Codes/eLearning-Platform.git
```

2. Navigate to the project directory:   
```
cd eLearning-Platform
```

3. Create and activate a virtual environment:
**Windows:**
```
python -m venv myvenv
myvenv\Scripts\activate.bat
```

**macOS/Linux:**
```
python3 -m venv myvenv
source myvenv/bin/activate
```

4. Install dependencies:
```
pip install -r requirements.txt
```

## Running the Application

1. Start the Redis Server:
**Windows (with Ubuntu terminal):**
```
redis-server
```

**macOS:**
```
redis-server
```

2. Start the Django Application using Uvicorn:

```
uvicorn eLearning.asgi:application --reload
```

3. Open a browser and navigate to:

```
http://127.0.0.1:8000/
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request. Before contributing, please ensure that any changes made follow the code structure and standards used throughout the project.

