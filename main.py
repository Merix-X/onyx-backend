from flask import Flask, request, jsonify
from flask_cors import CORS
import g4f

app = Flask(__name__)
CORS(app)  # Toto povolí CORS pro všechny endpointy

@app.route('/ask', methods=['POST'])
def ask_ai():
    user_query = request.json.get("query")
    if not user_query:
        return jsonify({"error": "No query provided!"}), 400

    response = g4f.ChatCompletion.create(model="gpt-4",
                                         messages=[{"role": "user", "content": user_query}])
    # Zpracování a vrácení odpovědi
    # Příklad: předpokládejme, že response je již řetězec nebo JSON
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
