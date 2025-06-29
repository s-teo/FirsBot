from handlers.users.start import router as start_router
from handlers.users.help import router as help_router
from handlers.users.hello import router as hello_router

def register_all_handlers(dp):
    dp.include_router(start_router)
    dp.include_router(help_router)
    dp.include_router(hello_router)
