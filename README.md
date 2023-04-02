# Apartment-room-scraper

The apartment and room scraper is the main pillar of my website https://mieszkaniator.vercel.app/search, which is an improved version of my previous project https://github.com/GrzegorzPustulka/Olx-Apartment-finder-GUI. This application is still under development.

## Why this app was created

It was created to help users of the largest classified ads website in Poland find apartments or rooms at a fair price, taking into account administrative fees and additional charges such as utilities, electricity, water, and gas. For example, if we set the filter for an apartment up to 3000 PLN, the same apartment could actually cost over 4000 PLN. Thanks to this application along with my website, we filter by the actual price.

## How this app works

In the main file of the application, the function create_room_table('city') or create_apartment_table('city') is called, which creates a table in the database if it does not exist yet. Then an instance of the class RoomScraper('city') or ApartmentScraper('city') is created and the start method is called. The program scrapes all the offer subpages for a given city and saves them to the database. Thanks to a separate thread for each subpage, the whole process is much faster.

On the website, the user selects the city and filters, and the query is sent to the server, which returns relevant offers from the database.

## Folders description

- Scraper - There are three files here. Scraper is an abstract class from which the other two classes, ApartmentScraper and RoomScraper, inherit. The main logic of the application for scraping OLX is implemented in these classes.

- dataClasses - This is the file with dataClasses, which stores our data.

- helpers - Here are the helper functions for scraping OLX, such as scraping descriptions, tags, photos, etc.

- emailSender, newScraper, emailSender Currently, there is still a surprise that will be ready by 01.07.2023. You have my word.
