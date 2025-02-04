# models.py
from dataclasses import dataclass, field
from datetime import datetime, date
from typing import Optional
from sqlalchemy import Column, Integer, String, Numeric, Date, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import registry, relationship

mapper_registry = registry()
Base = mapper_registry.generate_base()

# Utilizamos @dataclass para definir modelos que cumplen con SOLID (cada clase se encarga de un único concepto).

@mapper_registry.mapped
@dataclass
class DimProducto(Base):
    __tablename__ = 'dim_producto'
    __sa_dataclass_metadata_key__ = 'sa'

    id: Optional[int] = field(init=False, default=None, metadata={"sa": Column(Integer, primary_key=True)})
    nombre: str = field(default="", metadata={"sa": Column(String(50), nullable=False)})
    categoria: Optional[str] = field(default=None, metadata={"sa": Column(String(50))})
    stock: int = field(default=0, metadata={"sa": Column(Integer, default=0)})
    precio: Optional[float] = field(default=None, metadata={"sa": Column(Numeric(10,2))})
    created_at: datetime = field(default_factory=datetime.utcnow, metadata={"sa": Column(DateTime, default=datetime.utcnow)})
    updated_at: datetime = field(default_factory=datetime.utcnow, metadata={"sa": Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)})

@mapper_registry.mapped
@dataclass
class DimCliente(Base):
    __tablename__ = 'dim_cliente'
    __sa_dataclass_metadata_key__ = 'sa'

    id: Optional[int] = field(init=False, default=None, metadata={"sa": Column(Integer, primary_key=True)})
    nombre: str = field(default="", metadata={"sa": Column(String(100), nullable=False)})
    email: Optional[str] = field(default=None, metadata={"sa": Column(String(100), unique=True)})
    telefono: Optional[str] = field(default=None, metadata={"sa": Column(String(20))})
    direccion: Optional[str] = field(default=None, metadata={"sa": Column(String(200))})
    segmento: Optional[str] = field(default=None, metadata={"sa": Column(String(50))})
    created_at: datetime = field(default_factory=datetime.utcnow, metadata={"sa": Column(DateTime, default=datetime.utcnow)})
    updated_at: datetime = field(default_factory=datetime.utcnow, metadata={"sa": Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)})

@mapper_registry.mapped
@dataclass
class DimUsuario(Base):
    __tablename__ = 'dim_usuario'
    __sa_dataclass_metadata_key__ = 'sa'

    id: Optional[int] = field(init=False, default=None, metadata={"sa": Column(Integer, primary_key=True)})
    username: str = field(default="", metadata={"sa": Column(String(50), unique=True, nullable=False)})
    rol: Optional[str] = field(default=None, metadata={"sa": Column(String(20))})
    created_at: datetime = field(default_factory=datetime.utcnow, metadata={"sa": Column(DateTime, default=datetime.utcnow)})
    updated_at: datetime = field(default_factory=datetime.utcnow, metadata={"sa": Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)})

@mapper_registry.mapped
@dataclass
class DimTiempo(Base):
    __tablename__ = 'dim_tiempo'
    __sa_dataclass_metadata_key__ = 'sa'

    fecha: date = field(init=False, metadata={"sa": Column(Date, primary_key=True)})
    dia: Optional[int] = field(default=None, metadata={"sa": Column(Integer)})
    mes: Optional[int] = field(default=None, metadata={"sa": Column(Integer)})
    anio: Optional[int] = field(default=None, metadata={"sa": Column(Integer)})
    trimestre: Optional[int] = field(default=None, metadata={"sa": Column(Integer)})
    es_fin_de_semana: Optional[bool] = field(default=None, metadata={"sa": Column(Boolean)})

@mapper_registry.mapped
@dataclass
class HechoVentas(Base):
    __tablename__ = 'hecho_ventas'
    __sa_dataclass_metadata_key__ = 'sa'

    id: Optional[int] = field(init=False, default=None, metadata={"sa": Column(Integer, primary_key=True)})
    producto_id: Optional[int] = field(default=None, metadata={"sa": Column(Integer, ForeignKey('dim_producto.id'))})
    cliente_id: Optional[int] = field(default=None, metadata={"sa": Column(Integer, ForeignKey('dim_cliente.id'))})
    usuario_id: Optional[int] = field(default=None, metadata={"sa": Column(Integer, ForeignKey('dim_usuario.id'))})
    fecha: Optional[date] = field(default=None, metadata={"sa": Column(Date, ForeignKey('dim_tiempo.fecha'))})
    cantidad: int = field(default=0, metadata={"sa": Column(Integer, nullable=False)})
    monto: float = field(default=0.0, metadata={"sa": Column(Numeric(10,2), nullable=False)})
    tipo: Optional[str] = field(default=None, metadata={"sa": Column(String(10))})
    canal: Optional[str] = field(default=None, metadata={"sa": Column(String(50))})
    metodo_pago: Optional[str] = field(default=None, metadata={"sa": Column(String(50))})
    created_at: datetime = field(default_factory=datetime.utcnow, metadata={"sa": Column(DateTime, default=datetime.utcnow)})
    updated_at: datetime = field(default_factory=datetime.utcnow, metadata={"sa": Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)})

@mapper_registry.mapped
@dataclass
class Gastos(Base):
    __tablename__ = 'gastos'
    __sa_dataclass_metadata_key__ = 'sa'

    id: Optional[int] = field(init=False, default=None, metadata={"sa": Column(Integer, primary_key=True)})
    usuario_id: Optional[int] = field(default=None, metadata={"sa": Column(Integer, ForeignKey('dim_usuario.id'))})
    descripcion: Optional[str] = field(default=None, metadata={"sa": Column(String(100))})
    monto: Optional[float] = field(default=0.0, metadata={"sa": Column(Numeric(10,2))})
    fecha: datetime = field(default_factory=datetime.utcnow, metadata={"sa": Column(DateTime, default=datetime.utcnow)})
    created_at: datetime = field(default_factory=datetime.utcnow, metadata={"sa": Column(DateTime, default=datetime.utcnow)})
    updated_at: datetime = field(default_factory=datetime.utcnow, metadata={"sa": Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)})

