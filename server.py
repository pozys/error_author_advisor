from flask import Flask
# from conf_storage_history_handler import example
app = Flask(__name__)
# app.run(host='192.168.56.104', port=8080)
@app.route("/<name>", methods=['GET'])
def index(name):
    return "Hello World, %s" % name
if __name__ == "__main__":
    app.run(host='192.168.56.104', port=8080, debug=True)


