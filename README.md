```
     ██╗██╗   ██╗██████╗ ██████╗     ██████╗  ██████╗ ████████╗
     ██║██║   ██║██╔══██╗██╔══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝
     ██║██║   ██║██║  ██║██║  ██║    ██████╔╝██║   ██║   ██║   
██   ██║██║   ██║██║  ██║██║  ██║    ██╔══██╗██║   ██║   ██║   
╚█████╔╝╚██████╔╝██████╔╝██████╔╝    ██████╔╝╚██████╔╝   ██║   
 ╚════╝  ╚═════╝ ╚═════╝ ╚═════╝     ╚═════╝  ╚═════╝    ╚═╝                                                                  
```
# Judd Bot

## Judd Bot is a Discord bot that sends random files and messages from specified lists on a set interval.

## Requirements
* #### [Python 3.6+](https://www.python.org/downloads/)
* #### [discord.py library](https://pypi.org/project/discord.py/)
* #### [asyncio library](https://pypi.org/project/asyncio/)
* #### [aiohttp library](https://pypi.org/project/aiohttp/)
* #### [A Discord Bot token](https://discord.com/developers/docs/intro)
* #### [A Discord server to add the bot to](https://discord.com)

## Installation
* #### Clone the repository or download the source code.
* #### Install the required libraries by running pip install -r requirements.txt
* #### Replace 'CHANNEL_KEY_HERE_WITHOUT_QUOTES' with the key of the channel where you want the bot to send messages.
* #### Replace 'BOT_KEY_HERE' with your bot's token.
* #### Run the script using Judd-bot.py

## Features
* #### Sends random files and messages from specified lists on a set interval.
* #### Sends a specific message and file when the command 'headpat' is used in the chat.

## Customization
* #### You can customize the myfiles, myjudd, myjuddpet, myjuddmeow, and myqoutes lists to include your own files and messages.
* #### You can change the interval at which the bot sends messages by modifying the hours parameter in the @tasks.loop(hours=1) decorator.

## Limitations
* #### on_message event is not working at the moment.

## Contribution
* #### Feel free to fork this repository and make pull requests to add new features or fix bugs.

## License
* #### This project is licensed under the MIT License. See the LICENSE file for details.

## Other
* #### [Judd-Bot Twitter](https://twitter.com/Hourly_Judd)
* #### [SteamWolf's github](https://github.com/SteamWo1f)
