from twitter import Twitter
import time

tw = Twitter()

def start():
    print("memulai program")
    dms = list()
    while True:
        if len(dms) != 0:
            for i in range(len(dms)):
                message = dms[i]['message']
                sender_id = dms[i]['sender_id']
                id = dms[i]['id']

                if len(message) != 0 and len(message) < 280:
                    if "-blorabase" in message:
                        message = message.replace("-blorabase", "Blora Base Fess 🌈 ")
                        if len(message) != 0:
                            if dms[i]['media'] == None:
                                print("DM akan di post")
                                tw.post_tweet(message)
                                tw.delete_dm(id)
                            else:
                                print("DM akan di post dengan Media")
                                print(dms[i]['shorted_media_url'])
                                tw.post_tweet_with_media(message, dms[i]['media'],dms[i]['shorted_media_url'], dms[i]['type'])
                                tw.delete_dm(id)
                        else:
                            print("DM dihapus karena kosong")
                            tw.delete_dm(id)
                    else:
                        print("DM dihapus krn tidak mengandung keyword")
                        tw.delete_dm(id)

            dms = list()

        else:
            print("Direct message is empty...")
            dms = tw.read_dm()
            if len(dms) == 0:
                time.sleep(60)

if __name__ == "__main__":
    start()