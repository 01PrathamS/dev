from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__) 

PROJECTS = [
  {
    "project_id": 1, 
    "title": "first_project", 
    "description": "first project with machine leanring", 
    "status" : "completed"
  }, 
  {
    "project_id": 2, 
    "title": "second_project", 
    "description": "second project with machine leanring", 
    "status" : "completed"
  }, 
  {
    "project_id": 3, 
    "title": "third_project",
    "description": "third project with machine leanring",
    "status" : "completed"
  }, 
  {
    "project_id": 4, 
    "title": "fourth_project", 
    "description": "fourth project with machine leanring", 
    "status" : "completed"
  }
]

@app.route('/')
def hello_world(): 
  return render_template("home.html", projects=PROJECTS)

@app.route('/api/projects')
def show_projects(): 
  return jsonify(PROJECTS)



if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True, port=8080)