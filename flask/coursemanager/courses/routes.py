from flask import Blueprint, jsonify, request

courses_bp = Blueprint("courses", __name__, url_prefix="/api/courses")

courses = []

def find_course(course_id):
    for course in courses:
        if course["id"] == course_id:
            return course
    return None

@courses_bp.route("/<int:course_id>", methods=["GET"])
def get_course(course_id):
    course = find_course(course_id)

    if course:
        return jsonify(course)

    return jsonify({"error": "Course not found"}), 404

@courses_bp.route("/", methods=["POST"])
def create_course():
    data = request.get_json()

    course = {
        "id": len(courses) + 1,
        "name": data["name"]
    }

    courses.append(course)

    return jsonify(course), 201
@courses_bp.route("/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    course = find_course(course_id)

    if not course:
        return jsonify({"error": "Course not found"}), 404

    data = request.get_json()
    course["name"] = data["name"]

    return jsonify(course)

@courses_bp.route("/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    course = find_course(course_id)

    if not course:
        return jsonify({"error": "Course not found"}), 404

    courses.remove(course)

    return jsonify({"message": "Course deleted"})