import sys
from pathlib import Path
from datetime import date

# Add the parent directory to the path so we can import app
sys.path.insert(0, str(Path(__file__).parent.parent))

from app import create_app, db
from app.models import Department, Instructor, DegreeProgram, Classlist

def seed_data():
    app = create_app()
    with app.app_context():
        # Clear existing data
        db.session.query(Classlist).delete()
        db.session.query(DegreeProgram).delete()
        db.session.query(Instructor).delete()
        db.session.query(Department).delete()
        db.session.commit()
        
        # Create departments
        dept1 = Department(
            name="Computer Science",
            code="CS",
            head_of_department="Dr. Smith",
            building="Tech Building",
            phone="555-0101",
            email="cs@university.edu"
        )
        dept2 = Department(
            name="Mathematics",
            code="MATH",
            head_of_department="Dr. Johnson",
            building="Science Hall",
            phone="555-0102",
            email="math@university.edu"
        )
        dept3 = Department(
            name="Physics",
            code="PHYS",
            head_of_department="Dr. Brown",
            building="Science Hall",
            phone="555-0103",
            email="physics@university.edu"
        )
        
        db.session.add_all([dept1, dept2, dept3])
        db.session.commit()
        
        # Create instructors
        instr1 = Instructor(
            first_name="John",
            last_name="Doe",
            email="john.doe@university.edu",
            department_id=dept1.id,
            hire_date=date(2020, 1, 15),
            salary=75000.00,
            office_number="TB-201",
            phone="555-1001"
        )
        instr2 = Instructor(
            first_name="Jane",
            last_name="Smith",
            email="jane.smith@university.edu",
            department_id=dept1.id,
            hire_date=date(2019, 8, 20),
            salary=80000.00,
            office_number="TB-202",
            phone="555-1002"
        )
        instr3 = Instructor(
            first_name="Bob",
            last_name="Johnson",
            email="bob.johnson@university.edu",
            department_id=dept2.id,
            hire_date=date(2021, 3, 10),
            salary=70000.00,
            office_number="SH-301",
            phone="555-1003"
        )
        instr4 = Instructor(
            first_name="Alice",
            last_name="Brown",
            email="alice.brown@university.edu",
            department_id=dept3.id,
            hire_date=date(2018, 9, 1),
            salary=85000.00,
            office_number="SH-302",
            phone="555-1004"
        )
        
        db.session.add_all([instr1, instr2, instr3, instr4])
        db.session.commit()
        
        # Create degree programs
        prog1 = DegreeProgram(
            program_name="Computer Science",
            degree_type="Bachelor",
            department_id=dept1.id,
            required_credits=120,
            program_description="Comprehensive computer science program",
            is_active=True
        )
        prog2 = DegreeProgram(
            program_name="Mathematics",
            degree_type="Bachelor",
            department_id=dept2.id,
            required_credits=120,
            program_description="Pure and applied mathematics",
            is_active=True
        )
        prog3 = DegreeProgram(
            program_name="Physics",
            degree_type="Bachelor",
            department_id=dept3.id,
            required_credits=120,
            program_description="Physics and astronomy program",
            is_active=True
        )
        
        db.session.add_all([prog1, prog2, prog3])
        db.session.commit()
        
        # Create classes
        class1 = Classlist(
            course_code="CS101",
            course_name="Introduction to Programming",
            instructor_id=instr1.id,
            department_id=dept1.id,
            semester="Fall",
            year=2024,
            credits=3,
            max_enrollment=30,
            current_enrollment=25,
            classroom="TB-101",
            schedule_time="MWF 10:00-10:50"
        )
        class2 = Classlist(
            course_code="CS201",
            course_name="Data Structures",
            instructor_id=instr2.id,
            department_id=dept1.id,
            semester="Fall",
            year=2024,
            credits=3,
            max_enrollment=25,
            current_enrollment=20,
            classroom="TB-102",
            schedule_time="TTH 11:00-12:15"
        )
        class3 = Classlist(
            course_code="MATH101",
            course_name="Calculus I",
            instructor_id=instr3.id,
            department_id=dept2.id,
            semester="Fall",
            year=2024,
            credits=4,
            max_enrollment=35,
            current_enrollment=30,
            classroom="SH-201",
            schedule_time="MWF 9:00-9:50"
        )
        class4 = Classlist(
            course_code="PHYS101",
            course_name="General Physics I",
            instructor_id=instr4.id,
            department_id=dept3.id,
            semester="Fall",
            year=2024,
            credits=4,
            max_enrollment=30,
            current_enrollment=28,
            classroom="SH-301",
            schedule_time="TTH 2:00-3:15"
        )
        class5 = Classlist(
            course_code="CS301",
            course_name="Algorithms",
            instructor_id=instr1.id,
            department_id=dept1.id,
            semester="Spring",
            year=2024,
            credits=3,
            max_enrollment=20,
            current_enrollment=18,
            classroom="TB-103",
            schedule_time="MWF 1:00-1:50"
        )
        class6 = Classlist(
            course_code="MATH201",
            course_name="Calculus II",
            instructor_id=instr3.id,
            department_id=dept2.id,
            semester="Spring",
            year=2024,
            credits=4,
            max_enrollment=30,
            current_enrollment=25,
            classroom="SH-202",
            schedule_time="TTH 10:00-11:15"
        )
        
        db.session.add_all([class1, class2, class3, class4, class5, class6])
        db.session.commit()
        
        print("Successfully seeded database with sample data!")

if __name__ == "__main__":
    seed_data()