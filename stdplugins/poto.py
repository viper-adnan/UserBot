#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
Command - .poto or .poto <number>

Send all profile pic of user or chat to tge current chat.
"""

# ----------------------------------------------------------------
# All Thenks goes to Emily ( The creater of This Plugin)
# Some credits goes to me ( @kirito6969 ) for ported this plugin
# and `SnapDragon for` Helping me.
# ----------------------------------------------------------------

import logging

from uniborg.util import admin_cmd

from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
import asyncio
logger = logging.getLogger(__name__)



if 1 == 1:
    name = "Profile Photos"
    client = borg

    @borg.on(admin_cmd(pattern="poto ?(.*)"))
    async def potocmd(event):
        """Gets the profile photos of replied users, channels or chats"""
        id = "".join(event.raw_text.split(maxsplit=2)[1:])
        user = await event.get_reply_message()
        chat = event.input_chat
        if user:
            photos = await event.client.get_profile_photos(user.sender)
            u = True
        else:
            photos = await event.client.get_profile_photos(chat)
            u = False
        if id.strip() == "":
            if len(photos) > 0:
                await event.client.send_file(event.chat_id, photos)
                await event.delete()
            else:
                try:
                    if u is True:
                        photo = await event.client.download_profile_photo(user.sender)
                    else:
                        photo = await event.client.download_profile_photo(event.input_chat)
                    await event.client.send_file(event.chat_id, photo)
                    await event.delete()
                except a:
                    await event.edit("**This user does not have profile pictures.**")
                    return
        else:
            try:
                id = int(id)
                if id <= 0:
                    await event.edit("ID number Invalid!**")
                    return
            except:
                 await event.edit("**Something went wrong.**")
                 return
            if int(id) <= (len(photos)):
                send_photos = await event.client.download_media(photos[id - 1])
                await event.client.send_file(event.chat_id, send_photos)
                await event.delete()
            else:
                await event.edit("```No photo found.```")
                await asyncio.sleep(8)
                return