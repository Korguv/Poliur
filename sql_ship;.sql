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
  id_sum INT UNSIGNED NOT NULL, #содержание доставки
  date_in DATE NOT NULL,  #дата отправки
  date_out DATE NOT NULL,  #дата условного прибытия
  sum INT NOT NULL DEFAULT '0',  #денежное выражение
  ship_num TEXT(20) NOT NULL, #номер доставки
  id_stat INT UNSIGNED, #ключ словаря статусов
  id_ship_agent INT UNSIGNED, #транспортная
  text VARCHAR(150),  #коментарии
  CONSTRAINT ship_id_sum FOREIGN KEY (id_sum) REFERENCES sum_ship(id) ON DELETE RESTRICT,
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

DESC shipment;