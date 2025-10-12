# abcdefghijklmnñopqrstuvwxyz ,.

texto = "l.ziu,mf .fzmk,wzilwgfqw mfai kwukmsw flw,wfifsif.upamz plilflmf .fik,.isfm k.lwfmufmsfk.isfmsfiñ.psiftmcpkiuifdfmsfkwulwzfiulpuwgfk.isfiamfjpkmnisigfxzw,mñmufmsflm xspmñ.mflmsftixiflmfitmzpkifsi,puigflm lmfsifnzwu,mzifuwz,mflmftmcpkwfoi ,ifmsfkijwflmfowzuw gfxsi tiulwfsif.upnpkikpwuflmfsw fpjmzwitmzpkiuw gfu.m ,zwfkwu,pumu,mfu.mawfdfiu,pñ.wgfxzmlm ,puilwfifkwu,mumzf.uifzieify.pu,igfsifzieifkw tpkigfmufsifk.isf mfn.ulpziufsi flp xmz i fdf mfkwu .tizifsif.uplilh"

desplazamiento = 22
abecedario = "abcdefghijklmnñopqrstuvwxyz ,."
resultado = ""

for letra in texto:
    if letra in abecedario:
        posicion = abecedario.index(letra)
        nueva_posicion = (posicion + desplazamiento) % len(abecedario)
        resultado += abecedario[nueva_posicion]

print(resultado)


