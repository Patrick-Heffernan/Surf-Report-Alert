# Surf-Report-Alert
As an avid surfer, I wanted an easy way to get a surf report alert on my cell phone every morning. 

This program pulls selected data from Magic Seaweed's API, parses it, and emails it to my phone. I then set up a Task Scheduler so it runs every morning. 

You need to do a few things in order to make the modules work: 
  First, Magic Seaweed requires an API key to access their data. Visit their website (https://magicseaweed.com/developer/api) to get more informaiton. 
    You will also need to determine which surf locations you want to follow. Where I am from, the conditions don't vary much area to area, so I just track my normal spot with the code. 
    To find the surf location ID, go to the Magic Seaweed website normally and it should be in the html link as a 3 or 4 digit number. 
  
  The timinig of surf conditions is also essential. I usually go surfing in the morning, so I indexed the data to show 8AM times. Use the given timestamp data to figure out which times you want. 
    **Note** Magic Seaweed updates their data every 3 hours
  
  Next, you'll need to enable the gmail API for your account and give it access to send out emails. 
    I followed the description in Chapter 18 of the book "How to Automate the Boring Stuff." The Author also wrote the ezgmail module so its super easy to follow
    Set up the task scheduler on your OS to make sure the program runs every morning. 
