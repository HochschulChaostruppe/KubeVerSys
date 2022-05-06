from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

# APP / API
app = Flask("To-Do-List")
api = Api(app)

# List Parser
list_parser = reqparse.RequestParser()
list_parser.add_argument('list_name', required=True, help='Name (List) cannot be empty!')

# Item Parser
item_parser = reqparse.RequestParser()
item_parser.add_argument('item_name', type=str, required=True)

# Check Parser
check_parser = reqparse.RequestParser()
check_parser.add_argument('item_name', type=str, required=True)
check_parser.add_argument('checked', type=bool, required=True, help='Check (Item) needs to be a boolean (true/false)')

todolists = {
    'shopping': [
        {
            'name': 'masks',
            'checked': False
        },
        {
            'name': 'beer',
            'checked': True
        }
    ],

    'holidays': [
        {
            'name': 'beer',
            'checked': True
        },
        {
            'name': 'passport',
            'checked': False
        }
    ]
}


class Todolists(Resource):
    
    # Shows all todolists
    def get(self):
        return list(todolists.keys()), 200
    
    # Adds a new todolist
    def post(self):
        args = list_parser.parse_args()
        list_name = args['list_name']
        todolists[list_name] = []
        return todolists[list_name], 201
    
    # Deletes an existing todolist
    def delete(self):
        args = list_parser.parse_args()
        list_name = args['list_name']
        if list_name not in todolists.keys():
            abort(404, message=f'List "{list_name}" not found!')
        del todolists[list_name]
        return "", 204
   
class Todoitems(Resource):
    
    # Shows all items from todolist
    def get(self, list_name):
        if list_name not in todolists.keys():
            abort(404, message=f'List "{list_name}" not found!')
        return todolists[list_name], 200
    
    # Adds a new item to todolist
    def post(self, list_name):
        if list_name not in todolists.keys():
            abort(404, message=f'List "{list_name}" not found!')
        args = item_parser.parse_args()
        item_name = {'name': args['item_name'], 'checked': False}
        todolists[list_name].append(item_name)
        return item_name, 201
    
    # Updates the specified items check status
    def put(self, list_name):
        if list_name not in todolists.keys():
            abort(404, message=f'List "{list_name}" not found!')
        args = check_parser.parse_args()
        item_name = args['item_name']
        checked = args['checked']
        list_index = -1
        for i, item in enumerate(todolists[list_name]):
            if item['name'] == item_name:
                list_index = i
                break
        if list_index == -1:
            abort(404, message=f'Item "{item_name}" in List "{list_name}" not found!')
        todolists[list_name][list_index]['checked'] = checked
        return {'name': item_name, 'checked': checked}, 201
            
    # Deletes an existing item
    def delete(self, list_name):
        if list_name not in todolists.keys():
            abort(404, message=f'List "{list_name}" not found!')
        args = item_parser.parse_args()
        item_name = args['item_name']
        list_index = -1
        for i, item in enumerate(todolists[list_name]):
            if item['name'] == item_name:
                list_index = i
                break
        if list_index == -1:
            abort(404, message=f'Item "{item_name}" in List "{list_name}" not found!')
        del todolists[list_name][list_index]
        return "", 204   

    
api.add_resource(Todolists, '/')
api.add_resource(Todoitems, '/<string:list_name>')

def main() -> None:
    app.run()


if __name__ == '__main__':
    main()