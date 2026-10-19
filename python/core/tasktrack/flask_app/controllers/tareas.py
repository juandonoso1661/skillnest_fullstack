from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.tarea import Tarea
from flask_app.models.categoria import Categoria
from datetime import datetime

@app.route('/tareas')
def ver_tareas():
    if 'usuario_id' not in session:
        return redirect('/')
    
    lista_tareas = Tarea.obtener_por_usuario({'usuario_id': session['usuario_id']})
    lista_categorias = Categoria.obtener_por_usuario({'usuario_id': session['usuario_id']})
    
    hoy = datetime.now().date()
    pendientes = sum(1 for t in lista_tareas if t.estado == 'Pendiente')
    en_progreso = sum(1 for t in lista_tareas if t.estado == 'En progreso')
    completadas = sum(1 for t in lista_tareas if t.estado == 'Completada')
    
    for tarea in lista_tareas:
        tarea.dias_restantes = (tarea.fecha_limite - hoy).days

    return render_template('mis_tareas.html', tareas=lista_tareas, categorias=lista_categorias, 
                           pendientes=pendientes, en_progreso=en_progreso, completadas=completadas)

@app.route('/tareas/nueva')
def nueva_tarea():
    if 'usuario_id' not in session:
        return redirect('/')
    categorias = Categoria.obtener_por_usuario({'usuario_id': session['usuario_id']})
    return render_template('nueva_tarea.html', categorias=categorias)

@app.route('/tareas/crear', methods=['POST'])
def crear_tarea():
    if 'usuario_id' not in session:
        return redirect('/')
    if not Tarea.validar_tarea(request.form):
        return redirect('/tareas/nueva')
    
    datos = {
        'titulo': request.form['titulo'],
        'categoria_id': request.form['categoria_id'],
        'prioridad': request.form['prioridad'],
        'fecha_limite': request.form['fecha_limite'],
        'estado': 'Pendiente',
        'descripcion': request.form['descripcion'],
        'usuario_id': session['usuario_id']
    }
    Tarea.guardar(datos)
    return redirect('/tareas')

@app.route('/tareas/<int:id>')
def detalle_tarea(id):
    if 'usuario_id' not in session:
        return redirect('/')
    tarea = Tarea.obtener_por_id({'id': id})
    if not tarea or tarea.usuario_id != session['usuario_id']:
        return redirect('/tareas')
    return render_template('detalle_tarea.html', tarea=tarea)

@app.route('/tareas/editar/<int:id>')
def editar_tarea(id):
    if 'usuario_id' not in session:
        return redirect('/')
    tarea = Tarea.obtener_por_id({'id': id})
    if not tarea or tarea.usuario_id != session['usuario_id']:
        return redirect('/tareas')
    categorias = Categoria.obtener_por_usuario({'usuario_id': session['usuario_id']})
    return render_template('editar_tarea.html', tarea=tarea, categorias=categorias)

@app.route('/tareas/actualizar/<int:id>', methods=['POST'])
def actualizar_tarea(id):
    if 'usuario_id' not in session:
        return redirect('/')
    if not Tarea.validar_tarea(request.form):
        return redirect(f'/tareas/editar/{id}')
    
    datos = {
        'id': id,
        'titulo': request.form['titulo'],
        'categoria_id': request.form['categoria_id'],
        'prioridad': request.form['prioridad'],
        'fecha_limite': request.form['fecha_limite'],
        'descripcion': request.form['descripcion'],
        'usuario_id': session['usuario_id']
    }
    Tarea.actualizar(datos)
    return redirect(f'/tareas/{id}')

@app.route('/tareas/completar/<int:id>')
def completar_tarea(id):
    if 'usuario_id' not in session:
        return redirect('/')
    Tarea.marcar_completada({'id': id, 'usuario_id': session['usuario_id']})
    return redirect(f'/tareas/{id}')

@app.route('/tareas/borrar/<int:id>')
def borrar_tarea(id):
    if 'usuario_id' not in session:
        return redirect('/')
    Tarea.eliminar({'id': id, 'usuario_id': session['usuario_id']})
    return redirect('/tareas')