import os

api_id = int(os.environ.get("API_ID", "11381402"))
api_hash = os.environ.get("API_HASH", "349d6f6868d82dc82c7a9b356051f035")
bot_token = os.environ.get("BOT_TOKEN", "6139376350:AAHMxMnxX5ak02XQgTY2VpKLMHHUzfDGnPY")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://nydhfile:menfess1@menfess.fqhagjl.mongodb.net/?retryWrites=true&w=majority&appName=menfess")
db_name = os.environ.get("DB_NAME", "menfess")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1002217395004"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1002149352988"))
channel_3 = int(os.environ.get("CHANNEL_3", "-1002229382977"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1002180983975"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "2024030789"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "3"))
batas_talent = int(os.environ.get("BATAS_TALENT", "10"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "10"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "80"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "70"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "60"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "50"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "40"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "30"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#TestGirl #TestBoy #TestAsk #TestFind #TestSpill #TestStory #TestTalent").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph/file/88d94cecef8315ffca69a.jpg")
pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph/file/88d94cecef8315ffca69a.jpg")
pic_talentgirl = os.environ.get("PIC_TALENTGIRL", "https://telegra.ph/file/88d94cecef8315ffca69a.jpg")
pic_daddysugar = os.environ.get("PIC_DADDYSUGAR", "https://telegra.ph/file/88d94cecef8315ffca69a.jpg")
pic_moansgirl = os.environ.get("PIC_MOANSGIRL" , "https://telegra.ph/file/88d94cecef8315ffca69a.jpg")
pic_moansboy = os.environ.get("PIC_MOANSBOY" , "https://telegra.ph/file/88d94cecef8315ffca69a.jpg")
pic_gfrent = os.environ.get("PIC_GFRENT" , "https://telegra.ph/file/88d94cecef8315ffca69a.jpg")
pic_bfrent = os.environ.get("PIC_BFRENT" , "https://telegra.ph/file/88d94cecef8315ffca69a.jpg")
pic_owner = os.environ.get("PIC_OWNER" , "https://telegra.ph/file/88d94cecef8315ffca69a.jpg")
pic_neko = os.environ.get("PIC_NEKO" , "https://telegra.ph/file/88d94cecef8315ffca69a.jpg")
pic_admingirl = os.environ.get("PIC_ADMINGIRL" , "https://telegra.ph/file/88d94cecef8315ffca69a.jpg")
pic_adminboy = os.environ.get("PIC_ADMINBOY" , "https://telegra.ph/file/88d94cecef8315ffca69a.jpg")
# ============================================================#
pic_rekberboy = os.environ.get("PIC_REKBERBOY", "https://telegra.ph/file/88d94cecef8315ffca69a.jpg")

# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Tidak dapat diakses harap join terlebih dahulu")
start_msg = os.environ.get("START_MSG", """"
{mention},Silahkan gunakan hastag:

#TestBoy / #TestGirl untuk Mencari Pasangan,Teman , Partner dll
#TestAsk untuk Bertanya
#TestStory untuk Berbagi Cerita
#TestSpill untuk Spill Masalah
#TestFind untuk Mencari Pasangan, Teman, Partner dll

{fullname} 🌱\n\nIni adalah bot menfess, semua pesan yang kamu kirim akan masuk ke channel secara anonymous. ketik /help""")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, pesan mu gagal terkirim silahkan gunakan hastag:

#TestBoy / #TestGirl untuk Mencari Pasangan, Teman , Partner dll
#TestAsk untuk Bertanya
#TestStory untuk Berbagi Cerita
#TestSpill untuk Spill Masalah
#TestFind untuk Mencari Pasangan, Teman, Partner dll
""")
