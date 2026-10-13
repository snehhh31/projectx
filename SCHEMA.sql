USE Projectrec_1;
show tables;
CREATE TABLE goodsinfo (
	Code  INT PRIMARY KEY,
    Item_name VARCHAR(100),
    Size VARCHAR(30),
    Item_quantity INT,
    Item_price INT,
    Company_name VARCHAR(100),
    Mobileno VARCHAR(20),
    Placeoforigin VARCHAR(100)
);
show tables;
describe goodsinfo ;
select*from goodsinfo;