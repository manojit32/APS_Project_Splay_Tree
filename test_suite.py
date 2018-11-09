import bst
import splay
import random
import time

NUM_ROUNDS = 5
maxl=[]
avg_uni_bl=[]
avg_uni_sl=[]
avg_very_uneven_bl=[]
avg_very_uneven_sl=[]
avg_pretty_uneven_b10l=[]
avg_pretty_uneven_s10l=[]
avg_pretty_uneven_b4l=[]
avg_pretty_uneven_s4l=[]
avg_del_bl=[]
avg_del_sl=[]
avg_uni_b = 0
avg_pretty_uneven_b4 = 0
avg_pretty_uneven_b10 = 0
avg_very_uneven_b = 0
avg_inter_b = 0
avg_del_b = 0



avg_uni_s = 0
avg_pretty_uneven_s4 = 0
avg_pretty_uneven_s10 = 0
avg_very_uneven_s = 0
avg_inter_s = 0
avg_del_s = 0
# maxl=[10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
# avg_uni_bl=[0.06628730000000002, 0.15709480000000048, 0.2638007999999985, 0.3663744000000008, 0.5276966000000016, 0.6011109000000061, 0.738719100000003, 0.812878500000005, 0.9219297000000097, 1.0662428999999976]
# avg_uni_sl=[0.34743860000000004, 0.7673152000000003, 1.241260199999998, 1.727472300000001, 2.2974024999999982, 2.7329159999999915, 3.315187199999997, 3.68749719999999, 4.194082900000012, 4.708675299999993]
# avg_very_uneven_bl=[0.05416569999999967, 0.12725960000000072, 0.2284597000000012, 0.2682642000000001, 0.3908008000000024, 0.460667600000005, 0.5178116000000103, 0.6506406999999911, 0.6553414000000203, 0.8186458999999559]
# avg_very_uneven_sl=[0.007245099999999849, 0.014444600000000918, 0.021717700000001373, 0.028981199999992668, 0.03895760000000337, 0.04471820000000548,0.05075709999998708, 0.057063899999985776, 0.06702710000001844, 0.07263199999997597]
# avg_pretty_uneven_b10l=[0.05801960000000004, 0.14175739999999964, 0.2105470000000004, 0.2499303999999995, 0.37789139999999577, 0.4167005000000046, 0.5301683999999967, 0.6233391999999981, 0.6971893000000022, 0.7677791000000184]
# avg_pretty_uneven_s10l=[0.054838699999999886, 0.10847980000000028, 0.16845739999999906, 0.21959399999999932, 0.297357199999999, 0.3397685999999965, 0.39043740000000754, 0.43830590000000597, 0.4969690999999898, 0.5452351999999678]
# avg_pretty_uneven_b4l=[0.06245550000000022, 0.11008619999999958, 0.1910279999999993, 0.2661592000000027, 0.35213700000000187, 0.43749300000000063, 0.5458380999999974, 0.588740799999988, 0.7411646999999562, 0.7680398000000082]
# avg_pretty_uneven_s4l=[0.03531849999999988, 0.0664447000000008, 0.10216580000000164, 0.1351124999999996, 0.18388740000000894, 0.20690679999999873, 0.2422277000000065, 0.2672821999999712, 0.3014548999999874, 0.3332441000000017]
# avg_del_bl=[0.008523499999999884, 0.0095926999999989, 0.011023300000000801, 0.011258899999999983, 0.01264179999999726, 0.013351699999998346, 0.012192100000004303, 0.01225709999999367, 0.012887399999988247, 0.013613999999972749]
# avg_del_sl=[0.009476400000000051, 0.010717599999999194, 0.012712399999997358, 0.012373800000000301, 0.013895500000003835, 0.015388300000003597, 0.013821999999993295, 0.013813400000009324, 0.01383530000000519, 0.014984100000003765]

MAX = 10000
while(MAX<100001):

    def gen_accesses(n):
        accesses = []
        for i in range(n):
            accesses.append(random.randint(0, MAX))
        return accesses

    def insertions(data, tree):
        for datum in data:
            tree.insert(datum)

    def accesses(accs, tree):
        for a in accs:
            tree.search(a)

    def deletions(ds, tree):
        for d in ds:
            tree.remove(d)

    avg_uni_b = 0
    avg_pretty_uneven_b4 = 0
    avg_pretty_uneven_b10 = 0
    avg_very_uneven_b = 0
    avg_inter_b = 0
    avg_del_b = 0



    avg_uni_s = 0
    avg_pretty_uneven_s4 = 0
    avg_pretty_uneven_s10 = 0
    avg_very_uneven_s = 0
    avg_inter_s = 0
    avg_del_s = 0

    for i in range(NUM_ROUNDS):
        data = random.sample(range(MAX), MAX)
        dels = random.sample(data, 1000)
        even_accesses = random.sample(data, MAX)
        very_uneven_accesses = []
        element = data[random.randint(0, MAX)]
        for i in range(MAX):
            very_uneven_accesses.append(element)

        pretty_uneven_accesses4 = []
        base = random.randint(0, MAX - 4)
        for i in range(MAX):
            pretty_uneven_accesses4.append(random.randint(base, base + 4))

        pretty_uneven_accesses10 = []
        base = random.randint(0, MAX - 10)
        for i in range(MAX):
            pretty_uneven_accesses10.append(random.randint(base, base + 10))

        b = bst.BST()
        s = splay.Splay()
        insertions(data, b)
        insertions(data, s)

        # uniform accesses
        start = time.process_time()
        accesses(even_accesses, b)
        end = time.process_time()
        avg_uni_b += end - start


        start = time.process_time()
        accesses(even_accesses, s)
        end = time.process_time()
        avg_uni_s += end - start

        # nonuniform accesses
        start = time.process_time()
        accesses(pretty_uneven_accesses4, b)
        end = time.process_time()
        avg_pretty_uneven_b4 += end - start

        

        start = time.process_time()
        accesses(pretty_uneven_accesses4, s)
        end = time.process_time()
        avg_pretty_uneven_s4 += end - start

        start = time.process_time()
        accesses(pretty_uneven_accesses10, b)
        end = time.process_time()
        avg_pretty_uneven_b10 += end - start

        

        start = time.process_time()
        accesses(pretty_uneven_accesses10, s)
        end = time.process_time()
        avg_pretty_uneven_s10 += end - start

        start = time.process_time()
        accesses(very_uneven_accesses, b)
        end = time.process_time()
        avg_very_uneven_b += end - start

        

        start = time.process_time()
        accesses(very_uneven_accesses, s)
        end = time.process_time()
        avg_very_uneven_s += end - start

        # test cases for deletion
        start = time.process_time()
        deletions(dels, b)
        end = time.process_time()
        avg_del_b += end - start



        start = time.process_time()
        deletions(dels, s)
        end = time.process_time()
        avg_del_s += end - start

    # print("<<<<<<<< Uniform Access Results (in seconds) >>>>>>>>")
    # print("BST: ", avg_uni_b / NUM_ROUNDS)
    avg_uni_bl.append(avg_uni_b / NUM_ROUNDS)

    # print("Splay: ", avg_uni_s / NUM_ROUNDS)
    avg_uni_sl.append(avg_uni_s / NUM_ROUNDS)

    # print("<<<<<<<< Single Element Queried Repeatedly Results (in seconds) >>>>>>>>")
    # print("BST: ", avg_very_uneven_b / NUM_ROUNDS)
    avg_very_uneven_bl.append(avg_very_uneven_b / NUM_ROUNDS)

    # print("Splay: ", avg_very_uneven_s / NUM_ROUNDS)
    avg_very_uneven_sl.append(avg_very_uneven_s / NUM_ROUNDS)

    # print("<<<<<<<< Same 4 Elements Queried Randomly (in seconds) >>>>>>>>")
    # print("BST: ", avg_pretty_uneven_b4 / NUM_ROUNDS)
    avg_pretty_uneven_b4l.append(avg_pretty_uneven_b4 / NUM_ROUNDS)
    # print("Splay: ", avg_pretty_uneven_s4 / NUM_ROUNDS)
    avg_pretty_uneven_s4l.append(avg_pretty_uneven_s4 / NUM_ROUNDS)

    # print("<<<<<<<< Same 10 Elements Queried Randomly (in seconds) >>>>>>>>")
    # print("BST: ", avg_pretty_uneven_b10 / NUM_ROUNDS)
    avg_pretty_uneven_b10l.append(avg_pretty_uneven_b10 / NUM_ROUNDS)

    # print("Splay: ", avg_pretty_uneven_s10 / NUM_ROUNDS)
    avg_pretty_uneven_s10l.append(avg_pretty_uneven_s10 / NUM_ROUNDS)
    # print("<<<<<<<< Deleting 1000 Elements (in seconds) >>>>>>>>")
    # print("BST: ", avg_del_b / NUM_ROUNDS)
    avg_del_bl.append(avg_del_b / NUM_ROUNDS)
    # print("Splay: ", avg_del_s / NUM_ROUNDS)
    avg_del_sl.append(avg_del_s / NUM_ROUNDS)
    print("\n")
    maxl.append(MAX)
    MAX=MAX+10000

import matplotlib.pyplot as plt 
i=0
print(maxl) 
print(avg_uni_bl) 
print(avg_uni_sl) 
print(avg_very_uneven_bl) 
print(avg_very_uneven_sl) 
print(avg_pretty_uneven_b10l) 
print(avg_pretty_uneven_s10l) 
print(avg_pretty_uneven_b4l) 
print(avg_pretty_uneven_s4l) 
print(avg_del_bl) 
print(avg_del_sl)
def avg_del1():
    plt.plot(maxl,avg_del_bl,'o-',label='BST')
    plt.plot(maxl,avg_del_sl,'x-',label='Splay')
    plt.title("Deletion")
    plt.legend()
    plt.show()
def avg_pretty_uneven101():
    plt.plot(maxl,avg_pretty_uneven_b10l,'o-',label='BST')
    plt.plot(maxl,avg_pretty_uneven_s10l,'x-',label='Splay')
    plt.title("10 elements")
    plt.legend()
    plt.show()
def avg_pretty_uneven4l():
    plt.plot(maxl,avg_pretty_uneven_b4l,'o-',label='BST')
    plt.plot(maxl,avg_pretty_uneven_s4l,'x-',label='Splay')
    plt.title("4 elements")
    plt.legend()
    plt.show()
def avg_pretty_uneven1():
    plt.plot(maxl,avg_very_uneven_bl,'o-',label='BST')
    plt.plot(maxl,avg_very_uneven_sl,'x-',label='Splay')
    plt.title("single element")
    plt.legend()
    plt.show()
def avg_uni1():
    plt.plot(maxl,avg_uni_bl,'o-',label='BST')
    plt.plot(maxl,avg_uni_sl,'x-',label='Splay')
    plt.title("Uniform Access")
    plt.legend()
    plt.show()
