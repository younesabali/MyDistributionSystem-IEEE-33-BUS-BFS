
import numpy as np


P = np.zeros(shape=(33, 1), dtype=float)
Q = np.zeros(shape=(33, 1), dtype=float)
Z = np.zeros(shape=(33, 33), dtype=complex)
V = np.ones(shape=(33, 1), dtype=complex)
W = np.ones(shape=(33, 1), dtype=complex)
SL = np.zeros(shape=(33, 1), dtype=complex)
Sloss = np.zeros(shape=(33, 1), dtype=complex)
Sinj = np.zeros(shape=(33, 1), dtype=complex)
Ploss = np.zeros(shape=(33, 1), dtype=complex)
Qloss = np.zeros(shape=(33, 1), dtype=complex)
Vslack = np.ones(shape=(33, 1), dtype=complex)
Ibus = np.zeros(shape=(33, 1), dtype=complex)
Ibranche = np.zeros(shape=(33, 1), dtype=complex)
Ibranche1 =  np.zeros(shape=(33, 1), dtype=float)
AT = np.zeros(shape=(33, 33), dtype=complex)
DV = np.zeros(shape=(33, 1), dtype=float)
Ploss_S = np.zeros(shape=(10, 1), dtype=float)
Qloss_S = np.zeros(shape=(10, 1), dtype=float)
V_S = np.zeros(shape=(10, 1), dtype=complex)

y=np.array([[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0], [0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]], dtype=int)

matrice_scenarios=np.array([[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                            ])


def generate_scenarios(n):
    scenarios = []
    for i in range(2**n):
        binary_str = format(i, f'0{n}b')
        scenario = [int(bit) for bit in binary_str]
        scenarios.append(scenario)
    return scenarios

n_interrupteurs = 16
matrice_scenarios = generate_scenarios(n_interrupteurs)
nombre_scenarios = len(matrice_scenarios)
Ploss_S = np.zeros(shape=(nombre_scenarios, 1), dtype=float)
Qloss_S = np.zeros(shape=(nombre_scenarios, 1), dtype=float)
V_S = np.zeros(shape=(nombre_scenarios, 1), dtype=complex)
# Affichage de la matrice des scénarios
s=0
for scenario in matrice_scenarios:
    X=y.copy()
    #interepteur K2
    X[1][2]=scenario[0]
    #interepteur K3
    X[2][3]=scenario[1]
    #interepteur K5
    X[4][5]=scenario[2]
    #interepteur K7
    X[6][7]=scenario[3]
    #interepteur K8
    X[7][8]=scenario[4]
    #interepteur K11
    X[10][11]=scenario[5]
    #interepteur K14
    X[13][14]=scenario[6]
    #interepteur K16
    X[15][16]=scenario[7]
    #interepteur K20
    X[19][20]=scenario[8]
    #interepteur K28
    X[27][28]=scenario[9]
    #interepteur K32
    X[31][32]=scenario[10]
    #interepteur K33
    X[20][7]=scenario[11]
    #interepteur K34
    X[8][15]=scenario[12]
    #interepteur K35
    X[21][10]=scenario[13]
    #interepteur K36
    X[32][17]=scenario[14]
    #interepteur K37
    X[24][28]=scenario[15]
 
    Sb = 100
    Vb = 12.66
    Zb = (Vb ** 2) * 1000 / Sb

    # Pet Q initiale
    P0 = np.array([[0], [100], [90], [120], [60], [60], [200], [200], [60], [60], [45], [60], [60], [60], [120], [60], [60], [60], [80], [90], [90], [90], [90], [420], [420], [60], [60], [60], [120], [200], [150], [210], [60]], dtype=float)
    Q0 = np.array([[0], [60], [40], [80], [30], [20], [199], [100], [20], [20], [30], [35], [35], [80], [10], [20], [29], [40], [40], [40], [40], [40], [50], [200], [200], [25], [25], [20], [70], [600], [70], [100], [40]], dtype=float)
    Z0 = np.diag([0.0 + 0.0j, 0.0922 + 0.0470j, 0.4930 + 0.2511j, 0.3660 + 0.1864j, 0.38114 + 0.1941j, 0.8190 + 0.7070j, 0.1872 + 0.6188j, 0.7114 + 0.2351j, 1.0300 + 0.7400j, 1.0440 + 0.7400j, 0.1966 + 0.0650j, 0.3744 + 0.1238j, 1.4680 + 1.1550j, 0.5416 + 0.7129j, 0.5910 + 0.5260j, 0.7463 + 0.5450j, 1.2890 + 1.7210j, 0.7320 + 0.5740j, 0.1640 + 0.1865j, 1.5042 + 1.3554j, 0.4085 + 0.4784j, 0.7089 + 0.9373j, 0.4512 + 0.3083j, 0.89804 + 0.7091j, 0.8960 + 0.7011j, 0.2030 + 0.1034j, 0.2842 + 0.1447j, 1.0590 + 0.9337j, 0.8042 + 0.7006j, 0.5075 + 0.2585j, 0.9740 + 0.9630j, 0.3105 + 0.3619j, 0.3410 + 0.5302j])


    # Génération de A

    for k in range(33):
        for i in range(33):
            if X[i, k] == 1:
                for j in range(33):
                    if X[k, j] == 1:
                        X[i, j] = 1
    A = X

    for f in range(0, 33):
        P[f] = P0[f] / Sb
        Q[f] = Q0[f] / Sb
        Z[f][f] = np.abs(Z0[f][f]) / Zb


    for i in range(0, 33):
        for j in range(0, 33):
            AT [j][i] = A[i][j]
    ZA=np.dot(AT,Z)

    k=1
    erreur=1
    while erreur > 0.0001 and k < 40 :
        for i in range(0, 33):
            Ibus[i]=np.conj(complex(P[i],Q[i])/V[i])
        Ibranche=np.dot(A,Ibus)
        DV= np.dot(ZA,Ibranche)
        V=Vslack - DV
        erreur=max(np.abs(W)-np.abs(V))
        W=V
        k=k+1
    h=0
    for i in V :
        h=h+(1-np.abs(i))
    m=h/33
    v=0
    for i in V :
        v=v+(((1-np.abs(i))-m)**2)
    V_S[s]=v/33
    
    

    #Ploss
    for i in range(0, 33):
        Ibranche1[i] = (np.abs(Ibranche[i]))**2
        Ploss[i]=((Ibranche1[i]))* (np.real(Z0[i][i])/Zb)
        Qloss[i]= ((Ibranche1[i]))* (np.imag((Z0[i][i])/Zb))

    Sq=0        
    Sp=0

    for i in Ploss:
        Sp=Sp+i
    Ploss_S[s]=Sp*Sb
    

    
   
    for i in Qloss:
        Sq=Sq+i
    Qloss_S[s]=Sq*Sb
    #print ('scenario :',s,V_S[s],Ploss_S[s],Qloss_S[s])
    s=s+1
        

print("Nombre de scénarios :", nombre_scenarios)
