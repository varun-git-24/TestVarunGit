from flask import Flask , request

flask_app = Flask(__name__)


@flask_app.route('/')
def home():
    return "Hello, Flask!"


@flask_app.route('/my_details')
def details():
    return 'Varun Rotti'


@flask_app.route('/home/data')
def data():
    name = request.args.get('name')
    salary = request.args.get('salary')
    try:
        if name == 'Anusha':
            return f'{name} is earning {salary} per month'
    except Exception as e:
        return f'An error occurred: {str(e)}'


if __name__ == '__main__':
    flask_app.run(host='0.0.0.0',port=8080,debug=True)
