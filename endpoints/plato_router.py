from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import get_db
from entities.plato import Plato
from schemas.plato_schema import PlatoCreate, PlatoResponse, PlatoUpdate

router = APIRouter(prefix="/platos", tags=["Platos"])


@router.get("/", response_model=List[PlatoResponse])
def listar_platos(db: Session = Depends(get_db)):
   
    return db.query(Plato).all()


@router.get("/{plato_id}", response_model=PlatoResponse)
def obtener_plato(plato_id: int, db: Session = Depends(get_db)):
   
    plato = db.query(Plato).filter(Plato.id == plato_id).first()

    if not plato:
        raise HTTPException(status_code=404, detail="Plato no encontrado")

    return plato


@router.post("/", response_model=PlatoResponse, status_code=201)
def crear_plato(plato: PlatoCreate, db: Session = Depends(get_db)):
    
    nuevo_plato = Plato(
        nombre=plato.nombre,
        descripcion=plato.descripcion,
        precio=plato.precio,
        disponible=plato.disponible,
        categoria_id=plato.categoria_id
    )

    db.add(nuevo_plato)
    db.commit()
    db.refresh(nuevo_plato)

    return nuevo_plato


@router.put("/{plato_id}", response_model=PlatoResponse)
def actualizar_plato(plato_id: int, datos_actualizados: PlatoUpdate, db: Session = Depends(get_db)):
  
    plato = db.query(Plato).filter(Plato.id == plato_id).first()

    if not plato:
        raise HTTPException(status_code=404, detail="Plato no encontrado")

    for campo, valor in datos_actualizados.model_dump(exclude_unset=True).items():
        setattr(plato, campo, valor)

    db.commit()
    db.refresh(plato)

    return plato


@router.delete("/{plato_id}")
def eliminar_plato(plato_id: int, db: Session = Depends(get_db)):
    
    plato = db.query(Plato).filter(Plato.id == plato_id).first()

    if not plato:
        raise HTTPException(status_code=404, detail="Plato no encontrado")

    db.delete(plato)
    db.commit()

    return {"message": "Plato eliminado correctamente"}