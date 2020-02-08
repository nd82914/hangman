def hangman(word):
        wrong=0
        stages=["",
                "___________           ",
                "|          |          ",
                "|          |          ",
                "|          o          ",
                "|         (|)         ",
                "|         ( )         ",
                "|____________________ ",
                ]
        rletters = list(word)
        board=["_"]*len(word)
        win=False
        print("ハングマンゲーム！")
        while wrong < len(stages)-1:
            print(board)
            msg="１文字を予想してね:"
            char =input(msg)
            if char in rletters:
                cind=rletters.index(char)
                board[cind]=char
                rletters[cind]="$"
                print("gotcha!!!")
            else:
                wrong+=1
                print("\n".join(stages[0:wrong+1]))
            if "_" not in board:
                print("EXCELLENT!!!")
                print(" ".join(board))
                win=True
                break
        if not win:
            print("You're DEAD")
            print("Anser:{}".format(word))
                
            

hangman("difficult")
#print(board)
