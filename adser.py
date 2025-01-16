# Importing libraries
from rubpy import Client             # Import the Client class from rubpy for interacting with the bot
from rubpy.types import Updates      # Import Updates for handling message updates
import asyncio                        # Import asyncio for asynchronous programming
from rich.console import Console      # Import Console class for formatted output
from rich.text import Text            # Import the Text class for styled text
import time                           # Import time for sleep functionality

# Create a console object for rich output
console = Console()

# List of group links
list_links = []  # لیست لینک‌های گروها

text_ = "پیام"  # Message to be sent

n = 0  # Counter for sent messages

# Connect to the server with client
bot = Client(name='bot_ADSer')  # ایجاد یک مشتری جدید با نام 'bot_ADSer'

# Function to handle incoming messages
@bot.on_message_updates()
async def main(message: Updates):
    global n  # Access the global counter
    for group_link in list_links:  # Iterate through the list of group links
        try:
            # Join the group
            add_gap = await bot.join_group(group_link)
            # Get group GUID
            guid_gap = add_gap['group']['group_guid']
            
            # Send message
            await bot.send_message(guid_gap, text_)
            # Leave the group
            await bot.leave_group(guid_gap)
            
            n += 1  # Increase the counter
            
            # Print the number of sent messages with rich output
            console.print(Text(f'✅ تعداد پیام‌های ارسال‌شده: [bold blue]{n}[/bold blue]', style="green"))
            console.print(Text(f'✅ پیام با موفقیت به گروه: [bold magenta]{group_link}[/bold magenta]', style="green"))
            
            # Sleep to prevent hitting the rate limit
            await asyncio.sleep(5)  # Use asyncio.sleep for non-blocking sleep
        except Exception as e:
            console.print(Text(f'❌ خطا در ارسال پیام به {group_link}: {e}', style="red"))  # Print the error message in case of failure

# Running the bot
bot.run()  # Start the bot

# dev :
# rubika : @O_and_ONE_01
# telegram : @Hacker123457890