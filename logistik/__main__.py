from logistik import app
from logistik import db

if __name__ == '__main__':
    db.create_all()
    app.run()
