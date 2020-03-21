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
                if len(message) != 0 and len(message) < 200:
                    if "-blorabase" in message:
                        message = message.replace("-blorabase", "")
                        if len(message) != 0:
                            if dms[i]['media'] == None:
                                print("DM akan di post")
                                tw.post_tweet(message)
                                tw.delete_dm(id)
                            else:
                                print("DM akan di post dengan media")
                                tw.post_tweet_with_media(message, dms[i]['media'])
                                tw.delete_dm(id)

                        else:
                            print("DM akan dihapus karena kosong")
                            tw.delete_dm(id)
                            #hapus dm
                    else:
                        print("DM akan dihapus karena tidak ada keyword")
                        tw.delete_dm(id)
                        #hapus dm pancingan

            dms = list()
        else:
            print("DM kosong")
            dms = tw.read_dm()
            if len(dms) == 0:
                time.sleep(30)
if __name__ == "__main__":
    start()