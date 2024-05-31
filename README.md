# EU4 Graphs Bot

## Overview

This Discord bot is designed to create and display various graphs for the game Europa Universalis IV using Skanderbeg save data. The bot fetches data from the Skanderbeg API, processes it, and generates graphs based on different metrics. The bot also supports some basic commands for interacting with users.

## Features

- **Ping Command**: Responds with the bot's latency.
- **Help Command**: Provides a detailed description of the bot's functionality and available commands.
- **Graphs Command**: Generates and sends various graphs based on the provided Skanderbeg save ID.
- **Creator Command**: Provides the Discord ID of the bot's creator.

## Installation

### Prerequisites

- Python 3.6+
- Discord Bot Token
- Skanderbeg API Key

### Required Python Packages

Install the required packages using pip:

```sh
pip install discord.py requests beautifulsoup4 pandas matplotlib
```

### Configuration

Create a `config.py` file in the project directory with the following content:

```python
key = 'YOUR_DISCORD_BOT_TOKEN'
```

Replace `YOUR_DISCORD_BOT_TOKEN` with your actual Discord bot token.

## Usage

1. **Clone the Repository**

   ```sh
   git clone https://github.com/your-username/eu4-graphs-bot.git
   cd eu4-graphs-bot
   ```

2. **Run the Bot**

   Start the bot by running the following command:

   ```sh
   python bot.py
   ```

### Available Commands

- `,ping`: Responds with the bot's latency in milliseconds.
- `,help`: Displays the help message with a description of the bot and available commands.
- `,graphs [Skanderbeg_Save_ID]`: Generates and sends various graphs based on the provided Skanderbeg save ID.
- `,creator`: Displays the Discord ID of the bot's creator.

## Example

To generate graphs, use the `,graphs` command followed by the Skanderbeg save ID:

```sh
,graphs d852c8
```

This will fetch data from the Skanderbeg API, generate the graphs, and send them to the Discord channel.

## Error Handling

The bot includes basic error handling to manage command cooldowns and invalid save IDs. If a command is on cooldown, the bot will notify the user with the remaining cooldown time. If an invalid save ID is provided, the bot will inform the user.

## Customization

### Graph Storage Folder

The bot requires specifying a folder location to store generated graphs. This location can be set by updating the `folder.txt` file or providing the folder path during the bot's execution.

### Skanderbeg API Key

Ensure the Skanderbeg API key is correctly included in the URL for data fetching:

```python
url = f'https://skanderbeg.pm/api.php?key=YOUR_SKANDERBEG_API_KEY&scope=getCountryData&save={save}&tag=IRE&value=inc_no_subs;total_development;buildings_value;provinces;total_army;qualityScore;total_mana_spent_on_deving;total_mana_on_teching_up;spent_total;fdp;total_mana_spent_on_deving;battleCasualties;max_manpower;continents;dev_clicks;total_navy;total_army;hex;player;countryName&{ia}&format=json'
```

Replace `YOUR_SKANDERBEG_API_KEY` with your actual Skanderbeg API key.

## License

This project is licensed under the MIT License.

## Contact

For any questions or issues, please contact the repository owner.

---

Enjoy generating and analyzing your Europa Universalis IV data with the EU4 Graphs Bot!
