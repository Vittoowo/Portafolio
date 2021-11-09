DROP TABLE boleta CASCADE CONSTRAINTS;

DROP TABLE estado_mesa CASCADE CONSTRAINTS;

DROP TABLE estado_orden CASCADE CONSTRAINTS;

DROP TABLE estado_reserva CASCADE CONSTRAINTS;

DROP TABLE formato_stock CASCADE CONSTRAINTS;

DROP TABLE informe_rendimiento CASCADE CONSTRAINTS;

DROP TABLE marca_producto CASCADE CONSTRAINTS;

DROP TABLE mesas CASCADE CONSTRAINTS;

DROP TABLE orden CASCADE CONSTRAINTS;

DROP TABLE pedido_producto CASCADE CONSTRAINTS;

DROP TABLE pedido_proveedor CASCADE CONSTRAINTS;

DROP TABLE plato CASCADE CONSTRAINTS;

DROP TABLE platos_orden CASCADE CONSTRAINTS;

DROP TABLE productos CASCADE CONSTRAINTS;

DROP TABLE productos_receta CASCADE CONSTRAINTS;

DROP TABLE proveedor CASCADE CONSTRAINTS;

DROP TABLE receta CASCADE CONSTRAINTS;

DROP TABLE reserva CASCADE CONSTRAINTS;

DROP TABLE unidad_medida CASCADE CONSTRAINTS;

DROP TABLE utilidad_diarias CASCADE CONSTRAINTS;

DROP TABLE utilidad_mensual CASCADE CONSTRAINTS;

CREATE TABLE boleta (
    id_boleta       NUMBER(10) NOT NULL,
    mesas_id_mesa   NUMBER(3) NOT NULL,
    total_boleta    NUMBER(6) NOT NULL,
    fecha_boleta    DATE NOT NULL
);

ALTER TABLE boleta ADD CONSTRAINT boleta_pk PRIMARY KEY ( id_boleta );

CREATE TABLE estado_mesa (
    id_est_mesa      NUMBER(1) NOT NULL,
    desc_estd_mesa   NVARCHAR2(25) NOT NULL
);

ALTER TABLE estado_mesa ADD CONSTRAINT estado_mesa_pk PRIMARY KEY ( id_est_mesa );

CREATE TABLE estado_orden (
    id_est_ord    NUMBER(1) NOT NULL,
    desc_estado   NVARCHAR2(1) NOT NULL
);

ALTER TABLE estado_orden ADD CONSTRAINT estado_orden_pk PRIMARY KEY ( id_est_ord );

CREATE TABLE estado_reserva (
    id_est_reserva      NUMBER(1) NOT NULL,
    desc_estd_reserva   NVARCHAR2(25) NOT NULL
);

ALTER TABLE estado_reserva ADD CONSTRAINT estado_reserva_pk PRIMARY KEY ( id_est_reserva );

CREATE TABLE formato_stock (
    id_formato_stock     NUMBER(2) NOT NULL,
    desc_formato_stock   VARCHAR2(25) NOT NULL
);

ALTER TABLE formato_stock ADD CONSTRAINT formato_stock_pk PRIMARY KEY ( id_formato_stock );

CREATE TABLE informe_rendimiento 
    
    -- No Columns 
;

CREATE TABLE marca_producto (
    id_marca   NUMBER(5) NOT NULL,
    marca      NVARCHAR2(25) NOT NULL
);

ALTER TABLE marca_producto ADD CONSTRAINT marca_producto_pk PRIMARY KEY ( id_marca );

CREATE TABLE mesas (
    id_mesa                   NUMBER(3) NOT NULL,
    capacidad                 NUMBER(2) NOT NULL,
    estado_mesa_id_est_mesa   NUMBER(1) NOT NULL
);

ALTER TABLE mesas ADD CONSTRAINT mesas_pk PRIMARY KEY ( id_mesa );

CREATE TABLE orden (
    id_orden                  NUMBER(10) NOT NULL,
    boleta_id_boleta          NUMBER(10) NOT NULL,
    hora_inicio               TIMESTAMP WITH LOCAL TIME ZONE NOT NULL,
    hora_term                 TIMESTAMP WITH LOCAL TIME ZONE NOT NULL,
    estado_orden_id_est_ord   NUMBER(1) NOT NULL
);

ALTER TABLE orden ADD CONSTRAINT orden_pk PRIMARY KEY ( id_orden );

CREATE TABLE pedido_producto (
    pedido_proveedor_id_pedido   NUMBER(10) NOT NULL,
    productos_id_producto        NUMBER(20) NOT NULL,
    cantidad                     NUMBER(4,2) NOT NULL
);

ALTER TABLE pedido_producto ADD CONSTRAINT pedido_producto_pk PRIMARY KEY ( pedido_proveedor_id_pedido,
                                                                            productos_id_producto );

CREATE TABLE pedido_proveedor (
    proveedor_id_proveedor   NUMBER(2) NOT NULL,
    id_pedido                NUMBER(10) NOT NULL,
    fecha_pedido             DATE NOT NULL,
    fecha_entrega            DATE NOT NULL
);

ALTER TABLE pedido_proveedor ADD CONSTRAINT pedido_proveedor_pk PRIMARY KEY ( id_pedido );

CREATE TABLE plato (
    id_plato           NUMBER(4) NOT NULL,
    receta_id_receta   NUMBER(4) NOT NULL,
    nombre_plato       NVARCHAR2(50) NOT NULL,
    img_plato          BLOB NOT NULL,
    precio_plato       NUMBER(6) NOT NULL
);

CREATE UNIQUE INDEX plato__idx ON
    plato (
        receta_id_receta
    ASC );

ALTER TABLE plato ADD CONSTRAINT plato_pk PRIMARY KEY ( id_plato );

CREATE TABLE platos_orden (
    plato_id_plato   NUMBER(4) NOT NULL,
    orden_id_orden   NUMBER(10) NOT NULL,
    cantidad_plato   NUMBER(2) NOT NULL
);

ALTER TABLE platos_orden ADD CONSTRAINT platos_orden_pk PRIMARY KEY ( plato_id_plato,
                                                                      orden_id_orden );

CREATE TABLE productos (
    id_producto                      NUMBER(20) NOT NULL,
    nom_producto                     VARCHAR2(50) NOT NULL,
    proveedor_id_proveedor           NUMBER(2) NOT NULL,
    marca_producto_id_marca          NUMBER(5) NOT NULL,
    stock                            NUMBER(3) NOT NULL,
    formato_stock_id_formato_stock   NUMBER(2) NOT NULL,
    medida_stock                     NUMBER(5,2) NOT NULL,
    unidad_medida_id_unidad          NUMBER(1) NOT NULL
);

ALTER TABLE productos ADD CONSTRAINT productos_pk PRIMARY KEY ( id_producto );

CREATE TABLE productos_receta (
    productos_id_producto   NUMBER(20) NOT NULL,
    receta_id_receta        NUMBER(4) NOT NULL,
    cantidad                NUMBER(3,2) NOT NULL
);

ALTER TABLE productos_receta ADD CONSTRAINT productos_receta_pk PRIMARY KEY ( productos_id_producto,
                                                                              receta_id_receta );

CREATE TABLE proveedor (
    id_proveedor       NUMBER(2) NOT NULL,
    nombre_proveedor   NVARCHAR2(100) NOT NULL
);

ALTER TABLE proveedor ADD CONSTRAINT proveedor_pk PRIMARY KEY ( id_proveedor );

CREATE TABLE receta (
    plato_id_plato   NUMBER(4) NOT NULL,
    id_receta        NUMBER(4) NOT NULL,
    instrucciones    VARCHAR2(3000) NOT NULL
);

CREATE UNIQUE INDEX receta__idx ON
    receta (
        plato_id_plato
    ASC );

ALTER TABLE receta ADD CONSTRAINT receta_pk PRIMARY KEY ( id_receta );

CREATE TABLE reserva (
    id_reserva                      NUMBER(10) NOT NULL,
    estado_reserva_id_est_reserva   NUMBER(1) NOT NULL,
    rut_reserva                     NVARCHAR2(12) NOT NULL,
    fecha_reserva                   TIMESTAMP NOT NULL,
    email                           VARCHAR2(50),
    telefono_reserva                VARCHAR2(12) NOT NULL,
    cantidad_personas_reserva       NUMBER(2) NOT NULL,
    mesas_id_mesa                   NUMBER(3) NOT NULL
);

ALTER TABLE reserva ADD CONSTRAINT reserva_pk PRIMARY KEY ( id_reserva );

CREATE TABLE unidad_medida (
    id_unidad     NUMBER(1) NOT NULL,
    desc_unidad   NVARCHAR2(15) NOT NULL
);

ALTER TABLE unidad_medida ADD CONSTRAINT unidad_medida_pk PRIMARY KEY ( id_unidad );

CREATE TABLE utilidad_diarias 
    
    -- No Columns 
;

CREATE TABLE utilidad_mensual 
    
    -- No Columns 
;

ALTER TABLE boleta
    ADD CONSTRAINT boleta_mesas_fk FOREIGN KEY ( mesas_id_mesa )
        REFERENCES mesas ( id_mesa );

ALTER TABLE mesas
    ADD CONSTRAINT mesas_estado_mesa_fk FOREIGN KEY ( estado_mesa_id_est_mesa )
        REFERENCES estado_mesa ( id_est_mesa );

ALTER TABLE orden
    ADD CONSTRAINT orden_boleta_fk FOREIGN KEY ( boleta_id_boleta )
        REFERENCES boleta ( id_boleta );

ALTER TABLE orden
    ADD CONSTRAINT orden_estado_orden_fk FOREIGN KEY ( estado_orden_id_est_ord )
        REFERENCES estado_orden ( id_est_ord );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE pedido_producto
    ADD CONSTRAINT pedido_producto_pedido_proveedor_fk FOREIGN KEY ( pedido_proveedor_id_pedido )
        REFERENCES pedido_proveedor ( id_pedido );

ALTER TABLE pedido_producto
    ADD CONSTRAINT pedido_producto_productos_fk FOREIGN KEY ( productos_id_producto )
        REFERENCES productos ( id_producto );

ALTER TABLE pedido_proveedor
    ADD CONSTRAINT pedido_proveedor_proveedor_fk FOREIGN KEY ( proveedor_id_proveedor )
        REFERENCES proveedor ( id_proveedor );

ALTER TABLE platos_orden
    ADD CONSTRAINT platos_orden_orden_fk FOREIGN KEY ( orden_id_orden )
        REFERENCES orden ( id_orden );

ALTER TABLE platos_orden
    ADD CONSTRAINT platos_orden_plato_fk FOREIGN KEY ( plato_id_plato )
        REFERENCES plato ( id_plato );

ALTER TABLE productos
    ADD CONSTRAINT productos_formato_stock_fk FOREIGN KEY ( formato_stock_id_formato_stock )
        REFERENCES formato_stock ( id_formato_stock );

ALTER TABLE productos
    ADD CONSTRAINT productos_marca_producto_fk FOREIGN KEY ( marca_producto_id_marca )
        REFERENCES marca_producto ( id_marca );

ALTER TABLE productos
    ADD CONSTRAINT productos_proveedor_fk FOREIGN KEY ( proveedor_id_proveedor )
        REFERENCES proveedor ( id_proveedor );

ALTER TABLE productos_receta
    ADD CONSTRAINT productos_receta_productos_fk FOREIGN KEY ( productos_id_producto )
        REFERENCES productos ( id_producto );

ALTER TABLE productos_receta
    ADD CONSTRAINT productos_receta_receta_fk FOREIGN KEY ( receta_id_receta )
        REFERENCES receta ( id_receta );

ALTER TABLE productos
    ADD CONSTRAINT productos_unidad_medida_fk FOREIGN KEY ( unidad_medida_id_unidad )
        REFERENCES unidad_medida ( id_unidad );

ALTER TABLE reserva
    ADD CONSTRAINT reserva_estado_reserva_fk FOREIGN KEY ( estado_reserva_id_est_reserva )
        REFERENCES estado_reserva ( id_est_reserva );

ALTER TABLE reserva
    ADD CONSTRAINT reserva_mesas_fk FOREIGN KEY ( mesas_id_mesa )
        REFERENCES mesas ( id_mesa );

COMMIT;

--------------------------
-- Procedimientos Mesas --
--------------------------

CREATE OR REPLACE PROCEDURE SP_CREATE_MESAS
(
    v_id_mesa in NUMBER,
    v_capacidad in NUMBER, 
    v_estado_mesa in NUMBER,
    v_salida out NUMBER
)
AS
BEGIN
  INSERT INTO MESAS VALUES(v_id_mesa,v_capacidad,v_estado_mesa);
  v_salida:=1;
  

EXCEPTION WHEN OTHERS THEN

    v_salida:=0;

END;
/

CREATE OR REPLACE PROCEDURE SP_DELETE_MESAS(
    v_ID_Mesa in number,
    v_salida out number)
IS
BEGIN
    DELETE FROM MESAS
    WHERE ID_MESA = v_ID_Mesa;
    if sql%rowcount > 0 then
    v_salida:=1;
    end if;
    commit;
    EXCEPTION
    WHEN OTHERS THEN
    v_salida:=0;
END;
/

CREATE OR REPLACE PROCEDURE SP_R_ESTADO_MESA(estado out SYS_REFCURSOR)
IS 
BEGIN
    open estado for select*from estado_mesa;
END;
/

CREATE OR REPLACE PROCEDURE SP_READ_MESAS(mesas out SYS_REFCURSOR)
IS
BEGIN
    OPEN mesas for 
    SELECT 
    e.DESC_ESTD_MESA,
    m.id_mesa,
    m.capacidad
    FROM MESAS m
    JOIN estado_mesa e
    ON m.estado_mesa_id_est_mesa = e.id_est_mesa ;
END;
/

CREATE OR REPLACE PROCEDURE SP_UPDATE_MESA(
    v_id_mesa in number,
    v_id_estado number,
    v_salida out number
)
IS 
BEGIN
    UPDATE MESAS SET estado_mesa_id_est_mesa=v_id_estado
    WHERE id_mesa = v_id_mesa;
    commit;
    v_salida:=1;
    EXCEPTION
    WHEN OTHERS THEN
    v_salida:=0;
END;
/

create or replace PROCEDURE SP_UPDATE_MESAS(
    v_ID_Mesa in number,
    v_capacidad in number,
    v_id_estado in number,
    v_salida out number)
IS
BEGIN
    UPDATE MESAS SET capacidad=v_capacidad,estado_mesa_id_est_mesa=v_id_estado
    WHERE id_mesa = v_ID_Mesa;
    commit;
    v_salida:=1;
    EXCEPTION
    WHEN OTHERS THEN
    v_salida:=0;
END;
/

--------------------------
--Procedimientos Reservas-
--------------------------


create or replace PROCEDURE SP_AGREGAR_RESERVA(
    v_ID_Reserva number,
    v_ID_Estado_Mesa number,
    v_Rut_Reserva NVARCHAR2,
    v_Fecha_Reserva date,
    v_email VARCHAR2,
    v_telefono_reserva varchar2,
    v_cantidad_personas_reserva number,
    v_num_mesa number,
    v_salida out number)
IS
BEGIN
    INSERT INTO RESERVA (ID_RESERVA, estado_reserva_id_est_reserva, rut_reserva, fecha_reserva, email, telefono_reserva, cantidad_personas_reserva,mesas_id_mesa)
    VALUES(v_ID_Reserva, v_ID_Estado_Mesa, v_Rut_Reserva, v_Fecha_Reserva, v_email, v_telefono_reserva, v_cantidad_personas_reserva,v_num_mesa);
    commit;
    v_salida:=1;
    EXCEPTION

    WHEN OTHERS THEN
    v_salida:=0;
END;
/

create or replace PROCEDURE SP_BUSCAR_RESERVAS_POR_RUT(
    
    v_Rut_Reserva in NVARCHAR2,
    reservas out SYS_REFCURSOR)
IS
BEGIN
    open reservas for
    SELECT r.id_reserva,
    e.DESC_ESTD_RESERVA,
    r.rut_reserva,
    r.fecha_reserva,
    r.email,
    r.telefono_reserva,
    r.cantidad_personas_reserva,
    r.mesas_id_mesa     
    FROM RESERVA r
    JOIN estado_reserva e
    on r.estado_reserva_id_est_reserva = e.id_est_reserva
    where RUT_RESERVA = v_Rut_Reserva
    order by fecha_reserva desc;
END;


/

create or replace PROCEDURE SP_ELIMINAR_RESERVA(
    v_ID_Reserva in number,
    v_salida out number)
IS
BEGIN
    DELETE FROM RESERVA
    WHERE ID_RESERVA = v_ID_RESERVA;
    if sql%rowcount > 0 then
    v_salida:=1;
    end if;
    commit;
    EXCEPTION

    WHEN OTHERS THEN
    v_salida:=0;
END;
/

create or replace PROCEDURE SP_LISTAR_RESERVAS(reservas out SYS_REFCURSOR)
IS
BEGIN
    open reservas for
    SELECT r.id_reserva,
    e.DESC_ESTD_RESERVA,
    r.rut_reserva,
    r.fecha_reserva,
    r.email,
    r.telefono_reserva,
    r.cantidad_personas_reserva,
    r.mesas_id_mesa     
    FROM RESERVA r
    JOIN estado_reserva e
    on r.estado_reserva_id_est_reserva = e.id_est_reserva
    ORDER BY r.id_reserva;
END;
/

create or replace PROCEDURE SP_MODIFICAR_RESERVA(
    v_ID_Reserva number,
    v_ID_Estado_Mesa number,
    v_Rut_Reserva NVARCHAR2,
    v_Fecha_Reserva date,
    v_email VARCHAR2,
    v_telefono_reserva varchar2,
    v_cantidad_personas_reserva number,
    v_num_mesa number,
    v_salida out number)
IS
BEGIN
    UPDATE RESERVA SET ESTADO_RESERVA_ID_EST_RESERVA = v_ID_Estado_Mesa,
                       RUT_RESERVA = v_Rut_Reserva,
                       FECHA_RESERVA = v_Fecha_Reserva,
                       EMAIL = v_Email,
                       TELEFONO_RESERVA = v_Telefono_Reserva,
                       CANTIDAD_PERSONAS_RESERVA = v_cantidad_personas_reserva,
                       mesas_id_mesa = v_num_mesa
    WHERE id_reserva = v_ID_Reserva;
    commit;
    v_salida:=1;
    EXCEPTION

    WHEN OTHERS THEN
    v_salida:=0;
END;
/

create or replace PROCEDURE SP_R_ESTADO_RESERVA(estado out SYS_REFCURSOR)
IS 
BEGIN
    open estado for select * from estado_reserva;
END;
/

--------------------------
--    Proc. Productos   --
--------------------------

create or replace PROCEDURE SP_AGREGAR_PRODUCTO(
    v_ID_Producto in number,
    v_Nom_Producto in NVARCHAR2,
    v_Proveedor NVARCHAR2,
    v_Marca nvarchar2,
    v_Stock in number,
    v_Formato_Stock_ID_Formato in number,
    v_Medida_Stock in number,
    v_Unidad_Medida in number,
    v_salida out number)
IS
BEGIN
    INSERT INTO productos (id_producto, nom_producto, proveedor_id_proveedor, marca_producto_id_marca, stock, FORMATO_STOCK_ID_FORMATO_STOCK, medida_stock, unidad_medida_id_unidad)
    VALUES(v_ID_Producto, v_Nom_Producto, v_Proveedor, v_Marca, v_Stock, v_Formato_Stock_ID_Formato, v_Medida_Stock, v_Unidad_Medida);
    commit;
    v_salida:=1;
    EXCEPTION

    WHEN OTHERS THEN
    v_salida:=0;
END;
/

create or replace PROCEDURE SP_MODIFICAR_PRODUCTO(
    v_ID_Producto in number,
    v_Nom_Producto in NVARCHAR2,
    v_Proveedor NVARCHAR2,
    v_Marca nvarchar2,
    v_Stock in number,
    v_Formato_Stock in Nvarchar2,
    v_medida_stock in number,
    v_Unidad_Medida in numeric,
    v_salida out number)
IS
BEGIN
    UPDATE PRODUCTOS SET nom_producto = v_Nom_Producto,
                         proveedor_id_proveedor = v_Proveedor,
                         marca_producto_id_marca = v_Marca,
                         stock = v_Stock,
                         FORMATO_STOCK_ID_FORMATO_STOCK = v_Formato_Stock,
                         medida_stock = v_medida_stock,
                         unidad_medida_id_unidad = v_Unidad_Medida
    WHERE id_producto = v_ID_Producto;
    commit;
    v_salida:=1;
    EXCEPTION

    WHEN OTHERS THEN
    v_salida:=0;
END;
/


create or replace PROCEDURE SP_LISTAR_PRODUCTOS(produc out SYS_REFCURSOR)
IS 
BEGIN
    open produc for
    select pd.id_producto,
           pd.nom_producto,
           pv.nombre_proveedor,
           mp.marca,
           pd.stock,
           fs.desc_formato_stock,
           pd.medida_stock,
           ump.desc_unidad
    from productos pd
    join proveedor pv on pd.proveedor_id_proveedor = pv.id_proveedor
    join marca_producto mp on pd.marca_producto_id_marca = mp.id_marca
    join formato_stock fs on pd.FORMATO_STOCK_ID_FORMATO_STOCK = fs.id_formato_stock
    join unidad_medida ump on pd.unidad_medida_id_unidad = ump.id_unidad
    order by pd.nom_producto asc;
END;
/


create or replace PROCEDURE SP_ELIMINAR_PRODUCTO(
    v_ID_PRODUCTO in number,
    v_salida out number)
IS
BEGIN
    DELETE FROM PRODUCTOS
    WHERE ID_PRODUCTO = v_ID_PRODUCTO;
    if sql%rowcount > 0 then
    v_salida:=1;
    end if;
    commit;
    EXCEPTION

    WHEN OTHERS THEN
    v_salida:=0;
END;
/


create or replace PROCEDURE SP_BUSCAR_PRODUCTOS_POR_CODIGO(
    
    v_ID_Producto in number,
    productos out SYS_REFCURSOR)
IS
BEGIN
    open productos for
    select pd.id_producto,
           pd.nom_producto,
           pv.nombre_proveedor,
           mp.marca,
           pd.stock,
           fs.desc_formato_stock,
           pd.medida_stock,
           ump.desc_unidad
    from productos pd
    join proveedor pv on pd.proveedor_id_proveedor = pv.id_proveedor
    join marca_producto mp on pd.marca_producto_id_marca = mp.id_marca
    join formato_stock fs on pd.FORMATO_STOCK_ID_FORMATO_STOCK = fs.id_formato_stock
    join unidad_medida ump on pd.unidad_medida_id_unidad = ump.id_unidad
    WHERE pd.id_producto = V_ID_PRODUCTO
    order by pd.nom_producto asc;
END;
/

create or replace PROCEDURE SP_BUSCAR_PRODUCTOS_POR_MARCA(
    
    v_ID_MARCA in number,
    productos out SYS_REFCURSOR)
IS
BEGIN
    open productos for
    select pd.id_producto,
           pd.nom_producto,
           pv.nombre_proveedor,
           mp.marca,
           pd.stock,
           fs.desc_formato_stock,
           pd.medida_stock,
           ump.desc_unidad
    from productos pd
    join proveedor pv on pd.proveedor_id_proveedor = pv.id_proveedor
    join marca_producto mp on pd.marca_producto_id_marca = mp.id_marca
    join formato_stock fs on pd.FORMATO_STOCK_ID_FORMATO_STOCK = fs.id_formato_stock
    join unidad_medida ump on pd.unidad_medida_id_unidad = ump.id_unidad
    WHERE pd.marca_producto_id_marca = V_ID_MARCA
    order by pd.nom_producto asc;
END;
/

create or replace PROCEDURE SP_BUSCAR_PRODUCTOS_POR_PROVEEDOR(
    
    v_ID_PROVEEDOR in number,
    productos out SYS_REFCURSOR)
IS
BEGIN
    open productos for
    select pd.id_producto,
           pd.nom_producto,
           pv.nombre_proveedor,
           mp.marca,
           pd.stock,
           fs.desc_formato_stock,
           pd.medida_stock,
           ump.desc_unidad
    from productos pd
    join proveedor pv on pd.proveedor_id_proveedor = pv.id_proveedor
    join marca_producto mp on pd.marca_producto_id_marca = mp.id_marca
    join formato_stock fs on pd.FORMATO_STOCK_ID_FORMATO_STOCK = fs.id_formato_stock
    join unidad_medida ump on pd.unidad_medida_id_unidad = ump.id_unidad
    WHERE pd.proveedor_id_proveedor = V_ID_PROVEEDOR
    order by pd.nom_producto asc;
END;
/


create or replace PROCEDURE SP_BUSCAR_PRODUCTOS_POR_STOCK(
    
    v_STOCK in number,
    productos out SYS_REFCURSOR)
IS
BEGIN
    open productos for
    select pd.id_producto,
           pd.nom_producto,
           pv.nombre_proveedor,
           mp.marca,
           pd.stock,
           fs.desc_formato_stock,
           pd.medida_stock,
           ump.desc_unidad
    from productos pd
    join proveedor pv on pd.proveedor_id_proveedor = pv.id_proveedor
    join marca_producto mp on pd.marca_producto_id_marca = mp.id_marca
    join formato_stock fs on pd.FORMATO_STOCK_ID_FORMATO_STOCK = fs.id_formato_stock
    join unidad_medida ump on pd.unidad_medida_id_unidad = ump.id_unidad
    WHERE pd.stock = V_STOCK
    order by pd.nom_producto asc;
END;
/


create or replace PROCEDURE SP_LISTAR_FORMATO_STOCK(formstock out SYS_REFCURSOR)
IS 
BEGIN
    open formstock for select * from formato_stock order by id_formato_stock;
END;
/

create or replace PROCEDURE SP_LISTAR_MARCAS(marcas out SYS_REFCURSOR)
IS 
BEGIN
    open marcas for select * from marca_producto order by marca asc;
END;
/


create or replace PROCEDURE SP_LISTAR_MEDIDAS(uni_medidas out SYS_REFCURSOR)
IS 
BEGIN
    open uni_medidas for select * from unidad_medida;
END;
/

create or replace PROCEDURE SP_LISTAR_PROVEEDORES(proveedores out SYS_REFCURSOR)
IS 
BEGIN
    open proveedores for select * from proveedor order by nombre_proveedor;
END;
/

COMMIT;

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

commit;
