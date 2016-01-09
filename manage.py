#!/usr/bin/env python
import os
from app import create_app
from flask.ext.script import Manager

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


if __name__ == '__main__':
    # db.create_all()  # This will not run if the database is already created.
    # manager.run()
    app.run(debug=True)
