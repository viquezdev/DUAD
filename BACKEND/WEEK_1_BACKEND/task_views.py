from flask.views import MethodView
from flask import Flask, request, Response, jsonify
from dataclasses import dataclass
from data import *
import json 


app = Flask(__name__)

@dataclass
class Task:
    identifier:str
    title:str
    description:str
    status:str

def is_valid_task(task):
    current_tasks=read_json_file()
    task_objects = [Task(**task_dict) for task_dict in current_tasks]
    allowed_statuses={"to do","in progress","completed"}
    for element in task_objects:
        if(task.identifier==element.identifier):
            return "Identifier already exists"
    if task.title=="":
        return "Title required"
    if task.description=="":
        return "Description required"
    if task.status.strip().lower() not in  allowed_statuses:
        return "Status must be 'To Do', 'In Progress' or 'Completed'"
    return None

class TaskAPI(MethodView):
    def get(self, identifier=None):
        try:
            current_tasks = read_json_file()
            if not current_tasks:
                return jsonify({"error": "No tasks have been created"}), 400

            status_filter = request.args.get("status")
            task_objects = [Task(**task_dict) for task_dict in current_tasks]
            if status_filter:
                task_objects = [
                    task for task in task_objects
                    if task.status.lower() == status_filter.lower()
                ]

            task_dicts = [task.__dict__ for task in task_objects]

            return jsonify({"data": task_dicts}), 200
    
        except ValueError as ex:
            return jsonify(message=str(ex)), 400
        except Exception as ex:
            return jsonify(message=str(ex)), 500

    def post(self,identifier=None):
        try:
            data=request.get_json(silent=True)
            if data is None:
                return jsonify({"error":"No valid JSON body or incorrect Content-Type"}),400
            required_fields={"identifier","title","description","status"}
            if not data or not required_fields.issubset(data):
                return jsonify({"error":"Missing data"}),400
            else:
                task=Task(
                    identifier=data["identifier"],
                    title=data["title"],
                    description=data["description"],
                    status=data["status"]
                )
                validation_error=is_valid_task(task)
                if validation_error:
                    return jsonify({"error":validation_error}),400
                
                current_tasks = read_json_file()
                if not isinstance(current_tasks, list):
                    current_tasks = []
                task_dict = {
                    "identifier": task.identifier,
                    "title": task.title,
                    "description": task.description,
                    "status": task.status
                }
                current_tasks.append(task_dict)
                save_json_file(current_tasks)
                return jsonify({"message": "Task created"}), 201
        except ValueError as ex:
            return jsonify(message=str(ex)), 400
        except Exception as ex:
            return jsonify(message=str(ex)), 500
    
    def put(self,identifier):
        try:
            data=request.get_json(silent=True)
            if data is None:
                return jsonify({"error":"No valid JSON body or incorrect Content-Type"}),400
            current_tasks=read_json_file()
            task_objects = [Task(**task_dict) for task_dict in current_tasks]
            task_found=False
            for element in task_objects:
                if element.identifier ==identifier:
                    if "title" in data:
                        element.title=data["title"]
                    if "description" in data:
                        element.description=data["description"]
                    if "status" in data:
                        allowed_statuses={"to do","in progress","completed"}
                        if data["status"].strip().lower() not in allowed_statuses:
                            return jsonify({"error":"Invalid status. Must be 'To Do', 'In Progress' or 'Completed'"}), 400
                        element.status=data["status"]
                    task_found=True
                    break
                    
            if not task_found:
                return jsonify({"error": "Task not found"}), 404
            
            updated_tasks = [task.__dict__ for task in task_objects]
            save_json_file(updated_tasks)

            return jsonify({"message": "Task updated"}), 200
    
        except ValueError as ex:
            return jsonify(message=str(ex)), 400
        except Exception as ex:
            return jsonify(message=str(ex)), 500
        
    def patch(self,identifier):
        try:
            data=request.get_json(silent=True)
            if data is None:
                return jsonify({"error":"No valid JSON body or incorrect Content-Type"}),400
            current_tasks=read_json_file()
            task_objects = [Task(**task_dict) for task_dict in current_tasks]
            task_found=False
            for element in task_objects:
                if element.identifier ==identifier:
                    if "title" in data:
                        element.title=data["title"]
                    if "description" in data:
                        element.description=data["description"]
                    if "status" in data:
                        allowed_statuses={"to do","in progress","completed"}
                        if data["status"].strip().lower() not in allowed_statuses:
                            return jsonify({"error":"Invalid status. Must be 'To Do', 'In Progress' or 'Completed'"}), 400
                        element.status=data["status"]
                    task_found=True
                    break
                    
            if not task_found:
                return jsonify({"error": "Task not found"}), 404
            
            updated_tasks = [task.__dict__ for task in task_objects]
            save_json_file(updated_tasks)

            return jsonify({"message": "Task updated"}), 200
    
        except ValueError as ex:
            return jsonify(message=str(ex)), 400
        except Exception as ex:
            return jsonify(message=str(ex)), 500

    def delete(self,identifier):
        try:
            task_found=False
            current_tasks=read_json_file()
            task_objects = [Task(**task_dict) for task_dict in current_tasks]
            new_task_objects=[]
            for element in task_objects:
                if element.identifier==identifier:
                    task_found=True
                else:
                    new_task_objects.append(element)
            if not task_found:
                return jsonify({"error": "Task not found"}), 404
            
            task_dicts = [task.__dict__ for task in new_task_objects]
            save_json_file(task_dicts)
            return jsonify({"message": "Task deleted"}), 200
    
        except ValueError as ex:
            return jsonify(message=str(ex)), 400
        except Exception as ex:
            return jsonify(message=str(ex)), 500
        

task_view = TaskAPI.as_view('task_api')
app.add_url_rule('/tasks', defaults={'identifier': None},view_func=task_view, methods=['GET', 'POST'])

app.add_url_rule('/tasks/<identifier>',view_func=task_view, methods=['GET', 'PUT', 'PATCH', 'DELETE'])


if __name__ == '__main__':
    app.run(debug=True)