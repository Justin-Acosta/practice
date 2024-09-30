def find_number_indexes(string):

      number_found = False
      found_number = {
            'number_int': '',
            'number_indexes': []
      }
      found_numbers_array = []

      for index,character in enumerate(string):
            if character.isnumeric():
                  number_found = True
                  found_number['number_int'] += character
                  found_number['number_indexes'].append(index)
            else: 
                  if number_found:
                        found_number['number_int'] = int(found_number['number_int'])
                        found_numbers_array.append(found_number)
                        found_number = {
                              'number_int': '',
                              'number_indexes': []
                        }
                        number_found = False

      return found_numbers_array

def find_symbol_indexes(string):

      found_symbols_array = []

      for index,character in enumerate(string):

            found_symbol = {
            'symbol_indexes': []
            }

            if not character.isalnum() and character != '.':

                  found_symbol['symbol_indexes'].append(index)
                  found_symbols_array.append(found_symbol)

      return found_symbols_array