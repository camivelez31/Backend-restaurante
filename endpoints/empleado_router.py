from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import get_db
from entities.empleado import Empleado
from schemas.empleado_schema import EmpleadoCreate, EmpleadoResponse, EmpleadoUpdate

router = APIRouter(prefix="/empleados", tags=["Empleados"])


@router.get("/", response_model=List[EmpleadoResponse])
def listar_empleados(db: Session = Depends(get_db)):
  
    return db.query(Empleado).all()


@router.get("/{empleado_id}", response_model=EmpleadoResponse)
def obtener_empleado(empleado_id: int, db: Session = Depends(get_db)):
    
    empleado = db.query(Empleado).filter(Empleado.id == empleado_id).first()

    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")

    return empleado


@router.post("/", response_model=EmpleadoResponse, status_code=201)
def crear_empleado(empleado: EmpleadoCreate, db: Session = Depends(get_db)):
   
    nuevo_empleado = Empleado(
        nombre=empleado.nombre,
        cargo=empleado.cargo,
        telefono=empleado.telefono
    )

    db.add(nuevo_empleado)
    db.commit()
    db.refresh(nuevo_empleado)

    return nuevo_empleado


@router.put("/{empleado_id}", response_model=EmpleadoResponse)
def actualizar_empleado(
    empleado_id: int,
    datos_actualizados: EmpleadoUpdate,
    db: Session = Depends(get_db)
):
    
    empleado = db.query(Empleado).filter(Empleado.id == empleado_id).first()

    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")

    for campo, valor in datos_actualizados.model_dump(exclude_unset=True).items():
        setattr(empleado, campo, valor)

    db.commit()
    db.refresh(empleado)

    return empleado


@router.delete("/{empleado_id}")
def eliminar_empleado(empleado_id: int, db: Session = Depends(get_db)):
 
    empleado = db.query(Empleado).filter(Empleado.id == empleado_id).first()

    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")

    db.delete(empleado)
    db.commit()

    return {"message": "Empleado eliminado correctamente"}