from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from ftplib import FTP
from datetime import datetime
import time
from io import BytesIO

app = Flask(__name__)
api=Api(app)
CORS(app, origins=['*'])

datosTotalesRadiacion=[]

@app.route('/')
def saludo():
    return '<p><b>Bienvenido</b></p>'

def getDatosRad(RadNuevo):
    anio_= RadNuevo['anio']
    mes_= RadNuevo['mes']
    dia_= RadNuevo['dia']
    hr_= RadNuevo['hora']
    minuto_= RadNuevo['minuto']
    #time.sleep(20)
    try:
        fechaRequerida=datetime(anio_,mes_,dia_,hr_,minuto_,25)
        fechaRequerida2=datetime.strftime(fechaRequerida, '%Y%m%d%H%M%S')
        fecha="0011608501"+fechaRequerida2
        
        ftp = FTP('ftp-datos.senamhi.gob.pe')
        ftp.login("ftp_sutron", "Senamhi123")
        r = BytesIO()
        ftp.retrbinary('RETR '+fecha+'.txt', r.write)
        dato_rad=r.getvalue()
        
        dato_rad1=dato_rad.decode()
        
        dato_sep=dato_rad1.split(sep=',')
        
        dato_ind_1=dato_sep[3]
        dato_ind_1=dato_ind_1.split(sep="\n")
        dato_ind_2=dato_sep[6]
        dato_ind_2=dato_ind_2.split(sep="\n")
        dato_ind_3=dato_sep[9]
        dato_ind_3=dato_ind_3.split(sep="\n")
        dato_ind_4=dato_sep[12]
        dato_ind_4=dato_ind_4.split(sep="\n")
        dato_ind_5=dato_sep[15]
        dato_ind_5=dato_ind_5.split(sep="\n")
        dato_ind_6=dato_sep[18]
        dato_ind_6=dato_ind_6.split(sep="\n")
        dato_ind_7=dato_sep[21]
        dato_ind_7=dato_ind_7.split(sep="\n")
        dato_ind_8=dato_sep[24]
        dato_ind_8=dato_ind_8.split(sep="\n")
        dato_ind_9=dato_sep[27]
        dato_ind_9=dato_ind_9.split(sep="\n")
        

        return [dato_sep[0],float(dato_ind_1[0]),dato_ind_1[1],float(dato_ind_2[0]),dato_ind_2[1],float(dato_ind_3[0]),dato_ind_3[1],float(dato_ind_4[0]),dato_ind_4[1],float(dato_ind_5[0]),dato_ind_5[1],float(dato_ind_6[0]),dato_ind_6[1],float(dato_ind_7[0]),dato_ind_7[1],float(dato_ind_8[0]),dato_ind_8[1],float(dato_ind_9[0]),dato_ind_9[1],float(dato_sep[30])]
        
        #tempo='{}:{}'.format(hr_,minuto_)
        #if len(datoPrec_) > 20:
        #    return [tempo,datoPrec_[10],datoPrec_[13],datoPrec_[24]] 
        #else:
        #    return [tempo,datoPrec_[10],datoPrec_[13]]      
    except Exception as e:
        print("Error en el proceso: ",e)

class Radiacion(Resource):
    def post(self):
        nuevaRadiacion = request.get_json()
        datosRadiacion=getDatosRad(nuevaRadiacion)
        nuevaRadiacion['fecha_1']=datosRadiacion[0]
        nuevaRadiacion['indice_1']=datosRadiacion[1]
        nuevaRadiacion['fecha_2']=datosRadiacion[2]
        nuevaRadiacion['indice_2']=datosRadiacion[3]
        nuevaRadiacion['fecha_3']=datosRadiacion[4]
        nuevaRadiacion['indice_3']=datosRadiacion[5]
        nuevaRadiacion['fecha_4']=datosRadiacion[6]
        nuevaRadiacion['indice_4']=datosRadiacion[7]
        nuevaRadiacion['fecha_5']=datosRadiacion[8]
        nuevaRadiacion['indice_5']=datosRadiacion[9]
        nuevaRadiacion['fecha_6']=datosRadiacion[10]
        nuevaRadiacion['indice_6']=datosRadiacion[11]
        nuevaRadiacion['fecha_7']=datosRadiacion[12]
        nuevaRadiacion['indice_7']=datosRadiacion[13]
        nuevaRadiacion['fecha_8']=datosRadiacion[14]
        nuevaRadiacion['indice_8']=datosRadiacion[15]
        nuevaRadiacion['fecha_9']=datosRadiacion[16]
        nuevaRadiacion['indice_9']=datosRadiacion[17]
        nuevaRadiacion['fecha_10']=datosRadiacion[18]
        nuevaRadiacion['indice_10']=datosRadiacion[19]
        datosTotalesRadiacion.append(nuevaRadiacion)        
        return {
            'success': True,
            'content': nuevaRadiacion,
            'message': "listo POST"
        },200
    def get(self):
        return {
            'success':True,
            'content':datosTotalesRadiacion,
            'message':'total de datos acumulados'
        }

api.add_resource(Radiacion,'/radiacion')
if __name__=='__main__':
    app.run(debug=True, port=5560)