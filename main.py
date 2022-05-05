from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
import mariadb
import sys

# APP / API
app = Flask("To-Do-List")
api = Api(app)

# MariaDB Connection
try:
    conn = mariadb.connect(
        user='rn',
        password='dhge2022/vs!',
        host='157.90.152.100',
        port=3306,
        database='todoLists'
    )
except mariadb.Error as e:
    print(f'Error connecting to MariaDB: {e}')
    sys.exit(1)
cur = conn.cursor()

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


class Todolists(Resource):
    
    # Shows all todolists
    def get(self):
        todo_lists = cur.execute("select * from todolists.listNames")
        return todo_lists, 200
    
    # Adds a new todolist
    def post(self):
        args = list_parser.parse_args()
        list_name = args['list_name']
        cur.execute("insert into todoLists.listNames (listName) values (?)", (list_name,))
        return f'Created new list: "{list_name}"!', 201
    
    # Deletes an existing todolist
    def delete(self):
        args = list_parser.parse_args()
        list_name = args['list_name']
        todo_lists = cur.execute("select * from todolists.listNames")
        if list_name not in todo_lists:
            abort(404, message=f'List "{list_name}" not found!')
        cur.execute("call deleteList(?)", (list_name,))
        return f'Deleted list: "{list_name}"!', 204
   
class Todoitems(Resource):
    
    # Shows all items from todolist
    def get(self, list_name):
        todo_lists = cur.execute("select * from todolists.listNames")
        if list_name not in todo_lists:
            abort(404, message=f'List "{list_name}" not found!')
        list_items = cur.execute("select * from listView where listName = ?", (list_name))
        return list_items, 200
    
    # Adds a new item to todolist
    def post(self, list_name):
        todo_lists = cur.execute("select * from todolists.listNames")
        if list_name not in todo_lists:
            abort(404, message=f'List "{list_name}" not found!')
        args = item_parser.parse_args()
        item_name = args['item_name']
        cur.execute("call addItem(?, ?)", (list_name, item_name))
        return f'{item_name} added to {list_name}', 201
    
    # Updates the specified items check status
    def put(self, list_name):
        todo_lists = cur.execute("select * from todolists.listNames")
        if list_name not in todo_lists:
            abort(404, message=f'List "{list_name}" not found!')
        args = check_parser.parse_args()
        item_name = args['item_name']
        checked = args['checked']
        list_items = cur.execute("select * from listView where listName = ?", (list_name))
        if item_name not in list_items:
            abort(404, message=f'Item "{item_name}" in list "{list_name}" not found!')
        if checked:
            cur.execute("call checkItem(?, ?)", (list_name, item_name))
        else:
            cur.execute("call uncheckItem(?, ?)", (list_name, item_name))
        return f'{item_name} in {list_name} was {"un" if not checked else ""}checked', 201
            
    # Deletes an existing item
    def delete(self, list_name):
        todo_lists = cur.execute("select * from todolists.listNames")
        if list_name not in todo_lists:
            abort(404, message=f'List "{list_name}" not found!')
        args = item_parser.parse_args()
        item_name = args['item_name']
        list_items = cur.execute("select * from listView where listName = ?", (list_name))
        if item_name not in list_items:
            abort(404, message=f'Item "{item_name}" in list "{list_name}" not found!')
        cur.execute("call deleteItem(?, ?)", (list_name, item_name))
        return f'Deleted item "{item_name}" from list "{list_name}"!', 204   

    
api.add_resource(Todolists, '/')
api.add_resource(Todoitems, '/<string:list_name>')

def main() -> None:
    app.run()


if __name__ == '__main__':
    main()