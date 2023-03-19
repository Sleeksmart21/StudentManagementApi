from flask import request
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus
from management_portal import db
from management_portal.models.users import User
from management_portal.models.students import Student
from management_portal.models.admin import Admin
from management_portal.models.teachers import Teacher
from management_portal.models.courses import Course
from management_portal.models.scores import Score
from management_portal.models.mycourses import MyCourse
from management_portal.auth.views import auth_namespace
# from management_portal.student.views import students_namespace
# from management_portal.school.views import school_namespace
from management_portal.course.views import course_namespace
# from management_portal.serializers import (students_fields_serializer, courses_retrieve_fields_serializer, course_fields_serializer, score_add_fields_serializer, course_teacher_fields_serializer)
# from management_portal.decorators import admin_required, student_required, staff_required, teacher_required
from flask_jwt_extended import jwt_required , get_jwt_identity, jwt_required



school_namespace = Namespace('school', description='Name space for School')


course_creation_serializer = course_namespace.model(
    'Course creation serializer', {
        'name': fields.String(required=True, description="Course name"),
        'credit_hours': fields.Integer(description="Course credit hours"),
        'teacher_id': fields.Integer(required=True, description="Course teacher id"),
    }
)


course_teacher_serializer = course_namespace.model(
    'Course Teacher serializer', {
        'identifier': fields.String( description='User email address'),
        'email': fields.String(required=True, description='User email address'),
        'first_name': fields.String(required=True, description="First name"),
        'last_name': fields.String(required=True, description="Lat name"),
        'employee_no': fields.String(required=True, description="Course teacher id"),
        'created_at': fields.DateTime( description="Course creation date"),
    }
)


@school_namespace.route('/register_student')
class RegisterStudent(Resource):
    def post(self):
        return {"message": "Hello Admin nice to meet you"}


# Read a student 'function' should also be here
# Update a student 'function' should also be here
# Delete a student 'function' should also be here


@school_namespace.route('/register_teacher')
class RegisterTeacher(Resource):
    def post(self):
        return {"message": "Hello Admin nice to meet you"}


# Read a teacher 'function' should also be here
# Update a teacher 'function' should also be here
# Delete a teacher 'function' should also be here


@school_namespace.route('/retrieve_allcourses')
class RetrieveAllCourses(Resource):
    def get(self):
        return {"message": "Hello Admin nice to meet you"}


@school_namespace.route('/retrieve_studentsincourse')
class RetrieveStudentsInCourse(Resource):
    def get(self):
        return {"message": "Hello Admin nice to meet you"}



@school_namespace.route('/retrieve_gradesbystudent')
class RetrieveAStudentsGrades(Resource):
    def get(self):
        return {"message": "Hello Admin nice to meet you"}



@school_namespace.route('/calcgpa')
class CalcStudentGPA(Resource):
    def get(self):
        return {"message": "Hello Admin nice to meet you"}












































































































































































































































































































































