DROP DATABASE IF EXISTS db_poliur_sm;   # Удаление базыесли она существует

CREATE DATABASE db_poliur_sm;   # Создание базы
SHOW DATABASES; # показать базы находящиеся на сервере
USE db_poliur_sm; # Переход в базу
DROP TABLE IF EXISTS test1; # удаление таблицы если она существует
CREATE TABLE IF NOT EXISTS test1 ( #создаие таблицы с заданными столбцами и параметрами
  id INT UNSIGNED PRIMARY KEY  AUTO_INCREMENT,
  txt VARCHAR(100) DEFAULT 'TEXT' # тип данных VARCHAR (количество знаков 100) и автозаполнением TEXT
);
DESC test1; # Использование оператора для описания списка определений столбцов для указанной таблицы.
SHOW CREATE TABLE test1; # показать содержимое таблицы



CREATE TABLE agent (  # таблица контрагентов
  id SMALLINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,  #первичный ключ
  name VARCHAR(100) NOT NULL,  #наименование
  nicname VARCHAR(100) DEFAULT '  ', # условное обозначение
  status ENUM('поставщик', 'клиент'), # статус
  tnum VARCHAR(25) DEFAULT 'номер телефона',  # номер телефона
  email VARCHAR(30) DEFAULT '  ', # электронная почта
  text VARCHAR(200) DEFAULT '  '  # дополниетльная информация
);
DESC agent;



DROP  TABLE IF EXISTS order_sm;
CREATE TABLE order_sm ( 
  id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  date_in DATE NOT NULL, 
  date_out DATE NOT NULL, 
  id_agent SMALLINT UNSIGNED NOT NULL, 
  priority SMALLINT NOT NULL DEFAULT '0', 
  text VARCHAR(150),
  FOREIGN KEY (id_agent)  REFERENCES  agent(id) ON DELETE RESTRICT 
);
DESC  order_sm;



DROP  TABLE IF EXISTS workers;
CREATE TABLE workers (  # таблица сотрудников
  id SMALLINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,  #первичный ключ
  name VARCHAR(50) NOT NULL,  #ФИО
  status VARCHAR(100) DEFAULT '  ', # должность
  path VARCHAR(100) DEFAULT  '  ',  
  doc_name VARCHAR(20) DEFAULT '  ', 
  foto_name VARCHAR(20) DEFAULT '  ',  
  tnum VARCHAR(25) DEFAULT '+7(###)###-##-##', 
  email VARCHAR(30) DEFAULT '  ', # электронная почта
  text VARCHAR(200) DEFAULT '  ',  # дополниетльная информация
  salary INT NOT NULL DEFAULT '10800', 
  bonus SMALLINT NOT NULL DEFAULT '0', 
  date_in DATE, 
  data_out DATE 
);
DESC workers;



DROP  TABLE IF EXISTS hollyday;
CREATE TABLE hollyday (  #таблица празднки
  id_date DATE PRIMARY KEY, #дата и первичный ключ ключ
  name VARCHAR(100) DEFAULT 'праздник или пренос' #наименование праздника
);
DESC hollyday;



DROP  TABLE IF EXISTS works_hours;
CREATE TABLE work_hours(  #рабочие часы
  id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, #первичный ключ
  date_work DATE NOT NULL,  #дата
  hours TINYINT NOT NULL DEFAULT '0', #часы поле коофициента
  id_workers SMALLINT UNSIGNED, #ключ работника
  INDEX id_wo(id_workers), #индексация столбца id_agent
  CONSTRAINT hou_id_wor FOREIGN KEY (id_workers) REFERENCES workers(id) ON DELETE RESTRICT,
  CONSTRAINT id_w_h FOREIGN KEY (date_work) REFERENCES hollyday(id_date) ON DELETE RESTRICT 
);
DESC work_hours;



DROP  TABLE IF EXISTS group_sm;
CREATE TABLE group_sm(  #таблица групп
  id SMALLINT  PRIMARY KEY AUTO_INCREMENT, #первичный ключ группы
  name VARCHAR(30) NOT NULL DEFAULT 'Новая группа'  #имя
);
DESC group_sm;



DROP  TABLE IF EXISTS subgroup;
CREATE TABLE subgroup (  #таблица подгрупп
  id SMALLINT  PRIMARY KEY AUTO_INCREMENT, #первичный ключ подгруппы
  name VARCHAR(20) NOT NULL DEFAULT 'Новая подгруппа',  #имя
  id_group SMALLINT NOT NULL DEFAULT '1', #ключ группы
  INDEX id_gr(id_group), #индексация столбца id_agent
  CONSTRAINT sub_id_gro FOREIGN KEY (id_group) REFERENCES group_sm(id) ON DELETE RESTRICT 
);
DESC subgroup;



DROP  TABLE IF EXISTS nomenclature;
CREATE TABLE nomenclature (  #таблица номенклатуры
  id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,  #первичный ключ
  name VARCHAR(50) NOT NULL, #номенклатура
  nicname VARCHAR(50) DEFAULT '  ',  #условное наименование
  id_subgroup SMALLINT NOT NULL DEFAULT '1', #ключ от подгруппы
  text VARCHAR(150), #описание или коментарий
  path VARCHAR(100), #к чертежу/фото
  volume DECIMAL(8,3),  #объём для изделий
  id_form INT UNSIGNED, #номер формы для изделий
  INDEX id_sub(id_subgroup), #индексация столбца id_agent
  CONSTRAINT nom_id_sub FOREIGN KEY (id_subgroup) REFERENCES subgroup(id) ON DELETE RESTRICT 
);
DESC nomenclature;



DROP  TABLE IF EXISTS hardness;
CREATE TABLE hardness(  #таблица твердостей
  id SMALLINT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(10) NOT NULL
);
DESC hardness;



DROP  TABLE IF EXISTS source;
CREATE TABLE source(  #таблица подразделений источников записей
  id SMALLINT PRIMARY KEY AUTO_INCREMENT 
  name VARCHAR(20) NOT NULL 
);
DESC source;



DROP TABLE IF EXISTS teg;
CREATE TABLE teg(
  id int UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  name TINYTEXT NOT NULL
);
DESC teg;



DROP  TABLE IF EXISTS balance;
CREATE TABLE balance(  #таблица сальдо
  id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,  #первичный ключ
  plan_sm BOOL NOT NULL  DEFAULT '0',  #статус планового или натурального
  id_nomenclature INT UNSIGNED NOT NULL, #номенклатура
  date DATE NOT NULL,  #дата
  quantity MEDIUMINT NOT NULL DEFAULT '0',  #количественное выражение
  sum INT NOT NULL DEFAULT '0',  #денежное выражение
  id_source SMALLINT NOT NULL, #ключ источник/автора записи
  id_hardness SMALLINT,  #ключ твердости
  id_order INT UNSIGNED,  # ключ заказа
  id_plane INT UNSIGNED,  # номер операции с пометкой план для натуры
  text VARCHAR(150),  #коментарии
  CONSTRAINT bal_id_nom FOREIGN KEY (id_nomenclature) REFERENCES nomenclature(id) ON DELETE RESTRICT,
  CONSTRAINT bal_id_sou FOREIGN KEY (id_source) REFERENCES source(id) ON DELETE RESTRICT,
  CONSTRAINT bal_id_har FOREIGN KEY (id_hardness) REFERENCES hardness(id) ON DELETE RESTRICT,
  CONSTRAINT bal_id_ord FOREIGN KEY (id_order) REFERENCES order_sm(id) ON DELETE RESTRICT
);
DESC balance;



DROP TABLE IF EXISTS tegs_ag;
CREATE TABLE tegs_ag(
  id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  id_ag INT UNSIGNED NOT NULL,
  id_teg INT UNSIGNED NOT NULL,
  CONSTRAINT tegs_id_ag FOREIGN KEY (id_ag) REFERENCES agent(id) ON DELETE RESTRICT,
  CONSTRAINT tegs_id_teg FOREIGN KEY (id_teg) REFERENCES teg(id) ON DELETE RESTRICT
);
DESC tegs_ag;

DROP TABLE IF EXISTS stat_ship;

CREATE TABLE stat_ship(
id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
stat VARCHAR(50) NOT NULL #статус доставки
);

DESC stat_ship;



DROP TABLE IF EXISTS shipment;
CREATE TABLE shipment(
id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,  #первичный ключ
  payment BOOL NOT NULL  DEFAULT '0',  #сторона плательщик
  date_in DATE NOT NULL,  #дата отправки
  date_out DATE NOT NULL,  #дата условного прибытия
  sum INT NOT NULL DEFAULT '0',  #денежное выражение
  ship_num TEXT(20) NOT NULL, #номер доставки
  id_stat INT UNSIGNED, #ключ словаря статусов
  id_ship_agent SMALLINT UNSIGNED, #транспортная
  text VARCHAR(150),  #коментарии
  CONSTRAINT ship_id_stat FOREIGN KEY (id_stat) REFERENCES stat_ship(id) ON DELETE RESTRICT,
  CONSTRAINT ship_id_shipagent FOREIGN KEY (id_ship_agent) REFERENCES agent(id) ON DELETE RESTRICT
);

DESC shipment;


DROP TABLE IF EXISTS sum_ship;

CREATE TABLE sum_ship(
id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
id_bal INT UNSIGNED, # ключ опрерации отпуска
id_ship INT UNSIGNED, # ключ опрации доставки
CONSTRAINT sum_id_ship FOREIGN KEY (id_ship) REFERENCES shipment(id) ON DELETE RESTRICT,
CONSTRAINT sum_id_bal FOREIGN KEY (id_bal) REFERENCES balance(id) ON DELETE RESTRICT
);

DESC sum_ship;


SHOW TABLES; # показать таблицы
SHOW CREATE DATABASE db_poliur_sm; # показать содержимое таблицы
SHOW WARNINGS; # подробности по ошибкам