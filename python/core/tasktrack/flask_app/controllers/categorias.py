from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.categoria import Categoria

@app.route('/categorias')
def ver_categorias():
    if 'usuario_id' not in session:
        return redirect('/')
    categorias_usuario = Categoria.obtener_por_usuario_con_conteo({'usuario_id': session['usuario_id']})
    return render_template('categorias.html', categorias=categorias_usuario)

@app.route('/categorias/nueva')
def nueva_categoria():
    if 'usuario_id' not in session:
        return redirect('/')
    return render_template('nueva_categoria.html')

@app.route('/categorias/crear', methods=['POST'])
def crear_categoria():
    if 'usuario_id' not in session:
        return redirect('/')
    
    datos = {
        'nombre_categoria': request.form['nombre_categoria'],
        'usuario_id': session['usuario_id']
    }
    
    if not Categoria.validar_categoria(datos):
        return redirect('/categorias/nueva')
        
    Categoria.guardar(datos)
    return redirect('/categorias')