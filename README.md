# WeatherApp2

This is the second version of the weather forecast application.
The most significant change for the user is the time issue from the previous version has been corrected. Another addition to the functions is the inclusion of the "my location" feature. This is a button that, when chicken, uses JavaScript to get the users location (GPS coordinates) and enters it into the search bar. The user can then click the submit button and the rest of the program works as usual. I have added some survive routes, and included those links to the error messages page.


 This version has some differences from the users perspective, but there are also major differences in the code behind the app. I replaced the several python files with a single file that handles both user location inputs as well as the shortcut links. The previous version has a separate python file for each link and an additional file for user input. This inefficient use of mostly identical files has been reduced to a single file. This file is also broken up into functions while the last version has one function that does everything. Some improvements have been made to the error handling in this version as well, adding try-excepts to deal with missing data. The result is a more compact application made with better organization. 

A feature in the working stage is improving the section of the program that generates the location name to give better, more useful place names for the user. If and when a better way is completed, this will be updated. 
