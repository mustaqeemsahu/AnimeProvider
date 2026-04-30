# ==============================
# MAIN BOT FILE
# ==============================

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    InlineQueryHandler,
    filters,
)

from config import BOT_TOKEN

# ==============================
# IMPORT HANDLERS
# ==============================

# Core
from start import start
from anime import anime_search
from search import improved_anime, button_search, direct_search
from animelist import animelist
from callback import button_click
from inline import inline_query

# Admin / DB
from add import add_anime, del_anime
from broadcast import broadcast, stats, bulk_add

# Misc
from misc import (
    roast_user,
    id_command,
    owner_command,
    adminlist_command,
    help_cmd,
    ping,
    bot_on,
    bot_off,
)

# Group
from group import new_user, bot_added

# Mongo
from mongodb import load_anime_cache, create_indexes


# ==============================
# MAIN FUNCTION
# ==============================

async def main():

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # ==============================
    # STARTUP (CACHE + INDEX)
    # ==============================
    await create_indexes()
    await load_anime_cache()

    # ==============================
    # COMMAND HANDLERS
    # ==============================

    # Basic
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("ping", ping))

    # Anime
    app.add_handler(CommandHandler("anime", anime_search))
    app.add_handler(CommandHandler("search", improved_anime))
    app.add_handler(CommandHandler("btn", button_search))
    app.add_handler(CommandHandler("animelist", animelist))

    # Admin Anime
    app.add_handler(CommandHandler("add", add_anime))
    app.add_handler(CommandHandler("del", del_anime))

    # Broadcast / Stats
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("bulkadd", bulk_add))

    # Misc
    app.add_handler(CommandHandler("roast", roast_user))
    app.add_handler(CommandHandler("id", id_command))
    app.add_handler(CommandHandler("owner", owner_command))
    app.add_handler(CommandHandler("adminlist", adminlist_command))
    app.add_handler(CommandHandler("admins", adminlist_command))

    # System control
    app.add_handler(CommandHandler("on", bot_on))
    app.add_handler(CommandHandler("off", bot_off))

    # ==============================
    # MESSAGE HANDLERS
    # ==============================

    # Auto search (text)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, direct_search))

    # ==============================
    # CALLBACK + INLINE
    # ==============================

    app.add_handler(CallbackQueryHandler(button_click))
    app.add_handler(InlineQueryHandler(inline_query))

    # ==============================
    # GROUP EVENTS
    # ==============================

    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, new_user))
    app.add_handler(MessageHandler(filters.StatusUpdate.BOT_ADDED, bot_added))

    # ==============================
    # RUN BOT
    # ==============================

    print("🚀 Bot Started Successfully...")
    await app.run_polling()


# ==============================
# ENTRY
# ==============================

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
