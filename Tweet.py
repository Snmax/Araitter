import ui,tweet,tw,photos,json
from PIL import Image
import os.path,sys

def tweetpush(sender):
	textfield = sender.superview['textfield1']
	response = tweet.tweet(textfield.text)
	if response == 200 :
		textfield.text = ""

def pickimage(sender):
	url = "https://upload.twitter.com/1.1/media/upload.json?command=INIT&total_bytes=56&media_type=image/jpeg"
	image = photos.pick_image()
	imagedata = {"media":b'image'}
	req_media = tw.twitter.post(url,files=imagedata)
		
	print (req_media.text)
	
	# Media ID を取得
	media_id = json.loads(req_media.text)['media_id']
	print ("Media ID: %d" % media_id)

	# Media ID を付加してテキストを投稿
	
	params = {'status': '画像投稿テスト', "media_ids": [media_id]}
	req_media = tw.twitter.post(tw.statuses_update, params = params)
	
	if req_media.status_code != 200 :
		print("画像のアップロードに失敗したのだ。")

v = ui.load_view()
v.present('sheet')
