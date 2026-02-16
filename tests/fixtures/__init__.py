"""
Test fixtures for creating test data.
"""
import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from models.product import Product
from models.customer import Customer
from models.order import Order
from datetime import datetime

class ProductFactory:
    @staticmethod
    async def create_tshirt(db_session: AsyncSession, stock: int = 100) -> Product:
        product = Product(
            name="t-shirt",
            stock=stock,
            units_per_box=10,
            wholesale_price=10.0,
            retailer_price=15.0,
            individual_price=25.0
        )
        db_session.add(product)
        await db_session.commit()
        return product

@pytest.fixture
async def tshirt_product(db_session: AsyncSession):
    return await ProductFactory.create_tshirt(db_session)
