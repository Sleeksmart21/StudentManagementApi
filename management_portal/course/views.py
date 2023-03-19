from flask_restx import Namespace, Resource, fields

course_namespace = Namespace('course', description='Name space for Courses')


score_add_model = course_namespace.model(
    'ScoreAdd', {
        'student_id': fields.Integer(required=False, description='ID of student'),
        'course_id': fields.Integer(required=True, description='ID of course'),
        'score': fields.Integer(required=True, description="Score value"),
    }
)


@course_namespace.route('/')
class HelloAuth(Resource):
    def get(self):
        return {"message": "Hello Welcome to Your Courses, nice to meet you"}


@course_namespace.route('/create_course')
class CourseCreation(Resource):
    def post(self):
        return {"message": "Hello Welcome to Your Courses, nice to meet you"}



@course_namespace.route('/retrieve_courses')
class AllCoursesInSchool(Resource):
    def get(self):
        return {"message": "Hello Welcome to Your Courses, nice to meet you"}


@course_namespace.route('/add_score')
class AddCourseScore(Resource):
    def post(self):
        return {"message": "Hello Welcome to Your Courses, nice to meet you"}
