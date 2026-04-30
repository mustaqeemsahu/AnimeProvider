from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
    ChatMemberHandler,
    InlineQueryHandler
)

from config import BOT_TOKEN

# START
from start import start

# ANIME
from anime import anime_search
from search import improved_anime
from btnsearch import button_search
from animelist import animelist
from directsearch import direct_search

# GROUP
from addwelcome import chat_member_update, welcome_handler

# ADMIN ANIME
from addanime import add_anime, del_anime

# DIRECT CONTROL
from directonoff import direct_on, direct_off

# FUN
from roast import roast_user

# INFO
from idinfo import user_id, owner, admin_list

# ADMIN SYSTEM
from admincmd import stats, broadcast, bulk_add

# SYSTEM
from system import ping, help_cmd, bot_on, bot_off

# CALLBACK + INLINE
from callback import button_click
from inline import inline_query


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # ==========================
    # COMMANDS
    # ==========================
    app.add_handler(CommandHandler("start", start))

    app.add_handler(CommandHandler("anime", anime_search))
    app.add_handler(CommandHandler("search", improved_anime))
    app.add_handler(CommandHandler("btn", button_search))
    app.add_handler(CommandHandler("animelist", animelist))

    app.add_handler(CommandHandler("add", add_anime))
    app.add_handler(CommandHandler("del", del_anime))

    app.add_handler(CommandHandler("direct_on", direct_on))
    app.add_handler(CommandHandler("direct_off", direct_off))

    app.add_handler(CommandHandler("roast", roast_user))

    app.add_handler(CommandHandler("id", user_id))
    app.add_handler(CommandHandler("owner", owner))
    app.add_handler(CommandHandler("adminlist", admin_list))

    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(CommandHandler("bulkadd", bulk_add))

    # SYSTEM
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("on", bot_on))
    app.add_handler(CommandHandler("off", bot_off))

    # ==========================
    # GROUP EVENTS
    # ==========================
    app.add_handler(ChatMemberHandler(chat_member_update, ChatMemberHandler.CHAT_MEMBER))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_handler))

    # ==========================
    # DIRECT SEARCH
    # ==========================
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, direct_search))

    # ==========================
    # CALLBACK + INLINE
    # ==========================
    app.add_handler(CallbackQueryHandler(button_click))
    app.add_handler(InlineQueryHandler(inline_query))

    print("✅ Bot Started Successfully")
    app.run_polling()


if __name__ == "__main__":
    main()