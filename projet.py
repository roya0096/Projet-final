import streamlit as st
import formule as fm
from PIL import Image
import pandas


col1, col2= st.columns(2)

with col1:
    st.title("Calculatrice pour fonction financière")
with col2:
    image = Image.open('image_finance.jpg')

    st.image(image, caption='')


choix =  st.sidebar.selectbox ("Quel type de calcul financier désirez-vous faire ?",( 'Obligation','Options', 'Ratio', 'Valeurs intrisèque' ))



if choix == 'Options' : # Cette section demande les informations pour être en mesure de faire les calculs sur les options
    st.header("Voici la section pour les calculs sur les options")
    st.subheader("Veuiller entrer les informations suivantes")
   
    prix_s = st.number_input("Quelle est le prix de l'action sous-jacent? ", value=1.00)
    prix_k = st.number_input("Quelle est le prix d'exercise de cette option?",value=1.00)
    temp = st.number_input("Quelle est l'échéance de cette option ?",value=1.00)
    taux = st.number_input("Quelle est le taux sans risque ?",value=1.00)
    sig = st.number_input("Quelle est l'écart type du rendement de l'action sous-jacent ?",value=1.00)
    
    #On vient créer notre liste pour être en mesure de prendre faire le lien avec notre page formule
    option_1 = fm.Options(S = prix_s, X = prix_k, T = temp, r = taux, sigma = sig)
    call = option_1.bs_call()
    put = option_1.bs_put()

    st.header("Voici vos résultats ")
    st.write(f"Voici le prix du call selon les informations que vous avez entré : {call:.2f}$.")
    st.write(f"Voici le prix du put selon les informations que vous avez entré : {put:.2f}$.")
    



elif choix == 'Obligation': # Cette section demande les informations pour être en mesure de faire les calculs sur les obligations
    st.header("Voici la section pour les calculs sur les obligations")
    st.subheader("Veuiller entrer les informations suivantes")

    dur = st.number_input("Quelle est la durée modifié de cette obligation ?",value=1.00)
    delta_rend = st.number_input("Quelle est la variation du taux de cette obligation?",value=1.00)
    convex = st.number_input("Quel est la convexité de cette obligaton ?",value=1.00)
    rend_exige = st.number_input("Quel est le rendement de cette obligation ?",value=1.00)
    coup = st.number_input(" Quel est le taux de coupon de cette obligation ?",value=1.00)
    temp = st.number_input(" Combien reste t'il de période à cette obligation ?",value=1.00)
    prix = st.number_input("Quelle est le prix présentement de l'obligation ? ",value=1000.00)

    #On vient créer notre liste pour être en mesure de prendre faire le lien avec notre page formule
    obligation_1 = fm.Obligation(d_mod = dur, conv = convex, delta_i = delta_rend, rend_exig = rend_exige, taux_coup = coup ,t = temp ,p = prix)    
    var = obligation_1.variation_oblig()
    dure = obligation_1.duree()
    val = obligation_1.valeur()
    conv = obligation_1.convexite()

    # On affiche les résultats sur notre site web 
    st.header("Voici vos résultats ")
    st.write(f"La variation de prix pour cette obligation est égal à {var:.2f}.")
    st.write(f"La durée de cette obligation est {dure:.2f} années.")
    st.write(f"La valeur de cette obligation est de {val:.2f}$.")
    st.write(f"La convexité de cette obligation est de {conv:.2f}.")

elif choix == 'Valeurs intrisèque': # Cette section demande les informations pour être en mesure de faire les calculs sur la valeur intrinsèque d'une entreprise
    st.header(" Voici la section pour les calculs sur la valeurs d'une entreprise")
    st.subheader("Veuiller entrer les informations suivantes")
    
    Rend_att = st.number_input("Quelle est le rendement attendu ?",value=1.00)
    rend_0 = st.number_input("Quelle est le taux sans risque ?",value=1.00)
    flux_0 = st.number_input("Quelle est le dernier flux monétaire de l'entreprise ?",value=1.00)
    bet = st.number_input(" Quel est le beta de cette entreprise ?",value=1.00)
    croi = st.number_input(" Quel est le taux de croissance de l'entreprise ?",value=1.00)
    cour_b = st.number_input(" Quelle est le cour/bénifice de cette entreprise ?",value=1.00)
    cour_bx = st.number_input("Quelle est le prochain cour/bénifice estimé de cette entreprise ?",value=1.00)
    beni_1= st.number_input("Quelle est le benifice par action pour la prochaine période de cette entreprise ?",value=1.00)
    beni_fice = st.number_input("Quelle est le bénifice de cette entreprise ?",value=1.00)
    
    x = []
    for y in range (1,6):
        flux = st.number_input(f"Quelle est le flux monétaire de l'année{y}?", value=1.00)
        x.append(flux)


    #On vient créer notre liste pour être en mesure de prendre faire le lien avec notre page formule
    valorisation = fm.Valeur(Rm = Rend_att, Rf = rend_0, fcf_0= flux_0, fcf_futurs=x,  beta = bet, g = croi, CB = cour_b, BPA1= beni_1, CBx = cour_bx, benifice = beni_fice)
    CAPM = valorisation.capm()
    vale = valorisation.croissance_2()
    cb = valorisation.multiple_CB()
    fin = CAPM * 100

    # On affiche les résultats sur notre site web 
    st.header("Voici vos résultats ")
    st.write(f"Le modèle d'évaluation des actifs pour cette entreprise est de {fin:.2f}%.")
    st.write(f"La valeur de cette entreprise selon la méthode de cash flow est de {vale:.2f}$.")
    st.write(f"La valeur de cette entreprise selon la méthode du cour bénifice est de {cb:.2f}$.")

elif choix == 'Ratio': # Cette section demande les informations pour être en mesure de faire les calculs sur les ratios 
    st.header(" Voici la section sur des ratios financiers")
    st.subheader("Veuiller entrer les informations suivantes")
    rend = st.number_input("Quelle est le rendement attendu?",value=1.00)
    sig = st.number_input("Quelle est le sigma de ce portefeuille",value=1.00)
    be = st.number_input("Quelle est le beta du portefeuille ",value=1.00)
    rend_mar = st.number_input("Quelle est le rendement moyen du marché?",value=1.00)
    rend_0r = st.number_input("Quelle est le taux sans risque?",value=1.00)

    #On vient créer notre liste pour être en mesure de prendre faire le lien avec notre page formule
    rat = fm.Ratio(Rp =rend ,sigma = sig, beta = be, Rf =rend_mar, Rm= rend_0r)
    shar = rat.sharpe()
    trey = rat.treynor()
    jen = rat.jenson()

    # On affiche les résultats sur notre site web 
    st.header("Voici vos résultats ")
    st.write(f" Le ratio Sharpe de votre portefeuille est de {shar:.2f}.")
    st.write(f" Le ratio Treynor de votre portefeuille est de {trey:.2f}.")
    st.write(f" Le ratio de Jenson de votre portefeuille est de {jen:.2f}.")


st.write ("Ce site web fut créer par Anthony Roy, Antony Mercier-Saillant et Marc-Olivier Simard dans le but du cour Fin30521-71")
