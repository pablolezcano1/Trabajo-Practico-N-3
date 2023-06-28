# Cambiar el ID numerico por el uuid4.
# Agregar estilo de Boostrap.
# Agregar layout.html, EXTENDS, BLOCK.
# Guardar y Leer los datos con las funciones que estan dentro de el archivo toJSON. Moficar la funcion
# guardar_lista_diccionarios_como_json para que me mantenga los datos y no los sobreescriba, o bien arbitrar
# un metodo de guardado que cumpla la misma funcion. 

from flask import Flask, render_template, request, redirect
from uuid import uuid4
from tojson import guardar_lista_diccionarios_como_json, cargar_lista_diccionarios_desde_json

app = Flask(__name__)

# Lista de tareas (simulación de una base de datos)
tasks = [
    {"id": str(uuid4()), "title": "Tarea 1", "description": "Descripción de la tarea 1"},
    {"id": str(uuid4()), "title": "Tarea 2", "description": "Descripción de la tarea 2"},
    {"id": str(uuid4()), "title": "Tarea 3", "description": "Descripción de la tarea 3"}
]

# Archivo donde se guardarán los datos
DATA_FILE = "tasks.json"

# Cargar datos al inicio
try:
    tasks = cargar_lista_diccionarios_desde_json(DATA_FILE)
except FileNotFoundError:
    tasks = [
        {"id": str(uuid4()), "title": "Tarea 1", "description": "Descripción de la tarea 1"},
        {"id": str(uuid4()), "title": "Tarea 2", "description": "Descripción de la tarea 2"},
        {"id": str(uuid4()), "title": "Tarea 3", "description": "Descripción de la tarea 3"}
    ]
    guardar_lista_diccionarios_como_json(tasks, DATA_FILE)

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        task = {"id": str(uuid4()), "title": title, "description": description}
        tasks.append(task)
        guardar_lista_diccionarios_como_json(tasks, DATA_FILE)
        return redirect("/")
    else:
        return render_template("create.html")


@app.route("/edit/<string:task_id>", methods=["GET", "POST"])
def edit(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return "Tarea no encontrada"

    if request.method == "POST":
        task["title"] = request.form["title"]
        task["description"] = request.form["description"]
        guardar_lista_diccionarios_como_json(tasks, DATA_FILE)
        return redirect("/")
    else:
        return render_template("edit.html", task=task)

# task = next((task for task in tasks if task["id"] == task_id), None)
    # if task is None: 
    #     return "Tarea no encontrada"

    # if request.method == "POST":
    #     task["title"] = request.form["title"]
    #     task["description"] = request.form["description"]
    #     return redirect("/")
    # else:
    #     return render_template("edit.html", task=task)

@app.route("/delete/<string:task_id>")
def delete(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    guardar_lista_diccionarios_como_json(tasks, DATA_FILE)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

