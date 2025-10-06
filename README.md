# 🎓 UMGC Student Portal - Capstone Project

A comprehensive student portal application built with Flask, featuring GPA calculation, resume building, class scheduling, and wellness resources. This project integrates multiple open-source tools to provide students with a complete academic management solution.

## 🌟 Features

### 📊 GPA Calculator
- **Real-time GPA Calculation**: Calculate semester and cumulative GPA with support for multiple grade formats
- **Flexible Input**: Accept letter grades (A, A-, B+), numeric points (0-4.0), or percentages (0-100)
- **Prior GPA Integration**: Include previous academic history in calculations
- **Credit Validation**: Smart validation for course credits and grade ranges

### 📝 Resume Builder
- **Professional Templates**: Create modern, ATS-friendly resumes
- **Real-time Preview**: See your resume as you build it
- **Dynamic Sections**: Add/remove work experience and education entries
- **Multiple Formats**: Support for various input formats and export options
- **Download/Print**: Export your resume as PDF or print directly

### 📅 Class Timetable (PWA Integration)
- **Interactive Calendar**: Track classes, assignments, and exams
- **Offline Access**: Progressive Web App (PWA) functionality for offline use
- **Real-time Notifications**: Get alerts for upcoming classes and assignments
- **Mobile Friendly**: Responsive design for desktop and mobile devices
- **Platform Integration**: Direct links to Zoom, Google Meet, and other platforms

### 💙 Wellness Resources
- **Mental Health Support**: 24/7 crisis lines and support resources
- **National Hotlines**: Quick access to mental health and crisis support
- **Community Programs**: Local and online wellness resources
- **UMGC Services**: University-specific support and counseling services

## 🚀 Quick Start

### Setup
1) Open this folder in Cursor
2) In the Cursor terminal, create a virtual environment
   ```bash
   Mac/Linux: python3 -m venv .venv && source .venv/bin/activate
   Windows: python -m venv .venv ; .\.venv\Scripts\Activate.ps1
   ```
3) Install packages: `pip install -r requirements.txt`
4) Run the app: `python run.py`
   Then open http://127.0.0.1:5000
5) Seed classes: `python -c "from app.db_init import main; main()"`

### Accessing Features
- **Dashboard**: Main hub with access to all features
- **GPA Calculator**: `/gpa` - Calculate your academic performance
- **Resume Builder**: `/resume-builder` - Create professional resumes
- **Class Timetable**: `/timetable` - Manage your class schedule
- **Wellness Resources**: `/wellness` - Access mental health support

## 🛠️ Technologies Used

### Backend
- **Flask**: Python web framework
- **SQLAlchemy**: Database ORM
- **Flask-Login**: User authentication
- **SQLite**: Database for development

### Frontend
- **HTML5/CSS3**: Modern web standards
- **JavaScript**: Interactive functionality
- **Bootstrap**: Responsive design framework
- **Custom Styling**: UMGC-themed color scheme

### Integrated Projects
- **OpenResume**: Resume building functionality ([GitHub](https://github.com/xitanggg/open-resume))
- **PWA Timetable**: Class scheduling ([GitHub](https://github.com/StepanTita/pwa-timetable))

## 📱 Progressive Web App Features

The timetable feature includes PWA capabilities:
- **Offline Access**: Works without internet connection
- **Installable**: Add to home screen on mobile devices
- **Push Notifications**: Real-time alerts for classes and assignments
- **Responsive Design**: Optimized for all screen sizes

## 🎨 Design & Styling

- **UMGC Color Scheme**: Deep maroon (#a41e34) and warm gold (#f3b43b) accents
- **Dark Theme**: Modern dark interface with high contrast
- **Responsive Layout**: Works seamlessly on desktop, tablet, and mobile
- **Accessibility**: WCAG compliant design for all users

## 🤝 Contributing

This project integrates multiple open-source components:
- [OpenResume](https://github.com/xitanggg/open-resume) - Resume building functionality
- [PWA Timetable](https://github.com/StepanTita/pwa-timetable) - Class scheduling and calendar features

## 📄 License

This project is part of the UMGC Capstone Project and integrates multiple open-source components under their respective licenses.

## 🙌 Acknowledgments

- **OpenResume Team**: For the excellent resume building framework
- **StepanTita**: For the PWA Timetable project
- **UMGC Community**: For feedback and support during development
