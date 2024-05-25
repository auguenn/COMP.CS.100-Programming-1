"""
COMP.CS.100 Indeksikorotus opintotukeen
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
syöte = input("Enter the amount of the study benefits: ")
the_study_benefits = float(syöte)
index_raise = (1.17 / 100) + 1
the_study_benefit_2 = the_study_benefits * index_raise
the_study_benefits_3 = index_raise * the_study_benefit_2
print("If the index raise is 1.17 percent, the study benefit,")
print("after a raise, would be", the_study_benefit_2, "euros")
print("and if there was another index raise, the study")
print("benefits would be as much as", the_study_benefits_3, "euros")