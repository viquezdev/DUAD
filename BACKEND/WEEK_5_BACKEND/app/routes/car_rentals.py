from flask import request, Response, jsonify, Blueprint
from app.db.pg_manager import PgManager
from app.repositories.car_rental_repository import CarRentalRepository

car_rentals_bp=Blueprint("car_rentals",__name__)


@car_rentals_bp.route("/", methods=["POST"])
def create_car_rental():
    try:
        car_rental_data=request.get_json()
        required_fields = ["user_id", "car_id", "rental_date", "rental_status"]
        missing_fields = [f for f in required_fields if f not in car_rental_data]

        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
        db_manager = PgManager(
        db_name="postgres",
        user="postgres",
        password="VKVLLNTL2U",
        host="localhost"
        )

        car_rentals_repo = CarRentalRepository(db_manager)
        car_rentals_repo.create(**car_rental_data)
        db_manager.close_connection()
        return jsonify({"message":"Car rental created succesfully"}),201
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500

@car_rentals_bp.route("/<int:car_rental_id>/status", methods=["PUT","PATCH"])
def update_car_rental_status(car_rental_id):
    try:    
        db_manager = PgManager(
        db_name="postgres",
        user="postgres",
        password="VKVLLNTL2U",
        host="localhost"
        )
        car_rental_data=request.get_json()
        if not car_rental_data or "rental_status" not in car_rental_data:
            return jsonify({"error": "Missing 'rental_status' field"}), 400
        
        new_status=car_rental_data.get("rental_status")
        car_rentals_repo = CarRentalRepository(db_manager)
        car_rentals_repo.update_status(car_rental_id,new_status)
        db_manager.close_connection()
        return jsonify({"message":"Car rental status updated succesfully"}),200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500

@car_rentals_bp.route("/<int:car_rental_id>/complete", methods=["PUT","PATCH"])
def complete_rental(car_rental_id):
    try:    
        db_manager = PgManager(
        db_name="postgres",
        user="postgres",
        password="VKVLLNTL2U",
        host="localhost"
        )
        car_rentals_repo = CarRentalRepository(db_manager)
        car_rentals_repo.complete_rental(car_rental_id)
        db_manager.close_connection()
        return jsonify({"message":"Rental completed succesfully"}),200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500

@car_rentals_bp.route("/", methods=["GET"])
def get_all_car_rentals():
    
    try:
    
        db_manager = PgManager(
        db_name="postgres",
        user="postgres",
        password="VKVLLNTL2U",
        host="localhost"
        )
        car_rentals_repo = CarRentalRepository(db_manager)
        data_car_rentals=None
        
        filters = {
                "id": car_rentals_repo.get_by_id,
                "user_id": car_rentals_repo.get_by_user_id,
                "car_id": car_rentals_repo.get_by_car_id,
                "rental_date": car_rentals_repo.get_by_rental_date,
                "rental_status": car_rentals_repo.get_by_rental_status
            }

        for key, func in filters.items():
            if key in request.args:
                data_car_rentals = func(request.args[key])
                break

        if data_car_rentals is None:
            data_car_rentals=car_rentals_repo.get_all()
        
        if not data_car_rentals:
            return jsonify({"data": [], "message": "No car rentals found"}), 404
        db_manager.close_connection()
        return jsonify({"data": data_car_rentals}), 200
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500

