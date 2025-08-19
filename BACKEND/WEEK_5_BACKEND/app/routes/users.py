from flask import request, Response, jsonify, Blueprint
from app.db.pg_manager import PgManager
from app.repositories.user_repository import UserRepository

users_bp=Blueprint("users",__name__)

@users_bp.route("/", methods=["POST"])
def create_user():
    user_data=request.get_json()

    db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="VKVLLNTL2U",
    host="localhost"
    )

    users_repo = UserRepository(db_manager)
    users_repo.create(**user_data)
    db_manager.close_connection()
    return jsonify({"message":"User created succesfully"}),201


@users_bp.route("/<int:user_id>/status", methods=["PUT","PATCH"])
def update_user_status(user_id):
    db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="VKVLLNTL2U",
    host="localhost"
    )
    user_data=request.get_json()
    new_status=user_data.get("account_status")
    users_repo = UserRepository(db_manager)
    users_repo.update_status(user_id,new_status)
    db_manager.close_connection()
    return jsonify({"message":"User status updated succesfully"}),200


@users_bp.route("/<int:user_id>/moroso", methods=["PUT","PATCH"])
def flag_user(user_id):
    db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="VKVLLNTL2U",
    host="localhost"
    )
    users_repo = UserRepository(db_manager)
    users_repo.flag_user_as_moroso(user_id)
    db_manager.close_connection()
    return jsonify({"message":"User flagged as moroso"}),200












# def is_valid_task(data):
#     current_tasks=read_json_file()
#     required_fields={"identifier", "title", "description", "status"}
#     missing_fields=required_fields-data.keys()
#     allowed_statuses={"to do","in progress","completed"}
#     errors=[]
#     if missing_fields:
#         errors.append(f"Missing fields: {', '.join(missing_fields)}")
    
#     if data.get("title", "").strip() == "":
#         errors.append("Title is required")

#     if data.get("description", "").strip() == "":
#         errors.append("Description is required")

#     allowed_statuses = {"to do", "in progress", "completed"}
#     if data.get("status", "").strip().lower() not in allowed_statuses:
#         errors.append("Status must be 'To Do', 'In Progress' or 'Completed'")

#     current_tasks = read_json_file()
#     if any(task["identifier"] == data.get("identifier") for task in current_tasks):
#         errors.append("Identifier already exists")

#     return errors if errors else None

# @app.route("/tasks", methods=["GET"])
# def get_task():
#     try:
#         current_tasks = read_json_file()
#         if not current_tasks:
#             return jsonify({"data": [], "message": "No tasks found"}), 200

#         status_filter = request.args.get("status")
#         if status_filter:
#             current_tasks=list(
#                 filter(lambda task: task["status"].lower() == status_filter.lower(), current_tasks)
#             )

#         return jsonify({"data": current_tasks}), 200
    
#     except ValueError as ex:
#         print(str(ex))
#         return jsonify({"message": "Invalid input"}), 400

#     except Exception as ex:
#         print(str(ex))
#         return jsonify({"message": "There was a problem getting the tasks"}), 500


# @app.route("/tasks", methods=["POST"])
# def create_task():
#     try:
#         data = request.get_json(silent=True)
#         if data is None:
#             return jsonify({"error": "No valid JSON body or incorrect Content-Type"}), 400

#         validation_errors = is_valid_task(data)
#         if validation_errors:
#             return jsonify({"errors": validation_errors}), 400

#         task = Task(**data)
#         current_tasks = read_json_file()
#         if not isinstance(current_tasks, list):
#             current_tasks = []

#         current_tasks.append(asdict(task))
#         save_json_file(current_tasks)
#         return jsonify({
#             "message": f"Task with ID {task.identifier} created successfully"
#         }), 201

#     except ValueError as ex:
#         print(str(ex))
#         return jsonify({"message": "Invalid input"}), 400

#     except Exception as ex:
#         print(str(ex))
#         return jsonify({"message": "Error while creating your task."}), 500

# @app.route("/tasks/<identifier>", methods=["PUT","PATCH"])
# def update_task(identifier):
#     try:
#         data=request.get_json(silent=True)
#         if data is None:
#             return jsonify({"error":"No valid JSON body or incorrect Content-Type"}),400
#         current_tasks=read_json_file()
#         task_found=False
#         updated_task=None
#         for element in current_tasks:
#             if element["identifier"] ==identifier:
#                 if "title" in data:
#                     element["title"]=data["title"]
#                 if "description" in data:
#                     element["description"]=data["description"]
#                 if "status" in data:
#                     allowed_statuses={"to do","in progress","completed"}
#                     if data["status"].strip().lower() not in allowed_statuses:
#                         return jsonify({"error":"Invalid status. Must be 'To Do', 'In Progress' or 'Completed'"}), 400
#                     element["status"]=data["status"]
#                 updated_task=element.copy()
#                 task_found=True
#                 break
                
#         if not task_found:
#             return jsonify({"error": "Task not found"}), 404
        
#         save_json_file(current_tasks)

#         return jsonify({
#             "message": f"Task with ID {identifier} was updated successfully"
#         }), 200
    
#     except ValueError as ex:
#         print(str(ex))
#         return jsonify({"message": "Invalid input"}), 400

#     except Exception as ex:
#         print(str(ex))
#         return jsonify({"message": "Error while updating your task."}), 500


# @app.route("/tasks/<identifier>", methods=["DELETE"])
# def delete_task(identifier):
#     try:
#         current_tasks=read_json_file()
#         deleted_task=None
#         new_tasks = []
#         for element in current_tasks:
#             if element["identifier"] == identifier:
#                 deleted_task = element.copy()
#             else:
#                 new_tasks.append(element)

#         if deleted_task is None:
#             return jsonify({"error": "Task not found"}), 404

#         save_json_file(new_tasks)

#         return jsonify({
#             "message": f"Task with ID {identifier} was deleted successfully"
#         }), 200
    
#     except ValueError as ex:
#         print(str(ex))
#         return jsonify({"message": "Invalid input"}), 400

#     except Exception as ex:
#         print(str(ex))
#         return jsonify({"message": "Error while deleting your task."}), 500





