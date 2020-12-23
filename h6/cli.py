import click
from h6.zoom_h6 import ZoomH6

@click.command()
@click.option('--port', '-p', 'port', required=True,
    help='The USB serial port where your Zoom H6 is connected',)
@click.option('--command', '-c', 'command', required=True,
    help='The command you want to send to the Zoom H6')
def send_command(port, command):
    """
    Send a command to the Zoom H6 recorder

    Possible commands:

    \b
    | Command           | Button            |
    |-------------------|-------------------|
    | play_pause        | Play / Pause      |
    | stop              | Stop              |
    | record            | Record            |
    | forward           | Forward           |
    | reverse           | Reverse           |
    | vol_up            | Increase volume   |
    | vol_down          | Decrease volume   |
    | ch1               | Toggle Channel 1  |
    | ch2               | Toggle Channel 2  |
    | ch3               | Toggle Channel 3  |
    | ch4               | Toggle Channel 4  |
    | right             | Right             |
    | left              | Left              |
    """

    print(f'Initializing recorder in port "{port}"')
    recorder = ZoomH6(port)

    if recorder.is_initialized:
        print('Shaking hands')
        recorder.initialize()

        print('Sending command')
        recorder.send(command)

        print('Command sent')


if __name__ =='__main__':
    send_command()
