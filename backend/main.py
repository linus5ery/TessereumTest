from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sample employee data
employees = [
    {"id": 1, "name": "John Doe", "email": "johndoe@example.com", "address": "123 Elm St", "activated": 1},
    {"id": 2, "name": "Jane Smith", "email": "janesmith@example.com", "address": "456 Oak St", "activated": 0},
    {"id": 3, "name": "James Chen", "email": "jameschen@example.com", "address": "789 Clothes St", "activated": 0},
    {"id": 4, "name": "Lindsey Park", "email": "lindsey@example.com", "address": "012 Elm St", "activated": 1},
    {"id": 5, "name": "Linus Liew", "email": "linusliew@example.com", "address": "345 Oak St", "activated": 1},
    # Add more sample employees as needed
]

@app.route('/employee', methods=['GET'])
def get_all_employees():
    return jsonify(employees)

@app.route('/employee/<int:emp_id>', methods=['GET'])
def get_employee(emp_id):
    employee = next((e for e in employees if e["id"] == emp_id), None)
    if employee:
        return jsonify(employee)
    else:
        abort(404, description="Employee not found")

@app.route('/employee', methods=['POST'])
def add_employee():
    data = request.json
    new_id = max([e['id'] for e in employees]) + 1
    new_employee = {
        "id": new_id,
        "name": data['name'],
        "email": data['email'],
        "address": data['address'],
        "activated": data['activated']
    }
    employees.append(new_employee)
    return jsonify({"message": "Employee added successfully", "employee": new_employee}), 201

@app.route('/employee/<int:emp_id>', methods=['DELETE'])
def delete_employee(emp_id):
    global employees
    employees = [e for e in employees if e["id"] != emp_id]
    return jsonify({"message": "Employee data deleted successfully"}), 200

@app.route('/employee/<int:emp_id>', methods=['PUT'])
def update_employee(emp_id):
    employee = next((e for e in employees if e["id"] == emp_id), None)
    if not employee:
        abort(404, description="Employee not found")
    
    data = request.json
    if 'name' in data:
        employee['name'] = data['name']
    if 'email' in data:
        employee['email'] = data['email']
    if 'address' in data:
        employee['address'] = data['address']
    if 'activated' in data:
        employee['activated'] = data['activated']

    return jsonify({"message": "Employee data updated successfully", "updated_data": employee}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)
