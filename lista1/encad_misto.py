Ozzy = False
Distortion = False
Tony = False
Black_sabbath = False
Bill = False
Geezer = False
Politics_lyrics = True


def factual_base():
    global Ozzy
    Ozzy = True


if __name__ == '__main__':
    factual_base()
    c = 0
    while c < 10:
        if Ozzy and Geezer:
            Bill = True

        if Ozzy and Tony:
            Distortion = True
            Politics_lyrics = True

        if Black_sabbath:
            print(f'Black_sabbath = True')
            break

        if Politics_lyrics and Distortion:
            Black_sabbath = True

        if Ozzy:
            Tony = True
            Geezer = True

    else:
        print(f'Black_sabbath = False')

