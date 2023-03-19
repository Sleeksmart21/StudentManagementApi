from flask import Flask
from flask_restx import Api, Namespace
from flask_jwt_extended import JWTManager
from werkzeug.exceptions import NotFound, MethodNotAllowed
from management_portal.utils import db
from http import HTTPStatus
from flask_migrate import Migrate
from management_portal.models.admin import Admin
from management_portal.models.courses import Course
from management_portal.models.teachers import Teacher
from management_portal.models.scores import Score
from management_portal.models.students import Student
from management_portal.models.mycourses import MyCourse
from management_portal.models.users import User
from management_portal.auth.views import auth_namespace
from management_portal.student.views import students_namespace
from management_portal.school.views import school_namespace
from management_portal.course.views import course_namespace
from management_portal.config.config import config_dict
# from management_portal import serializers

def create_app(config=config_dict['dev']):
    app = Flask(__name__)
    
    app.config.from_object(config)

    db.init_app(app)

    jwt = JWTManager(app)

    migrate = Migrate(app, db)

    authorizations = {
        "Bearer Auth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Add a JWT token to the header with ** Bearer &lt;JWT&gt; token to authorize** "
        }
    }



    api = Api(app,
        title='School Management API',
        description='A simple School Management REST API Service',
        authorizations=authorizations,
        security='Bearer Auth'
    )

    api.add_namespace(auth_namespace)
    api.add_namespace(students_namespace, path='/students')
    api.add_namespace(school_namespace, path='/school')
    api.add_namespace(course_namespace, path='/course')


    @api.errorhandler(NotFound)
    def not_found(error):
        return {"error": "Not Found"},404

    @api.errorhandler(MethodNotAllowed)
    def method_not_allowed(error):
        return {"error": "Method Not Allowed"},404

    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db,
            'User': User,
            'Admin': Admin,
            'Score': Score,
            'Course': Course,
            'Student': Student,
            'Teacher': Teacher,
            'MyCourse': MyCourse
        }

    return app


