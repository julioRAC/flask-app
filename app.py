from flask import Flask, request, jsonify
import math
import os

app = Flask(__name__)

@app.route('/sqrt', methods=['GET'])
def get_sqrt():
    try:
        # Obtiene el parámetro 'number' de la consulta
        number = request.args.get('number', type=float)
        if number is None:
            return jsonify({'error': 'No se proporcionó ningún número.'}), 400

        # Calcula la raíz cuadrada
        sqrt_result = math.sqrt(number)

        # Retorna el resultado en formato JSON
        return jsonify({'number': number, 'sqrt': sqrt_result})
    except ValueError:
        return jsonify({'error': 'Proporcione un número válido.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
