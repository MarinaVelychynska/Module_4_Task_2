import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

print("Програма калькулятор, допоможе провести розрахунки")

def calculator(num_1, num_2, action):
  logger.info(f"Користувач ввів наступні значення для чисел num_1 = {num_1}, num_2 = {num_2} та обрав дію action = {action}")

  if action == '1':
     result = num_1+num_2

  elif action == '2':
     result = num_1-num_2

  elif action == '3':
     result = num_1*num_2
    
  elif action == '4':
      if num_2 != 0:
       result = num_1/num_2
      else:
       logger.info("Ділення на 0 є неможливим")

  else :
    print("Невідома операція")
  
  return result

if __name__ == "__main__":
   action = input("Введи дію, використовуючи відповідне число: 1. Додавання\n2. Віднімання\n3. Множення\n4. Ділення\n")
   num_1 = float(input("Введи перше число:"))
   num_2 = float(input("Введи друге число:"))
   
   result_2 = calculator(num_1, num_2, action)
   logger.info(f"Результат обчислення: {num_1} і {num_2}: ")
   logger.info(result_2)
