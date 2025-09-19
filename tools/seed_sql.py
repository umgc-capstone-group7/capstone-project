import sys
from pathlib import Path
from sqlalchemy import text

# Add the parent directory to the path so we can import app
sys.path.insert(0, str(Path(__file__).parent.parent))

from app import create_app, db

SQL_FILE_CANDIDATES = [
    "../database.sql",   # repo root
    "database.sql",      # backend/
    "../data/database.sql",
]

def load_sql_text():
    for p in SQL_FILE_CANDIDATES:
        f = Path(p)
        if f.exists():
            return f.read_text(), f
    raise SystemExit("database.sql not found. Place it at repo root or backend/")

def normalize_mysql_to_sqlite(sql: str) -> str:
    sql = sql.replace("AUTO_INCREMENT", "AUTOINCREMENT")
    sql = sql.replace("BOOLEAN", "INTEGER")
    sql = sql.replace("ENUM('Fall', 'Spring', 'Summer')", "TEXT")
    sql = sql.replace("ENUM('Associate', 'Bachelor', 'Master', 'Doctorate')", "TEXT")
    
    # Map table names from Morgan's schema to our model names
    sql = sql.replace("Departments", "department")
    sql = sql.replace("Instructors", "instructor")
    sql = sql.replace("Degree_Programs", "degree_program")
    sql = sql.replace("Classlist", "classlist")
    
    # Map column names to match our models
    sql = sql.replace("department_name", "name")
    sql = sql.replace("department_code", "code")
    
    return sql

def run():
    sql_raw, src_path = load_sql_text()
    sql = normalize_mysql_to_sqlite(sql_raw)

    app = create_app()
    with app.app_context():
        db.session.execute(text("PRAGMA foreign_keys = ON"))
        statements = [s.strip() for s in sql.split(";\n") if s.strip()]
        # Only execute INSERT statements, skip CREATE TABLE
        insert_statements = [stmt for stmt in statements if stmt.upper().startswith('INSERT')]
        for stmt in insert_statements:
            db.session.execute(text(stmt))
        db.session.commit()
        print(f"Seeded from {src_path}")

if __name__ == "__main__":
    run()
