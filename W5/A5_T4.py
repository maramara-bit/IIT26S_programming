def askDimension(PPrompt: str) -> float:
   Feed = float(input(f"Insert {PPrompt}: "))
   return Feed

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
   area = PWidth * PHeight
   return area

def main():
   print("Program starting.")
   width = askDimension("width")
   height = askDimension("height")
   area = calcRectangleArea(width, height)
   print(f"\nArea is {area}\u00b2")
   print("Program ending.")

main()