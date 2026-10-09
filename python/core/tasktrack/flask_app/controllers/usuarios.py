from flask import render_template, redirect, request, session, flash
from flask_app import app, bcrypt 
from flask_app.models.usuario import Usuario

@app.route('/')
def inicio():
    # Si el usuario ya inició sesión, redirigir directamente al panel de tareas
    if 'usuario_id' in session:
        return redirect('/tareas')
    return render_template('login_registro.html')

@app.route('/registro', methods=['POST'])
def registro():
    # Validar campos del formulario de registro
    if not Usuario.validar_registro(request.form):
        return redirect('/')
    
    # Encriptar la contraseña antes de guardar en MySQL con Bcrypt
    contrasena_encriptada = bcrypt.generate_password_hash(request.form['contrasena'])
    
    datos_usuario = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "contrasena": contrasena_encriptada
    }
    
    # Guardar en la base de datos y guardar ID en la sesión
    usuario_id = Usuario.guardar(datos_usuario)
    session['usuario_id'] = usuario_id
    session['usuario_nombre'] = request.form['nombre']
    
    return redirect('/tareas')

@app.route('/login', methods=['POST'])
def login():
    # Buscar usuario por correo electrónico
    usuario = Usuario.obtener_por_email({'email': request.form['email']})
    
    # Verificar si existe el usuario y si la contraseña coincide
    if not usuario or not bcrypt.check_password_hash(usuario.contrasena, request.form['contrasena']):
        flash("Credenciales inválidas. Verifica tu correo y contraseña.", "login")
        return redirect('/')
    
    # Iniciar sesión
    session['usuario_id'] = usuario.id
    session['usuario_nombre'] = usuario.nombre
    
    return redirect('/tareas')

@app.route('/logout')
def logout():
    # Limpiar todos los datos de la sesión
    session.clear()
    return redirect('/')