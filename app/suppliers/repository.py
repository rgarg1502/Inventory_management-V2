
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.exceptions import NotFoundError
from app.database.session import get_db
from app.suppliers.models import Supplier
from app.suppliers.schemas import SupplierCreate, SupplierUpdate


class SupplierRepository:
    def __init__(self, db:AsyncSession):
        self.db = db

    async def create_supplier(self, create_data:SupplierCreate) -> Supplier:
        supplier_data = Supplier(**create_data.model_dump())

        self.db.add(supplier_data)
        await self.db.flush()
        await self.db.refresh(supplier_data)
        return supplier_data

    async def get_by_id(self,supplier_id:int) -> Supplier:
        stmt = select(Supplier).where(Supplier.id == supplier_id)
        result = await self.db.execute(stmt)

        return result.scalar_one_or_none()

    async def get_by_name(self,supplier_name:str) -> Supplier:
        stmt = select(Supplier).where(Supplier.name == supplier_name)
        result = await self.db.execute(stmt)

        return result.scalar_one_or_none()

    async def get_all(self) -> list[Supplier]:
        stmt = select(Supplier).order_by(Supplier.name)
        result = await self.db.execute(stmt)
        
        return result.scalars().all()

    async def update_supplier(self,supplier_id:int,update_data:SupplierUpdate) -> Supplier:
        stmt = select(Supplier).where(Supplier.id == supplier_id)
        result = await self.db.execute(stmt)
        supplier_to_update = result.scalar_one_or_none()

        if supplier_to_update is None:
            raise NotFoundError(f"supplier with this id :{supplier_id} is not found")

        supplier_update_data = update_data.model_dump(exclude_unset=True)

        for key,value in supplier_update_data.items():
            setattr(supplier_to_update, key, value)

        return supplier_to_update