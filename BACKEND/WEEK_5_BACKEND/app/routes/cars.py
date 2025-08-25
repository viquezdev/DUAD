from flask import request, Response, jsonify, Blueprint
from app.db.pg_manager import PgManager
from app.repositories.car_repository import CarRepository

cars_bp=Blueprint("cars",__name__)

@cars_bp.route("/", methods=["POST"])
def create_car():
    try:
        car_data=request.get_json()
        required_fields = ["make", "model", "manufacture_year", "car_status"]
        missing_fields = [field for field in required_fields if field not in car_data]

        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

        db_manager = PgManager(
        db_name="postgres",
        user="postgres",
        password="VKVLLNTL2U",
        host="localhost"
        )

        cars_repo = CarRepository(db_manager)
        cars_repo.create(**car_data)
        db_manager.close_connection()
        return jsonify({"message":"Car created succesfully"}),201
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500

@cars_bp.route("/<int:car_id>/status", methods=["PUT"])
def update_car_status(car_id):
    try:    
        db_manager = PgManager(
        db_name="postgres",
        user="postgres",
        password="VKVLLNTL2U",
        host="localhost"
        )
        car_data=request.get_json()

        if not car_data or "car_status" not in car_data:
            return jsonify({"error": "Missing 'car_status' field"}), 400
        
        new_status=car_data.get("car_status")
        cars_repo = CarRepository(db_manager)
        cars_repo.update_status(car_id,new_status)
        
        db_manager.close_connection()
        return jsonify({"message":"Car status updated succesfully"}),200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500

@cars_bp.route("/", methods=["GET"])
def get_all_cars():
    
    try:
        
        db_manager = PgManager(
        db_name="postgres",
        user="postgres",
        password="VKVLLNTL2U",
        host="localhost"
        )
        cars_repo = CarRepository(db_manager)
        data_cars=None
        
        filters = {
                "id": cars_repo.get_by_id,
                "make": cars_repo.get_by_make,
                "model": cars_repo.get_by_model,
                "manufacture_year": cars_repo.get_by_manufacture_year,
                "car_status": cars_repo.get_by_car_status
            }

        for key, func in filters.items():
            if key in request.args:
                data_cars = func(request.args[key])
                break

        if data_cars is None:
            data_cars=cars_repo.get_all()
        
        if not data_cars:
            return jsonify({"data": [], "message": "No cars found"}), 404
        
        db_manager.close_connection()
        return jsonify({"data": data_cars}), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
