from sqlalchemy.ext.asyncio import AsyncSession
from app.core.exceptions import AlreadyExistsError, NotFoundError

from .repository import CategoryRepository
from .schemas import CategoryCreate
from .models import Category
from app.database.base_service import BaseService

class CategoryService(BaseService):

    def __init__(self, db:AsyncSession):
        super().__init__(db)
        self.repository = CategoryRepository(db)

    async def create(self, category: CategoryCreate) -> Category:
        async with self.db.begin():
            existing_category = await self.repository.get_by_name(category.name)

            if existing_category:
                raise AlreadyExistsError("Category with this name already exists.")
            
            
            return await self.repository.create(category)
    

    async def get_by_id(self,category_id:int) -> Category:
        category = await self.repository.get_by_id(category_id)

        if category is None:
            raise NotFoundError(f"Category not found with this id {category_id}")
        
        return category
    
    async def get_all(self) -> list[Category]:
        return await self.repository.get_all()