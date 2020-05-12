import numpy as np
import matplotlib.pyplot as plt

m = 3
p = 3
U1 = 220
R1 = 2.533
R2 = 1.877
C1 = 1.0034
X1 = 2.205
X2 = 2.980
f = 50
pi = 3.1415
n1 = 1500
S_ = np.arange(-2.0, 2.0, 0.01)
N_ = np.arange(-2000, 4000, 50)

M_mass_1 = []
S_mass_1 = []

M_mass_2 = []
S_mass_2 = []
N_mass_2 = []

P_mass_3 = []
N_mass_3 = []
M_mass_3 = []

def point_1(plt, S, label):
    M = (m*p*U1*U1*R2 / S) / (2*pi*f* ((R1 + C1 * R2 / S)**2 + (X1 + C1 * X2)**2))
    plt.plot([0, S, S],[M, M, 0], label=label)
    plt.legend()

def point_2(plt, n2, label):
    S = 1 - n2/n1
    M = (m*p*U1*U1*R2 / S) / (2*pi*f* ((R1 + C1 * R2 / S)**2 + (X1 + C1 * X2)**2))
    plt.plot([0, M, M],[n2, n2, 0], label=label)
    plt.legend()

def graf_1(plt):
    for S in S_:
        S = round(S, 2)
        if S != 0.0:
            M = (m*p*U1*U1*R2 / S) / (2*pi*f* ((R1 + C1 * R2 / S)**2 + (X1 + C1 * X2)**2))
            M = round(M, 2)
            S_mass_1.append(S)
            M_mass_1.append(M)

    plt.subplot(2, 2, 2)
    plt.plot(S_mass_1, M_mass_1)
    plt.vlines(0, -250, 100)
    plt.hlines(0, -2, 2)
    point_1(plt, 0.36, 'Кр')
    point_1(plt, 0.047, 'Н')
    plt.ylabel('Момент M')
    plt.xlabel('Скольжение S')
    plt.xlim(-2,2)
    plt.ylim(-250, 100)
    plt.minorticks_on()
    plt.grid(which='minor', color = 'k', linestyle = ':')
    plt.grid(which='major', color = 'k', linestyle = ':')
    # plt.savefig('2')

def graf_2(plt):
    for n2 in N_:
        n2 = round(n2, 2)
        S = 1 - n2/n1
        S = round(S, 2)
        if S != 0.0:
            M = (m*p*U1*U1*R2 / S) / (2*pi*f* ((R1 + C1 * R2 / S)**2 + (X1 + C1 * X2)**2))
            M = round(M, 1)
            N_mass_2.append(n2)
            M_mass_2.append(M)

    plt.subplot(2, 2, 1)
    plt.plot(M_mass_2, N_mass_2)
    plt.vlines(0, -2000, 3950)
    plt.hlines(0, -250, 100)
    point_2(plt, 960, 'Кр')
    point_2(plt, 1431, 'Н')
    plt.ylabel('Обороты N')
    plt.xlabel('Момент M')
    plt.ylim(-2000,3900)
    plt.xlim(-250, 100)
    plt.minorticks_on()
    plt.grid(which='minor', color = 'k', linestyle = ':')
    plt.grid(which='major', color = 'k', linestyle = ':')
    # plt.savefig('1')


def graf_3(plt):
    for S in S_:
        S = round(S, 2)
        if S != 0.00:
            N = n1 * (1 - S)
            N = round(N, 2)
            M = (m*p*U1*U1*R2 / S) / (2*pi*f* ((R1 + C1 * R2 / S)**2 + (X1 + C1 * X2)**2))
            M = round(M, 2)
            P = M * 2 * pi * N / 60
            P = round(P, 2)
            N_mass_3.append(N)
            M_mass_3.append(M)
            P_mass_3.append(P)
    
    plt.subplot(2, 2, 4)
    plt.plot(P_mass_3, M_mass_3)
    plt.xlabel('Мощность на валу P')
    plt.ylabel('Момент на валу M')
    plt.xlim(0, 10000)
    plt.ylim(0, 85)
    plt.minorticks_on()
    plt.grid(which='minor', color = 'k', linestyle = ':')
    plt.grid(which='major', color = 'k', linestyle = ':')
    # plt.savefig('4')

def graf_4(plt):
    plt.subplot(2, 2, 3)
    plt.plot(P_mass_3, N_mass_3)
    plt.xlabel('Мощность на валу P')
    plt.ylabel('Обороты на валу N')
    plt.xlim(0, 10000)
    plt.ylim(0, 1500)
    plt.minorticks_on()
    plt.grid(which='minor', color = 'k', linestyle = ':')
    plt.grid(which='major', color = 'k', linestyle = ':')
    # plt.savefig('3')

graf_1(plt)
graf_2(plt)
graf_3(plt)
graf_4(plt)
plt.show()