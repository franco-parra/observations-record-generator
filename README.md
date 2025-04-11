# Observations Record Generator API

API para generar automáticamente registros de observaciones en formato Excel a partir de datos JSON.

## Configuración del Entorno

1. Clonar el repositorio:

```bash
git clone [URL_DEL_REPOSITORIO]
cd observations-record-generator
```

2. Crear un entorno virtual e instalar dependencias:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Configurar variables de entorno:

```bash
export FLASK_ENV=production
export SECRET_KEY=tu-clave-secreta-aqui
export SHEET_NAME=Hoja1  # Nombre de la hoja en el archivo Excel
```

## Estructura del Proyecto

```
observations-record-generator/
├── app.py                 # Aplicación principal
├── config/
│   ├── settings.py        # Configuración de la aplicación
│   ├── template.xlsx      # Plantilla Excel
│   └── cell_mapping.json  # Mapeo de celdas
├── requirements.txt       # Dependencias
└── README.md             # Documentación
```

## Ejecución en Producción

1. Asegurarse de que el archivo `template.xlsx` esté en la carpeta `config/`
2. Iniciar el servidor:

```bash
python app.py
```

El servidor se ejecutará en `http://0.0.0.0:5000`

## Formato del JSON de Entrada

El API espera un JSON con la siguiente estructura. A continuación se detallan todas las claves posibles y su descripción:

### Información Básica

- `street_or_road`: Calle o camino
- `number`: Número de la propiedad
- `entry_date`: Fecha de ingreso (formato dd-mm-yyyy)
- `owner_name`: Nombre o razón social del propietario
- `owner_email`: Correo electrónico del propietario
- `entry_number`: Número de ingreso (formato ING-XXX)
- `architect_name`: Nombre o razón social del arquitecto
- `architect_email`: Correo electrónico del arquitecto

### Normas y Regulaciones

La sección `norms` puede contener las siguientes claves:

- `land_use`: Uso de suelo
- `easements`: Cesiones
- `grouping`: Agrupamiento
- `construction_coefficient`: Coeficiente de constructibilidad
- `land_occupation_coefficient`: Coeficiente de ocupación de suelo
- `upper_floors_occupation_coefficient`: Coeficiente de ocupación de pisos superiores
- `minimum_plot_area`: Superficie predial mínima
- `maximum_building_height`: Altura máxima de edificación
- `adjacent_building`: Adosamiento
- `setback`: Distanciamiento
- `front_garden`: Antejardín
- `chamfer`: Ochavo
- `grade`: Rasante
- `maximum_density`: Densidad máxima
- `parking`: Estacionamientos
- `zoning_strips`: Franjas
- `risk_areas`: Áreas de riesgo
- `occupation_density_and_contribution_calculation`: Densidad de ocupación y cálculo de aportes

Cada norma puede contener:

- `status`: Estado de cumplimiento (ver valores válidos abajo)
- `observations`: Observaciones sobre la norma (opcional)

### Información de Revisión

- `review_date`: Fecha de revisión (formato dd-mm-yyyy)
- `observations_response_date`: Fecha de respuesta a observaciones (formato dd-mm-yyyy)
- `reviewing_architect_name`: Nombre y apellido del arquitecto revisor

### Valores válidos para el campo `status`:

- `"complies"`: Cumple
- `"does_not_comply"`: No cumple
- `"not_applicable"`: No aplica

### Ejemplo de JSON completo:

```json
{
  "street_or_road": "Av. Einstein",
  "number": "264",
  "entry_date": "01-01-2024",
  "owner_name": "Comercial Color-Estampados Limitada",
  "owner_email": "correo@ejemplo.com",
  "entry_number": "ING-123456",
  "architect_name": "Miguel A. Pérez Rojas",
  "architect_email": "arquitecto@ejemplo.com",
  "norms": {
    "land_use": {
      "status": "complies"
    },
    "easements": {
      "status": "does_not_comply",
      "observations": "Observaciones sobre cesiones"
    },
    "grouping": {
      "status": "not_applicable"
    },
    "construction_coefficient": {
      "status": "complies"
    },
    "land_occupation_coefficient": {
      "status": "complies"
    },
    "upper_floors_occupation_coefficient": {
      "status": "complies"
    },
    "maximum_building_height": {
      "status": "complies"
    },
    "parking": {
      "status": "does_not_comply",
      "observations": "Puntos 3 y 4 del informe de Solicitud fundada adjunta no se ajustan a preceptos de la DDU 260"
    }
  },
  "review_date": "01-01-2024",
  "observations_response_date": "31-01-2024",
  "reviewing_architect_name": "Francisca Salazar Herrera"
}
```

## Ejemplo de Llamada a la API

```bash
curl -X POST http://localhost:5000/fill-template \
  -H "Content-Type: application/json" \
  -d '{
    "street_or_road": "Av. Einstein",
    "number": "264",
    "entry_date": "01-01-2024",
    "owner_name": "Comercial Color-Estampados Limitada",
    "entry_number": "ING-123456",
    "architect_name": "Miguel A. Pérez Rojas",
    "norms": {
        "land_use": {
            "status": "complies"
        }
    },
    "review_date": "01-01-2024",
    "observations_response_date": "31-01-2024",
    "reviewing_architect_name": "Francisca Salazar Herrera"
  }'
```

La API devolverá un archivo Excel con los datos ingresados.

## Notas Importantes

- El archivo Excel generado se descargará automáticamente
- El formato de fecha debe ser "dd-mm-yyyy"
- Todos los campos son opcionales excepto los necesarios para el formato del documento
