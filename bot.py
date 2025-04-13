from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Ganti dengan token yang kamu dapatkan dari BotFather
TOKEN = '7588964408:AAEMKxgV1CBtT1MA-Bp1T7updm_iysJp2sk'

# Fungsi untuk command /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Halo, saya bot promosi kamu!')

# Fungsi untuk command /promosi
async def promosi(update: Update, context: CallbackContext):
    await update.message.reply_text('Promo terbaru: Dapatkan hadiah besar! Kunjungi website kami sekarang!')

async def bill(update: Update, context: CallbackContext):
    await update.message.reply_text('Real Madrid over 2.5')

# Fungsi utama untuk menjalankan bot
def main():
    # Inisialisasi Application dengan token
    application = Application.builder().token(TOKEN).build()

    # Menambahkan handler untuk command /start dan /promosi
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("promosi", promosi))
    application.add_handler(CommandHandler("bill", bill))

    # Mulai bot
    application.run_polling()

if __name__ == '__main__':
    main()