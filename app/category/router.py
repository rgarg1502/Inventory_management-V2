from fastapi import APIRouter,status, Depends
from .schemas import CategoryCreate, CategoryResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from .service import CategoryService

router = APIRouter(
    prefix="/categories",
    tags = ["Categories"]    
)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=CategoryResponse)
async def create_category(category:CategoryCreate,db:AsyncSession=Depends(get_db)):
    service = CategoryService(db)

    return await service.create(category)