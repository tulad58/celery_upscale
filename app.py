from flask import Flask, jsonify
from upscale import upscale 
app = Flask('app')

@app.route('/upscale/', methods=['POST'])
def get_task():
    task = upscale('lama_300px.png', 'lama_300px.png', 'EDSR_x2.pb')
    return jsonify({'task_id': 'task'})




app.run(debug=True)