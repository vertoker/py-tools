import operations as op
import subprocess
import datetime
import time

if not op.is_admin():
    print("Для работы бота необходимы права администратора")
    print("Запусите программу от имени администратора\n")
    input("Нажмите Enter")
    exit(0)

# Настройки бота
nickname = "opastny_kostya"  # Никнейм
prison_lobby_collect = 2 # На каком лобби собирает игрок
account_count_start = 80 # Стартовый аккаунт
account_count_end = 140  # Конечный аккаунт
pathOpen = "C:\\Users\\VERTO\\Desktop\\VimeWorld.exe"  # Путь, где лежит файл запуска
waitBarrier = 60 # Если будет ошибка, через столько секунд перезагрузится аккаунт
money = 345
tn = datetime.datetime.now()

_collect_loot = False
_give_loot = False
_give_money = False

# Функционал
def time_now(tp):
    tn = datetime.datetime.now()

    h = tn.hour
    if h < 10:
        h = "0" + str(tn.hour)

    m = tn.minute
    if m < 10:
        m = "0" + str(tn.minute)

    s = tn.second
    if s < 10:
        s = "0" + str(tn.second)

    delta = tn - tp
    if delta.total_seconds() < 1:
        print(str(h) + ":" + str(m) + ":" + str(s))
    else:
        print(tn - tp)
    return tn

def dr_everyday(i):
    op.ChestMenu(i, 0, 1, 0.2)

def prison_lobby(count_prison):
    waitLobby = 0
    op.RightClick(0, 0, 0.5)
    op.ChestMenu(0, 2, 5, 0.5)
    if count_prison == 0:
        while op.GetColorScreen(815, 395) != (54, 198, 95):
            time.sleep(0.5)
            waitLobby = waitLobby + 1
            if waitLobby == waitBarrier * 2:
                return True
        else:
            op.ChestMenu(0, 1, 6, 3)
    elif count_prison == 1:
        while op.GetColorScreen(851, 395) != (54, 198, 95):
            time.sleep(0.5)
            waitLobby = waitLobby + 1
            if waitLobby == waitBarrier * 2:
                return True
        else:
            op.ChestMenu(1, 1, 6, 3)
    elif count_prison < 9:
        op.ChestMenu(count_prison, 1, 6, 3)
    else:
        op.ChestMenu(0, 2, 6, 5)

    if op.is_chest():
        op.Press("esc", 1)
    if _collect_loot:
        op.Press("Enter", 0.1)
        op.Write("/dr", 0.5)
        op.Press("Enter", 0.1)
        for i in range(8):
            dr_everyday(i)
    if count_prison < 9:
        if _collect_loot:
            op.Press("esc", 0.1)
        if (count_prison == prison_lobby_collect - 1) and _give_loot:
            give_loot()
        if (count_prison == prison_lobby_collect - 1) and _give_money:
            give_money()
        op.Press("Enter", 0.4)
        op.Write("/hub", 0.1)
        op.Press("Enter", 4)
    else:
        op.Press("Enter", 0.1)
    return False


def give_loot():
    print("stars and busters")
    for item in range(9):
        op.Press(str(item + 1), 0.2)
        op.Press("Enter", 0.2)
        op.Write("/auc sell 0.1 " + nickname, 0.2)
        op.Press("Enter", 0.5)
        dr_everyday(2)

def give_money():
    op.Press("Enter", 0.3)
    op.Write("/pay " + nickname + " " + str(money), 0.3)
    op.Press("Enter", 1)

def account(count, tp):
    tn = time_now(tp)
    subprocess.call(pathOpen)
    time.sleep(25 + (count == 0) * 15)
    op.Click(1270, 250, 0.5)
    op.Click(1280, 390, 1)
    op.Click(1100, 400, 0.1)
    op.Click(1100, 400, 0.1)
    op.Write(op.GetLogin(count), 0.5)
    op.Click(1100, 440, 0.1)
    op.Write(op.GetPassword(count), 0.5)
    print("Account #" + str(count))
    op.Click(960, 530, 7)
    op.Click(1300, 770, 0)
    time.sleep(45 + (count == 0) * 15)

    for count_prison in range(10):
        if prison_lobby(count_prison):
            return tn, True
    return tn, False

def main_launcher(id, tp):
    op.kill_process("VimeWorld.exe")  # закрыть vimeworld
    tp, reload = account(count + account_count_start, tn)
    if reload:
        main_launcher(id, tp)
    return tp

for count in range(account_count_end - account_count_start + 1):
    tn = main_launcher(count, tn)

op.kill_process("VimeWorld.exe")
