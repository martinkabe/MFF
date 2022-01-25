def reverse(text: str):
    if len(text) != 0:
        print(text[-1], end="")
        reverse(text[:-1])

reverse("hello")