from handlers.users.start import router as start_router

def register_all_handlers(dp):
    dp.include_router(start_router)
