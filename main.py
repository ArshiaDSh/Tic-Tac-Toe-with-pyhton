import os
from colorama import init, Fore
import pyfiglet
import random
import time

init(autoreset=True)


def inp(msg, valid=[], meth=None, msgOut="", rel=True, all=False, invalid=[], **args):
    while True:
        inn = input(msg)
        if inn in valid or (all and inn not in invalid):
            return inn
        if rel:
            os.system("cls")
            if args:
                meth(args)
            else:
                meth()
        if msgOut:
            print(msgOut)


def table(lens, cols, colors=None):
    res = ""
    if not colors:
        colors = []
        for _ in range(len(cols)):
            colors.append(Fore.WHITE)
    for i in range(len(cols)):
        res += f"{colors[i]}{((lens[i] - len(str(cols[i]))) // 2) * ' '}{cols[i]}{((lens[i] + 1 - len(str(cols[i]))) // 2) * ' '} {Fore.RESET}"
    return res


class page:
    def __init__(self):
        os.system("cls")
        self.fetch = fetch()

    def mms(self):
        os.system("cls")
        prefix = 5 * " "
        banner = pyfiglet.figlet_format("XO", font="slant")
        sbanner = banner.split("\n")
        print(prefix + Fore.GREEN + sbanner[0])
        print(prefix + Fore.GREEN + sbanner[1])
        print(prefix + Fore.CYAN + sbanner[2])
        print(prefix + Fore.RED + sbanner[3])
        print(prefix + Fore.RED + sbanner[4])
        print("\n")
        print("1) New game")
        print("2) Users")
        print("3) Leaderboard")
        print("4) Game history")
        print("5) Setting")
        print("6) Instruction")
        print("7) About us")
        print("8) Exit")

    def main_menu(self):
        self.mms()
        pg = inp("choose a page: ", ["1", "2", "3", "4", "5", "6", "7", "8"], self.mms)
        if pg == "1":
            self.new_game()
        elif pg == "2":
            self.users()
        elif pg == "3":
            self.leaderboard()
        elif pg == "4":
            self.game_history()
        elif pg == "5":
            self.setting()
        elif pg == "6":
            self.instruction()
        elif pg == "7":
            self.about_us()
        elif pg == "8":
            os.system("cls")
            exit()

    def ngs(self):
        os.system("cls")
        print("1) With ai")
        print("2) 1v1")

    def new_game(self):
        f = fetch()
        if len(f.games()) and f.games()[-1]["time"] in ["1", "2"]:
            g = game()
        else:
            self.ngs()
            gm = inp("Choose the game mode : ", ["1", "2", "b"], self.new_game)
            if gm == "1":
                g = game({"mode": 1})
            elif gm == "2":
                g = game({"mode": 2})
            else:
                self.main_menu()

    def leaderboard(self):
        self.urs = self.fetch.users()
        self.games = self.fetch.games()
        os.system("cls")
        res = []
        sep = "-" * 65
        print(
            f"\n    {Fore.YELLOW}RANK |      NAME      |  WINS  |  LOSTS  |  TIES  |  WIN RATE(%)  \n   {sep}"
        )
        for i in range(1, len(self.urs) + 1):
            w = 0
            l = 0
            t = 0
            for g in self.games:
                if (g["winner"] == str(i) or g["looser"] == str(i)) and g[
                    "time"
                ] not in ["1", "2"]:
                    if g["res"] == "T":
                        t += 1
                    elif g["winner"] == str(i):
                        w += 1
                    else:
                        l += 1
            res.append(
                [
                    [
                        self.urs[i - 1],
                        w,
                        l,
                        t,
                        round(w / (w + l + t) * 100, 2) if w + l + t != 0 else 0,
                    ]
                ]
            )
        cs = True
        while cs:
            for i in range(1, len(res)):
                if res[i][0][1] > res[i - 1][0][1]:
                    res[i], res[i - 1] = res[i - 1], res[i]
                    break
                elif res[i][0][1] == res[i - 1][0][1]:
                    if res[i][0][4] > res[i - 1][0][4]:
                        res[i], res[i - 1] = res[i - 1], res[i]
                        break
                    elif res[i][0][4] == res[i - 1][0][4]:
                        if res[i][0][3] > res[i - 1][0][3]:
                            res[i], res[i - 1] = res[i - 1], res[i]
                            break
                        elif res[i][0][3] == res[i - 1][0][3]:
                            if res[i][0][2] > res[i][0][2]:
                                res[i], res[i - 1] = res[i - 1], res[i]
                                break
                            else:
                                res[i - 1].append(res[i][0])
                                res.pop(i)
                                break
                if i == len(res) - 1:
                    cs = False
            if len(res) <= 1:
                cs = False
                if len(res) == 0:
                    print(27 * " " + "No history")
        ranks = {}
        r = 1
        for i in res:
            if r in [1, 2, 3]:
                ranks[f"*{str(r)}*"] = i
            else:
                ranks[str(r)] = i
            r += len(i)
        for k, v in ranks.items():
            for i in v:
                if k == "*1*":
                    color = Fore.YELLOW
                elif k == "*2*":
                    color = Fore.LIGHTCYAN_EX
                elif k == "*3*":
                    color = Fore.LIGHTYELLOW_EX
                else:
                    color = Fore.WHITE
                row = table(
                    [6, 16, 8, 9, 8, 15],
                    [k] + i,
                    [
                        color,
                        Fore.LIGHTYELLOW_EX,
                        Fore.LIGHTGREEN_EX,
                        Fore.LIGHTRED_EX,
                        Fore.LIGHTBLUE_EX,
                        Fore.LIGHTMAGENTA_EX,
                    ],
                )
                print(f"   {row}")
                print(f"   {Fore.LIGHTBLACK_EX}{sep}")

        print("\n**Note that ranks is based on: 1)Wins 2)Win Rate 3)Ties 4)Games**\n")
        inp("Press any key to get back...", all=True, rel=False)
        self.main_menu()

    def ghs(self):
        self.urs = self.fetch.users()
        games = self.games
        sep = "   " + "-" * 94
        print(
            Fore.YELLOW
            + "\n      ID   |                PLAYERS                |      WINNER      |          DATE       "
        )
        print(Fore.YELLOW + sep)
        if games and games[-1]["time"] in ["1", "2"]:
            games.pop()
        for i in range(len(games)):
            g = games[i]
            try:
                if g["winner"] == "0":
                    w = "PC"
                else:
                    w = self.urs[(int(g["winner"])) - 1]
            except:
                w = g["winner"]
            try:
                if g["looser"] == "0":
                    l = "PC"
                else:
                    l = self.urs[(int(g["looser"])) - 1]
            except:
                l = g["looser"]
            t = g["time"]
            row = table(
                [8, 39, 18, len(t)],
                [
                    str(i + 1),
                    f"{w + ' vs ' + l}",
                    "Tied" if g["res"] == "T" else w,
                    t,
                ],
                [
                    Fore.LIGHTCYAN_EX,
                    Fore.LIGHTYELLOW_EX,
                    Fore.LIGHTMAGENTA_EX,
                    Fore.LIGHTGREEN_EX,
                ],
            )
            print(f"   {row}")
            print(Fore.LIGHTBLACK_EX + sep)
        if len(games) == 0:
            print(42 * " " + "No history")
        print("\n", end="")

    def game_history(self):
        self.urs = self.fetch.users()
        self.games = self.fetch.games()[::-1]
        os.system("cls")
        self.ghs()
        if len(self.games) == 0:
            inp("Press any key to get back...", all=True, rel=False)
            self.main_menu()
        else:
            x = inp(
                "choose the game id to show('s-name' to sort by name): ",
                [f"s-{i}" for i in self.urs]
                + [str(i + 1) for i in range(len(self.games))]
                + ["b"],
                self.ghs,
            )
            if x == "b":
                self.main_menu()
            elif "s-" in x:
                while True:
                    os.system("cls")
                    sgs = self.sg(self.urs.index(x[2:]) + 1)
                    if len(sgs) > 0:
                        gi = inp(
                            "choose the game id to show: ",
                            [str(i + 1) for i in range(len(sgs))] + ["b"],
                            rel=False,
                        )
                        if gi == "b":
                            self.game_history()
                            break
                        else:
                            os.system("cls")
                            self.gs(sgs[int(gi) - 1])
                            inp("press any key to get back....", all=True)
                    else:
                        inp("press any key to get back....", all=True)
                        self.game_history()
                        break
            else:
                os.system("cls")
                self.gs(self.games[int(x) - 1])
                inp("press any key to get back....", all=True)
                self.game_history()

    def sg(self, id):
        games = self.games
        sg = []
        id = str(id)
        for g in games:
            if g["winner"] == id or g["looser"] == id:
                sg.append(g)
        sep = "   " + "-" * 94
        print(
            Fore.YELLOW
            + "\n      ID   |                PLAYERS                |      WINNER      |          DATE       "
        )
        print(Fore.YELLOW + sep)
        if len(sg) == 0:
            print(" " * 42 + "No History")
        for i in range(len(sg)):
            g = sg[i]
            try:
                if g["winner"] == "0":
                    w = "PC"
                else:
                    w = self.urs[(int(g["winner"])) - 1]
            except:
                w = g["winner"]
            try:
                if g["looser"] == "0":
                    l = "PC"
                else:
                    l = self.urs[(int(g["looser"])) - 1]
            except:
                l = g["looser"]
            t = g["time"]
            if g["res"] == "T":
                color = Fore.LIGHTCYAN_EX
            elif g["winner"] == id:
                color = Fore.LIGHTGREEN_EX
            else:
                color = Fore.LIGHTRED_EX
            row = table(
                [8, 39, 18, len(t)],
                [
                    str(i + 1),
                    f"{w + ' vs ' + l}",
                    "Tied" if g["res"] == "T" else w,
                    t,
                ],
                [color] * 4,
            )
            print(f"   {row}")
            print(Fore.LIGHTBLACK_EX + sep)
        print("\n", end="")
        return sg

    def gs(self, game):
        fm = game["start"]
        if fm == "X":
            sm = "O"
        else:
            sm = "X"
        b = []
        for _ in range(3):
            row = []
            for _ in range(3):
                row.append(" ")
            b.append(row)
        vs = " | "
        hs = "---+---+---"
        if "Guest" in game["winner"]:
            fp = game["winner"]
        elif game["winner"] == "0":
            fp = "PC"
        else:
            fp = self.fetch.users(int(game["winner"]))

        if "Guest" in game["looser"]:
            sp = game["looser"]
        elif game["looser"] == "0":
            sp = "PC"
        else:
            sp = self.fetch.users(int(game["looser"]))
        print(
            f"\n    {Fore.LIGHTYELLOW_EX}{fp} vs {sp}   {'Tied' if game['res'] == 'T' else 'Winner:' + fp}    {game['time']}\n"
        )
        for i in range(len(game["seq"])):
            cell = int(game["seq"][i])
            if i % 2 == 0:
                b[-(-cell // 3 + 1)][-(-cell % 3 + 1)] = fm
            else:
                b[-(-cell // 3 + 1)][-(-cell % 3 + 1)] = sm
            rows = [0, 0, 0]
            rows[0] = f"     {b[0][0]}{vs}{b[0][1]}{vs}{b[0][2]}"
            rows[1] = f"     {b[1][0]}{vs}{b[1][1]}{vs}{b[1][2]}"
            rows[2] = f"     {b[2][0]}{vs}{b[2][1]}{vs}{b[2][2]}"
            br = rows[0]
            print(f"  {i + 1}) ")
            for i in range(1, 3):
                br += f"\n    {hs}\n{rows[i]}"
            print(br + "\n")

    def about_us(self):
        os.system(
            "start https://aftabmusic.com/%D9%85%D9%87%D8%B3%D8%AA%DB%8C-%D8%AF%D9%86%D8%A8%D8%A7%D9%84-%DA%86%D9%87-%D9%85%DB%8C-%DA%AF%D8%B1%D8%AF%DB%8C/"
        )
        self.main_menu()

    def ss(self):
        c = 0
        print("\n", end="")
        for k, v in self.sts.items():
            c += 1
            print(f"  {c}) {k} : {v}")
        print("  *) reset the game\n")

    def cs(self, item="", ops=[], reset=False):
        if reset:
            print(
                "**Please notice that you if you reset the game, all data including game histories, users, settings \n and ranking will be purged and there will be no way to recover them**\n"
            )
            asurement = inp(
                "Do you want to reset the game?:( (y/n)", ["y", "n"], rel=False
            )
            if asurement == "y":
                self.fetch.reset()
                self.main_menu()
            else:
                self.setting()
        else:
            print(f" {Fore.LIGHTYELLOW_EX}{item} : {self.sts[item]}\n")
            for i in range(len(ops)):
                print(f"  {i + 1}) {ops[i]}")
            print("\n", end="")
            inpVal = inp(
                "Choose the number the change the setting: ",
                [str(i + 1) for i in range(len(ops))] + ["b"],
                rel=False,
            )

            if inpVal != "b":
                inpVal = int(inpVal)
                self.fetch.setting({item: ops[inpVal - 1]})
            self.setting()

    def setting(self):
        self.sts = self.fetch.setting()
        os.system("cls")
        self.ss()
        inpNum = inp(
            "Choose the number to change the related setting: ",
            [str(i + 1) for i in range(len(self.sts))] + ["*", "b"],
            self.ss,
        )
        os.system("cls")
        if inpNum == "1":
            self.cs("primary_mark", ["X", "O"])
        elif inpNum == "2":
            self.cs("autosave", ["On", "Off"])
        elif inpNum == "3":
            self.cs("show_board_number", ["On", "Off"])
        elif inpNum == "4":
            self.cs("turn_duration", ["15s", "20s", "25s", "30s"])
        elif inpNum == "5":
            self.cs("undo&replay", ["On", "Off"])
        elif inpNum == "*":
            self.cs(reset=True)
        elif inpNum == "b":
            self.main_menu()

    def us(self):
        self.urs = self.fetch.users()
        self.user_c = len(self.urs)
        for i in range(1, self.user_c + 1):
            print(f"{i}) {self.urs[i - 1]}")
        print("+) New User\n")

    def users(self):
        os.system("cls")
        self.us()
        if len(self.fetch.users()) == 0:
            txt = "Enter '+' to add user: "
        else:
            txt = "Choose the user id to edit the name('+' to add a new user): "
        ui = inp(
            txt,
            [str(i + 1) for i in range(self.user_c)] + ["+", "b"],
            self.us,
        )
        if ui == "b":
            self.main_menu()
        elif ui == "+":
            self.add_user()
        else:
            self.edit_user(self.fetch.users(int(ui)))

    def edit_user(self, cuser):
        os.system("cls")
        while True:
            nuser = inp(f"Enter new name for user {cuser}:", all=True, rel=False)
            if nuser == "b":
                self.users()
                break
            if nuser not in self.urs:
                self.fetch.users(cuser, nuser)
                self.users()
                break
            else:
                print("User with this name already exit choose another name")

    def add_user(self):
        os.system("cls")
        while True:
            nuser = inp("Enter new user's name: ", rel=False, all=True)
            if nuser == "b":
                self.users()
                break
            if nuser not in self.urs:
                self.fetch.users(nuser)
                self.users()
                break
            else:
                print("User with this name already exit choose another name")

    def instruction(self):
        os.system("cls")
        print(self.fetch.instruction())
        inp("\nPress any key to get back...", all=True, rel=False)
        self.main_menu()


class fetch:
    def __init__(self):
        self.dir = "DB/"

    def users(self, name=None, new_name=None):
        if not name:
            file = open(self.dir + "users.txt", "+r")
            names = file.readlines()
            names = list(map(lambda x: x[:-1:], names))
            file.close()
            return names
        elif type(name) != int:
            names = self.users()
            if new_name:
                for i in range(len(names)):
                    if names[i] == name:
                        names[i] = new_name
                file = open(self.dir + "users.txt", "+w")
                file.write("\n".join(names) + "\n")
                file.close()
            else:
                if name not in names:
                    file = open(self.dir + "users.txt", "+a")
                    file.write(name + "\n")
                    file.close()
        else:
            file = open(self.dir + "users.txt", "+r")
            names = file.readlines()
            names = list(map(lambda x: x[:-1:], names))
            file.close()
            return names[name - 1]

    def games(self, game=None, pop=False):
        if pop:
            games = self.games()[:-1]
            file = open(self.dir + "games.txt", "+w")
            txt = ""
            for i in games:
                i = list(i.values())
                i[3] = ",".join(i[3])
                txt += f"{'|'.join(i)}\n"
            file.seek(0)
            file.write(txt)
            return
        if not game:
            games = []
            file = open(self.dir + "games.txt").read().split("\n")
            for i in file[:-1]:
                i = i.split("|")
                games.append(
                    {
                        "start": i[0],
                        "winner": i[1],
                        "looser": i[2],
                        "seq": i[3].split(","),
                        "time": i[4],
                        "res": i[5],
                    }
                )
            return games
        else:
            file = open(self.dir + "games.txt", "+a")
            game[3] = map(str, game[3])
            game[3] = ",".join(game[3])
            game[1] = str(game[1])
            game[2] = str(game[2])
            file.write("|".join(game) + "\n")
        file.close()

    def setting(self, sets={}):
        if not sets:
            file = open(self.dir + "setting.txt")
            settings = file.read().split("\n")
            settings = dict(map(lambda x: (x.split("=")[0], x.split("=")[1]), settings))
            file.close()
            return settings
        else:
            file = open(self.dir + "setting.txt", "+r")
            settings = self.setting()
            file.seek(0)
            file.truncate()
            for k, v in sets.items():
                settings[k] = v
            set_txt = ""
            for k, v in settings.items():
                set_txt += f"{k}={v}\n"
            set_txt = set_txt[:-1:]
            file.write(set_txt)
            file.close()

    def instruction(self):
        f = open(self.dir + "instruction.txt", "+r")
        return f.read()

    def reset(self):
        self.setting({"primary_mark": "X", "autosave": "On", "show_board_number": "On"})
        f = open(self.dir + "games.txt", "+w")
        f.close()
        f = open(self.dir + "users.txt", "+w")
        f.close()


class game:
    def __init__(self, args=None):
        self.fetch = fetch()
        lastg = self.fetch.games()
        self.i_board = [[(i * 3 + j + 1) for j in range(3)] for i in range(3)]
        self.board = [i[:] for i in self.i_board]
        if self.fetch.setting()["undo&replay"] == "On":
            self.ur = ["u", "r"]
        else:
            self.ur = []
        if len(lastg) > 0 and lastg[-1]["time"] in ["1", "2"]:
            lastg = lastg[-1]
            self.mode = int(lastg["time"])
            users = self.fetch.users()
            argums = list(map(int, lastg["res"].split(",")))
            if self.mode == 1:
                if lastg["winner"] != "g":
                    self.player = users[int(lastg["winner"]) - 1]
                else:
                    self.player = "g"
                self.d = argums[0]
                self.gir = argums[1]
                self.pt = argums[2]
                if len(argums) > 3:
                    self.seq = list(map(int, lastg["seq"][: int(argums[3])]))
                else:
                    self.seq = list(map(int, lastg["seq"]))
                if self.gir % 2 == 0:
                    self.pm = lastg["start"]
                elif lastg["start"] == "X":
                    self.pm = "O"
                else:
                    self.p = "X"

            else:
                if lastg["winner"] != "g":
                    self.fp = users[int(lastg["winner"]) - 1]
                else:
                    self.fp = "g"
                if lastg["looser"] != "g":
                    self.sp = users[int(lastg["winner"]) - 1]
                else:
                    self.sp = "g"

                self.spt = argums[1]
                self.fpt = argums[0]
                self.pm = lastg["start"]
                if len(argums) > 2:
                    self.seq = list(map(int, lastg["seq"][: int(argums[2])]))
                else:
                    self.seq = list(map(int, lastg["seq"]))
            if self.pm == "X":
                self.sm = "O"
            else:
                self.sm = "X"
            self.cell_count = len(self.seq)
            for i in range(len(self.seq)):
                val = self.seq[i]
                if i % 2 == 0:
                    self.board[-(-val // 3 + 1)][-(-val % 3 + 1)] = lastg["start"]
                else:
                    self.board[-(-val // 3 + 1)][-(-val % 3 + 1)] = (
                        "X" if lastg["start"] == "O" else "O"
                    )

        else:
            os.system("cls")
            self.mode = args["mode"]
            if self.mode == 1:
                self.player = inp(
                    "Enter your name (g for guest) : ",
                    all=True,
                    rel=False,
                )
                if self.player == "b":
                    p.new_game()
                    return
                if self.player != "g":
                    self.fetch.users(self.player)
                self.d = inp(
                    "Ditermin difficaulty (1 to 3): ",
                    ["1", "2", "3", "b"],
                    rel=False,
                )
                if self.d == "b":
                    p.new_game()
                    return
                self.d = int(self.d)
                self.pt = int(self.fetch.setting()["turn_duration"][:-1])
                self.gir = 0

            elif self.mode == 2:
                self.fp = inp(
                    "Enter first player's name(g for guest): ", all=True, rel=False
                )
                if self.fp == "b":
                    p.new_game()
                    return
                self.sp = inp(
                    "Enter second player's name(g for guest): ", all=True, rel=False
                )
                if self.sp == "b":
                    p.new_game()
                    return
                while self.fp == self.sp and self.fp != "g":
                    print("Players' name cannot be the same")
                    self.sp = input("Enter second player's name(g for guest): ")
                if self.fp != "g":
                    self.fetch.users(self.fp)
                if self.sp != "g":
                    self.fetch.users(self.sp)
                self.fpt = int(self.fetch.setting()["turn_duration"][:-1])
                self.spt = int(self.fetch.setting()["turn_duration"][:-1])
            self.seq = []
            self.pm = self.fetch.setting()["primary_mark"]
            if self.pm == "X":
                self.sm = "O"
            else:
                self.sm = "X"
            self.cell_count = 0
        self.start()

    def win(self, b):
        if self.mode == 1 and self.pt < 0:
            return self.sm
        if self.mode == 2 and self.fpt < 0:
            return self.sm
        if self.mode == 2 and self.spt < 0:
            return self.pm
        for i in b:
            if i[0] == i[1] and i[1] == i[2]:
                return i[0]
        for j in range(3):
            if b[0][j] == b[1][j] and b[1][j] == b[2][j]:
                return b[0][j]
        if b[0][0] == b[1][1] and b[1][1] == b[2][2]:
            return b[0][0]
        if b[0][2] == b[1][1] and b[1][1] == b[2][0]:
            return b[0][2]

        return False

    def win_process(self):
        print("\n")
        if self.fetch.games()[-1]["time"] in ["1", "2"]:
            self.fetch.games(pop=True)

        if self.win(self.board):
            tie = False
            if self.mode == 1:
                if self.player == "g":
                    user = "Guest_" + str(random.randint(1000, 9999))
                else:
                    user = self.fetch.users().index(self.player) + 1
                if self.win(self.board) == self.pm:
                    print(f"{self.player} wins!")
                    wir = user
                    lsr = 0
                else:
                    print("You lost :(")
                    lsr = user
                    wir = 0

            else:
                if self.win(self.board) == self.pm:
                    print(f"{self.fp}({self.pm}) wins!")
                    if self.fp == "g":
                        wir = "Guest_" + str(random.randint(1000, 9999))
                    else:
                        wir = self.fetch.users().index(self.fp) + 1
                    if self.sp == "g":
                        lsr = "Guest_" + str(random.randint(1000, 9999))
                    else:
                        lsr = self.fetch.users().index(self.sp) + 1
                else:
                    print(f"{self.sp}({self.sm}) wins!")
                    if self.sp == "g":
                        wir = "Guest_" + str(random.randint(1000, 9999))
                    else:
                        wir = self.fetch.users().index(self.sp) + 1
                    if self.fp == "g":
                        lsr = "Guest_" + str(random.randint(1000, 9999))
                    else:
                        lsr = self.fetch.users().index(self.fp) + 1

        else:
            if self.mode == 1:
                if self.player == "g":
                    user = "Guest_" + str(random.randint(1000, 9999))
                else:
                    user = self.fetch.users().index(self.player) + 1
                wir = user
                lsr = 0
            else:
                if self.fp == "g":
                    fuser = "Guest_" + str(random.randint(1000, 9999))
                else:
                    fuser = self.fetch.users().index(self.fp) + 1
                if self.sp == "g":
                    suser = "Guest_" + str(random.randint(1000, 9999))
                else:
                    suser = self.fetch.users().index(self.sp) + 1
                wir = fuser
                lsr = suser
            tie = True
            print("Game ties!")

        if self.seq:
            if self.fetch.setting()["autosave"] == "Off":
                sg = inp("Do you want to save the game?(y/n)", ["y", "n"], rel=False)
                if sg == "y":
                    if self.mode == 1:
                        self.fetch.games(
                            [
                                self.pm if self.gir % 2 == 0 else self.sm,
                                wir,
                                lsr,
                                self.seq,
                                time.ctime(),
                                "T" if tie else "",
                            ]
                        )
                    else:
                        self.fetch.games(
                            [
                                self.pm,
                                wir,
                                lsr,
                                self.seq,
                                time.ctime(),
                                "T" if tie else "",
                            ]
                        )

            else:
                if self.mode == 1:
                    self.fetch.games(
                        [
                            self.pm if self.gir % 2 == 0 else self.sm,
                            wir,
                            lsr,
                            self.seq,
                            time.ctime(),
                            "T" if tie else "",
                        ]
                    )
                else:
                    self.fetch.games(
                        [self.pm, wir, lsr, self.seq, time.ctime(), "T" if tie else ""]
                    )

        rg = inp(
            "Do you want to repeat the match?(y/n)",
            ["y", "n"],
            rel=False,
        )

        if rg == "y":
            if self.mode == 1:
                self.gir += 1
                self.pt = int(self.fetch.setting()["turn_duration"][:-1])
            else:
                self.fp, self.sp = self.sp, self.fp
                self.fpt = int(self.fetch.setting()["turn_duration"][:-1])
                self.spt = int(self.fetch.setting()["turn_duration"][:-1])
            self.seq = []
            self.cell_count = 0
            self.board = [i[:] for i in self.i_board]
            self.start()

        else:
            p.main_menu()

    def start(self):
        os.system("cls")
        self.show_b()
        tcount = self.cell_count
        if self.mode == 1:
            if self.player == "g":
                user = "g"
            else:
                user = self.fetch.users().index(self.player) + 1
            while True:
                if tcount % 2 == (self.gir % 2):
                    stime = int(time.time())
                    print(f"{self.pt}s left")
                    inpVal = inp(
                        f"{self.player}'s({self.pm}) turn: ",
                        [str(i) for i in range(1, 10)] + self.ur,
                        self.show_b,
                        turn=self.pm,
                    )
                    self.pt += stime - int(time.time())
                    if self.pt >= 0:
                        if inpVal in ["u", "r"]:
                            lastg = self.fetch.games()[-1]
                            if inpVal == "u":
                                if tcount > 1:
                                    tcount -= 2
                                    self.fetch.games(pop=True)
                                    if len(self.seq) - 2 > 0 or True:
                                        self.fetch.games(
                                            [
                                                self.pm
                                                if self.gir % 2 == 0
                                                else self.sm,
                                                user,
                                                0,
                                                lastg["seq"],
                                                str(self.mode),
                                                f"{self.d},{self.gir},{self.pt},{len(self.seq) - 2}",
                                            ]
                                        )
                                    for _ in range(2):
                                        lmove = int(self.seq[-1])
                                        self.board[-(-lmove // 3 + 1)][
                                            -(-lmove % 3 + 1)
                                        ] = lmove
                                        self.seq.pop()

                            else:
                                if len(self.seq) < len(lastg["seq"]):
                                    tcount += 2
                                    ppos = int(lastg["seq"][len(self.seq)])
                                    spos = int(lastg["seq"][len(self.seq) + 1])
                                    self.board[-(-ppos // 3 + 1)][-(-ppos % 3 + 1)] = (
                                        self.pm
                                    )
                                    self.board[-(-spos // 3 + 1)][-(-spos % 3 + 1)] = (
                                        self.sm
                                    )
                                    self.seq.append(ppos)
                                    self.seq.append(spos)
                                    self.fetch.games(pop=True)
                                    self.fetch.games(
                                        [
                                            self.pm if self.gir % 2 == 0 else self.sm,
                                            user,
                                            0,
                                            lastg["seq"],
                                            str(self.mode),
                                            f"{self.d},{self.gir},{self.pt},{len(self.seq)}",
                                        ]
                                    )

                        else:
                            inpVal = int(inpVal)
                            i = -(-inpVal // 3 + 1)
                            j = -(-inpVal % 3 + 1)
                            if self.board[i][j] in range(1, 10):
                                self.board[i][j] = self.pm
                                self.seq.append(inpVal)
                                if tcount > 0:
                                    self.fetch.games(pop=True)
                                self.fetch.games(
                                    [
                                        self.pm if self.gir % 2 == 0 else self.sm,
                                        user,
                                        0,
                                        self.seq,
                                        str(self.mode),
                                        f"{self.d},{self.gir},{self.pt}",
                                    ]
                                )
                                tcount += 1
                else:
                    if self.d == 1:
                        point = self.random_ai(self.board)
                    elif self.d == 2:
                        point = self.medium_ai(self.board)[0]
                    else:
                        point = self.mcts_ai()
                    self.seq.append(point[0] * 3 + point[1] + 1)
                    if tcount > 0:
                        self.fetch.games(pop=True)
                    self.fetch.games(
                        [
                            self.pm if self.gir % 2 == 0 else self.sm,
                            user,
                            0,
                            self.seq,
                            str(self.mode),
                            f"{self.d},{self.gir},{self.pt}",
                        ]
                    )
                    tcount += 1
                os.system("cls")
                self.show_b()
                if self.win(self.board) or tcount == 9:
                    self.win_process()
                    break

        else:
            if self.fp == "g":
                fuser = "g"
            else:
                fuser = self.fetch.users().index(self.fp) + 1
            if self.sp == "g":
                suser = "g"
            else:
                suser = self.fetch.users().index(self.sp) + 1
            while True:
                if tcount % 2 == 0:
                    turn = self.fp
                    mark = self.pm
                    print(f"{self.fpt}s left")
                else:
                    turn = self.sp
                    mark = self.sm
                    print(f"{self.spt}s left")
                stime = int(time.time())
                inpVal = inp(
                    f"{turn}'s({mark}) turn: ",
                    [str(i) for i in range(1, 10)] + self.ur,
                    self.show_b,
                    turn=self.pm if tcount % 2 == 0 else self.sm,
                )
                if tcount % 2 == 0:
                    self.fpt += stime - int(time.time())
                else:
                    self.spt += stime - int(time.time())
                if self.fpt > 0 and self.spt > 0:
                    if inpVal in ["u", "r"]:
                        lastg = self.fetch.games()[-1]
                        if inpVal == "u":
                            if tcount > 0:
                                tcount -= 1
                                lmove = int(self.seq[-1])
                                self.board[-(-lmove // 3 + 1)][-(-lmove % 3 + 1)] = (
                                    lmove
                                )
                                self.fetch.games(pop=True)
                                if self.seq or True:
                                    self.fetch.games(
                                        [
                                            self.pm,
                                            fuser,
                                            suser,
                                            lastg["seq"],
                                            str(self.mode),
                                            f"{self.fpt},{self.spt},{len(self.seq) - 1}",
                                        ]
                                    )
                                self.seq.pop()

                        else:
                            if len(self.seq) < len(lastg["seq"]):
                                tcount += 1
                                pos = int(lastg["seq"][len(self.seq)])
                                if len(self.seq) % 2 == 0:
                                    self.board[-(-pos // 3 + 1)][-(-pos % 3 + 1)] = (
                                        self.pm
                                    )
                                else:
                                    self.board[-(-pos // 3 + 1)][-(-pos % 3 + 1)] = (
                                        self.sm
                                    )
                                self.seq.append(pos)
                                self.fetch.games(pop=True)
                                self.fetch.games(
                                    [
                                        self.pm,
                                        fuser,
                                        suser,
                                        lastg["seq"],
                                        str(self.mode),
                                        f"{self.fpt},{self.spt},{len(self.seq)}",
                                    ]
                                )

                    else:
                        inpVal = int(inpVal)
                        i = -(-inpVal // 3 + 1)
                        j = -(-inpVal % 3 + 1)
                        if self.board[i][j] != self.pm and self.board[i][j] != self.sm:
                            self.board[i][j] = mark
                            self.seq.append(inpVal)
                            if tcount > 0:
                                self.fetch.games(pop=True)
                            self.fetch.games(
                                [
                                    self.pm,
                                    fuser,
                                    suser,
                                    self.seq,
                                    str(self.mode),
                                    f"{self.fpt},{self.spt}",
                                ]
                            )
                            tcount += 1
                os.system("cls")
                self.show_b()
                if self.win(self.board) or tcount == 9:
                    self.win_process()
                    break

    def show_b(self, timer={}):
        vs = " | "
        hs = "---+---+---"
        rows = [0, 0, 0]
        if self.fetch.setting()["show_board_number"] == "On":
            tb = [
                [
                    f"{Fore.LIGHTBLACK_EX}{c}{Fore.RESET}"
                    if c in range(1, 10)
                    else f"{Fore.WHITE}{c}{Fore.RESET}"
                    for c in r
                ]
                for r in self.board
            ]
        else:
            tb = [[" " if j in range(1, 10) else j for j in i] for i in self.board]
        rows[0] = f" {tb[0][0]}{vs}{tb[0][1]}{vs}{tb[0][2]}"
        rows[1] = f" {tb[1][0]}{vs}{tb[1][1]}{vs}{tb[1][2]}"
        rows[2] = f" {tb[2][0]}{vs}{tb[2][1]}{vs}{tb[2][2]}"
        b = rows[0]
        for i in range(1, 3):
            b += f"\n{hs}\n{rows[i]}"
        print(b)
        if timer:
            if timer["turn"] == self.pm:
                if self.mode == 1:
                    print(f"{self.pt}s left")
                else:
                    print(f"{self.fpt}s left")
            else:
                print(f"{self.spt}s left")

    def random_ai(self, board, s=None):
        if not s:
            s = self.sm
        ri = random.randint(0, 2)
        rj = random.randint(0, 2)
        while self.board[ri][rj] not in range(1, 10):
            ri = random.randint(0, 2)
            rj = random.randint(0, 2)
        board[ri][rj] = s
        return [ri, rj]

    def medium_ai(self, board, s=None, o=None):
        if not o:
            o = self.pm
        if not s:
            s = self.sm
        b = [i[:] for i in board]
        for i in range(3):
            for j in range(3):
                if b[i][j] in range(1, 10):
                    b[i][j] = s
                    if self.win(b) == s:
                        board[i][j] = s
                        return [i, j], True
                    b = [i[:] for i in board]
        for i in range(3):
            for j in range(3):
                if b[i][j] in range(1, 10):
                    b[i][j] = o
                    if self.win(b) == o:
                        board[i][j] = s
                        return [i, j], True
                    b = [i[:] for i in board]
        return self.random_ai(board, s), False

    def mcts_ai(self):
        bo = [i[:] for i in self.board]
        if self.medium_ai(bo)[1] == True:
            return self.medium_ai(self.board)[0]
        else:
            paths = []
            chances = [[0, 0, 0] for i in range(1, 10)]
            cbp = [[0, 0, i - 1] for i in range(1, 10)]

            for _ in range(400):
                path = []
                bo = [i[:] for i in self.board]
                tcount = 0
                for i in self.board:
                    for j in i:
                        if j not in range(1, 10):
                            tcount += 1
                while True:
                    if tcount % 2 == (self.gir % 2):
                        point = self.medium_ai(bo, self.pm, self.sm)[0]
                    else:
                        point = self.medium_ai(bo)[0]
                    tcount += 1
                    path.append(point[0] * 3 + point[1] + 1)
                    if self.win(bo):
                        if path not in paths:
                            if self.win(bo) == self.sm:
                                chances[path[0] - 1][0] += 1
                            else:
                                chances[path[0] - 1][1] += 1
                            paths.append(path)
                        break
                    if tcount >= 9:
                        if path not in paths:
                            paths.append(path)
                        break

            for i in range(0, len(chances)):
                w = chances[i][0]
                l = chances[i][1]
                n = 0
                for j in paths:
                    if j[0] == i + 1:
                        n += 1
                chances[i][2] = n
                if n != 0:
                    cbp[i][0] = w / n * 100
                    cbp[i][1] = l / n * 100
                else:
                    cbp[i][0] = 0
                    cbp[i][1] = 0
            scbp = list(cbp)
            sc = True
            while sc and len(scbp) > 1:
                for i in range(1, len(scbp)):
                    if scbp[i][0] > scbp[i - 1][0]:
                        scbp[i], scbp[i - 1] = scbp[i - 1], scbp[i]
                        break
                    if scbp[i][0] == scbp[i - 1][0]:
                        if (
                            scbp[i][1] < scbp[i - 1][1] and chances[scbp[i][2]][2] != 0
                        ) or (
                            chances[scbp[i - 1][2]][2] == 0
                            and chances[scbp[i - 1][2]] != chances[scbp[i][2]]
                        ):
                            scbp[i], scbp[i - 1] = scbp[i - 1], scbp[i]
                            break
                    if i == len(scbp) - 1:
                        sc = False
            selected = scbp[0][2] + 1
            self.board[-(-selected // 3 + 1)][-(-selected % 3 + 1)] = self.sm
            return [-(-selected // 3 + 1), -(-selected % 3 + 1) + 3]


p = page()
p.main_menu()
