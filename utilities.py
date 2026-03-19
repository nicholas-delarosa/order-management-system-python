def title(title_text):
    # Centers the title with dashes on the sides
    if len(title_text) % 2 == 0:
        dash_count = (58 - len(title_text)) // 2
        print("\033[34m" + "-"*dash_count + " " + title_text + " " + "-"*dash_count + "\033[0m")
    else:
        dash_count = ((58 - 1) - len(title_text) + 1) // 2
        print("\n\033[34m" + "-"*dash_count + " " + title_text + " -" + "-"*dash_count + "\033[0m")


def confirm_exit(message="Press (n) to finish and any key to continue: "):

    user_option = input(f"\n\033[31m >> \033[0m{message}").strip().lower()
        
    if user_option == "n":
        return True     


def iterate_list(collection):

    title("List Categories")
    for index, category in enumerate(collection):
        print(f"{index + 1}. {category}")
