import curses
import time
import random
import os
import platform
import getpass

colors = {
    'Green': curses.COLOR_GREEN,
    'Yellow': curses.COLOR_YELLOW,
    'Cyan': curses.COLOR_CYAN,
    'Red': curses.COLOR_RED
}
current_color = 'Green'
brightness = 'Medium'
theme = 'Classic'

main_menu = ['STATUS', 'INVENTORY', 'MAP', 'RADIO', "DATA", 'EXIT']

submenus = {
    'STATUS': ['Vitals', 'SPECIAL', 'Skills', 'Perks', 'Quests'],
    'INVENTORY': ['Weapons', 'Apparel', 'Aid', 'Misc', 'Mods'],
    'DATA': ['Info', 'Sys', 'Config', 'Reboot'],
    'MAP': ['Local Maps', 'World'],
    'RADIO': ['Galaxy News', 'Classical', 'Silence']
}

sub_submenus = {
    'Apparel': ['Leather Armor', 'Combat Armor', 'Power Armor'],
    'Weapons': ['Laser Pistol', 'Combat Knife', 'Plasma Rifle', 'Hunting Rifle'],
    'Aid': ['Stimpak x2', 'RadAway', 'Food Ration'],
    'Misc': ['Nuka-Cola', 'Pre-War Money', 'Bobby Pins', 'Scrap Electronics'],
    'Mods': ['Laser Sight', 'Silencer', 'Scope'],
    'Info': [f'Name: {getpass.getuser()}', 'Level: Wanderer', 'Location: Vault 101', 'Reputation: Neutral'],
    'Sys': [
        f'OS: {platform.system()} {platform.release()}',
        f'CPU: {platform.processor() or "Unknown"}',
        f'Machine: {platform.machine()}',
        f'Python: {platform.python_version()}'
    ],
    'Config': [
        f'Color: {current_color}',
        f'Brightness: {brightness}',
        f'Theme: {theme}',
        'Sound: On',
        'Notifications: Enabled'
    ],
    'Quests': ['Find Water Purifier', 'Rescue Nick Valentine', 'Defeat Raiders'],
    'Perks': ['Strong Back', 'Lady Killer', 'Commando']
}



def get_content(main_choice, sub_choice=None, sub_sub_choice=None):
    # STATUS
    if main_choice == 'STATUS':
        if sub_choice == 'Vitals':
            return "HP: 85/100\nRAD: 12\nXP: 2300/2500\nHunger: Normal\nThirst: Normal"
        elif sub_choice == 'SPECIAL':
            return "STR: 6  PER: 5  END: 5\nCHA: 3  INT: 7  AGI: 6\nLCK: 4"
        elif sub_choice == 'Skills':
            return "Barter: 35\nLockpick: 45\nScience: 50\nSneak: 40\nGuns: 55\nMelee: 48"
        elif sub_choice == 'Perks':
            return "\n".join(sub_submenus['Perks'])
        elif sub_choice == 'Quests':
            return "\n".join(sub_submenus['Quests'])

    # INVENTORY
    if main_choice == 'INVENTORY':
        if sub_sub_choice:
            # Info detallada por ítem
            details = {
                'Laser Pistol': "Energy Weapon\nDamage: 33\nWeight: 4.2\nValue: 120 caps",
                'Combat Knife': "Melee Weapon\nDamage: 15\nWeight: 1.5\nValue: 50 caps",
                'Plasma Rifle': "Energy Weapon\nDamage: 50\nWeight: 13.5\nValue: 300 caps",
                'Hunting Rifle': "Firearm\nDamage: 40\nWeight: 8.0\nValue: 200 caps",
                'Leather Armor': "Light Armor\nDamage Res.: 20\nWeight: 7.0\nValue: 100 caps",
                'Combat Armor': "Medium Armor\nDamage Res.: 35\nWeight: 15.0\nValue: 250 caps",
                'Power Armor': "Heavy Armor\nDamage Res.: 80\nWeight: 35.0\nValue: 1500 caps",
                'Stimpak x2': "Restores HP quickly.\nWeight: 0.5\nValue: 75 caps",
                'RadAway': "Reduces radiation.\nWeight: 0.3\nValue: 100 caps",
                'Food Ration': "Restores hunger.\nWeight: 1.0\nValue: 25 caps",
                'Nuka-Cola': "Refreshes thirst.\nWeight: 1.2\nValue: 30 caps",
                'Pre-War Money': "Old currency.\nValue: 5 caps",
                'Bobby Pins': "Used for lockpicking.\nValue: 1 cap each",
                'Scrap Electronics': "Crafting material.\nWeight: 2.0\nValue: 50 caps",
                'Laser Sight': "Improves aiming.\nWeight: 0.4\nValue: 150 caps",
                'Silencer': "Reduces noise.\nWeight: 0.6\nValue: 200 caps",
                'Scope': "Improves accuracy.\nWeight: 0.7\nValue: 250 caps"
            }
            return details.get(sub_sub_choice, "No detailed info available.")
        else:
            return f"Category: {sub_choice}\nSelect an item for details."

    # RADIO
    if main_choice == 'RADIO':
        if sub_choice == 'Galaxy News':
            return "♪ Galaxy News Radio\nNow playing: 'I Don't Want to Set the World on Fire' ♪"
        elif sub_choice == 'Classical':
            return "♪ Classical Station\nNow playing: 'Moonlight Sonata - Beethoven' ♪"
        elif sub_choice == 'Silence':
            return "Radio off."

    # DATA
    if main_choice == 'DATA' and sub_choice == 'Reboot':
        return "System rebooting...\nPlease wait..."
    elif sub_choice == 'Config':
        return "Use ENTER to change selected option"
    elif sub_sub_choice:
        return f"{sub_sub_choice}"
    return "Data Loaded."

def loading_screen(stdscr):
    curses.curs_set(0)
    stdscr.erase()
    stdscr.bkgd(' ', curses.color_pair(1))
    stdscr.addstr(10, 20, "BOOTING PIP-BOY 3000")
    stdscr.refresh()
    time.sleep(1)
    for i in range(3):
        stdscr.addstr(12, 20 + i, ".")
        stdscr.refresh()
        time.sleep(0.4)
    stdscr.clear()

def generate_local_map(map_name, width=20, height=10):
    grid = [['#' for _ in range(width)] for _ in range(height)]

    for y in range(1, height-1):
        for x in range(1, width-1):
            grid[y][x] = '.' if random.random() > 0.15 else '#'

    points = 5
    placed = 0
    while placed < points:
        x = random.randint(1, width-2)
        y = random.randint(1, height-2)
        if grid[y][x] == '.':
            grid[y][x] = 'X'
            placed += 1

    if map_name == 'Vault':
        for y in range(2, height-2):
            for x in range(2, width-2):
                if random.random() < 0.7:
                    grid[y][x] = '.'
    elif map_name == 'Ruins':
        for _ in range(int(width * height * 0.2)):
            rx = random.randint(1, width-2)
            ry = random.randint(1, height-2)
            grid[ry][rx] = '#'
    elif map_name == 'Wasteland':
        for y in range(1, height-1):
            for x in range(1, width-1):
                grid[y][x] = '.' if random.random() > 0.1 else '#'
        points = 10
        placed = 0
        while placed < points:
            x = random.randint(1, width-2)
            y = random.randint(1, height-2)
            if grid[y][x] == '.':
                grid[y][x] = 'X'
                placed += 1
    return grid

def generate_world_map(width=40, height=15):
    grid = [['.' for _ in range(width)] for _ in range(height)]
    points = 20
    placed = 0
    while placed < points:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if grid[y][x] != 'X':
            grid[y][x] = 'X'
            placed += 1
    return grid

def draw_map_grid(stdscr, grid, title):
    stdscr.erase()
    stdscr.bkgd(' ', curses.color_pair(1))
    max_y, max_x = stdscr.getmaxyx()
    stdscr.addstr(1, 2, f"== {title} MAP ==")
    max_lines = max_y - 6
    max_cols = max_x - 8

    # Ajustar el tamaño del mapa al tamaño de la terminal
    for y, row in enumerate(grid):
        if y >= max_lines:
            break
        line = ''.join(row)
        if len(line) > max_cols:
            line = line[:max_cols]
        stdscr.addstr(3 + y, 4, line)
    stdscr.addstr(3 + min(len(grid), max_lines) + 2, 4, "Press any key to return...")
    stdscr.refresh()
    stdscr.getch()

def draw_vertical_menu(stdscr, title, items, selected):
    stdscr.erase()
    stdscr.bkgd(' ', curses.color_pair(1))
    max_y, max_x = stdscr.getmaxyx()
    stdscr.addstr(1, 2, f"{title}:")
    for i, item in enumerate(items):
        if 3 + i >= max_y - 3:
            break  # Evitar overflow vertical
        if i == selected:
            stdscr.attron(curses.A_REVERSE)
        display_item = item
        if len(display_item) > max_x - 8:
            display_item = display_item[:max_x - 8]
        stdscr.addstr(3 + i, 4, display_item)
        if i == selected:
            stdscr.attroff(curses.A_REVERSE)
    stdscr.addstr(min(3 + len(items) + 2, max_y - 2), 4, "↑ ↓ to move | ENTER to select | B to go back")
    stdscr.refresh()

def show_section(stdscr, title, content):
    stdscr.erase()
    stdscr.bkgd(' ', curses.color_pair(1))
    max_y, max_x = stdscr.getmaxyx()
    stdscr.addstr(1, 2, f"== {title} ==")
    lines = content.split("\n")
    for i, line in enumerate(lines):
        if 3 + i >= max_y - 2:
            break
        display_line = line
        if len(display_line) > max_x - 8:
            display_line = display_line[:max_x - 8]
        stdscr.addstr(3 + i, 4, display_line)
    stdscr.addstr(min(3 + len(lines) + 2, max_y - 2), 4, "Press any key to return...")
    stdscr.refresh()
    stdscr.getch()

def apply_config(index):
    global current_color, brightness, theme
    options = list(colors.keys())
    if index == 0:  # Color
        idx = options.index(current_color)
        current_color = options[(idx + 1) % len(options)]
    elif index == 1:  # Brightness
        brightness = 'Low' if brightness == 'Medium' else 'Medium' if brightness == 'High' else 'High'
    elif index == 2:  # Theme
        theme = 'Retro' if theme == 'Classic' else 'Classic'

def update_color():
    curses.init_pair(1, colors[current_color], curses.COLOR_BLACK)

def draw_menu(stdscr, selected):
    stdscr.erase()
    stdscr.bkgd(' ', curses.color_pair(1))
    stdscr.addstr(1, 2, f"╔═{'═'*61}═╗")
    stdscr.addstr(2, 2, "║{:^61}║".format("PIP-BOY 3000 TERMINAL"))
    stdscr.addstr(3, 2, f"╚═{'═'*61}═╝")
    stdscr.addstr(5, 2, "════>")
    x = 9
    for idx, item in enumerate(main_menu):
        if idx == selected:
            stdscr.attron(curses.A_REVERSE)
        stdscr.addstr(5, x, f"{item}")
        if idx == selected:
            stdscr.attroff(curses.A_REVERSE)
        x += len(item) + 4
    stdscr.addstr(7, 2, "Use ← → to navigate, ENTER to select, Q to quit.")
    stdscr.refresh()

def draw_submenu(stdscr, main_choice, submenu_items, selected):
    stdscr.erase()
    stdscr.bkgd(' ', curses.color_pair(1))
    stdscr.addstr(1, 2, f"== {main_choice} ==")
    stdscr.addstr(3, 2, "Select a category:")
    x = 4
    for idx, item in enumerate(submenu_items):
        stdscr.attron(curses.A_REVERSE) if idx == selected else stdscr.attroff(curses.A_REVERSE)
        stdscr.addstr(5, x, f"{item}")
        x += len(item) + 4
    stdscr.addstr(7, 2, "← → move | ENTER select | B back")
    stdscr.refresh()

def main(stdscr):
    
    curses.start_color()
    update_color()
    loading_screen(stdscr)
    curses.curs_set(0)

    selected_main = 0
    local_maps = ['Vault', 'Ruins', 'Wasteland']
    while True:
        update_color()
        draw_menu(stdscr, selected_main)
        key = stdscr.getch()

        if key == curses.KEY_RIGHT:
            selected_main = (selected_main + 1) % len(main_menu)
        elif key == curses.KEY_LEFT:
            selected_main = (selected_main - 1) % len(main_menu)
        elif key in [curses.KEY_ENTER, 10, 13]:
            main_choice = main_menu[selected_main]
            if main_choice == 'EXIT':
                break

            if main_choice == 'MAP':
                submenu_items = submenus['MAP']
                selected_sub = 0
                while True:
                    draw_submenu(stdscr, 'MAP', submenu_items, selected_sub)
                    subkey = stdscr.getch()
                    if subkey == curses.KEY_RIGHT:
                        selected_sub = (selected_sub + 1) % len(submenu_items)
                    elif subkey == curses.KEY_LEFT:
                        selected_sub = (selected_sub - 1) % len(submenu_items)
                    elif subkey in [curses.KEY_ENTER, 10, 13]:
                        map_type = submenu_items[selected_sub]
                        if map_type == 'Local Maps':
                            selected_local = 0
                            while True:
                                draw_vertical_menu(stdscr, "Select Local Map", local_maps, selected_local)
                                lkey = stdscr.getch()
                                if lkey == curses.KEY_DOWN:
                                    selected_local = (selected_local + 1) % len(local_maps)
                                elif lkey == curses.KEY_UP:
                                    selected_local = (selected_local - 1) % len(local_maps)
                                elif lkey in [curses.KEY_ENTER, 10, 13]:
                                    local_map = local_maps[selected_local]
                                    grid = generate_local_map(local_map)
                                    draw_map_grid(stdscr, grid, local_map)
                                elif lkey in [ord('b'), ord('B')]:
                                    break
                        elif map_type == 'World':
                            grid = generate_world_map()
                            draw_map_grid(stdscr, grid, "World")
                    elif subkey in [ord('b'), ord('B')]:
                        break

            elif main_choice in submenus:
                submenu_items = submenus[main_choice]
                selected_sub = 0
                while True:
                    draw_submenu(stdscr, main_choice, submenu_items, selected_sub)
                    subkey = stdscr.getch()
                    if subkey == curses.KEY_RIGHT:
                        selected_sub = (selected_sub + 1) % len(submenu_items)
                    elif subkey == curses.KEY_LEFT:
                        selected_sub = (selected_sub - 1) % len(submenu_items)
                    elif subkey in [curses.KEY_ENTER, 10, 13]:
                        sub_choice = submenu_items[selected_sub]
                        if sub_choice in sub_submenus:
                            sub_sub_items = sub_submenus[sub_choice]
                            selected_subsub = 0
                            while True:
                                draw_vertical_menu(stdscr, sub_choice, sub_sub_items, selected_subsub)
                                vkey = stdscr.getch()
                                if vkey == curses.KEY_DOWN:
                                    selected_subsub = (selected_subsub + 1) % len(sub_sub_items)
                                elif vkey == curses.KEY_UP:
                                    selected_subsub = (selected_subsub - 1) % len(sub_sub_items)
                                elif vkey in [curses.KEY_ENTER, 10, 13]:
                                    if sub_choice == 'Config':
                                        apply_config(selected_subsub)
                                        sub_submenus['Config'] = [
                                            f'Color: {current_color}',
                                            f'Brightness: {brightness}',
                                            f'Theme: {theme}',
                                            'Sound: On',
                                            'Notifications: Enabled'
                                        ]
                                        update_color()
                                    content = get_content(main_choice, sub_choice, sub_sub_items[selected_subsub])
                                    show_section(stdscr, f"{main_choice} > {sub_choice}", content)
                                elif vkey in [ord('b'), ord('B')]:
                                    break
                        else:
                            content = get_content(main_choice, sub_choice)
                            show_section(stdscr, f"{main_choice} > {sub_choice}", content)
                            if main_choice == 'DATA' and sub_choice == 'Reboot':
                                loading_screen(stdscr)
                                break
                    elif subkey in [ord('b'), ord('B')]:
                        break
            else:
                content = get_content(main_choice)
                show_section(stdscr, main_choice, content)
        elif key in [ord('q'), ord('Q')]:
            break

curses.wrapper(main)
