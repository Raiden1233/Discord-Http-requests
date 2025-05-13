import requests

import time


class send:
        
    def __init__(self, dms_channel_id, profile_id, auth_token):
        self.dms_channel_id = dms_channel_id
        self.profile_id = profile_id
        self.auth_token = auth_token
        
    def send_text(self):
        
        while True:
            posturl=f"https://discord.com/api/v9/channels/{self.dms_channel_id}/messages"
            

            profile_ulr =f'https://discord.com/api/v9/users/{self.profile_id}/profile'
            
            header = {
            'Authorization': self.auth_token
            }
            get_data= requests.get(url=profile_ulr,headers=header)
            
            user_data = get_data.json()
            
            print(f"\n[ You are Dming to {user_data['user']['global_name']} aka {user_data['user']['username']} ] \n".upper())


            data={
                'content':f'{input("Enter the text you want to send. (Press ctrl + c to exit the script.)\n-> ")}'

            }
        
            
            r = requests.post(url=posturl,data=data, headers=header)
            
            
            print(f"\nMessage Sent! {r}\n")
            time.sleep(1.5)


if __name__ == '__main__':
    with open('Information.txt', 'r') as read:
        list_of_info = read.readlines()
        
        Dm_channel_id = list_of_info[0].strip('channel_id: ')
        Profile_id = list_of_info[1].strip('User_id: ')
        authorization_token = list_of_info[2].strip('Auth_token: ')

    ref = send(Dm_channel_id, Profile_id, authorization_token)

    ref.send_text()
