# Apartment-room-scraper

The apartment and room scraper is the main pillar of my website https://mieszkaniator.vercel.app/search, which is an improved version of my previous project https://github.com/GrzegorzPustulka/Olx-Apartment-finder-GUI. This application is still under development.

## Why this app was created

Powstała ona po to, aby pomóc użytkownikom największego serwisu ogłoszeniowego w Polsce w znalezieniu mieszkań lub pokojów po prawdziwej cenie, uwzględniającej czynsz administracyjny oraz dodatkowe opłaty, takie jak media, prąd, woda i gaz. Więc przykładowo jeśli w filtrach ustawiliśmy mieszkanie do 3000zł to samo mieszkanie może kosztować nawet ponad 4000zł. Dzięki tej aplikacji wraz z moją stroną internetową, filtrujemy po prawdziwej cenie.

## How this app works

It was created to help users of the largest classified ads website in Poland find apartments or rooms at a fair price, taking into account administrative fees and additional charges such as utilities, electricity, water, and gas. For example, if we set the filter for an apartment up to 3000 PLN, the same apartment could actually cost over 4000 PLN. Thanks to this application along with my website, we filter by the actual price.

On the website, the user selects the city and filters, and the query is sent to the server, which returns relevant offers from the database.

## Folders description

- Scraper - There are three files here. Scraper is an abstract class from which the other two classes, ApartmentScraper and RoomScraper, inherit. The main logic of the application for scraping OLX is implemented in these classes.

- dataClasses - This is the file with dataClasses, which stores our data.

- helpers - Here are the helper functions for scraping OLX, such as scraping descriptions, tags, photos, etc.

- emailSender, newScraper, emailSender Currently, there is still a surprise that will be ready by 01.07.2023. You have my word.
