from datetime import datetime, date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Numeric
from . import db

# --------------------------
# Auth / Core domain
# --------------------------
class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default="student")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, raw: str) -> None:
        self.password_hash = generate_password_hash(raw)

    def check_password(self, raw: str) -> bool:
        return check_password_hash(self.password_hash, raw)


class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    credits = db.Column(db.Integer, nullable=False, default=3)


class Enrollment(db.Model):
    __tablename__ = "enrollment"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)
    term = db.Column(db.String(20), nullable=False)

    user = db.relationship("User", backref="enrollments")
    course = db.relationship("Course")

# --------------------------
# Catalog layer (Morgan's DB)
# --------------------------
class Department(db.Model):
    __tablename__ = "department"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)           # department_name
    code = db.Column(db.String(10), unique=True, nullable=False)  # department_code
    head_of_department = db.Column(db.String(100))
    building = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))

    instructors = db.relationship("Instructor", back_populates="department")
    degree_programs = db.relationship("DegreeProgram", back_populates="department")
    classes = db.relationship("Classlist", back_populates="department")


class Instructor(db.Model):
    __tablename__ = "instructor"
    id = db.Column(db.Integer, primary_key=True)  # instructor_id
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey("department.id"))
    hire_date = db.Column(db.Date)  # DATE
    salary = db.Column(Numeric(10, 2))  # DECIMAL(10,2)
    office_number = db.Column(db.String(20))
    phone = db.Column(db.String(20))

    department = db.relationship("Department", back_populates="instructors")
    classes = db.relationship("Classlist", back_populates="instructor")


class DegreeProgram(db.Model):
    __tablename__ = "degree_program"
    id = db.Column(db.Integer, primary_key=True)  # program_id
    program_name = db.Column(db.String(100), nullable=False)
    # ENUM -> text with app-level validation: Associate/Bachelor/Master/Doctorate
    degree_type = db.Column(db.String(20), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey("department.id"))
    required_credits = db.Column(db.Integer)
    program_description = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True)  # SQLite stores as 0/1

    department = db.relationship("Department", back_populates="degree_programs")


class Classlist(db.Model):
    __tablename__ = "classlist"
    id = db.Column(db.Integer, primary_key=True)  # class_id
    course_code = db.Column(db.String(20), nullable=False)
    course_name = db.Column(db.String(100), nullable=False)

    instructor_id = db.Column(db.Integer, db.ForeignKey("instructor.id"))
    department_id = db.Column(db.Integer, db.ForeignKey("department.id"))

    # ENUM -> text with app-level validation: Fall/Spring/Summer
    semester = db.Column(db.String(10), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    credits = db.Column(db.Integer, default=3)
    max_enrollment = db.Column(db.Integer, default=30)
    current_enrollment = db.Column(db.Integer, default=0)
    classroom = db.Column(db.String(20))
    schedule_time = db.Column(db.String(50))

    instructor = db.relationship("Instructor", back_populates="classes")
    department = db.relationship("Department", back_populates="classes")