<<<<<<< HEAD
dimension1 = int(input("Please enter the first dimensions of the room = "))
dimension2 = int(input("Please enter the second dimensions of the room = "))


Tunpaintable = int(input("Please enter the dimensions of the unpaintable areas = "))
Tcoats = int(input("How many coats of paint are required? = "))

sq = (dimension1 * dimension2) - Tunpaintable
Tsq = sq*Tcoats
Anwser = Tsq/11

print("in total you will need", Anwser, " amount of paint")

=======
dimension1 = int(input("Please enter the first dimensions of the room = "))
dimension2 = int(input("Please enter the second dimensions of the room = "))


Tunpaintable = int(input("Please enter the dimensions of the unpaintable areas = "))
Tcoats = int(input("How many coats of paint are required? = "))

sq = (dimension1 * dimension2) - Tunpaintable
Tsq = sq*Tcoats
Anwser = Tsq/11

print("in total you will need", Anwser, " amount of paint")

## ACS - i think you need heigh and wdith not just area but for the moment it is fine
## ACS - Logically it woprks but your code needs annotations (comments)
>>>>>>> 923698615c989ade9d14ee55bb4c08e1fc9c8bc7
