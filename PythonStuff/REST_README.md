# REST API for TODO Lists

## Usage

[`https://127.0.0.1:5000/`](https://127.0.0.1:5000/)

### Show all todo lists

**Definition**

`GET /`

**Response**

- `200 OK` on success

```json
{
    "0": "shopping",
    "1": "holidays",
    "2": "groceries"
}
```

### Add todo list

**Definition**

`POST /` 

**Arguments**

- `"list_name":string` the name of the new list

**Response**

- `201 Created` on success

```json
Created new list: 'groceries'!
```

### Delete todo list

**Definition**

`DELETE /`

**Arguments**

- `"list_name":string` the name of the list to delete

**Response**

- `204 No content` on success
- `404 Not found` if the list does not exist

```json
Deleted list: 'shopping'!
```

### Show all items from todo list

**Definition**

`GET /<list_name>` 

**Arguments**

- `NONE`

**Response**

- `200 OK` on success
- `404 Not found` if the list does not exist

```json
[
    {
        "item_name": "beer",
        "checked": True
    },
    {
        "item_name": "suncream",
        "checked": False
    }
]

```

### Add a new item to todo list

**Definition**

`POST /<list_name>`

**Arguments**

- `"item_name":string` the name of the item to add (ALWAYS unchecked state!)

**Response**

- `201 Created` on success
- `404 Not found` if list does not exist (should not happen!)

```json
beer added to groceries
```

### Update an items check status (checked / unchecked)

**Definition**

`PUT /<list_name>`

**Arguments**

- `"item_name:string"` the name of the item to (un)check
- `"checked":bool` true for checked, false for unchecked

**Response**

- `201 Created` on success
- `404 Not found` if list (should not happen!) or item in list does not exist


```json
beer in groceries was checked
```

### Delete an item from a list

**Definition**

`DELETE /<list_name>`

**Arguments** 

- `"item_name:string"` the name of the item to delete

**Response**

- `204 No content` on success
- `404 Not found` if list (should not happen!) or item in list does not exist

```json
Deleted item suncream from list groceries!
```