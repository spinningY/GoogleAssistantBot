from config import admin_group


def init(update, context):
    """
    This rule, allow to notify the admins in their private group
    """

    if "@admin" in update.message.text.lower():
        # message for user
        msg = "Grazie della segnalazione, ho avvisato gli admin del gruppo."
        update.message.reply_text(text=msg)

        # message for admins
        msg = "Qualcuna/o ha richiesto la vostra attenzione qui:\n\n"
        msg += f"Gruppo: {update.message.chat.title}\n"
        msg += f"link: {update.message.link}"

        notification_message = context.bot.send_message(chat_id=admin_group, text=msg)
        context.bot.pin_chat_message(chat_id=admin_group,
                                     message_id=notification_message.message_id,
                                     disable_notification=False)
        