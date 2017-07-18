from twython import TwythonStreamer, Twython
import sys
import os

data_file_path = os.path.expanduser(sys.argv[1])

data_file = open(data_file_path, "r")
data_dict = {}
for line in data_file:
	key, val = line.split("=")
	data_dict[key] = val.strip("\n")

class MyStreamer(TwythonStreamer):
	def __init__(self, *args, **kwargs):
		super(MyStreamer, self).__init__(*args, **kwargs)
		self.twitter = Twython(args[0], args[1], args[2], args[3])
	

	def on_success(self, data):
		user_data = data["user"]
		if "text" in data and data["in_reply_to_user_id_str"] == None:
			str_message = "hi @" + user_data["screen_name"] + ", thanks for tweeting at me :)"
			self.twitter.update_status(status = str_message, in_reply_to_status_id = data["id_str" ])
			

	def on_error(self, status_code, error):
		print status_code


stream  = MyStreamer(data_dict["api_key"], 
                      data_dict["api_secret"],
                      data_dict["access_token"], 
                      data_dict["access_token_secret"])
stream.statuses.filter(track = "@" + data_dict["screen_name"])
