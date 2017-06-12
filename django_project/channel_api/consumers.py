from channels import Channel, Group
from channels.sessions import channel_session
from channels.auth import channel_session_user


# Connected to websocket.connect
@channel_session
def ws_add(message):
    # Accept the connection
    message.reply_channel.send({"accept": True})
    # get group name
    room = message.content['path'].strip("/")
    # set room in session
    message.channel_session['room'] = room;
    # Add to the group
    Group(room).add(message.reply_channel)


@channel_session
def ws_message(message):
    Group(message.channel_session['room']).send({
        "text": message['text'],
    })


# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message):
    Group(message.channel_session['room']).discard(message.reply_channel)