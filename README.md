# Hackathon
by SheTechiez

The world is moving towards energy optimization. We propose an idea to make betterment to the existing Solar Energy Consumption System, by building a hybrid of the existing Grid Tied and Grid On Solar Energy System.
This project proposes to fulfill both the criteria to use energy as efficiently as possible. The project focuses on such a feedback system that manages and supplies power from the optimized source. This utilizes the power from the solar panel, electricity grid, and the stored energy in an optimized way to save power and consume as minimum power as possible.

IMPLEMENTATION

-The project implements the Hybrid Grid Tie Solar System using **LabVIEW** Software and sends data to Thingspeak(an IOT platform).
LabVIEW implements different cases: 1. When solar energy is equal to the energy required by house/building, then the entire energy is drawn from solar.
                                    2. When energy required by home is greater than solar enegry produced, the enerhy is drawn from solar and remaining by power grid.
                                    3. When energy required by home is lesser than the energy produced by solar panels, the excess energy is sent to the grid.
                                    4. During the power cuts in the night, energy is drawn from the battery wich was used to store solar power.

-The **IOT Dashboard** can be found here: https://thingspeak.com/channels/1333842 

-Thingspeak produces a csv file with the following parameters: 1. Voltage produced by solar energy(Solar output)
                                                               2. AC voltage recieved from electricity grid(AC Output)
                                                               3. Energy stored in batter(Battery output)
                                                               4. The amount of energy saved during the process(credits), with day indication

-This data is used for data visualization done on jupyter notebook.

-An application is built using **android studio** to display the number of credits he gets on that day, after validating him for Building number, Username and Password.

The UI looks like this:

![WhatsApp Image 2021-03-21 at 8 30 19 AM](https://user-images.githubusercontent.com/56498610/111892398-2e48aa00-8a21-11eb-8b8b-85a0fc02e34e.jpeg)
![WhatsApp Image 2021-03-21 at 8 39 29 AM](https://user-images.githubusercontent.com/56498610/111892407-4ae4e200-8a21-11eb-813d-0f54b7651ac5.jpeg)

Unable to add androd studio project to github


Video link: https://drive.google.com/drive/folders/16F_Pm_GydpV2iT1rUPVSQIwTFCoo6M_Q?usp=sharing




