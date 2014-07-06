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

    urllib.request.urlretrieve(sound_url, '{0}.mp3'.format(id))

    print(match.group(1))

    print(f.title + " " + f.waveform_url)
