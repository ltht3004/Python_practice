from flask import Flask, jsonify
import json

app = Flask(__name__)
@app.route('/employees', methods=['GET'])
def get_employees():
    with open('employees.json', 'r') as file:
        employees = json.load(file)
    return jsonify(employees)

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    with open('employees.json', 'r') as file:
        employees = json.load(file)
    for employee in employees:
        if employee['id'] == id:
            return jsonify(employee)
    return jsonify({'message': 'Employee not found'}), 404
if __name__ == '__main__':
    app.run(debug=True) 
    
    
    
    
    
"""from flask import Flask, jsonify
import json
app = Flask(__name__)

def load_employees():
   with open("employees.json", "r", encoding="utf-8") as file:
       return json.load(file)
       
@app.route("/employees", methods=["GET"])
def get_employees():
   return jsonify(load_employees())
   
@app.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
   employees = load_employees()
   for employee in employees:
       if employee["id"] == employee_id:
           return jsonify(employee)
   return jsonify({
       "message": "Employee not found"
   }), 404
   
if __name__ == "__main__":
   app.run(debug=True)"""