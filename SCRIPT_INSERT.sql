INSERT INTO formato_stock VALUES (1,'Envases de Papel');
INSERT INTO formato_stock VALUES (2,'Envases de Plastico');
INSERT INTO formato_stock VALUES (3,'Envases de Aluminio');
INSERT INTO formato_stock VALUES (4,'Envases de Carton');
INSERT INTO formato_stock VALUES (5,'Bolsas de Papel');
INSERT INTO formato_stock VALUES (6,'Bolsas de Plastico');
INSERT INTO formato_stock VALUES (7,'Bolsas de Aluminio');
INSERT INTO formato_stock VALUES (8,'Cajas Unitarias Carton');
INSERT INTO formato_stock VALUES (9,'Cajas Unitarias Aluminio');
INSERT INTO formato_stock VALUES (10,'Cajas de Madera (Huacal)');
INSERT INTO formato_stock VALUES (11,'Botellas de Plastico');
INSERT INTO formato_stock VALUES (12,'Botellas de Vidrio');
INSERT INTO formato_stock VALUES (13,'Latas');
INSERT INTO formato_stock VALUES (14,'Unidades');
/
INSERT INTO ESTADO_RESERVA VALUES(1,'Agendada');
INSERT INTO ESTADO_RESERVA VALUES(2,'Finalizada');
INSERT INTO ESTADO_RESERVA VALUES(3,'Cancelada');
/
---------- Fin de Cristiancito -----------

INSERT INTO ESTADO_MESA VALUES(1,'Disponible');
INSERT INTO ESTADO_MESA VALUES(2,'En Uso');
INSERT INTO ESTADO_MESA VALUES(3,'Por Limpiar');
INSERT INTO ESTADO_MESA VALUES(4,'Reservada');
/


INSERT INTO MARCA_PRODUCTO VALUES(1, 'Coca-Cola');
INSERT INTO MARCA_PRODUCTO VALUES(2, 'Minuto Verde');
INSERT INTO MARCA_PRODUCTO VALUES(3, 'Colun');
INSERT INTO MARCA_PRODUCTO VALUES(4, 'Cousin n Co');
INSERT INTO MARCA_PRODUCTO VALUES(5, 'Dolbeck');

INSERT INTO PROVEEDOR VALUES(1, 'Coca-Loca');
INSERT INTO PROVEEDOR VALUES(2, 'Frutos');
INSERT INTO PROVEEDOR VALUES(3, 'Lactos');
INSERT INTO PROVEEDOR VALUES(4, 'Jumbo');
INSERT INTO PROVEEDOR VALUES(5, 'El Cielo');


insert into unidad_medida values (1, 'Gramos' );
insert into unidad_medida values (2, 'Kilogramos' );
insert into unidad_medida values (3, 'Mililitros' );
insert into unidad_medida values (4, 'Litros' );



INSERT INTO RANGO_HORA VALUES(1,'09:00-10:00');
INSERT INTO RANGO_HORA VALUES(2,'10:30-11:30');
INSERT INTO RANGO_HORA VALUES(3,'12:00-13:00');
INSERT INTO RANGO_HORA VALUES(4,'13:30-14:30');
INSERT INTO RANGO_HORA VALUES(5,'15:00-16:00');
INSERT INTO RANGO_HORA VALUES(6,'16:30-17:30');
INSERT INTO RANGO_HORA VALUES(7,'18:00-19:00');

INSERT INTO MESAS VALUES(1,3,1);
INSERT INTO MESAS VALUES(2,3,1);
INSERT INTO MESAS VALUES(3,3,1);
INSERT INTO MESAS VALUES(4,3,1);


commit;
