import curses

# Função para criar o menu
def menu(stdscr):
    # Definir opções do menu
    menu_items = ['Opção 1', 'Opção 2', 'Opção 3', 'Sair']
    selected_row = 0

    # Função para mostrar o menu
    def print_menu(stdscr, selected_row_idx):
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        
        for idx, item in enumerate(menu_items):
            x = w//2 - len(item)//2
            y = h//2 - len(menu_items)//2 + idx
            if idx == selected_row_idx:
                stdscr.attron(curses.color_pair(1))  # Realçar a opção selecionada
                stdscr.addstr(y, x, item)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, item)

        stdscr.refresh()

    # Inicializando cores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Mostra o menu inicialmente
    print_menu(stdscr, selected_row)

    # Loop para capturar as teclas
    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and selected_row > 0:
            selected_row -= 1
        elif key == curses.KEY_DOWN and selected_row < len(menu_items) - 1:
            selected_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:  # Enter
            if selected_row == len(menu_items) - 1:
                break  # Sair do menu se a última opção for "Sair"
            stdscr.addstr(0, 0, f"Você escolheu {menu_items[selected_row]}")
            stdscr.refresh()
            stdscr.getch()

        # Atualizar o menu
        print_menu(stdscr, selected_row)

# Executar o programa
curses.wrapper(menu)
