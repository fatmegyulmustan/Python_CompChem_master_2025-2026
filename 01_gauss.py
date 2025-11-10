LIGHT_SPEED = 299792458 #m⋅s-1 Light speed in vacuum
PLANCK_CONST = 6.62607015 * (10 ** (-34)) # J.s
IDEAL_GAS_CONST = 8.314462618 # J/mol/K
AVOGADRO_CONST = 6.02214076 * (10 ** 23) # mol-1
ELEMENTARY_CHARGE = 1.602176634 * (10 ** (-19)) # C

cal_to_J = 4.184 # J
HARTREE_TO_eV = 27.211386245988 # eV
eV_to_Joule = ELEMENTARY_CHARGE * HARTREE_TO_eV #  J
eV_to_kJ_mol = eV_to_Joule * AVOGADRO_CONST / 1000 # kJ/mol
kJ_to_kcal = eV_to_kJ_mol / cal_to_J # kcal/mol
wavenumber_Hz = eV_to_Joule / (LIGHT_SPEED*100) / PLANCK_CONST # cm-1
temperature = eV_to_Joule / (IDEAL_GAS_CONST / AVOGADRO_CONST) # K
Hz = eV_to_Joule / PLANCK_CONST

print(f'eV = {HARTREE_TO_eV} \n cm-1 = {wavenumber_Hz} \n kcal/mol = {kJ_to_kcal} \n kJ/mol = {eV_to_kJ_mol} \n'
      f'oK = {temperature} \n J = {eV_to_Joule} \n Hz = {Hz}')





