# MPI RMFAR Demo
Usage
-----

#### Clone the repo:

    git clone https://github.com/JuanCa11/RMFAR_Rest_API
    cd RMFAR_Rest_API

#### Create virtualenv:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

#### Run the sample server

    python api.py

#### Try the endpoints:

    curl -XGET "http://localhost:5000/api/recomendaciones?fecha=2020%2D06%2D01%2021%3A00&barrio=PASADENA%20E%2D11&genero=MASCULINO&actividad=SENDERO%20PUBLICO"

#### Response

```json
{
  "pred": "HURTO A PATRIMONIO", 
  "recommendations": [
    {
      "if": " BARRIO MUY PEQUEÑO", 
      "score": 0.1456317844072873, 
      "then": " BARRIO PEQUEÑO"
    }, 
    {
      "if": "IR O ESTAR EN EL MES DE JUNIO", 
      "score": 0.1505289094006772, 
      "then": "IR O ESTAR EN EL MES DE ENERO"
    }, 
    {
      "if": "BARRIO CON DENSIDAD BANCARIA MEDIA", 
      "score": 0.18532698007460324, 
      "then": "BARRIO CON DENSIDAD BANCARIA ALTA"
    }, 
    {
      "if": "LA ACTIVIDAD EN SENDERO PUBLICO", 
      "score": 0.3577326648198124, 
      "then": "LA ACTIVIDAD EN PROPIEDAD PRIVADA"
    }, 
    {
      "if": "BARRIO CON TRANSPORTE BAJO", 
      "score": 0.5398171178432919, 
      "then": "BARRIO CON TRANSPORTE MEDIO"
    }, 
    {
      "if": "BARRIO CON SEGURIDAD MEDIA", 
      "score": 0.5403423680428336, 
      "then": "BARRIO CON SEGURIDAD MUY BAJA"
    }, 
    {
      "if": "IR O ESTAR EN EL/LA NOCHE", 
      "score": 0.5436515249778486, 
      "then": "IR O ESTAR EN EL/LA MAÑANA"
    }, 
    {
      "if": "BARRIO CON DENSIDAD BANCARIA ALTA", 
      "score": 0.6273300240336104, 
      "then": "BARRIO CON DENSIDAD BANCARIA BAJA"
    }
  ], 
  "score": 0.6464238110471306
}
```
