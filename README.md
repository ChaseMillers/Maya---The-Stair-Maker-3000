# Stone-Stair-Maker

A stair maker tool for Maya.

Generate a stair with any given parameters. 

Install instructions are on python file. 

By Chase Miller


![](pics/tool.JPG)
How it's generated.
 - NOTE - Maya uses centimeters for units of measurement.
 - Step 1 - A pollyplane grid is created based on the users sellected width and length. 
 - Step 2 - The pollyplane is extruded by users sellected height.
 - Step 3 - Top surface sellection is decreased by in increamant of 1.
 - Step 4 - Top surface sellection is again extruded.
 - Step 5 - Reapeates step 3.
 - Step 6 - Reapeates step 4.
 - Last two steps Repeate in loop until final result is achieved.
![](pics/building.jpg)

