def converter(number):
  number = str(number)
  digits = [number[i] for i in range(len(number))]
  outline = ""
  notation = {1: '', 2: 'K', 3: 'М', 4: 'Б', 5: 'Т', 6: 'Q'}
  step = 1
  while len(digits) // 3 != 0:  # Пока в длине числа помещается хотя бы одна тройка
      if step > len(notation):
          raise KeyError(
              f"Максимальное чисел {len(notation)}")
      if digits[-3] == digits[-2] == digits[-1] == '0':
          for i in range(3):
              digits.pop(-1)
      else:
          outline = digits[-3] + digits[-2] + \
              digits[-1] + notation[step] + ' ' + outline
          for i in range(3):
              digits.pop(-1)
      step += 1
  if 0 < len(digits) < 3:
      outline = ''.join(digits) + notation[step] + ' ' + outline
  return outline
