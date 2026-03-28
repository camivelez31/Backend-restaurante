from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import get_db
from entities.pago import Pago
from schemas.pago_schema import PagoCreate, PagoResponse, PagoUpdate

router = APIRouter(prefix="/pagos", tags=["Pagos"])


@router.get("/", response_model=List[PagoResponse])
def listar_pagos(db: Session = Depends(get_db)):
  
    return db.query(Pago).all()


@router.get("/{pago_id}", response_model=PagoResponse)
def obtener_pago(pago_id: int, db: Session = Depends(get_db)):
    
    pago = db.query(Pago).filter(Pago.id == pago_id).first()

    if not pago:
        raise HTTPException(status_code=404, detail="Pago no encontrado")

    return pago


@router.post("/", response_model=PagoResponse, status_code=201)
def crear_pago(pago: PagoCreate, db: Session = Depends(get_db)):
    
    nuevo_pago = Pago(
        metodo_pago=pago.metodo_pago,
        total=pago.total,
        pedido_id=pago.pedido_id
    )

    db.add(nuevo_pago)
    db.commit()
    db.refresh(nuevo_pago)

    return nuevo_pago


@router.put("/{pago_id}", response_model=PagoResponse)
def actualizar_pago(pago_id: int, datos_actualizados: PagoUpdate, db: Session = Depends(get_db)):
    
    pago = db.query(Pago).filter(Pago.id == pago_id).first()

    if not pago:
        raise HTTPException(status_code=404, detail="Pago no encontrado")

    for campo, valor in datos_actualizados.model_dump(exclude_unset=True).items():
        setattr(pago, campo, valor)

    db.commit()
    db.refresh(pago)

    return pago


@router.delete("/{pago_id}")
def eliminar_pago(pago_id: int, db: Session = Depends(get_db)):
    
    pago = db.query(Pago).filter(Pago.id == pago_id).first()

    if not pago:
        raise HTTPException(status_code=404, detail="Pago no encontrado")

    db.delete(pago)
    db.commit()

    return {"message": "Pago eliminado correctamente"}