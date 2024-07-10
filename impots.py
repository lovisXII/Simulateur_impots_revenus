
import argparse
import matplotlib.pyplot as plt
import numpy as np

def old_tax(wage) :
    tax_to_pay = 0
    tax_rate = [
                (0     , 11294  , 0),
                (11295 , 28797  , 0.11),
                (28798 , 82341  , 0.30),
                (82342 , 177106 , 0.41)
                ]

    for min_tranch, max_tranch, rate in tax_rate :
        tax_per_tranch = 0
        if wage >= max_tranch : # case where wage is higher than the max value of the tranch (ex : wage = 20k should pay 102,92 + 257.3 + 456.2)
            tax_per_tranch += (max_tranch - min_tranch)*rate
        elif min_tranch <= wage <= max_tranch :
            tax_per_tranch += (wage - min_tranch)*rate
        tax_to_pay += tax_per_tranch
    if wage > 177106 :
        tax_to_pay += (wage - 177106) * 0.45
    return tax_to_pay

def new_tax(wage) :
    tax_to_pay = 0
    tax_rate = [
                (0     , 10292  , 0.01),
                (10292 , 15438  , 0.05),
                (15438 , 20584  , 0.1),
                (20584 , 27789  , 0.15),
                (27789 , 30876  , 0.2),
                (30876 , 33964  , 0.25),
                (33964 , 38081  , 0.3),
                (38081 , 44256  , 0.35),
                (44256 , 61752  , 0.40),
                (61752 , 102921 , 0.45),
                (102921, 144089 , 0.50),
                (144089, 267592 , 0.55),
                (267592, 411683 , 0.60)
                ]

    for min_tranch, max_tranch, rate in tax_rate :
        tax_per_tranch = 0
        if wage >= max_tranch : # case where wage is higher than the max value of the tranch (ex : wage = 20k should pay 102,92 + 257.3 + 456.2)
            tax_per_tranch += (max_tranch - min_tranch)*rate
        elif min_tranch <= wage <= max_tranch :
            tax_per_tranch += (wage - min_tranch)*rate
        tax_to_pay += tax_per_tranch
    if wage > 411683 :
        tax_to_pay += (wage - 411683) * 0.9
    return tax_to_pay

def parse_arguments():
    parser = argparse.ArgumentParser(description='Calcule et trace l\'impot sur le revenu avec l\'ancien et le nouveau system de tranche')
    parser.add_argument('-s', type=int, default=0, help='Valeur seule, prends une valeur de salaire et donne les valeurs de l\'ancien vs nouveau systeme')
    parser.add_argument('--min', type=int, default=0, help='Salaire minimum de la courbe')
    parser.add_argument('--max', type=int, default=500000, help='Salaire maximum de la courbe')
    parser.add_argument('--nbr_points', type=int, default=10000, help='Nombre de points')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    if not args.s :
        wages = np.linspace(args.min, args.max, args.nbr_points)  # 10000 points between 0 and 500,000
        newTax = []
        oldTax = []
        for wage in wages:
            newTax.append(new_tax(wage))
            oldTax.append(old_tax(wage))
        plt.figure(figsize=(10, 6))
        plt.plot(wages, newTax, label='New Tax', color='blue')
        plt.plot(wages, oldTax, label='Old Tax', color='red')

        # Adding titles and labels
        plt.title('Comparison of Old and New Tax Systems')
        plt.xlabel('Wage (in euros/year)')
        plt.ylabel('Tax (in euros)')
        plt.legend()
        plt.grid(True)
        plt.show()
    else :
        print("Salaire entre : ", args.s)
        print("Nouvel taxe : ", new_tax(args.s))
        print("Ancienne taxe : ", old_tax(args.s))
