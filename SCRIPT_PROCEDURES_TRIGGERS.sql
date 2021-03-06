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
    ON m.estado_mesa_id_est_mesa = e.id_est_mesa 
    ORDER BY M.ID_MESA ASC;
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


DROP SEQUENCE reservas_seq;
CREATE SEQUENCE reservas_seq
 START WITH     1
 INCREMENT BY   1;
 
/

CREATE OR REPLACE TRIGGER trigger_reserva_id
BEFORE INSERT ON reserva 
FOR EACH ROW

BEGIN
  SELECT reservas_seq.NEXTVAL
  INTO   :new.id_reserva
  FROM   dual;
  
  SELECT id_est_reserva INTO :NEW.estado_reserva_id_est_reserva FROM estado_reserva WHERE id_est_reserva = 1;
END;
/

create or replace PROCEDURE SP_AGREGAR_RESERVA_TOTEM(
    v_Estado_Reserva number,
    v_Rut_Reserva VARCHAR2,
    v_fecha_hora VARCHAR2,
    v_cantidad_personas_reserva number,
    v_num_mesa number,
    v_salida out NUMBER)
AS
v_verificar NUMBER;

BEGIN

    SELECT COUNT(*) INTO v_verificar FROM RESERVA WHERE fecha_reserva = v_fecha_hora  AND mesas_id_mesa = v_num_mesa;

    IF v_verificar=0 then

    INSERT INTO RESERVA ( estado_reserva_id_est_reserva, rut_reserva, fecha_reserva, cantidad_personas_reserva,mesas_id_mesa)
    VALUES(v_Estado_Reserva, v_Rut_Reserva,TO_DATE(v_fecha_hora,'DD-MM-YYYY HH24:MI'), v_cantidad_personas_reserva,v_num_mesa);
    commit;
    v_salida:=1;
    ELSE 
    v_salida:=0;
    END IF;
    EXCEPTION

    WHEN OTHERS THEN
     DBMS_OUTPUT.PUT_LINE('Error'||SQLCODE||SQLERRM);
    v_salida:=0;
    commit;
END;
/
create or replace PROCEDURE SP_AGREGAR_RESERVA(
    v_Rut_Reserva VARCHAR2,
    v_fecha_hora VARCHAR2,
    v_email VARCHAR2,
    v_telefono_reserva varchar2,
    v_cantidad_personas_reserva number,
    v_num_mesa number,
    v_salida out NUMBER)
AS
v_verificar NUMBER;

BEGIN

    SELECT COUNT(*) INTO v_verificar FROM RESERVA WHERE fecha_reserva = v_fecha_hora  AND mesas_id_mesa = v_num_mesa;

    IF v_verificar=0 then

    INSERT INTO RESERVA ( rut_reserva, fecha_reserva, email, telefono_reserva, cantidad_personas_reserva,mesas_id_mesa)
    VALUES( v_Rut_Reserva,TO_DATE(v_fecha_hora,'DD-MM-YYYY HH24:MI'), v_email, v_telefono_reserva, v_cantidad_personas_reserva,v_num_mesa);
    commit;
    v_salida:=1;
    ELSE 
    v_salida:=0;
    END IF;
    EXCEPTION

    WHEN OTHERS THEN
     DBMS_OUTPUT.PUT_LINE('Error'||SQLCODE||SQLERRM);
    v_salida:=0;
END;
/

create or replace PROCEDURE SP_MODIFICAR_RESERVA(
    v_ID_Reserva NUMBER,
    v_ID_Estado_Reserva NUMBER,
    v_Rut_Reserva VARCHAR2,
    v_Fecha_Reserva VARCHAR2,
    v_email VARCHAR2,
    v_telefono_reserva VARCHAR2,
    v_cantidad_personas_reserva NUMBER,
    v_num_mesa NUMBER,
    v_salida OUT NUMBER)
IS
v_verificar NUMBER;
BEGIN
   
    SELECT COUNT(*) INTO v_verificar FROM RESERVA WHERE  v_ID_Reserva = ID_Reserva;

    IF v_verificar=1 THEN
        UPDATE RESERVA SET ESTADO_RESERVA_ID_EST_RESERVA = v_ID_Estado_Reserva,
                           RUT_RESERVA = v_Rut_Reserva,
                           Fecha_Reserva = TO_DATE(v_Fecha_Reserva,'DD-MM-YYYY HH24:MI'),
                           EMAIL = v_Email,
                           TELEFONO_RESERVA = v_Telefono_Reserva,
                           CANTIDAD_PERSONAS_RESERVA = v_cantidad_personas_reserva,
                           mesas_id_mesa = v_num_mesa
        WHERE id_reserva = v_ID_Reserva;
    COMMIT;
        v_salida:=1;
    
    ELSE
        v_salida:=0;
    END IF;
    
    EXCEPTION

    WHEN OTHERS THEN
    v_salida:=0;
END;
/

create or replace PROCEDURE SP_BUSCAR_RESERVAS_POR_ID(
    
    v_id_Reserva in NVARCHAR2,
    reservas out SYS_REFCURSOR)
IS
BEGIN
    open reservas for
    SELECT r.id_reserva,
    r.mesas_id_mesa,
    trim(SUBSTR(r.RUT_RESERVA,0,INSTR(r.RUT_RESERVA,' ',1,1))) as RUT ,trim(SUBSTR(r.RUT_RESERVA,INSTR(r.RUT_RESERVA,' ',1,2),3)) as DV,
    to_char(r.FECHA_RESERVA,'YYYY-MM-DD') AS Fecha,
    to_char(r.FECHA_RESERVA,'HH24:MI') as Hora,
    e.DESC_ESTD_RESERVA,
    r.email,
    r.telefono_reserva,
    r.cantidad_personas_reserva    
    FROM RESERVA r
    JOIN estado_reserva e
    on r.estado_reserva_id_est_reserva = e.id_est_reserva
    where id_reserva = v_id_Reserva
    ORDER BY r.id_reserva;
    
END;
/

create or replace PROCEDURE SP_BUSCAR_RESERVAS_POR_RUT(
    
    v_Rut_Reserva in VARCHAR2,
    reservas out SYS_REFCURSOR)
IS
BEGIN
    open reservas for
    SELECT r.id_reserva,
    r.mesas_id_mesa,
    r.RUT_RESERVA,
    to_char(r.FECHA_RESERVA,'DD-MM-YYYY') AS Fecha,
    to_char(r.FECHA_RESERVA,'HH24:MI') as Hora,
    e.DESC_ESTD_RESERVA,
    r.email,
    r.telefono_reserva,
    r.cantidad_personas_reserva    
    FROM RESERVA r
    JOIN estado_reserva e
    on r.estado_reserva_id_est_reserva = e.id_est_reserva
    where RUT_RESERVA = v_Rut_Reserva
    order by r.FECHA_RESERVA desc;

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
    r.mesas_id_mesa,
    r.rut_reserva,
    to_char(r.FECHA_RESERVA,'DD-MM-YYYY') AS Fecha,
    to_char(r.FECHA_RESERVA,'HH24:MI') as Hora,
    e.DESC_ESTD_RESERVA,
    r.email,
    r.telefono_reserva,
    r.cantidad_personas_reserva    
    FROM RESERVA r
    JOIN estado_reserva e
    on r.estado_reserva_id_est_reserva = e.id_est_reserva
    ORDER BY r.id_reserva;
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
    v_ID_PRODUCTO in NUMBER,
    v_NOM_PRODUCTO in VARCHAR2,
    v_PROVEEDOR_ID_PROVEEDOR NUMBER,
    v_MARCA_PRODUCTO_ID_MARCA NUMBER,
    v_STOCK in NUMBER,
    v_FORMATO_STOCK_ID_FORMATO in NUMBER,
    v_MEDIDA in NUMBER,
    v_UNIDAD_MEDIDA_ID_UNIDAD in NUMBER,
    v_salida out NUMBER) 
IS
BEGIN

    INSERT INTO productos(
                            ID_PRODUCTO,
                            NOM_PRODUCTO,
                            PROVEEDOR_ID_PROVEEDOR,
                            MARCA_PRODUCTO_ID_MARCA,
                            STOCK,
                            FORMATO_STOCK_ID_FORMATO_STOCK,
                            MEDIDA_STOCK,
                            UNIDAD_MEDIDA_ID_UNIDAD)
    VALUES(
                            v_ID_PRODUCTO,
                            v_NOM_PRODUCTO,
                            v_PROVEEDOR_ID_PROVEEDOR,
                            v_MARCA_PRODUCTO_ID_MARCA,
                            v_STOCK,
                            v_FORMATO_STOCK_ID_FORMATO,
                            v_MEDIDA,
                            v_UNIDAD_MEDIDA_ID_UNIDAD
    );
    commit;
    v_salida:=1;
    EXCEPTION

    WHEN OTHERS THEN
    v_salida:=0;
END;


/

create or replace PROCEDURE SP_MODIFICAR_PRODUCTO(
    v_ID_PRODUCTO in NUMBER,
    v_NOM_PRODUCTO in VARCHAR2,
    v_PROVEEDOR_ID_PROVEEDOR NUMBER,
    v_MARCA_PRODUCTO_ID_MARCA NUMBER,
    v_STOCK in NUMBER,
    v_FORMATO_STOCK_ID_FORMATO_STOCK in NUMBER,
    v_MEDIDA_STOCK in NUMBER,
    v_UNIDAD_MEDIDA_ID_UNIDAD in NUMBER,
    v_salida out NUMBER)  
IS
BEGIN
    UPDATE PRODUCTOS SET    ID_PRODUCTO=v_ID_PRODUCTO,
                            NOM_PRODUCTO=v_NOM_PRODUCTO,
                            PROVEEDOR_ID_PROVEEDOR=v_PROVEEDOR_ID_PROVEEDOR,
                            MARCA_PRODUCTO_ID_MARCA=v_MARCA_PRODUCTO_ID_MARCA,
                            STOCK=v_STOCK,
                            FORMATO_STOCK_ID_FORMATO_STOCK=v_FORMATO_STOCK_ID_FORMATO_STOCK,
                            MEDIDA_STOCK=v_MEDIDA_STOCK,
                            UNIDAD_MEDIDA_ID_UNIDAD=v_UNIDAD_MEDIDA_ID_UNIDAD
    
    
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

------------------------------------------
--------Procedimientos Insumos------------
------------------------------------------
create or replace PROCEDURE SP_AGREGAR_INSUMO(
    v_ID_INSUMO in number,
    v_NOM_INSUMO in NVARCHAR2,
    v_STOCK in number,
    v_PROVEEDOR_ID_PROVEEDOR NVARCHAR2,
    v_FORMATO_STOCK_ID_FORMATO in number,
    v_salida out number) 
IS
BEGIN

    INSERT INTO INSUMO 
    VALUES(v_ID_INSUMO, v_NOM_INSUMO, v_STOCK, v_PROVEEDOR_ID_PROVEEDOR, v_FORMATO_STOCK_ID_FORMATO);
    commit;
    v_salida:=1;
    EXCEPTION

    WHEN OTHERS THEN
    v_salida:=0;
END;

/
create or replace PROCEDURE SP_ELIMINAR_INSUMO(
    v_ID_INSUMO in number,
    v_salida out number)
IS
BEGIN
    DELETE FROM INSUMO
    WHERE ID_INSUMO = v_ID_INSUMO;
    if sql%rowcount > 0 then
    v_salida:=1;
    end if;
    commit;
    EXCEPTION

    WHEN OTHERS THEN
    v_salida:=0;
END;

/

create or replace PROCEDURE SP_LISTAR_INSUMOS(insum out SYS_REFCURSOR)
IS 
BEGIN
    open insum for
    select ins.id_insumo,
           ins.nom_insumo,
           ins.stock,
           pv.nombre_proveedor,
           fs.desc_formato_stock
    from insumo ins
    join proveedor pv on ins.proveedor_id_proveedor = pv.id_proveedor
    join formato_stock fs on ins.FORMATO_STOCK_ID_FORMATO_STOCK = fs.id_formato_stock
    order by ins.nom_insumo asc;
END;

/

create or replace PROCEDURE SP_MODIFICAR_INSUMO(
    v_ID_INSUMO in number,
    v_NOM_INSUMO in NVARCHAR2,
    v_STOCK in number,
    v_PROVEEDOR_ID_PROVEEDOR NVARCHAR2,
    v_FORMATO_STOCK_ID_FORMATO in number,
    v_salida out number)  
IS
BEGIN
    UPDATE INSUMO SET nom_insumo = v_Nom_Insumo,
                      proveedor_id_proveedor = v_PROVEEDOR_ID_PROVEEDOR,
                      stock = v_Stock,
                      FORMATO_STOCK_ID_FORMATO_STOCK = v_FORMATO_STOCK_ID_FORMATO
    WHERE id_Insumo = v_ID_Insumo;
    if sql%rowcount > 0 then
    v_salida:=1;
    end if;
    commit;
    
    EXCEPTION

    WHEN OTHERS THEN
    v_salida:=0;
END;

/
create or replace PROCEDURE SP_BUSCAR_INSUMOS_POR_CODIGO(
        
    v_ID_INSUMO in number,
    insum out SYS_REFCURSOR)
IS 
BEGIN
    open insum for
    select ins.id_insumo,
           ins.nom_insumo,
           ins.stock,
           pv.nombre_proveedor,
           fs.desc_formato_stock
    from insumo ins
    join proveedor pv on ins.proveedor_id_proveedor = pv.id_proveedor
    join formato_stock fs on ins.FORMATO_STOCK_ID_FORMATO_STOCK = fs.id_formato_stock
    where ins.id_insumo = v_ID_INSUMO
    order by ins.nom_insumo asc;
END;

/
create or replace PROCEDURE SP_BUSCAR_INSUMOS_POR_PROVEEDOR(
        
    v_ID_PROVEEDOR in number,
    insum out SYS_REFCURSOR)
IS 
BEGIN
    open insum for
    select ins.id_insumo,
           ins.nom_insumo,
           ins.stock,
           pv.nombre_proveedor,
           fs.desc_formato_stock
    from insumo ins
    join proveedor pv on ins.proveedor_id_proveedor = pv.id_proveedor
    join formato_stock fs on ins.FORMATO_STOCK_ID_FORMATO_STOCK = fs.id_formato_stock
    where ins.proveedor_id_proveedor = v_ID_PROVEEDOR
    order by ins.nom_insumo asc;
END;

/

create or replace PROCEDURE SP_BUSCAR_INSUMOS_POR_STOCK(
        
    v_STOCK in number,
    insum out SYS_REFCURSOR)
IS 
BEGIN
    open insum for
    select ins.id_insumo,
           ins.nom_insumo,
           ins.stock,
           pv.nombre_proveedor,
           fs.desc_formato_stock
    from insumo ins
    join proveedor pv on ins.proveedor_id_proveedor = pv.id_proveedor
    join formato_stock fs on ins.FORMATO_STOCK_ID_FORMATO_STOCK = fs.id_formato_stock
    where ins.stock = v_STOCK
    order by ins.nom_insumo asc;
END;
/


--------------------------
-----Proc. Proveedores----
--------------------------


create or replace PROCEDURE SP_AGREGAR_PROVEEDOR(
    v_ID_PROVEEDOR in number,
    v_NOM_PROVEEDOR in NVARCHAR2,
    v_salida out number) 
IS
BEGIN

    INSERT INTO PROVEEDOR
    VALUES(v_ID_PROVEEDOR, v_NOM_PROVEEDOR);
    commit;
    v_salida:=1;
    EXCEPTION

    WHEN OTHERS THEN
    v_salida:=0;
END;

/
create or replace PROCEDURE SP_BUSCAR_PROVEEDOR_POR_NOMBRE(
        
    v_NOMBRE_PROVEEDOR varchar2,
    prove out SYS_REFCURSOR)
IS 
BEGIN
    open prove for
    select *
    from PROVEEDOR
    where UPPER(NOMBRE_PROVEEDOR) = UPPER(v_NOMBRE_PROVEEDOR)
    order by NOMBRE_PROVEEDOR asc;
END;

/

create or replace PROCEDURE SP_MODIFICAR_PROVEEDOR(
    v_ID_PROVEEDOR in number,
    v_NOMBRE_PROVEEDOR in NVARCHAR2,
    v_salida out number)  
IS
BEGIN
    UPDATE PROVEEDOR SET NOMBRE_PROVEEDOR = v_NOMBRE_PROVEEDOR
    WHERE ID_PROVEEDOR = v_ID_PROVEEDOR;
    if sql%rowcount > 0 then
    v_salida:=1;
    end if;
    commit;

    EXCEPTION

    WHEN OTHERS THEN
    v_salida:=0;
END;

/
create or replace PROCEDURE SP_ELIMINAR_PROVEEDOR(
    v_ID_PROVEEDOR in number,
    v_salida out number)
IS
BEGIN
    DELETE FROM PROVEEDOR
    WHERE ID_PROVEEDOR = v_ID_PROVEEDOR;
    if sql%rowcount > 0 then
    v_salida:=1;
    else
    v_salida:=0;
    end if;
    commit;
    EXCEPTION

    WHEN OTHERS THEN
    v_salida:=0;
END;

/


--------------------------
-----PROC MARCAS----------
--------------------------

create or replace PROCEDURE SP_AGREGAR_MARCA(
    v_ID_MARCA in number,
    v_MARCA in NVARCHAR2,
    v_salida out number) 
IS
BEGIN

    INSERT INTO MARCA_PRODUCTO
    VALUES(v_ID_MARCA, v_MARCA);
    commit;
    v_salida:=1;
    EXCEPTION

    WHEN OTHERS THEN
    v_salida:=0;
END;


/


create or replace PROCEDURE SP_BUSCAR_MARCA_POR_NOMBRE(
        
    v_MARCA varchar2,
    mar out SYS_REFCURSOR)
IS 
BEGIN
    open mar for
    select *
    from MARCA_PRODUCTO
    where UPPER(MARCA) = UPPER(v_MARCA);
END;


/

create or replace PROCEDURE SP_MODIFICAR_MARCA(
    v_ID_MARCA in number,
    v_MARCA in NVARCHAR2,
    v_salida out number)  
IS
BEGIN
    UPDATE MARCA_PRODUCTO SET MARCA = v_MARCA
    WHERE ID_MARCA = v_ID_MARCA;
    if sql%rowcount > 0 then
    v_salida:=1;
    end if;
    commit;

    EXCEPTION

    WHEN OTHERS THEN
    v_salida:=0;
END;
/


create or replace PROCEDURE SP_ELIMINAR_MARCA(
    v_ID_MARCA in number,
    v_salida out number)
IS
BEGIN
    DELETE FROM MARCA_PRODUCTO
    WHERE ID_MARCA = v_ID_MARCA;
    if sql%rowcount > 0 then
    v_salida:=1;
    else
    v_salida:=0;
    end if;
    commit;
    EXCEPTION

    WHEN OTHERS THEN
    v_salida:=0;
END;

/

COMMIT;
