class Translation(object):
    START_TEXT = """Hi {},
๐๐ธ ๐ ๐๐ฎ๐ฎ๐ญ ๐ฃ๐ธ ๐ข๐ช๐ ๐ข๐ธ๐ถ๐ฎ๐ฝ๐ฑ๐ฒ๐ท๐ฐ?
<a href="t.me/OngoingAnimess">๐๐ธ๐ฒ๐ท ๐๐พ๐ป ๐ฃ๐ฎ๐ต๐ฎ๐ฐ๐ป๐ช๐ถ ๐๐ป๐ธ๐พ๐น</a>"""
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    DOWNLOAD_START = "Downloading To My Temp Server"
    UPLOAD_START = "Uploading Into Telegram"
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Thanks for using me \n\n<b>Join @OngoingAnimess </b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds.\n\n@OngoingAnimess"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "โ Custom thumbnail cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    ABOUT_MSG = """ Something About Me :
    
   โMy Name  : Lazy

   โJoin  : @OngoingAnimess  

   โLanguage : Python3

   โLibrary  : <a href="https://docs.pyrogram.org/">Pyrogram 1.0.7</a>"""
    HELP_USER = """๐๐ธ ๐ ๐๐ฎ๐ฎ๐ญ ๐ฃ๐ธ ๐ข๐ช๐ ๐ข๐ธ๐ถ๐ฎ๐ฝ๐ฑ๐ฒ๐ท๐ฐ?
<a href="t.me/OngoingAnimess">๐๐ธ๐ฒ๐ท ๐๐พ๐ป ๐ฃ๐ฎ๐ต๐ฎ๐ฐ๐ป๐ช๐ถ ๐๐ป๐ธ๐พ๐น</a>"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
You can use /rename command after receiving file to rename it with custom thumbnail support.
"""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
