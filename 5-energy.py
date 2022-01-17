def e_cinetique(masse,vitesse):
    ec = (1/2) * masse * vitesse**2
    #print(ec,"joules")
    return ec

def e_potentielle(masse,hauteur,g=9.81):
    ep = masse * hauteur * g 
    return ep 

def e_mecanique(e_cinetique,e_potentielle):
    em = e_cinetique + e_potentielle
    return em 

print("Bienvenu sur votre programme de calcul d'énergie. Vous pouvez effectuer le calcul de l'énergie cinétique, potentielle ou mécanique.")
print("Voici la liste des choix: ")
print("- ec pour énergie cinétique")
print("- ep pour énérgie potentielle")
print("- em pour énergie mécanique")

choix = input("Que voulez-vous calculer ?: ")

if choix == "ec":
    m_c = input("Masse(en kilogramme): ")
    v = input('Vitesse(en mètre par seconde): ')
    if m_c.isnumeric() == True and v.isnumeric == True:
        m_c = float(m_c)
        v = float(v)
    resutl_ec = e_cinetique(float(m_c),float(v))
    print("L'énergie cinétique vaut:",resutl_ec,"joules")
elif choix == "ep":
    m_p = input("Masse(en kilogramme): ")
    h = input("Hauteur(en mètre): ")
    if m_p.isnumeric() and h.isnumeric():
        m_p = float(m_p)
        h = float(h)
    g = input("Constante gravitationnelle (Si vide, g=9.81): ")
    if g.isnumeric():
        g = float(g)
    else:
        g = 9.81
    resutl_ep = e_potentielle(float(m_p),float(h),float(g))
    print("L'énergie potentielle vaut:",resutl_ep,"Joules")
elif choix == "em":
    m = input("Masse(en kilogramme): ")
    v = input('Vitesse(en mètre par seconde): ')
    if m.isnumeric() == True and v.isnumeric == True:
        m = float(m)
        v = float(v)
    resutl_ec = round(e_cinetique(float(m),float(v)),2)

    h = input("Hauteur(en mètre): ")
    if m.isnumeric() and h.isnumeric():
        m = float(m)
        h = float(h)
    g = input("Constante gravitationnelle (Si vide, g=9.81): ")
    if g.isnumeric():
        g = float(g)
    else:
        g = 9.81
    resutl_ep = round(e_potentielle(float(m),float(h),float(g)),2)
    
    print("L'énergie cinétique vaut:",resutl_ec,"joules")
    print("L'énergie potentielle vaut:",resutl_ep,"Joules")

    resutl_em = round(e_mecanique(resutl_ec,resutl_ep),2)
    print("L'énergie mécanique vaut:",resutl_em,"Joules")
else:
    print("Make sur you entrer the right choice please...! ")