# Calculate-Volume
Calculates volume of water from rainfall

Scenario
Rainfall from a garden shed with a roof area of 10 m2 feeds into a Jojo water tank with a capacity of 1000 litres.
Next to the garden shed is a swimming pool, with a volume of 20 000 litres (when completely full) and a surface area of 6 m2.
A pump and hose connect the Jojo tank to the pool, so that water can be pumped from the Jojo tank to the pool.
Water evaporates from the pool, causing the volume of water in the pool to decrease.  When it rains, the volume of water in the pool increases.
On Thursdays, a gardener comes and fills up the pool from the Jojo tank.  Sometimes there is more water in the Jojo tank than can fit in the pool, 
in which case some water is left over in the tank afterwards.  Sometimes there is not enough water in the Jojo tank to fill up the pool, in which case the pool is not filled up completely that day.

Assumptions
•	1 mm of rainfall or evaporation = 1 litre per m2 of surface area
•	All the rain that falls on the roof goes into the Jojo tank (there are no losses).
•	If the Jojo tank is full when it is raining, the excess rainfall (overflow) goes down the drain.
•	If the pool is full when it is raining, the excess rainfall overflows and goes down the drain.
•	The gardener switches off the water from the Jojo tank at the exact moment that the pool is full.
•	Rainfall and evaporation happen simultaneously, and before the gardener arrives.

Task
You are required to write a computer program that reads daily rainfall (mm) and evaporation (mm) from a csv file and answer the questions that follow.  
The program must calculate, each day, the volume of water in the Jojo tank and the pool; when there is rain, it must calculate the volumes of water 
going into the tank and the pool, and the volume of water evaporating out of the pool.  
The program must also check the day of the week, and if it is a Thursday, the pool must be filled-up with water from the tank.
Remember: if there is no space in the tank or pool for water, it is lost! 

Questions
1.	If, on 1 January 2015, the pool was 50% full, and the Jojo tank was empty, what are the volumes of water in the pool and tank on 15 January 2016 and 31 December 2016?
2.	If, on 1 January 2015, the pool was 50% full, and the Jojo tank was empty, how much water in total was pumped from the Jojo tank into the pool between 1 January 2015 and 31 December 2019?  (a four-year period).  You will need to add up the amounts the gardener pumped each Thursday over the 4-year period.
