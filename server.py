from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

DELAY = 10

@app.route('/status', methods=['GET'])
def get_status():

    time.sleep(random.uniform(0, DELAY))
    status = random.choice(['pending', 'completed', 'error'])

    # Reducing Error Chances - Use the below code only if you want to reduce the error chances
    # status = random.choices(['pending', 'completed', 'error'], weights=[70, 25, 5], k=1)[0]

    return jsonify({"result": status})


if __name__ == '__main__':
    app.run(port=8000)
