from flask_restful import Resource
from flask_restful import reqparse
from flask import Flask
from flask_restful import Api

##http://localhost:8000/?a=2&b=3

class Plus(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('a', required=True, type=int, help='a cannot be blank')
            parser.add_argument('b', required=True, type=int, help='b cannot be blank')
            args = parser.parse_args()
            result = args['a'] + args['b']
            return {'result': result}
        except Exception as e:
            return {'error': str(e)}


app = Flask('plus value')
api = Api(app)
api.add_resource(Plus, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
