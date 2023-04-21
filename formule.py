from math import log, sqrt, pi, exp 
from scipy.stats import norm



class Options : # Formule pour calcule d'option
    """ Cette classe nous permet de calculer la valeur d'un put et d'un call"""
    def __init__(self, S, X, T, r, sigma):
        self.S = S
        self.X = X
        self.T = T
        self.r = r
        self.sigma = sigma

    def d1(self):
        return (log(self.S / self.X) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * sqrt(self.T))
    
    def d2(self):
        return (Options.d1(self) - (self.sigma * sqrt(self.T)))
    
    def bs_call(self):
        return self.S*norm.cdf(Options.d1(self)) - (self.X * exp(-self.r*self.T) * norm.cdf(Options.d2(self)))
    
    def bs_put(self):
        return Options.bs_call(self) - self.S + ( self.X *exp ( - self.r * self.T ))
    

class Valeur : # Formule pour le calcul de la valeur entreprise
    """ Cette classe nous permet de calculer la valeur intrisèque d'une entreprise """
    def __init__(self, Rm, Rf, fcf_0, fcf_futurs, beta, g, CB, BPA1, CBx, benifice ):
        self.Rm = Rm
        self.Rf = Rf
        self.fcf_0 = fcf_0
        self.fcf_futurs = fcf_futurs
        self.beta = beta
        self.g = g
        self.CB = CB
        self.BPA1 = BPA1
        self.CBx = CBx 
        self.benifice = benifice

    def capm(self) :
        medaf = self.Rf + self.beta *(self.Rm - self.Rf)
        return medaf 
    
    def croissance_1 (self) :
        fcf_act = []
        i = 0
        for i in range(len(self.fcf_futurs)):
            fcft = self.fcf_futurs[i] / (( 1 + Valeur.capm(self) )** (i + 1))
            fcf_act.append(fcft)
            i = i + 1

        V1 = sum(fcf_act)
        return V1 
    
    def croissance_2 (self):
        V2 = (self.fcf_futurs[-1] * ( 1 + self.g)) / (Valeur.capm(self) - self.g) * ( 1 + Valeur.capm(self) ) ** (-len(self.fcf_futurs))
        valeur_entre = Valeur.croissance_1(self) + V2
        return valeur_entre
    
    def multiple_CB (self):
        valeur_cb = Valeur.croissance_1(self) + (self.benifice * self.CBx)/ (( 1 + Valeur.capm(self))**len(self.fcf_futurs))
        return valeur_cb
    
class Obligation:
    """ Cette classe nous permet faire différent calcul sur les obligations"""
    def __init__ (self, d_mod, conv, delta_i, rend_exig, taux_coup,t,p,):
        self.d_mod = d_mod
        self.conv = conv
        self.delta_i = delta_i
        self.rend_exig = rend_exig
        self.taux_coup = taux_coup
        self.t = t
        self.p = p
        
    def variation_oblig (self): 
        delta_2 = pow(self.delta_i,2)
        var = (- self.d_mod * self.delta_i) + (delta_2) * (0.5 * self.conv)  
        return var
    
    def valeur (self):
        x = self.rend_exig / 100
        y = self.taux_coup * 10
        p_0 = y*((1-(1 + x)**-self.t)/x) + 1000/(1+x)**self.t
        return p_0
    def duree (self):
        coup = (10 * self.taux_coup) /2
        rend_eche = self.rend_exig / 100

        dur =[]
        valeur_actuelle = 0

        for x in range(int(1//self.t)+1):
            terme = coup / (1 + rend_eche)**x
            valeur_actuelle += terme
            dur.append(x * terme)
    
        valeur_actuelle += 1000 / (1 + rend_eche)**self.t
        dur.append(self.t * (1000 / (1 + rend_eche)**self.t))
        duree_mac = sum(dur) / valeur_actuelle
        return duree_mac
    

    def convexite (self):
        coup = (10 * self.taux_coup) /2
        rend_eche = self.rend_exig / 100

        conv = ((1 + rend_eche) / ((1 + rend_eche) * (1 + rend_eche) + coup / self.p)) * ((coup * self.t * (self.t + 1)) / ((1 + rend_eche) ** (self.t + 2))) + ((self.t + 1) / (1 + rend_eche)) * (Obligation.duree(self) - (self.t / (1 + rend_eche)))
        return conv

class Ratio :
    """ Cette classe nous permet de calculer les ratios de Sharpe, Treynor et de Jenson avec le CAPM qui est aussi calculé"""
    def __init__(self ,Rp ,sigma, beta, Rf, Rm):
        self.Rp = Rp
        self.sigma = sigma
        self.beta = beta
        self.Rf = Rf
        self.Rm = Rm

    def sharpe(self):
        return (self.Rp - self.Rf)/self.sigma

    def treynor(self):
        return (self.Rp - self.Rf)/self.beta

    def capm(self):
        return self.Rf + (self.Rm - self.Rf)*self.beta

    def jenson(self):
        return self.Rp - Ratio.capm(self)
