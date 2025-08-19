CREATE TABLE lyfter_car_rental.users
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
	name character varying(50) NOT NULL,
	email character varying(100) NOT NULL,
    username character varying(50) NOT NULL,
    password character varying(255) NOT NULL,
	birth_date date NOT NULL,
	account_status character varying(30) NOT NULL,
    PRIMARY KEY (id)
);



insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Hadria Deere', 'hdeere0@census.gov', 'hdeere0', 'pI7+3vwYC_yS', '2013-06-02', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Darius Mulloch', 'dmulloch1@smugmug.com', 'dmulloch1', 'pU9*X8xiD(', '1976-02-16', 'suspended');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Maisey Grigorey', 'mgrigorey2@51.la', 'mgrigorey2', 'aA1(oO<>}N0R_#Yf', '2018-02-05', 'suspended');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Osbourn Isham', 'oisham3@usda.gov', 'oisham3', 'bC4?k''VM,w9SA', '2005-07-24', 'suspended');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Agata Moggle', 'amoggle4@360.cn', 'amoggle4', 'oR9/+yf3yx8#_', '1995-03-24', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Aylmar Fieldsend', 'afieldsend5@upenn.edu', 'afieldsend5', 'wM4@7ymd"&B', '1996-12-29', 'suspended');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Wilden Allabush', 'wallabush6@usnews.com', 'wallabush6', 'sJ7*qoK(d%sXPUI6', '1987-04-23', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Friederike Tuffs', 'ftuffs7@wunderground.com', 'ftuffs7', 'yQ1~k1I$tN', '1979-12-20', 'inactive');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Mikol Glison', 'mglison8@is.gd', 'mglison8', 'oG4$3Y_9xhXb', '1984-05-12', 'suspended');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Lauren Habercham', 'lhabercham9@slideshare.net', 'lhabercham9', 'tZ8{{|1~lAqr|gF', '2015-10-21', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Maisie Swinnerton', 'mswinnertona@ezinearticles.com', 'mswinnertona', 'vE9!uDe@w?(IXbo', '2015-02-21', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Tiena Geeraert', 'tgeeraertb@example.com', 'tgeeraertb', 'vO8>h\(vCnGxuJy', '1977-12-05', 'inactive');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Gregoor Gooke', 'ggookec@51.la', 'ggookec', 'tC7}OXR+Bf7N9q/?', '2015-10-23', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Conroy McKeand', 'cmckeandd@yellowbook.com', 'cmckeandd', 'zB1`nZO=I!e_n.F', '1973-10-21', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Lev Lelliott', 'llelliotte@rakuten.co.jp', 'llelliotte', 'uT7(1I_}xW6', '1987-11-04', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Shannen Petyanin', 'spetyaninf@squarespace.com', 'spetyaninf', 'aM5`2~H9)', '2006-01-12', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Cody Wroth', 'cwrothg@issuu.com', 'cwrothg', 'jX1,YUfv%wk`j+j', '1987-11-25', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Corry Connelly', 'cconnellyh@canalblog.com', 'cconnellyh', 'gV8#,s{Aw_a', '1990-12-03', 'suspended');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Rasia Rentelll', 'rrentellli@1und1.de', 'rrentellli', 'gI5<@/}*w~dtYH#', '2003-12-07', 'inactive');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Saidee Dallender', 'sdallenderj@biglobe.ne.jp', 'sdallenderj', 'mD9`&EDk!m"Q5', '1970-08-16', 'suspended');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Agnella Guyonnet', 'aguyonnetk@jigsy.com', 'aguyonnetk', 'tT6"!KB)Ak)S', '2020-05-11', 'suspended');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Steven Aleswell', 'saleswelll@go.com', 'saleswelll', 'wD7@b10!ZUnZ', '1995-06-04', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Mechelle Ivory', 'mivorym@who.int', 'mivorym', 'wA0,oQ!TsIyjr', '1981-07-17', 'suspended');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Val Keddey', 'vkeddeyn@opera.com', 'vkeddeyn', 'zK9,5?,h?g4{j*6o', '2007-04-20', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Shir Diddams', 'sdiddamso@noaa.gov', 'sdiddamso', 'iY3#$JqqWw', '1995-03-18', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Ross Gibbetts', 'rgibbettsp@google.de', 'rgibbettsp', 'uQ9$l4jK}J77e.`', '1994-01-25', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Alexandra Enston', 'aenstonq@fema.gov', 'aenstonq', 'pP3<8tuOWy', '2004-06-22', 'inactive');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Damara Alecock', 'dalecockr@pen.io', 'dalecockr', 'zQ6+V*Cd9', '1994-06-01', 'inactive');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Florentia Farfoot', 'ffarfoots@upenn.edu', 'ffarfoots', 'kB4#Q0Vz', '2019-08-20', 'suspended');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Sheila-kathryn Monks', 'smonkst@4shared.com', 'smonkst', 'eP4"O$L,"', '1980-06-27', 'inactive');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Austina Rizzini', 'arizziniu@mediafire.com', 'arizziniu', 'iX4)@D8o3N5', '2018-09-24', 'suspended');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Ryon Ryley', 'rryleyv@mit.edu', 'rryleyv', 'aS4<AJ%?8/+7VN2', '2004-10-13', 'suspended');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Yanaton Mulroy', 'ymulroyw@ow.ly', 'ymulroyw', 'fZ9/u#3s', '2023-11-10', 'suspended');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Lil Gellately', 'lgellatelyx@nationalgeographic.com', 'lgellatelyx', 'sQ5.e"PuEJGBC5@', '1972-11-17', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Horatius Morrall', 'hmorrally@tmall.com', 'hmorrally', 'sV4"JBdQKSrak', '2013-08-01', 'inactive');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Rowen Sanders', 'rsandersz@java.com', 'rsandersz', 'vU1.KBL`L5h*Y', '2003-03-13', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Mycah Morratt', 'mmorratt10@rediff.com', 'mmorratt10', 'qN5=%`#_&6x', '1994-06-07', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Gery Wayper', 'gwayper11@java.com', 'gwayper11', 'uV7}zc9<.?H.+', '2025-02-17', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Reg Madine', 'rmadine12@mapy.cz', 'rmadine12', 'aM1'',tEq<', '2012-07-21', 'inactive');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('April Heritege', 'aheritege13@weather.com', 'aheritege13', 'oO1+2Y*)J/4C', '2005-01-31', 'inactive');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Zena Scarse', 'zscarse14@sohu.com', 'zscarse14', 'cV3''<O=$mfk', '2002-02-27', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Stu O''Teague', 'soteague15@etsy.com', 'soteague15', 'vQ3$("19', '2021-05-25', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Sallyann Antoszczyk', 'santoszczyk16@slideshare.net', 'santoszczyk16', 'zM0`T`2x4a~&', '2017-03-23', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Humphrey Chastaing', 'hchastaing17@nature.com', 'hchastaing17', 'aY8~v<WTf', '1991-11-13', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Malena de Amaya', 'mde18@earthlink.net', 'mde18', 'pS5>=h|},@''JwU{G', '1980-01-13', 'suspended');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Helge Narbett', 'hnarbett19@independent.co.uk', 'hnarbett19', 'lE1,N$zwo/*', '1998-09-04', 'inactive');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Cyndia Aleksankov', 'caleksankov1a@hao123.com', 'caleksankov1a', 'iE3*XCDMDmS)"uu', '2010-01-30', 'suspended');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Birgit Laxtonne', 'blaxtonne1b@google.it', 'blaxtonne1b', 'xR8+wK3{eTKQ<oU', '1994-11-20', 'inactive');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Rozella Bixley', 'rbixley1c@imgur.com', 'rbixley1c', 'kB8_J$b%w=/cY', '2024-09-17', 'suspended');
insert into lyfter_car_rental.users (name, email, username, password, birth_date, account_status) values ('Marjory Castiglione', 'mcastiglione1d@dagondesign.com', 'mcastiglione1d', 'dY5*2o%=3''', '1982-09-14', 'inactive');