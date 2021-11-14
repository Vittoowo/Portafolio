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
    m.capacidad,
    m.ESTADO_MESA_ID_EST_MESA
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
    v_ID_PRODUCTO in number,
    v_NOM_PRODUCTO in NVARCHAR2,
    v_PROVEEDOR_ID_PROVEEDOR NVARCHAR2,
    v_STOCK in number,
    v_MARCA_PRODUCTO_ID_MARCA nvarchar2,
    v_UNIDAD_MEDIDA_ID_UNIDAD in number,
    v_FORMATO_STOCK_ID_FORMATO in number,
    v_MEDIDA in number,
    v_salida out number) 
IS
BEGIN

    INSERT INTO productos 
    VALUES(v_ID_PRODUCTO,v_NOM_PRODUCTO,v_PROVEEDOR_ID_PROVEEDOR,v_STOCK,v_MARCA_PRODUCTO_ID_MARCA,v_UNIDAD_MEDIDA_ID_UNIDAD,v_FORMATO_STOCK_ID_FORMATO,v_MEDIDA);
    commit;
    v_salida:=1;
    EXCEPTION

    WHEN OTHERS THEN
    v_salida:=0;
END;


/

create or replace PROCEDURE SP_MODIFICAR_PRODUCTO(
    v_ID_PRODUCTO in number,
    v_NOM_PRODUCTO in NVARCHAR2,
    v_PROVEEDOR_ID_PROVEEDOR NVARCHAR2,
    v_STOCK in number,
    v_MARCA_PRODUCTO_ID_MARCA nvarchar2,
    v_UNIDAD_MEDIDA_ID_UNIDAD in number,
    v_FORMATO_STOCK_ID_FORMATO in number,
    v_MEDIDA in number,
    v_salida out number) 
IS
BEGIN
    UPDATE PRODUCTOS SET nom_producto = v_Nom_Producto,
                         proveedor_id_proveedor = v_PROVEEDOR_ID_PROVEEDOR,
                         marca_producto_id_marca = v_MARCA_PRODUCTO_ID_MARCA,
                         stock = v_Stock,
                         FORMATO_STOCK_ID_FORMATO_STOCK = v_FORMATO_STOCK_ID_FORMATO,
                         medida_stock =  v_MEDIDA,
                         unidad_medida_id_unidad = v_UNIDAD_MEDIDA_ID_UNIDAD
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
