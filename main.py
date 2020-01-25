from flask import Flask

app=Flask(__name__)

@app.route('/api/add')
def add_return():
    return  "add  sucess"


@app.route('/api/info')
def info_return():
    return "select sucess"

@app.route('/api/update')
def update_return():
    return "update sucess"

@app.route('/api/delete')
def delete_return():
    return  "delete sucess"

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    
