from contextlib import asynccontextmanager

import uvicorn
from aiogram import types
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from bot.bot import dp, bot
from config import TOKEN, NGROC_TUNEL_URL

WEBHOOK_PATH = f'/bot/{TOKEN}'
WEBHOOK_URL = f'{NGROC_TUNEL_URL}{WEBHOOK_PATH}'

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@asynccontextmanager
@app.on_event("startup")
async def startup_event():
    await bot.delete_webhook(drop_pending_updates=True)
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL,
            allowed_updates=dp.resolve_used_update_types(),
            drop_pending_updates=True
        )


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    await dp.feed_update(bot=bot, update=telegram_update)


@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", reload=True, workers=1)