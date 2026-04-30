# ==============================
# ANIME ADMIN COMMANDS
# ==============================

from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_IDS
from database.mongo import add_anime_db, delete_anime_db


# ==============================
# ADD ANIME
# ==============================

async def add_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id not in ADMIN_IDS:
        return await update.message.reply_text("❌ Only admins can use this.")

    text = update.message.text.replace("/add", "", 1).strip()

    if not text:
        return await update.message.reply_text(
            "❌ Format:\n/add Name | keyword1, keyword2 | STICKER_ID | LINK"
        )

    parts = [p.strip() for p in text.split("|")]

    if len(parts) != 4:
        return await update.message.reply_text(
            "❌ Wrong format!\n\nUse:\n/add Naruto | ninja, leaf | STICKER_ID | https://link"
        )

    name, keywords, sticker, link = parts

    keys = [k.strip().lower() for k in keywords.split(",")]

    await add_anime_db(name, keys, sticker, link)

    await update.message.reply_text(
        f"✅ <b>Anime Added Successfully</b>\n\n🎌 {name}",
        parse_mode="HTML"
    )


# ==============================
# DELETE ANIME
# ==============================

async def del_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id not in ADMIN_IDS:
        return await update.message.reply_text("❌ Only admins can use this.")

    name = update.message.text.replace("/del", "", 1).strip()

    if not name:
        return await update.message.reply_text("❌ Usage:\n/del Naruto")

    await delete_anime_db(name)

    await update.message.reply_text(
        f"🗑️ <b>Anime Deleted</b>\n\n🎌 {name}",
        parse_mode="HTML"
    )
