create database todoLists;
connect todoLists
--creation of two tables one to store the listnames / titles and one for all list-items
create table todoLists.listNames(ID int not null AUTO_INCREMENT, listName char(255) not null, primary key(ID));
create table todoLists.listItems(ID int not null AUTO_INCREMENT, listID int not null, itemName char(255) not null, checked boolean default 0, primary key(ID), foreign key(listID) references listNames(ID));

--creation of view for easier access by python code
create view todoLists.listView 
as select listName, itemName, checked 
from todoLists.listItems 
join todoLists.listNames
on listItems.listID = listNames.ID;

--creation of delete procedure to delete whole lists easily
DELIMITER //
create or replace procedure deleteList(IN listParam CHAR(255)) 
BEGIN
    select ID into @currentListID from todoLists.listNames where listName = listParam;
    delete from todoLists.listItems where listID = @currentListID;
    delete from todoLists.listNames where ID = @currentListID;
END;
//

DELIMITER;

