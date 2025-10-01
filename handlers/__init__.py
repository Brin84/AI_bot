from aiogram import Router
from .h01_start import router as start_router

router = Router()
router.include_router(start_router)