import janus_swi as pl 


# Подключаем базу знаний
pl.consult("lab_1.pl")


# Словарь для блоков
blocks = {
    'стекло': 'glass',
    'бетон': 'concrete',
    'кирпичи': 'bricks',
    'камень': 'stone',
    
    'угольная руда': 'coal_ore',
    'железная руда': 'iron_ore',
    'медная руда': 'copper_ore',
    'лазуритовая руда': 'lapis_lazuli_ore',
    'редстоун руда': 'redstone_ore',
    'золотая руда': 'gold_ore',
    'алмазная руда': 'diamond_ore',
    'изумрудная руда': 'emerald_ore',
    
    'уголь': 'coal_ore',
    'железо': 'iron_ore',
    'медь': 'copper_ore',
    'лазурит': 'lapis_lazuli_ore',
    'редстоун': 'redstone_ore',
    'золото': 'gold_ore',
    'алмазы': 'diamond_ore',
    'изумруды': 'emerald_ore',
    
    'древние обломки': 'ancient_debris_ore',
    'обсидиан': 'obsidian',
    'листья дуба': 'oak_leaves',
    'трава': 'grass',
    'лоза': 'vines',
    'папоротник': 'fern'
}

# Словарь для инструментов
tools = {
    'рука': 'hand',
    'ножницы': 'shears',
    'деревянная кирка': 'wooden_pickaxe',
    'золотая кирка': 'golden_pickaxe',
    'каменная кирка': 'stone_pickaxe',
    'железная кирка': 'iron_pickaxe',
    'алмазная кирка': 'diamond_pickaxe',
    'незеритовая кирка': 'netherite_pickaxe',
}

get = ['получить', 'добыть', 'достать']
wish = ['хочу', 'хочется', 'хотелось']
ability = ['могу']



def parse_input(user_input):
    # Получаем интересы из ввода пользователя
    parts = user_input.lower().split(", ")
    name = parts[0].split(" ")[2].capitalize()
    request = parts[-1]
    return name, request
    
def recomendation(name, request):
    wish_or_ability = 'wish' if any(w in request for w in wish) else 'ability'
    get_action = [item for item in get if item in request]
    block = [key for key in blocks.keys() if key in request]
    tool = [key for key in tools.keys() if key in request]
    need = {'pickaxe': ['нужна', ', или любая кирка лучше этой'], 'shears': ['нужны', '']}
    
    match wish_or_ability:
        case 'wish':
            if get_action and block:  # Проверяем, что нашли хотя бы один элемент
                tool_query, tools_found = pl.query(f"obtained_with_tool({blocks[block[0]]}, Tool)."), []
                for result in tool_query:
                    tools_found.append(result['Tool'])  # Добавляем найденный инструмент в список
                if tools_found:
                    tool_name = list(tools.keys())[list(tools.values()).index(tools_found[0])]
                    confirmed_need = need[tools_found[0].split("_")[-1]]
                    print(f"{name}, чтобы {get_action[0]} {block[0]}, тебе {confirmed_need[0]} {tool_name}{confirmed_need[1]}!")
                else:
                    print(f"{name}, для {block[0]} нет подходящего инструмента.")
            else:
                print(f"{name}, не найдены подходящие блоки или действия в вашем запросе.")
                
        case 'ability':
            if get_action and (block or tool):  # Проверяем, что нашли хотя бы один элемент
                tool_query, tools_found = pl.query(f"obtained_with_tool({blocks[block[0]]}, Tool)."), []
                
                for result in tool_query:
                    tools_found.append(result['Tool'])  # Добавляем найденный инструмент в список
                
                if tools_found:
                    tool_name = list(tools.keys())[list(tools.values()).index(tools_found[0])]
                    confirmed_need = need[tools_found[0].split("_")[-1]]
                    print(f"{name}, чтобы {get_action[0]} {block[0]}, тебе {confirmed_need[0]} {tool_name}{confirmed_need[1]}!")

                else:
                    print(f"{name}, для {block[0]} нет подходящего инструмента.")
            else:
                print(f"{name}, не найдены подходящие блоки или действия в вашем запросе.")



def main():
    print("Введите информацию о себе (например, 'Меня зовут Андрей, я хочу добыть алмазы!'):")
    user_input = input("Ввод: ")
    name, request = parse_input(user_input)
    recomendation(name, request)
    
 
if __name__ == "__main__":
    main()