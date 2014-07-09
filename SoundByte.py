import soundcloud
import re
import urllib

from urllib.error import HTTPError

CLIENT_ID = 'f06362a90de4a12555c9798e8a9b27d3'

RECORD_FILE = 'soundbyte_record.txt'

USERNAME = 'kevin-brey'

client = soundcloud.Client(client_id=CLIENT_ID)

user = client.get('/resolve', url='https://soundcloud.com/{username}'.format(username=USERNAME))

with open(RECORD_FILE) as f:
   already_downloaded = f.readlines()
   
already_downloaded = set([int(x.rstrip()) for x in already_downloaded])

favorite_tracks = temp = client.get('/users/{0}/favorites'.format(user.id))

while len(temp) > 0:
    temp = client.get('/users/{0}/favorites'.format(user.id), offset=(len(favorite_tracks)))
    favorite_tracks += temp

tracks_to_download = [x for x in favorite_tracks if x.id not in already_downloaded]

print("Found {numtracks} favorite tracks you have yet to download.".format(numtracks=len(tracks_to_download)))

with open(RECORD_FILE, 'a') as output_file:
    for f in tracks_to_download:
        match = re.match('https://[^/]*/(.*)_m.png', f.waveform_url)
        
        id = match.group(1)
    
        sound_url = 'http://media.soundcloud.com/stream/{0}'.format(id)
	
        artist = f.user['username']
    	
        filename = '{artist} - {title}.mp3'.format(artist=artist, title=f.title)
    
        filename = re.sub('[^\w\-_\. \(\)\'\[\]\&\#]', ' - ', filename)
		
        filename = re.sub(' +',' ', filename)
				
        print('Downloading "{filename}" from "{url}"...'.format(filename=filename, url=sound_url))
    
        try:
            urllib.request.urlretrieve(sound_url, filename)
            print('Download complete!')
            output_file.write('{song_id}\n'.format(song_id=f.id))
        except HTTPError:
            print("I couldn't download the file ({url}). Now I'm sad.".format(url=sound_url))