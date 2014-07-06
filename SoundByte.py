import soundcloud

CLIENT_ID = 'f06362a90de4a12555c9798e8a9b27d3'
CLIENT_SECRET = 'ce4dbed1c6255b897c6bb7c5401d2c68'
USERNAME = 'user'
PASSWORD = 'pass'

client = soundcloud.Client(
	client_id=CLIENT_ID,
	client_secret=CLIENT_SECRET,
	username=USERNAME,
	password=PASSWORD
)


print(client.get('/me'))

