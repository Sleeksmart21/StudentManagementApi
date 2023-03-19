from management_portal import db
from flask import request
from flask_restx import Namespace, Resource, fields
from management_portal.models.admin import Admin
from management_portal.models.courses import Course
from management_portal.models.teachers import Teacher
from management_portal.models.scores import Score
from management_portal.models.students import Student
from management_portal.models.mycourses import MyCourse
from management_portal.models.users import User
from management_portal.auth.views import auth_namespace
# from management_portal.student.views import students_namespace
from management_portal.school.views import school_namespace
from management_portal.course.views import course_namespace
# from management_portal.serializers import (students_fields_serializer, courses_retrieve_fields_serializer, course_fields_serializer, score_add_fields_serializer)
from http import HTTPStatus
from flask_jwt_extended import get_jwt, verify_jwt_in_request
# from management_portal.decorators import (admin_required, student_required, staff_required, teacher_required)


students_namespace = Namespace('student', description='Name space for Students')


# students_serializer = students_namespace.model('Students list serializer', students_fields_serializer)
# courses_retrieve_serializer = students_namespace.model('Students courses list serializer', courses_retrieve_fields_serializer)
# course_serializer = students_namespace.model('Courses add serializer', course_fields_serializer)
# score_add_serializer = students_namespace.model('Courses add serializer', score_add_fields_serializer)

Student_registration_model = students_namespace.model(
    'StudentRegistration', {
        'id': fields.String(),
        'identifier': fields.String(required=False, description='User identifier'),
        'email': fields.String(required=True, description='User email address'),
        'first_name': fields.String(required=True, description="First name"),
        'last_name': fields.String(required=True, description="Lat name"),
        'admission_no': fields.String(required=True, description="First name"),
    }
)

courses_registration_model = students_namespace.model(
    'CourseRegistration', {
        'id': fields.Integer(),
        'course_title': fields.String(required=True, description="A course name"),
        'course_code': fields.String(description="A course code"),
        'teacher_id': fields.Integer(), 
        'created_at': fields.DateTime( description="Course registration date"),
    }
)


@students_namespace.route('/')
class HelloAuth(Resource):
    def get(self):
        return {"message": "Hello Student nice to meet you"}


@students_namespace.route('/add_course')
class RegisterMyCourse(Resource):

    @students_namespace.marshal_with(courses_registration_model)
    @students_namespace.expect(courses_registration_model)

    # @student_required()  
    def post(self):
        """ 
        Register for a course 
        """     
        authenticated_user_id = get_jwt_identity() 
        student = Student.query.filter_by(id=authenticated_user_id).first()   
        data = request.get_json()
        course = Course.query.filter_by(id=data.get('course_id')).first()  
        if course:
            #check if student has registered for the course before
            get_student_in_course = StudentCourse.query.filter_by(student_id=student.id, course_id=course.id).first()
            if get_student_in_course:
                return {
                    'message':'Course has already been registered'
                    } , HTTPStatus.OK
            # Register the student to the course
            add_student_to_course = MyCourse(student_id=student.id, course_id=course.id)
            try:
                add_student_to_course.save()
                return {'message': 'Course successfully registered'} , HTTPStatus.CREATED
            except:
                db.session.rollback()
                return {'message': 'An error occurred while registering course'}, HTTPStatus.INTERNAL_SERVER_ERROR
        return {'message': 'Course does not exist'} , HTTPStatus.NOT_FOUND


    # Delete a course 'function' should also be here
    @students_namespace.expect(courses_registration_model)

    # @student_required()
    def delete(self):

        """ Deregister a  course """

        data = request.get_json()
        authenticated_user_id = get_jwt_identity()
        student = Student.query.filter_by(id=authenticated_user_id).first()   
        data = request.get_json()
        course = Course.query.filter_by(id=data.get('course_id')).first()  
        if course:
            #check if student has registered for the course before
            get_student_in_course = StudentCourse.query.filter_by(student_id=student.id, course_id=course.id).first()
            if get_student_in_course:
                try:
                    get_student_in_course.delete()
                    return {'message': 'Course deleted successfully'} , HTTPStatus.NO_CONTENT
                except:
                    db.session.rollback()
                    return {'message': 'An error occurred while deleting the course'}, HTTPStatus.INTERNAL_SERVER_ERROR
        return {
                'message':'You are not registered for this course'
                } , HTTPStatus.BAD_REQUEST
    # return {'message': 'Course does not exist'} , HTTPStatus.NOT_FOUND



@students_namespace.route('/<int:student_id>/courses')
class RetrieveMyCourse(Resource):

    @students_namespace.marshal_with(courses_registration_model)
    def get(self, student_id):

        """ Retrieve all courses by a student """

        courses = MyCourse.get_student_courses(student_id)
        return courses , HTTPStatus.OK



@students_namespace.route('/<int:student_id>/courses/grade')
class MyGradesView(Resource):
    def get(self):
        return {"message": "Hello Admin nice to meet you"}

    # @admin_required()
    def get(self, student_id):

        """ Fetch a student's grades across all courses"""

        courses = MyCourse.get_student_courses(student_id)
        Studentgrades = []
        
        for course in courses:
            current_grades = {}
            score_in_course = Score.query.filter_by(student_id=student_id , course_id=course.id).first()
            current_grades['course_title'] = course.course_title
            if score_in_course:
                current_grades['score'] = score_in_course.score
                current_grades['grade'] = score_in_course.grade
            else:
                current_grades['score'] = None
                current_grades['grade'] = None 
            Studentgrades.append(current_grade)
        return Studentgrades , HTTPStatus.OK
    













