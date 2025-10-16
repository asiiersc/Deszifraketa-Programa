from collections import Counter

textua = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."
maiztasunak = {
    "E": 0.1678,
    "R": 0.0494,
    "Y": 0.0154,
    "J": 0.0030,
    "A": 0.1196,
    "U": 0.0480,
    "Q": 0.0153,
    "Ñ": 0.0029,
    "O": 0.0869,
    "I": 0.0415,
    "B": 0.0092,
    "Z": 0.0015,
    "L": 0.0837,
    "T": 0.0331,
    "H": 0.0089,
    "X": 0.0006,
    "S": 0.0788,
    "C": 0.0292,
    "G": 0.0073,
    "K": 0.0000,
    "N": 0.0701,
    "P": 0.02776,
    "F": 0.0052,
    "W": 0.0000,
    "D": 0.0687,
    "M": 0.0212,
    "V": 0.0039
}
def sortu_ordezkapena(array_letras, array_maiztasunak):
    return {array_letras[i]: array_maiztasunak[i] for i in range(min(len(array_letras), len(array_maiztasunak)))}

def aplikatu_ordezkapena(textua, ordezkapena):
    return ''.join([ordezkapena.get(c, c) for c in textua])

def maiztasunakKonparatu():
    # Gure frekuentziak kalkulatu eta normalen aurka konparatu (Hasierakoa)
    letrak = [c for c in textua if c.isalpha()]
    kontadorea = Counter(letrak)

    osoa = sum(kontadorea.values())
    frekuentziak = {letra: kontadorea[letra] / osoa for letra in kontadorea}

    ohikoenak = sorted(frekuentziak.items(), key=lambda x: x[1], reverse=True)
    letrak_array = [letra for letra, freq in ohikoenak]

    maiztasunak_ordenatuta = sorted(maiztasunak.items(), key=lambda x: x[1], reverse=True)
    maiztasun_array = [letra for letra, prob in maiztasunak_ordenatuta]

    print(letrak_array)
    print(maiztasun_array)

    ordezkapena = sortu_ordezkapena(letrak_array, maiztasun_array)
    testu_berria = aplikatu_ordezkapena(textua, ordezkapena)

    print(ordezkapena)
    print(testu_berria)

froga = {'X': 'E', 
         'E': 'A',
         'K': 'R',
         'I': 'O',
         'C': 'I',
         'J': 'N',
         'T': 'L',
         'A': 'D',
         'R': 'C',
         'Z': 'U',
         'H': 'T', 
         'N': 'S', 
         'P': 'M', 
         'D': 'P', 
         'Q': 'B', 
         'O': 'F', 
         'S': 'Q', 
         'G': 'J', 
         'V': 'Y', 
         'v': 'V', 
         'U': 'G', 
         'M': 'H', 
         'F': 'X', 
         'L': 'Z'}
print(aplikatu_ordezkapena(textua, froga))
# 1. maiztasunakKonparatu()
# 2. Froga sortu
# 3. aplikatu_ordezkapena froga erabiliz
