from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api=Api(app)
CORS(app, origins=['*'])

alumnos=[]

@app.route('/')
def saludo():
    return '<p><b>Bienvenido</b></p>'

class Alumnos(Resource):
    def post(self):
        nuevoAlumno=request.get_json()
        alumnos.append(nuevoAlumno)
        return {
            'success':True,
            'content':nuevoAlumno,
            'message':'Desplegando coco'
        },200
    def get(self):
        return {
            'success':True,
            'content':alumnos,
            'message':'Desplegados todos'
        }
    
api.add_resource(Alumnos,'/alumnos')

if __name__=='__main__':
    app.run()
