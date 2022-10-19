""" User input module """
from app import create_pdf


def user_input():
    ask = input("Do u want to know weather of another city ? [Y/N] : ").lower()
    while True:
        if ask in ["yes", "y"]:
            break
        elif ask in ["no", "n"]:
            create_pdf()
            break
        else:
            print("Enter Yes/No ...")
            break
