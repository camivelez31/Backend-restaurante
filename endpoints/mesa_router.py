from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import get_db
from entities.mesa import Mesa
from schemas.mesa_schema import MesaCreate, MesaResponse, MesaUpdate

router = APIRouter(prefix="/mesas", tags=["Mesas"])


@router.get("/", response_model=List[MesaResponse])
def listar_mesas(db: Session = Depends(get_db)):
  
    return db.query(Mesa).all()


@router.get("/{mesa_id}", response_model=MesaResponse)
def obtener_mesa(mesa_id: int, db: Session = Depends(get_db)):
    
    mesa = db.query(Mesa).filter(Mesa.id == mesa_id).first()

    if not mesa:
        raise HTTPException(status_code=404, detail="Mesa no encontrada")

    return mesa


@router.post("/", response_model=MesaResponse, status_code=201)
def crear_mesa(mesa: MesaCreate, db: Session = Depends(get_db)):
   
    nueva_mesa = Mesa(
        numero_mesa=mesa.numero_mesa,
        capacidad=mesa.capacidad,
        estado=mesa.estado
    )

    db.add(nueva_mesa)
    db.commit()
    db.refresh(nueva_mesa)

    return nueva_mesa


@router.put("/{mesa_id}", response_model=MesaResponse)
def actualizar_mesa(mesa_id: int, datos_actualizados: MesaUpdate, db: Session = Depends(get_db)):
    
    mesa = db.query(Mesa).filter(Mesa.id == mesa_id).first()

    if not mesa:
        raise HTTPException(status_code=404, detail="Mesa no encontrada")

    for campo, valor in datos_actualizados.model_dump(exclude_unset=True).items():
        setattr(mesa, campo, valor)

    db.commit()
    db.refresh(mesa)

    return mesa


@router.delete("/{mesa_id}")
def eliminar_mesa(mesa_id: int, db: Session = Depends(get_db)):
   
    mesa = db.query(Mesa).filter(Mesa.id == mesa_id).first()

    if not mesa:
        raise HTTPException(status_code=404, detail="Mesa no encontrada")

    db.delete(mesa)
    db.commit()

    return {"message": "Mesa eliminada correctamente"}