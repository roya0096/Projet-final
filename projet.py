import streamlit as st
import formule as fm
from PIL import Image
import pandas


col1, col2= st.columns(2)

with col1:
    st.title("Calcul financier")
with col2:
    image = Image.open('image_finance.jpg')

    st.image(image, caption='')


choix =  st.sidebar.selectbox ("Quel type de calcul financier désirez-vous faire ?",( 'Obligation','Options', 'Valeurs', 'Ratio' ))



if choix == 'Options' :
    st.title(" Voici la section pour les calculs sur les options")

    prix_s = st.number_input(" Quelle est le prix de l'option sous-jacent? ")
    prix_k = st.number_input(" Quelle est le prix d'exercise de cette option?")
    temp = st.number_input(" Quelle est l'échéance de cette option ?")
    taux = st.number_input(" Quelle est le taux sans risque ?")
    sig = st.number_input(" Quelle est l'écart type du rendement de l'action sous-jacent?")
    
    option_1 = fm.Options(S = prix_s, X = prix_k, T = temp, r = taux, sigma = sig)
    call = option_1.bs_call()
    put = option_1.bs_put()

    st.write(f"C'est la valeurs du call pour le denier point {call}.")
    



elif choix == 'Obligation':
    st.title(" Voici la section pour les calculs sur les obligations")
    dur = st.number_input("Quelle est la durée modifié de cette obligation ?")
    delta_rend = st.number_input("Quelle est la variation du I de cette obligation?")
    convex = st.number_input("Quel est la convexité de cette obligaton ?")
    rend_exige = st.number_input(" Quel est le rendement exigé de cette obligation?")
    coup = st.number_input(" Quel est le taux de coupon de cette obligation?")
    temp = st.number_input(" Combien le nombre de période restante a cette obligations")
    prix = st.number_input("Quelle est le prix présentement de l'obligation ")

    obligation_1 = fm.Obligation(d_mod = dur, conv = convex, delta_i = delta_rend, rend_exig = rend_exige, taux_coup = coup ,t = temp ,p = prix)    
    var = obligation_1.variation_oblig
    duree = obligation_1.duree
    val = obligation_1.valeur
    conv = obligation_1.convexite

elif choix == 'Valeurs':
    st.title(" Voici la section pour les calculs sur la valeurs d'une entreprise")
    Rend_att = st.number_input("Quelle est le rendement attendu?")
    rend_0 = st.number_input("Quelle est le taux sans risque")
    flux_0 = st.number_input("Quelle est le dernier flux de l'entreprise ?")
    bet = st.number_input(" Quel est le beta de cette entreprise")
    croi = st.number_input(" Quel est le taux de croissance de l'entreprise")
    cour_b = st.number_input(" Quelle est le cour/bénifice de cette entreprise")
    cour_bx = st.number_input("Quelle est le prochain cour bénifice estimé de cette entreprise ")
    beni_1= st.number_input("Quelle est le benifice par action +1 de cette entreprise")
    beni_fice = st.number_input("Quelle est le bénifice de cette entreprise")
    x=10

    valorisation = fm.Valeur(Rm = Rend_att, Rf = rend_0, fcf_0= flux_0, fcf_futurs=x,  beta = bet, g = croi, CB = cour_b, BPA1= beni_1, CBx = cour_bx, benifice = beni_fice)
    CAPM = valorisation.capm
    vale = valorisation.croissance_2
    cb = valorisation.multiple_CB

elif choix == 'Ratio':
    st.title(" Voici la section sur des ratios financiers")
    rend = st.number_input("Quelle est le rendement attendu?")
    sig = st.number_input("Quelle est le sigma de ce portefeuille")
    be = st.number_input("Quelle est le beta du portefeuille ")
    rend_mar = st.number_input("Quelle est le rendement moyen du marché?")
    rend_0r = st.number_input("Quelle est le taux sans risque?")


    rat = fm.Ratio(Rp =rend ,sigma = sig, beta = be, Rf =rend_mar, Rm= rend_0r)

    shar = rat.sharpe
    trey = rat.treynor
    jen = rat.jenson


# utiliser les append pour ajouter les formules dans une liste pour pouvoir prendre ensuite les êtres
# en mesure d'utiliser les formules et les chiffres.