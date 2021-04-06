from flask import Flask, render_template , request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)


#Mysql Connection
config = {
  'user': 'root',
  'password': 'secret',
  'host': '34.234.66.107',
  'database': 'camiones',
  'raise_on_warnings': True
}

#Settings
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM Conductores')
    Conductores = cursor.fetchall()
    print(Conductores)
    ###Conductores Cursor
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM Camiones')
    Camiones = cursor.fetchall()
    print(Camiones)
    ###Conductores Cursor
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM Bases')
    Bases = cursor.fetchall()
    print(Bases)
    ###Conductores Cursor
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM Gasolineras')
    Gasolineras = cursor.fetchall()
    print(Gasolineras)
    ###Conductores Cursor
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM Rutas')
    Rutas = cursor.fetchall()
    print(Rutas)
    ###Conductores Cursor
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM Viajes')
    Viajes = cursor.fetchall()
    print(Viajes)
    ###Conductores Cursor
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM Gastos_Viajes')
    Gastos_Viajes = cursor.fetchall()
    print(Gastos_Viajes)
    #### Send Database Values to Index html
    return render_template('index.html', Conductores = Conductores, Camiones = Camiones, Bases = Bases, Gasolineras = Gasolineras, Rutas = Rutas, Viajes= Viajes, Gastos_Viajes = Gastos_Viajes)
    cursor.close()




@app.route('/', methods=['POST'])
def add_conductor():
  if request.method == 'POST':
      Nombre = request.form['Nombre'];Apellido = request.form['Apellido'];Direccion = request.form['Direccion'];Telefono = request.form['Telefono'];BaseID = request.form['BaseID'];IsActive = request.form['IsActive']; EmployeeID = request.form['EmployeeID']
      #print(fullname); print(phone);print(email) #Printing Request
      cnx = mysql.connector.connect(**config) #Open DB Connection
      cursor = cnx.cursor() #Initializing db Action
      cursor.execute('INSERT INTO Conductores (Nombre,Apellido,Direccion,Telefono,BaseID,IsActive,EmployeeID) VALUES (%s,%s,%s,%s,%s,%s,%s)',(Nombre,Apellido,Direccion,Telefono,BaseID,IsActive,EmployeeID))
      cnx.commit()
      cursor.close()
      flash('New contact Added sucesfully')   
      return redirect(url_for('Index'))

@app.route('/edit/conductores/<id>', methods = ['POST', 'GET'])
def get_conductor(id):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM Conductores WHERE EmployeeID = \'{}\'".format(id))
    data = cursor.fetchall()
    cursor.close()
    print(data[0])
    return render_template('edit-contact.html', conductor = data[0])



@app.route('/update/conductores/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        Nombre = request.form['Nombre'];Apellido = request.form['Apellido'];Direccion = request.form['Direccion'];Telefono = request.form['Telefono'];BaseID = request.form['BaseID'];IsActive = request.form['IsActive']; EmployeeID = request.form['EmployeeID']
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        sql = "UPDATE Conductores SET Nombre = \'{}\' , Apellido = \'{}\' , Direccion = \'{}\' , Telefono = \'{}\', BaseID = \'{}\',IsActive = \'{}\' WHERE EmployeeID = \'{}\'".format(Nombre,Apellido,Direccion,Telefono,BaseID,IsActive,EmployeeID)
        cursor.execute(sql)
        cnx.commit()
        cursor.close()
        flash('Contact Updates Sucesfully')
        return redirect(url_for('Index'))

@app.route('/delete/conductores/<string:id>', methods = ['POST','GET'])
def delete_contact(id):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    cnx.commit()
    cursor.close()
    flash('Contact Removed Successfully')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0", debug=True)


