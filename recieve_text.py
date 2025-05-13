
import requests
import time

class recieve:
    def __init__(self, dms_channel_id, auth_token):
        
        self.dms_channel_id = dms_channel_id
        self.auth_token = auth_token


    def recieve_text(self):
        
        
        
        try:
            geturl=f'https://discord.com/api/v9/channels/{self.dms_channel_id}/messages'
            auth = self.auth_token
            header ={
                'Authorization': auth
            }
            last_message = None
        
            while True:
                r = requests.get(url=geturl,  headers=header, timeout=7 )
                
                if r.status_code != 200:
                    print(f"Server failed to reach. status:{r.status_code}")
                response = r.json()
                current_message = list(response[0].values())[1]
            
                if response:
                    
                    if current_message != last_message: 
                        a = list(response[0].values())[12]
                        
                        
                        if a['primary_guild'] != None:
                            print(f'\nUsername: {a['username']}\nIn guild: {a['primary_guild']['identity_enabled']}\nGuild Name: {a['primary_guild']['tag']}\nMessage: {list(response[0].values())[1]}\nMessage Id: {a['id']}')
                        else:
                            print(f'\nUsername: {a['username']}\nIn_guild: False\nMessage: {list(response[0].values())[1]}')
                
                    print('')
                else:
                    print("\nYou got nothing in return :p")
                last_message = list(response[0].values())[1]
                time.sleep(6)

        except requests.exceptions.ConnectionError as e:

            print(e)
        except requests.exceptions.ConnectTimeout as e:
            print(e)



if __name__ == '__main__':
    with open('Information.txt', 'r') as read:
        list_of_info = read.readlines()
        
        Dm_channel_id = list_of_info[0].strip('channel_id: ')
        authorization_token = list_of_info[2].strip('Auth_token: ')

    ref = recieve(Dm_channel_id,authorization_token)
    ref.recieve_text()