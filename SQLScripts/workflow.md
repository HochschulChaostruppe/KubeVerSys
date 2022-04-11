# SQLQueries

###Get Queries:

Get whole List:
`select * from listView where listName = <yourListName>;``

Get Listnames:
`select * from todolists.listNames;`

Get single item:
`select * from todoLists.listView where itemName = <yourItemName>;`

Get single item from specific list:
`select * from todoLists.listView where itemName = <yourItemName> and listName = <yourListName>;`

###Add Queries:

Add List:
`insert into todoLists.listNames (listName) values (<yourListName>);`

Add Item (Check not specified):
`call addItem(<yourListName>, <yourItemName>);`

Add Item (Check specified):
`call addItemChecked(<yourListName>, <yourItemName>, <0|1>);`

###Check Queries:

Checking a listItem:
`call checkItem(<yourListName>, <yourItemName>);`

Unchecking a listItem:
`call uncheckItem(<yourListName>, <yourItemName>);`

###Delete Queries:

Delete item from list:
`call deleteItem(<yourListName>, <yourItemName>);`

Delete whole list:
`call deleteList(<yourListName>);`
