
'''limit = 0
if str(message.channel) == 'kolmas_tase':
    limit = 140
elif str(message.channel) == 'teine_tase':
    limit = 70

if len(message.content) < limit and len(message.attachments) == 0:
    await
    client.send_message(
        message.author,
        "Su sõnum oli alla " + str(limit) + " tähemärgi: \n```" + message.content + "```")
    await
    client.delete_message(message)'''