import PySimpleGUI as sg
from discord_webhook import DiscordWebhook

layout = [  [sg.Text("Webhook URL adress")],
            [sg.Input()],
            [sg.Button('Sumbit'), sg.Button('Close')]]



window = sg.Window('Webhook Tool by. zeeq.', layout)     


event, url = window.read()
window.close()
if event == 'Close':
    window.close()
    quit()

def send():
    second = [  [sg.Text("Message")],     
            [sg.Input()],
            [sg.Button('Sumbit'), sg.Button('Close')]]


    tt = sg.Window('Webhook Tool by. zeeq.', second)

    event, mess = tt.read()
    if event == 'Close':
        tt.close()
        quit()
    print(mess)
    webhook = DiscordWebhook(url=url[0], content = mess[0] )
    response = webhook.execute()
    tt.close()
while True:
    send()
