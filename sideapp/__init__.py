from flask import Flask   

app = Flask(__name__)

# App has a route
@app.route('/')
def home_page():
    return "Welcome to the Sports Tracker Homepage!"
    
@app.route('/results/')
def get_results():
    return "This will be display games that have resulted"

@app.route('/result/<int:result_id>/')
def get_specific_student(result_id):
    return f"This will be a page displaying information about a specific result {result_id}

# Checking if this module is running 
if __name__ == '__main__':
    app.run(debug=True)

# ^^ Delivering simple website ^^
