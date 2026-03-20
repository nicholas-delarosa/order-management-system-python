def title(title_text):
    """
    Function: title

    Parameters:

    - title_text:
    Text that will be displayed as a centered title.

    Description:
    This function formats and prints a given text as a centered title,
    usually decorated with characters (such as dashes) for better visual presentation.
    """
    # Centers the title with dashes on the sides
    if len(title_text) % 2 == 0:
        dash_count = (58 - len(title_text)) // 2
        print("\033[34m" + "-"*dash_count + " " + title_text + " " + "-"*dash_count + "\033[0m")
    else:
        dash_count = ((58 - 1) - len(title_text) + 1) // 2
        print("\n\033[34m" + "-"*dash_count + " " + title_text + " -" + "-"*dash_count + "\033[0m")


def confirm_exit(message="Press (n) to finish and any key to continue: "):
    """
    Function: confirm_exit

    Parameters:

    - message:
    Text message displayed to the user to decide whether to continue
    or exit a loop. By default, it prompts the user to press (n) to finish
    or any other key to continue.

    Description:
    This function displays a confirmation message that allows the user
    to either continue or terminate a loop (e.g., a while loop) based
    on their input.
    """

    user_option = input(f"\n\033[31m >> \033[0m{message}").strip().lower()
        
    if user_option == "n":
        return True     


def iterate_list(collection):
    """
    Function: iterate_list

    Parameters:

    - collection:
    Represents the data structure to iterate over, such as a dictionary
    or tuple. The elements of this collection will be displayed.

    Description:
    This function iterates through the given collection and displays
    its elements as a numbered list for better readability and organization.
    """

    title("List Categories")
    for index, category in enumerate(collection):
        print(f"{index + 1}. {category}")
