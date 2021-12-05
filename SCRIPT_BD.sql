DROP TABLE boleta CASCADE CONSTRAINTS;

DROP TABLE estado_mesa CASCADE CONSTRAINTS;

DROP TABLE estado_orden CASCADE CONSTRAINTS;

DROP TABLE estado_reserva CASCADE CONSTRAINTS;

DROP TABLE formato_stock CASCADE CONSTRAINTS;

DROP TABLE informe_rendimiento CASCADE CONSTRAINTS;

DROP TABLE insumo CASCADE CONSTRAINTS;

DROP TABLE marca_producto CASCADE CONSTRAINTS;

DROP TABLE mesas CASCADE CONSTRAINTS;

DROP TABLE orden CASCADE CONSTRAINTS;

DROP TABLE pedido_insumo CASCADE CONSTRAINTS;

DROP TABLE pedido_producto CASCADE CONSTRAINTS;

DROP TABLE pedido_proveedor CASCADE CONSTRAINTS;

DROP TABLE plato CASCADE CONSTRAINTS;

DROP TABLE platos_orden CASCADE CONSTRAINTS;

DROP TABLE producto_receta CASCADE CONSTRAINTS;

DROP TABLE productos CASCADE CONSTRAINTS;

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

CREATE TABLE insumo (
    id_insumo                        NUMBER(20) NOT NULL,
    nom_insumo                       VARCHAR2(50) NOT NULL,
    stock                            NUMBER NOT NULL,
    proveedor_id_proveedor           NUMBER(2) NOT NULL,
    formato_stock_id_formato_stock   NUMBER(2) NOT NULL
);

ALTER TABLE insumo ADD CONSTRAINT insumo_pk PRIMARY KEY ( id_insumo );

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

CREATE TABLE pedido_insumo (
    pedido_proveedor_id_pedido   NUMBER(10) NOT NULL,
    insumo_id_insumo             NUMBER(20) NOT NULL
);

ALTER TABLE pedido_insumo ADD CONSTRAINT pedido_insumo_pk PRIMARY KEY ( pedido_proveedor_id_pedido,
                                                                        insumo_id_insumo );

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
    id_plato       NUMBER(4) NOT NULL,
    nombre_plato   NVARCHAR2(50) NOT NULL,
    descripcion    VARCHAR2(300) NOT NULL,
    precio_plato   NUMBER(6) NOT NULL,
    id_receta      NUMBER(4) NOT NULL
);

ALTER TABLE plato ADD CONSTRAINT plato_pk PRIMARY KEY ( id_plato );

CREATE TABLE platos_orden (
    plato_id_plato   NUMBER(4) NOT NULL,
    orden_id_orden   NUMBER(10) NOT NULL,
    cantidad_plato   NUMBER(2) NOT NULL
);

ALTER TABLE platos_orden ADD CONSTRAINT platos_orden_pk PRIMARY KEY ( plato_id_plato,
                                                                      orden_id_orden );

CREATE TABLE producto_receta (
    cantidad                  NUMBER NOT NULL,
    receta_id_receta          NUMBER(4) NOT NULL,
    productos_id_producto     NUMBER(20) NOT NULL,
    unidad_medida_id_unidad   NUMBER(1) NOT NULL
);

CREATE TABLE productos (
    id_producto                      NUMBER(20) NOT NULL,
    nom_producto                     VARCHAR2(50) NOT NULL,
    proveedor_id_proveedor           NUMBER(2) NOT NULL,
    marca_producto_id_marca          NUMBER(5) NOT NULL,
    stock                            NUMBER NOT NULL,
    formato_stock_id_formato_stock   NUMBER(2) NOT NULL,
    medida_stock                     NUMBER NOT NULL,
    unidad_medida_id_unidad          NUMBER(1) NOT NULL
);

ALTER TABLE productos ADD CONSTRAINT productos_pk PRIMARY KEY ( id_producto );

CREATE TABLE proveedor (
    id_proveedor       NUMBER(2) NOT NULL,
    nombre_proveedor   NVARCHAR2(100) NOT NULL
);

ALTER TABLE proveedor ADD CONSTRAINT proveedor_pk PRIMARY KEY ( id_proveedor );

CREATE TABLE receta (
    id_receta       NUMBER(4) NOT NULL,
    instrucciones   VARCHAR2(3000) NOT NULL,
    id_plato        NUMBER(4) NOT NULL
);

ALTER TABLE receta ADD CONSTRAINT receta_pk PRIMARY KEY ( id_receta );

CREATE TABLE reserva (
    id_reserva                      NUMBER(10) NOT NULL,
    estado_reserva_id_est_reserva   NUMBER(1) NOT NULL,
    rut_reserva                     NVARCHAR2(12) NOT NULL,
    fecha_reserva                   DATE NOT NULL,
    email                           VARCHAR2(50),
    telefono_reserva                VARCHAR2(12),
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

ALTER TABLE insumo
    ADD CONSTRAINT insumo_formato_stock_fk FOREIGN KEY ( formato_stock_id_formato_stock )
        REFERENCES formato_stock ( id_formato_stock );

ALTER TABLE insumo
    ADD CONSTRAINT insumo_proveedor_fk FOREIGN KEY ( proveedor_id_proveedor )
        REFERENCES proveedor ( id_proveedor );

ALTER TABLE mesas
    ADD CONSTRAINT mesas_estado_mesa_fk FOREIGN KEY ( estado_mesa_id_est_mesa )
        REFERENCES estado_mesa ( id_est_mesa );

ALTER TABLE orden
    ADD CONSTRAINT orden_boleta_fk FOREIGN KEY ( boleta_id_boleta )
        REFERENCES boleta ( id_boleta );

ALTER TABLE orden
    ADD CONSTRAINT orden_estado_orden_fk FOREIGN KEY ( estado_orden_id_est_ord )
        REFERENCES estado_orden ( id_est_ord );

ALTER TABLE pedido_insumo
    ADD CONSTRAINT pedido_insumo_insumo_fk FOREIGN KEY ( insumo_id_insumo )
        REFERENCES insumo ( id_insumo );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE pedido_insumo
    ADD CONSTRAINT pedido_insumo_pedido_proveedor_fk FOREIGN KEY ( pedido_proveedor_id_pedido )
        REFERENCES pedido_proveedor ( id_pedido );

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

ALTER TABLE producto_receta
    ADD CONSTRAINT producto_receta_productos_fk FOREIGN KEY ( productos_id_producto )
        REFERENCES productos ( id_producto );

ALTER TABLE producto_receta
    ADD CONSTRAINT producto_receta_receta_fk FOREIGN KEY ( receta_id_receta )
        REFERENCES receta ( id_receta );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE producto_receta
    ADD CONSTRAINT producto_receta_unidad_medida_fk FOREIGN KEY ( unidad_medida_id_unidad )
        REFERENCES unidad_medida ( id_unidad );

ALTER TABLE productos
    ADD CONSTRAINT productos_formato_stock_fk FOREIGN KEY ( formato_stock_id_formato_stock )
        REFERENCES formato_stock ( id_formato_stock );

ALTER TABLE productos
    ADD CONSTRAINT productos_marca_producto_fk FOREIGN KEY ( marca_producto_id_marca )
        REFERENCES marca_producto ( id_marca ) on delete cascade;

ALTER TABLE productos
    ADD CONSTRAINT productos_proveedor_fk FOREIGN KEY ( proveedor_id_proveedor )
        REFERENCES proveedor ( id_proveedor ) on delete cascade;

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
