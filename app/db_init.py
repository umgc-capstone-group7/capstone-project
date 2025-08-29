from . import create_app, db
from .models import Class

seed = [
    ("CMSC331", "Programming Languages"),
    ("CMSC451", "Design and Analysis of Algorithms"),
    ("STAT200", "Intro to Statistics"),
]

def main():
    app = create_app()
    with app.app_context():
        if Class.query.count() == 0:
            for code, title in seed:
                db.session.add(Class(code=code, title=title))
            db.session.commit()
            print("Seeded classes")

if __name__ == "__main__":
    main()
