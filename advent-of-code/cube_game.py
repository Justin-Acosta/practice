example_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

from puzzle_input import fetch_input

available_cubes = {
      "red":12,
      "green":13,
      "blue":14
}

def construct_game_object(line):
      colon_split = line.split(':')
      #create object for game
      game_object = {
            "game_number":0,
            "red":0,
            "green":0,
            "blue":0
      }
      #add game number to object
      game_object["game_number"] = int(colon_split[0][4:])
      #divide cube pulls by ";"
      cube_pulls = colon_split[1].split(';')
      #itterate through cube_pulls and assign highest value for each color in game_object
      for pull in cube_pulls:
            color_split = pull.split(",")
            for color_string in color_split:
                  
                  if "red" in color_string:
                        red_cubes = int(color_string[:color_string.index('red')])
                        if red_cubes > game_object["red"]:
                              game_object["red"] = red_cubes

                  if "green" in color_string:
                        green_cubes = int(color_string[:color_string.index('green')])
                        if green_cubes > game_object["green"]:
                              game_object["green"] = green_cubes

                  if "blue" in color_string:
                        blue_cubes = int(color_string[:color_string.index('blue')])
                        if blue_cubes > game_object["blue"]:
                              game_object["blue"] = blue_cubes

      return game_object

def solve_puzzle(available, input):
      #create an array to organize each game
      game_array = []
      possible_games_sum = 0
      possible_games_product_sum = 0

      # split into individual lines
      split_input = input.splitlines()

      # split each line into "game" text and "cubes"
      for line in split_input:

            #create object with game number and highest cube count of each color
            game_object = construct_game_object(line)

            #add game object to game array
            game_array.append(game_object)

      #if the game object is possible, add the game number to the possible games sum
      for object in game_array:
            if object['red'] <= available['red'] and object['green'] <= available['green'] and object['blue'] <= available['blue']:
                  possible_games_sum += object['game_number']

      for object in game_array:
            power = object['red'] * object['green'] * object['blue']
            possible_games_product_sum += power

      
      print(possible_games_sum)
      print(possible_games_product_sum)
      return [possible_games_sum,possible_games_product_sum]

solve_puzzle(available_cubes,fetch_input('cube_game')) 