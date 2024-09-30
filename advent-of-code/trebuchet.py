from puzzle_input import fetch_input

number_dictionary = {
      # 'eleven':'11',
      # 'twelve':'12',
      # 'thirteen':'13',
      # 'fourteen':'14',
      # 'fifteen':'15',
      # 'sixteen':'16',
      # 'seventeen': '17',
      # 'eighteen':'18',
      # 'ninteen':'19',
      # 'twenty':'20',
      'one':'1',
      'two':'2',
      'three':'3',
      'four':'4',
      'five':'5',
      'six':'6',
      'seven':'7',
      'eight':'8',
      'nine':'9',
      'ten':'10'
}

def parse_calebration(calebration):

      calebration_lines = calebration.splitlines()    
      decoded_numbers = []
      total = 0

      for line in calebration_lines:
            test_string = ''
            first_number = ''
            last_number = ''

            for character in line:
                  if first_number.isnumeric():
                        break
                  else:
                        if character.isnumeric():
                              first_number = character
                              test_string = ''
                              break

                        test_string += character

                        for key, value in number_dictionary.items():
                              if key in test_string:
                                    first_number = value
                                    test_string = ''
                                    break

            for character in reversed(line):
                  if last_number.isnumeric():
                        break
                  else:
                        if character.isnumeric():
                              last_number = character
                              test_string = ''
                              break

                        test_string = character + test_string

                        for key, value in number_dictionary.items():
                              if key in test_string:
                                    last_number = value
                                    test_string = ''
                                    break

            decoded_numbers.append(int(first_number + last_number))

      for number in decoded_numbers:
            total += number

      print(total)

parse_calebration(fetch_input("trebuchet"))