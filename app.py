from flask import Flask, request, jsonify
import math
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Bienvenido a la API de raíz cuadrada. Usa la ruta /sqrt con el parámetro number para obtener la raíz cuadrada de un número. Por ejemplo: /sqrt?number=16"

@app.route('/sqrt', methods=['GET'])
def get_sqrt():
    try:
        number = request.args.get('number', type=float)
        if number is None:
            return jsonify({'error': 'No se proporcionó ningún número.'}), 400

        sqrt_result = math.sqrt(number)
        return jsonify({'number': number, 'sqrt': sqrt_result})
    except ValueError:
        return jsonify({'error': 'Proporcione un número válido.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
