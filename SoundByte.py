import soundcloud
import re
import urllib
CLIENT_ID = 'f06362a90de4a12555c9798e8a9b27d3'

client = soundcloud.Client(client_id=CLIENT_ID)


user = client.get('/resolve', url='https://soundcloud.com/kevin-brey')

print(user.id)

favorite_tracks = client.get('/users/{0}/favorites'.format(user.id), limit=10)

for f in favorite_tracks:
    match = re.match('https://[^/]*/(.*)_m.png', f.waveform_url)
    
    id = match.group(1)

    sound_url = 'http://media.soundcloud.com/stream/{0}'.format(id)

    filename = '{artist} - {title}.mp3'.format(artist=f.user['username'], title=f.title)

    print('Downloading "{filename}" from "{url}"...'.format(filename=filename, url=sound_url))

    urllib.request.urlretrieve(sound_url, filename)

    print('Download complete!')
