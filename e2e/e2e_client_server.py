import sys
sys.path.append("./library")

import argparse
import utils.CallBacks
from BluetoothHandler import BluetoothHandler

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-server", help="flag indicating if it should initiate as a server",
                    action="store_true")
    group.add_argument("--client", help='Indicates client mode and accepts the MAC address of the server for bluetooth connection as an argument', type=str)

    parser.add_argument('--nativeLanguage', "-l", choices=['en', 'ch', 'terminal'], required=True)
    parser.add_argument('-v', '--verbose', action="store_true")
    args = parser.parse_args()

    # Create callbacks based on language
    if args.nativeLanguage == 'en':
        sendingCallback = utils.CallBacks.get_input_to_english
        receivingCallback = [utils.CallBacks.synthesize_speech_english]
    elif args.nativeLanguage == 'ch':
        sendingCallback = utils.CallBacks.getInputFromChinese
        receivingCallback = [utils.CallBacks.outputInputChinese]
    else:
        sendingCallback = utils.CallBacks.getInputFromTerminal
        receivingCallback = [utils.CallBacks.print_input]

    # Add print callback if verbose
    if args.verbose and args.nativeLanguage != 'terminal':
        receivingCallback.append(utils.CallBacks.print_input)

    # Create client or server
    if args.server: # Server
        print("aaaaaaaaaaaaaaaaaaaaaa")
        clientServer = BluetoothHandler(receivingCallback, sendingCallback)
    else:
        clientServer = BluetoothHandler(receivingCallback, sendingCallback, args.serverMac)

    clientServer.start()

if __name__ == '__main__':
    main()
