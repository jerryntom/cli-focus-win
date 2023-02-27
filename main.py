from os import system
import winsound
import time

version = '2302023'
work_time = 30
break_time = 5
long_break_time = 10
rounds_to_long_break = 4
rounds_elapsed = 0
task_title = "Task title"
menu_focus_option = 0


def change_task_title():
    global task_title

    system('cls')
    task_title = input("Please input task title:")
    focus_on_task()


def break_focus(type_of_break):
    global menu_focus_option, break_time

    start_time = time.localtime()
    break_time_secs = break_time * 60
    progress_bar = ['.'] * 20
    progress_bar_pos = 0
    progress_bar_part = break_time_secs / 20

    while True:
        now_time = time.localtime()
        time_diff = break_time_secs - (time.mktime(now_time) - time.mktime(start_time))
        time_elapsed = time.mktime(now_time) - time.mktime(start_time)
        time_diff_minutes = int(time_diff // 60)
        time_diff_secs = int(time_diff % 60)

        system('cls')

        if type_of_break == 'normal':
            print("| Enjoy your break! |")
        elif type_of_break == 'long':
            print("| Enjoy your long break! |")

        if time_diff_secs < 10:
            print(f"Time to finish break: {time_diff_minutes}:0{time_diff_secs}")
        else:
            print(f"Time to finish break: {time_diff_minutes}:{time_diff_secs}")

        print('[', end="")
        for char in progress_bar:
            print(char, end="")
        print(']')

        if (time_elapsed // progress_bar_part) >= progress_bar_pos and progress_bar_pos <= 19:
            progress_bar[progress_bar_pos] = u'█'
            progress_bar_pos += 1

        if progress_bar_pos < 19:
            if time_diff_secs % 2 == 0:
                progress_bar[progress_bar_pos] = u'█'
            else:
                progress_bar[progress_bar_pos] = '.'

        time.sleep(1)

        if time_diff_minutes == 0 and time_diff_secs == 0:
            while True:
                system('cls')
                print("Break session is over! Let's do some work!")
                print("1. Focus session")
                print("2. Abort")
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

                try:
                    menu_focus_option = int(input("Option: "))
                except ValueError:
                    print("Incorrect option!")
                    time.sleep(0.5)
                    continue

                if menu_focus_option == 1:
                    system('cls')
                    while True:
                        print('Do you want to change task to focus on?')
                        print('1. Yes')
                        print('2. No')
                        try:
                            menu_focus_option = int(input("Option: "))

                            if menu_focus_option == 1:
                                change_task_title()
                            elif menu_focus_option == 2:
                                focus_on_task()
                            else:
                                print("Incorrect option!")
                                time.sleep(0.5)
                                system('cls')
                        except ValueError:
                            print("Incorrect option!")
                            time.sleep(0.5)
                            system('cls')
                elif menu_focus_option == 2:
                    print_menu()
                else:
                    print("Incorrect option!")
                    time.sleep(0.5)
                    continue


def focus_on_task():
    global rounds_elapsed, rounds_to_long_break, menu_focus_option, break_time

    start_time = time.localtime()
    work_time_secs = work_time * 60
    progress_bar = ['.'] * 20
    progress_bar_pos = 0
    progress_bar_part = work_time_secs / 20

    while True:
        now_time = time.localtime()
        time_elapsed = time.mktime(now_time) - time.mktime(start_time)
        time_diff = work_time_secs - time_elapsed
        time_diff_minutes = int(time_diff // 60)
        time_diff_secs = int(time_diff % 60)

        system('cls')
        print(f"| {task_title} |")
        print(f"| Rounds to long break: {rounds_to_long_break - rounds_elapsed} |")

        if time_diff_secs < 10:
            print(f"Time to finish: {time_diff_minutes}:0{time_diff_secs}")
        else:
            print(f"Time to finish: {time_diff_minutes}:{time_diff_secs}")

        print('[', end="")
        for char in progress_bar:
            print(char, end="")
        print(']')

        if (time_elapsed // progress_bar_part) >= progress_bar_pos and progress_bar_pos <= 19:
            progress_bar[progress_bar_pos] = u'█'
            progress_bar_pos += 1

        if progress_bar_pos < 19:
            if time_diff_secs % 2 == 0:
                progress_bar[progress_bar_pos] = u'█'
            else:
                progress_bar[progress_bar_pos] = '.'

        time.sleep(1)

        if time_diff_minutes == 0 and time_diff_secs == 0:
            rounds_elapsed += 1
            progress_bar_pos = 0

            while True:
                system('cls')
                print("Focus session is over! Enjoy your free time!")
                print("1. Break session")
                print("2. Focus session")
                print("3. Abort")
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

                try:
                    menu_focus_option = int(input("Option: "))
                except ValueError:
                    print("Incorrect option!")
                    time.sleep(0.5)
                    continue

                if menu_focus_option == 1:
                    system('cls')
                    if rounds_elapsed == rounds_to_long_break:
                        rounds_elapsed = 0
                        break_focus('long')
                    else:
                        break_focus('normal')
                elif menu_focus_option == 2:
                    if rounds_elapsed == rounds_to_long_break:
                        rounds_elapsed = 0
                    system('cls')
                    focus_on_task()
                elif menu_focus_option == 3:
                    rounds_elapsed = 0
                    print_menu()
                else:
                    print("Incorrect option!")
                    time.sleep(0.5)
                    continue


def config():
    global work_time, break_time, long_break_time, rounds_to_long_break, task_title

    while True:
        system('cls')
        print("| Work time (minutes) | " + str(work_time))
        print("| Break time (minutes) | " + str(break_time))
        print("| Long break time (minutes) | " + str(long_break_time))
        print("| Rounds before long break | " + str(rounds_to_long_break))
        print("| Task title | " + task_title + '\n\n')
        print('1. Set work time')
        print('2. Set break time')
        print('3. Set long break time')
        print('4. Set rounds before long break')
        print('5. Set task to focus on')
        print('6. Exit configuration menu')

        try:
            config_option = int(input("Option: "))
        except ValueError:
            print("Incorrect value!")
            time.sleep(0.5)
            continue

        if config_option == 1:
            system('cls')
            while True:
                try:
                    work_time = int(input("Please input work time (minutes):"))
                    if work_time <= 0:
                        print("Time has to be greater than 0!")
                        time.sleep(1)
                        system('cls')
                        continue
                    break
                except ValueError:
                    print("Incorrect value!")
                    time.sleep(1)
                    system('cls')
        elif config_option == 2:
            system('cls')
            while True:
                try:
                    break_time = int(input("Please input break time (minutes):"))
                    if break_time <= 0:
                        print("Time has to be greater than 0!")
                        time.sleep(1)
                        system('cls')
                        continue
                    break
                except ValueError:
                    print("Incorrect value!")
                    time.sleep(1)
                    system('cls')
        elif config_option == 3:
            system('cls')
            while True:
                try:
                    long_break_time = int(input("Please input long break time (minutes):"))
                    if long_break_time <= 0:
                        print("Time has to be greater than 0!")
                        time.sleep(1)
                        system('cls')
                        continue
                    break
                except ValueError:
                    print("Incorrect value!")
                    time.sleep(1)
                    system('cls')
        elif config_option == 4:
            system('cls')
            while True:
                try:
                    rounds_to_long_break = int(input("Please input amount of rounds to long break:"))
                    if rounds_to_long_break <= 0:
                        print("Amount of rounds has to be greater than 0!")
                        time.sleep(1)
                        system('cls')
                        continue
                    break
                except ValueError:
                    print("Incorrect value!")
                    time.sleep(1)
                    system('cls')
        elif config_option == 5:
            system('cls')
            task_title = input("Please input title of task:")
        elif config_option == 6:
            return 0
        else:
            print("Incorrect option!")
            time.sleep(0.5)
            continue


def print_menu():
    menu_option = 0

    while True:
        try:
            system('cls')
            print('CLI FOCUS ' + version)
            print('1. Focus')
            print('2. Configure')
            print('3. Exit')
            menu_option = int(input("Option:"))
        except ValueError:
            print("Incorrect option!")

        if menu_option == 1:
            system('cls')
            focus_on_task()
        elif menu_option == 2:
            system('cls')
            config()
        elif menu_option == 3:
            exit(-1)
        else:
            print("Incorrect option!")
            time.sleep(0.5)
            continue


print_menu()
