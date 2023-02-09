import csv
import random
import math
import sys
import copy
from datetime import datetime

global_periyod = 8
global_gun = 5
global_derslik = 5

ogretmenler = [[1, 11, "Edebiyat Öğretmeni 1"],             # 0
               [2, 12, "Edebiyat Öğretmeni 2"],             # 1
               [3, 113, "Müzik Öğretmeni"],                 # 2
               [4, 124, "Resim Öğretmeni"],                 # 3
               [5, 135, "Beden Öğretmeni"],                 # 4
               [6, 146, "Yabancı Dil Öğretmeni 1"],         # 5
               [7, 147, "Yabancı Dil Öğretmeni 2"],         # 6
               [8, 88, "Matematik Öğretmeni 1"],            # 7
               [9, 89, "Matematik Öğretmeni 2"],            # 8
               [10, 910, "Biyoloji Öğretmeni 1"],           # 9
               [11, 911, "Biyoloji Öğretmeni 2"],           # 10
               [12, 712, "Kimya Öğretmeni 1"],              # 11
               [13, 713, "Kimya Öğretmeni 2"],              # 12
               [14, 614, "Fizik Öğretmeni 1"],              # 13
               [15, 615, "Fizik Öğretmeni 2"],              # 14
               [16, 516, "Coğrafya Öğretmeni 1"],           # 15
               [17, 517, "Coğrafya Öğretmeni 2"],           # 16
               [18, 418, "Tarih Öğretmeni 1"],              # 17
               [19, 419, "Tarih Öğretmeni 2"],              # 18
               [20, 220, "Sosyoloji Öğretmeni"],            # 19
               [21, 321, "Din Kültürü Öğretmeni"],          # 20
               [22, 1022, "İstatistik Öğretmeni 1"],        # 21
               [23, 1023, "İstatistik Öğretmeni 2"]         # 22
               ]

dersler = [[1, "Edebiyat", [11, 12], [4, 4, 4, 4, 4]],           # 0
           [2, "Sosyoloji", [220], [2, 2, 2, 2, 2]],             # 1
           [3, "Din Kültürü", [321], [2, 2, 2, 2, 2]],           # 2
           [4, "Tarih", [418, 419], [4, 4, 4, 4, 4]],            # 3
           [5, "Coğrafya", [516, 517], [2, 2, 2, 2, 2]],         # 4
           [6, "Fizik", [614, 615], [4, 4, 4, 4, 4]],            # 5
           [7, "Kimya", [712, 713], [4, 4, 4, 4, 4]],            # 6
           [8, "Matematik", [88, 89], [4, 4, 4, 4, 4]],          # 7
           [9, "Biyoloji", [9, 10], [2, 2, 2, 2, 2]],            # 8
           [10, "İstatistik", [1022, 1023], [4, 4, 4, 4, 4]],    # 9
           [11, "Müzik", [113], [1, 1, 1, 1, 1]],                # 10
           [12, "Resim", [124], [2, 2, 2, 2, 2]],                # 11
           [13, "Beden", [135], [1, 1, 1, 1, 1]],                # 12
           [14, "Yabancı Dil", [146, 147], [4, 4, 4, 4, 4]]]     # 13

ders_index = {11: 0, 12: 0, 220: 1, 321: 2, 418: 3, 419: 3, 516: 4, 517: 4, 614: 5, 615: 5, 712: 6, 713: 6, 88: 7, 89: 7, 9: 8, 10: 8, 1022: 9, 1023: 9, 113: 10, 124: 11, 135: 12, 146: 13, 147: 13}


def get_ders_tanimli_saat(derslik, ogretmen):
    return dersler[ders_index[ogretmen]][3][derslik]


def get_ders_ogretmenler(ogretmen):
    return dersler[ders_index[ogretmen]][2]


def ogretmen_sec(dr_program, dr):
    secilen = 0
    for ogretmen in dr[2]:
        secilen = ogretmen
        for gun in range(global_gun):
            for periyod in range(global_periyod):
                if ogretmen == dr_program[gun][periyod]:
                    secilen = 0

    index = random.randint(0, 1)
    if len(dr[2])>1:
        secilen = dr[2][index]
    else:
        secilen = dr[2][0]
#    if secilen == 0:
#        for ogretmen in dr[2]:
#            secilen = ogretmen
#            if random.randint(0, 1) == 1:
#                break
    return secilen


def get_ders_saat(dr_program, dr):
    saat = 0
    for ogretmen in dr[2]:
        for gun in range(global_gun):
            for periyod in range(global_periyod):
                if ogretmen == dr_program[gun][periyod]:
                    saat = saat + 1
    return saat


def get_ders_saat_ogretmen(dr_program, ogretmen):
    saat = 0
    for gun in range(global_gun):
        for periyod in range(global_periyod):
            if ders_index[ogretmen] == ders_index[dr_program[gun][periyod]]:
                saat = saat + 1
    return saat


def rastgele_bos_gun_periyod_bul(dr_program):
    gg = -1
    pp = -1

    while gg == -1:
        gun = random.randint(0, 4)
        periyod = random.randint(0, 7)
        if dr_program[gun][periyod] == 0:
            gg = gun
            pp = periyod

    return gg, pp


def fill_ders_programi():
    pp = global_periyod
    gg = global_gun
    dr = global_derslik
    ders_programi = [[[0] * pp for i in range(gg)] for i in range(dr)]

    for ders in dersler:
        for derslik in range(global_derslik):
            ogretmen = ogretmen_sec(ders_programi[derslik], ders)
            dr = ders[3]
            while get_ders_saat(ders_programi[derslik], ders) < dr[derslik]:
                gun, periyod = rastgele_bos_gun_periyod_bul(ders_programi[derslik])
                ders_programi[derslik][gun][periyod] = ogretmen

    return copy.deepcopy(ders_programi)


def puanla(dr_program, derslik, gun, periyod):
    katsayi = 1
    dd = derslik
    gg = gun
    pp = periyod
    # Farklı dersliklerde aynı gün aynı dersin aynı öğretmen ile olması
    for i in range(global_derslik):
        if i != derslik:
            if dr_program[derslik][gun][periyod] == dr_program[i][gun][periyod]:
                katsayi = katsayi + (3 * 0.9)
    # Ders saati derslik için tanımlanandan farklı olması
    if get_ders_tanimli_saat(dd, dr_program[dd][gg][pp]) != get_ders_saat_ogretmen(dr_program[dd], dr_program[dd][gg][pp]):
        katsayi = katsayi + (3 * 0.9)
    # Aynı dersin farklı öğretmenlerle aynı dersliğe girmesi
    for i in range(global_gun):
        for j in range(global_periyod):
            if (ders_index[dr_program[dd][gg][pp]] == ders_index[dr_program[dd][i][j]]) & (dr_program[dd][gun][periyod] != dr_program[dd][i][j]):
                katsayi = katsayi + (3 * 0.7)
    # Aynı ders 4 saat ise 2+2 olarak günlere bölünmeli
    if get_ders_tanimli_saat(dd, dr_program[dd][gg][pp]) == 4:
        saat = 0
        for i in range(global_periyod):
            if dr_program[dd][gg][pp] == dr_program[dd][gg][i]:
                saat = saat + 1
        if saat != 2:
            katsayi = katsayi + (1 * 0.7)
    # Aynı dersin aynı günde farklı saatlerde olması
    for i in range(global_periyod):
        if i != pp:
            if (dr_program[dd][gg][i] == dr_program[dd][gg][pp]) & (i+1 != pp) & (i-1 != pp):
                katsayi = katsayi + (1 * 0.7)
    return katsayi


def toplam_program_puanla(dr_program):
    puan = 0
    for derslik in range(global_derslik):
        for gun in range(global_gun):
            for periyod in range(global_periyod):
                puan = puan + puanla(dr_program, derslik, gun, periyod)
    return puan


def ders_puan_karsilastir(dr_program):
    d = random.randint(0, global_derslik - 1)
    g = random.randint(0, global_gun - 1)
    p = random.randint(0, global_periyod - 1)

    dd = random.randint(0, global_derslik-1)
    gd = random.randint(0, global_gun-1)
    pd = random.randint(0, global_periyod-1)

    new_program = copy.deepcopy(dr_program)
    new_program[d][g][p], new_program[dd][gd][pd] = new_program[dd][gd][pd], new_program[d][g][p]

    return copy.deepcopy(new_program)


def str_ders_ogretmen(ders):
    dersstr = ""
    for dd in range(14):
        for dr in dersler[dd][2]:
            if dr == ders:
                dersstr = dersler[dd][1]
                break
    for dd in range(23):
        if ogretmenler[dd][1] == ders:
            dersstr = dersstr + "/" + ogretmenler[dd][2]
            break
    return dersstr


def programi_ciz(ders_programi):
    gunler = ["P.tesi", "Salı", "Çarş.", "Perş.", "Cuma"]
    for dr in range(global_derslik):
        ll = dr + 1
        derslikBaslik = "Derslik " + str(ll)
        print(derslikBaslik.ljust(299, "-"))
        print("%s|%s|%s|%s|%s|%s|%s|%s|%s|" % ("".ljust(10, ' '),
                                               "1.Saat".ljust(35, ' '),
                                               "2.Saat".ljust(35, ' '),
                                               "3.Saat".ljust(35, ' '),
                                               "4.Saat".ljust(35, ' '),
                                               "5.Saat".ljust(35, ' '),
                                               "6.Saat".ljust(35, ' '),
                                               "7.Saat".ljust(35, ' '),
                                               "8.Saat".ljust(35, ' ')
                                               ))
        for gg in range(global_gun):
            print("%s|%s|%s|%s|%s|%s|%s|%s|%s|" % (gunler[gg].ljust(10, ' '),
                                                                    str_ders_ogretmen(ders_programi[dr][gg][0]).ljust(35, ' '),
                                                                    str_ders_ogretmen(ders_programi[dr][gg][1]).ljust(35, ' '),
                                                                    str_ders_ogretmen(ders_programi[dr][gg][2]).ljust(35, ' '),
                                                                    str_ders_ogretmen(ders_programi[dr][gg][3]).ljust(35, ' '),
                                                                    str_ders_ogretmen(ders_programi[dr][gg][4]).ljust(35, ' '),
                                                                    str_ders_ogretmen(ders_programi[dr][gg][5]).ljust(35, ' '),
                                                                    str_ders_ogretmen(ders_programi[dr][gg][6]).ljust(35, ' '),
                                                                    str_ders_ogretmen(ders_programi[dr][gg][7]).ljust(35, ' ')
                                                                    ))


class Bee:
    def __init__(self, ders_programi):
        self.role = ''
        self.cycle = 0
        self.ders_programi = copy.deepcopy(ders_programi)
        self.fitness = 0


def initialize_hive(population):
    pp = global_periyod
    gg = global_gun
    dr = global_derslik
    ders_programi = [[[0] * pp for i in range(gg)] for i in range(dr)]
    hive = [Bee(ders_programi) for i in range(0, population)]
    return hive


def assign_roles(hive, role_percentiles):
    population = len(hive)
    onlooker_count = math.floor(population * role_percentiles[0])
    forager_count = math.floor(population * role_percentiles[1])

    for i in range(0, onlooker_count):
        hive[i].role = 'O'

    for i in range(onlooker_count, (onlooker_count + forager_count)):
        hive[i].role = 'F'
        hive[i].ders_programi = fill_ders_programi()
        hive[i].fitness = toplam_program_puanla(hive[i].ders_programi)

    return hive


def forage(bee, limit):
    new_ders_programi = ders_puan_karsilastir(bee.ders_programi)
    new_fitness = toplam_program_puanla(new_ders_programi)

    if new_fitness < bee.fitness:
        bee.ders_programi = new_ders_programi
        bee.fitness = new_fitness
        bee.cycle = 0
    else:
        bee.cycle += 1
    if bee.cycle >= limit:
        bee.role = 'S'
    return bee.fitness, bee.ders_programi


def scout(bee):
    new_ders_programi = fill_ders_programi()
    bee.ders_programi = new_ders_programi
    bee.fitness = toplam_program_puanla(new_ders_programi)
    bee.role = 'F'
    bee.cycle = 0


def dans(hive, best_fitness, forager_limit, scout_count):
    best_ders_programi = []
    results = []

    for i in range(0, len(hive)):
        if hive[i].role == 'F':
            fitness, ders_programi = forage(hive[i], forager_limit)
            if fitness < best_fitness:
                best_fitness = fitness
                best_ders_programi = list(hive[i].ders_programi)
            results.append((i, fitness))

        elif hive[i].role == 'S':
            scout(hive[i])

    results.sort(reverse = True, key=lambda tup: tup[1])
    scouts = [ tup[0] for tup in results[0:int(scout_count)] ]
    for new_scout in scouts:
        hive[new_scout].role = 'S'
    return best_fitness, best_ders_programi


def recruit(hive, best_fitness, best_ders_programi):
    for i in range(0, len(hive)):
        if hive[i].role == 'O':
            new_ders_programi = ders_puan_karsilastir(best_ders_programi)
            new_fitness = toplam_program_puanla(new_ders_programi)
            if new_fitness < best_fitness:
                best_fitness = new_fitness
                best_ders_programi = new_ders_programi
    return best_fitness, best_ders_programi


def print_details(cycle, ders_programi, fitness, bee):
    # print("Ders programı: {}".format(ders_programi))
    programi_ciz(ders_programi)
    print("CYCLE: {}".format(cycle))
    print("Fitness: {}".format(fitness))
    print("BEE: {}".format(bee))
    print("\n")


def main():
    start_datetime = datetime.now()
    cycle_time = start_datetime
    population = 20
    forager_percent = 0.5
    onlooker_percent = 0.5
    role_percent = [onlooker_percent, forager_percent]
    scout_percent = 0.2
    scout_count = math.ceil(population * scout_percent)
    forager_limit = 1000
    cycle_limit = 2500
    cycle = 1

    best_cycle=0
    best_bee=""

    best_fitness = sys.maxsize
    best_ders_programi = []
    result = ()

    hive = initialize_hive(population)
    assign_roles(hive, role_percent)

    while cycle < cycle_limit:
        dans_fitness, dans_ders_programi = dans(hive, best_fitness, forager_limit, scout_count)
        if dans_fitness < best_fitness:
            best_fitness = dans_fitness
            best_ders_programi = copy.deepcopy(dans_ders_programi)
            # print_details(cycle, best_ders_programi, best_fitness, 'F')
            best_cycle = cycle
            best_bee = "F"
            result = (cycle, best_ders_programi, best_fitness, 'F')

        recruit_fitness, recruit_ders_programi = recruit(hive, best_fitness, best_ders_programi)
        if recruit_fitness < best_fitness:
            best_fitness = recruit_fitness
            best_ders_programi = copy.deepcopy(recruit_ders_programi)
            # print_details(cycle, best_ders_programi, best_fitness, 'R')
            best_cycle = cycle
            best_bee = "R"
            result = (cycle, best_ders_programi, best_fitness, 'R')

        if cycle % 100 == 0:
            cycle_elapsed_time = datetime.now()-cycle_time
            cycle_time = datetime.now()
            print("CYCLE #: {} FITNESS #: {} ELAPSED TIME #: {}".format(cycle, best_fitness, cycle_elapsed_time))

        cycle += 1

    print(result)
    print_details(best_cycle, best_ders_programi, best_fitness, best_bee)
    stop_datetime = datetime.now()
    elapsed_datetime = stop_datetime - start_datetime

    print("Start Time    : %s" % start_datetime)
    print("Stop Time     : %s" % stop_datetime)
    print("Elapsed Time  : %s\n" % elapsed_datetime)


if __name__ == '__main__':
    for i in range(0, 100):
        main()

    # main()





