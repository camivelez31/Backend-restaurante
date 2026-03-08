from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import get_db
from entities.pedido import Pedido
from schemas.pedido_schema import PedidoCreate, PedidoResponse, PedidoUpdate

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])


@router.get("/", response_model=List[PedidoResponse])
def listar_pedidos(db: Session = Depends(get_db)):
    
    return db.query(Pedido).all()


@router.get("/{pedido_id}", response_model=PedidoResponse)
def obtener_pedido(pedido_id: int, db: Session = Depends(get_db)):
  
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()

    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    return pedido


@router.post("/", response_model=PedidoResponse, status_code=201)
def crear_pedido(pedido: PedidoCreate, db: Session = Depends(get_db)):
   
    nuevo_pedido = Pedido(
        estado=pedido.estado,
        cliente_id=pedido.cliente_id,
        empleado_id=pedido.empleado_id,
        mesa_id=pedido.mesa_id
    )

    db.add(nuevo_pedido)
    db.commit()
    db.refresh(nuevo_pedido)

    return nuevo_pedido


@router.put("/{pedido_id}", response_model=PedidoResponse)
def actualizar_pedido(
    pedido_id: int,
    datos_actualizados: PedidoUpdate,
    db: Session = Depends(get_db)
):
    
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()

    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    for campo, valor in datos_actualizados.model_dump(exclude_unset=True).items():
        setattr(pedido, campo, valor)

    db.commit()
    db.refresh(pedido)

    return pedido


@router.delete("/{pedido_id}")
def eliminar_pedido(pedido_id: int, db: Session = Depends(get_db)):
   
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()

    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    db.delete(pedido)
    db.commit()

    return {"message": "Pedido eliminado correctamente"}