
from flask import request, jsonify, Blueprint
from repositories.product_repository import CarRepository

cars_bp=Blueprint("cars",__name__)

@cars_bp.route("/", methods=["POST"])
def create_car():
    try:
        car_data=request.get_json()
        required_fields = ["make", "model", "year"]
        missing_fields = [field for field in required_fields if field not in car_data]

        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

        new_car=CarRepository.create(**car_data)
        if new_car:
            return jsonify({"message":"Car created succesfully"}),201
        return jsonify({"error":"error creating car"}),400
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@cars_bp.route("/", methods=["GET"])
def get_all_cars():
    try:
        
        data_cars=CarRepository.get_all()
        
        if not data_cars:
            return jsonify({"data": [], "message": "No cars found"}), 404
        
        return jsonify({"data": data_cars}), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@cars_bp.route("/<identifier>", methods=["GET"])
def get_by_id(identifier):
    try:
        
        data_cars=CarRepository.get_by_id(identifier)
        
        if not data_cars:
            return jsonify({"data": [], "message": "No car found"}), 404
        
        return jsonify({"data": data_cars}), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    
@cars_bp.route("/<identifier>", methods=["DELETE"])
def delete_car(identifier):
    try:
            
            data_cars=CarRepository.delete(identifier)

            if data_cars is None:
                return jsonify({"data": [], "message": "No car found"}), 404

            return jsonify({
                "message": f"Car with ID {identifier} was deleted successfully"
            }), 200

    except Exception as ex:
        print(str(ex))
        return jsonify({"message": "Error while deleting a car."}), 500
    

@cars_bp.route("/<identifier>", methods=["PUT"])
def update_car(identifier):
    try:
        data_car=request.get_json()
        
        updated_car=CarRepository.update(
            car_id=identifier,
            make=data_car.get("make"),
            model=data_car.get("model"),
            year=data_car.get("year")
        )
        if not updated_car:
            return jsonify({"error": "Car not found"}), 404
        return jsonify({
            "message": f"Car with ID {identifier} was updated successfully"
        }), 200

    except Exception as ex:
        return jsonify({"error": "Error updating car", "details": str(ex)}), 500
    

@cars_bp.route("/assign-user", methods=["PUT"])
def assign_car_to_user():
    try:
        data_car = request.get_json()

        car_id = data_car.get("car_id")
        user_id = data_car.get("user_id")

        if not car_id or not user_id:
            return jsonify({"error": "car_id and user_id are required"}), 400

        updated_car = CarRepository.assign_to_user(car_id, user_id)

        if not updated_car:  
            return jsonify({"message": f"Car {car_id} or User {user_id} not found"}), 404

        return jsonify({
            "message": f"Car with ID {car_id} assigned to User with ID {user_id} successfully",
            "car": updated_car
        }), 200
    
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
    

@cars_bp.route("/unassigned", methods=["GET"])
def get_cars_whithout_users():
    try:
        data_cars=CarRepository.get_cars_without_users()
        
        if not data_cars:
            return jsonify({"data": [], "message": "No cars found"}), 404
        
        return jsonify({"data": data_cars}), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500