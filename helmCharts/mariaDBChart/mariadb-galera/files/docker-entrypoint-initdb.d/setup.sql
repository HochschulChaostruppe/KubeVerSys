create or replace database todoLists;
connect todoLists
/*creation of two tables one to store the listnames / titles and one for all list-items*/
create or replace table todoLists.listNames(ID int not null AUTO_INCREMENT, listName char(255) not null, primary key(ID));
create or replace table todoLists.listItems(ID int not null AUTO_INCREMENT, listID int not null, itemName char(255) not null, checked boolean default 0, primary key(ID), foreign key(listID) references listNames(ID));

/*creation of view for easier access by python code*/
create or replace view todoLists.listView 
as select listName, itemName, checked 
from todoLists.listItems 
join todoLists.listNames
on listItems.listID = listNames.ID;

DELIMITER //
/*creation of delete procedure to delete items precisely*/
create or replace procedure deleteItem(listParam CHAR(255), itemParam CHAR(255)) 
BEGIN
    select ID into @currentListID from todoLists.listNames where listName = listParam;
    delete from todoLists.listItems where listID = @currentListID and itemName = itemParam;
END;
//
//
/*creation of delete procedure to delete whole lists easily*/
create or replace procedure deleteList(listParam CHAR(255)) 
BEGIN
    select ID into @currentListID from todoLists.listNames where listName = listParam;
    delete from todoLists.listItems where listID = @currentListID;
    delete from todoLists.listNames where ID = @currentListID;
END;
//
//
/*creation of addItem procedure to add Items to a list by the list name*/
create or replace procedure addItem(listParam CHAR(255), itemParam CHAR(255)) 
BEGIN
    select ID into @currentListID from todoLists.listNames where listName = listParam;
    insert into listItems (listID, itemName) values (@currentListID, itemParam)
END;
//
//
/*creation of addItem procedure to add Items to a list by the list name, additionally specifying checked parameter*/
create or replace procedure addItemCheck(listParam CHAR(255), itemParam CHAR(255), itemChecked boolean) 
BEGIN
    select ID into @currentListID from todoLists.listNames where listName = listParam;
    insert into listItems (listID, itemName, checked) values (@currentListID, itemParam, itemChecked)
END;
//
//
/*creation of checkItem procedure to check a specific item (change value of checked to 1)*/
create or replace procedure checkItem(listParam CHAR(255), itemParam CHAR(255)) 
BEGIN
    select ID into @currentListID from todoLists.listNames where listName = listParam;
    update listItems set checked = 1 values where listID = @currentListID and itemName = itemParam
END;
//
//
/*creation of checkItem procedure to check a specific item (change value of checked to 0)*/
create or replace procedure uncheckItem(listParam CHAR(255), itemParam CHAR(255)) 
BEGIN
    select ID into @currentListID from todoLists.listNames where listName = listParam;
    update listItems set checked = 0 values where listID = @currentListID and itemName = itemParam
END;
//

DELIMITER;

