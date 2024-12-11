ALTER TABLE `zona_fit`.`cliente` 
ADD UNIQUE INDEX `membresia_UNIQUE` (`membresia`);
USE zona_fit;
SELECT * FROM `zona_fit`.`cliente` WHERE `membresia` IN (100, 200);

INSERT INTO `zona_fit`.`cliente` (`nombre`, `apellido`, `membresia`) 
VALUES ('Jorge', 'Garcia', 100);

DESCRIBE `zona_fit_db`.`cliente`;
SELECT * FROM zona_fit.cliente;

ALTER TABLE cliente MODIFY id INT AUTO_INCREMENT PRIMARY KEY;


INSERT INTO cliente (nombre, apellido, membresia) 
VALUES ("Malena", "Patrona", 200);
