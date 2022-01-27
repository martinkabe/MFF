from typing import List

cisla = [1,3,7,4,5,3]

def najdi_operatory(cisla: List, vysledek: int, operatory: str) -> None:
    if not cisla and vysledek != 0:
        return
    elif vysledek == 0 and not cisla:
        print(operatory)
    else:
        najdi_operatory(cisla[1:], vysledek + cisla[0], operatory + f' - {cisla[0]}')
        najdi_operatory(cisla[1:], vysledek - cisla[0], operatory + f' + {cisla[0]}')

def najdi_operatory_pomoc(cisla: List, vysledek: int) -> None:
    najdi_operatory(cisla[1:], vysledek - cisla[0], f'{cisla[0]}')

najdi_operatory_pomoc(cisla, 9)