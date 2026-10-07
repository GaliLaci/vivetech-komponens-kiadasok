# ViVeTech aláírt komponenskiadások

A Névjegyből letölthető, aláírt AI Box-komponenscsomagok HTTPS-futára. Ez a tár a kiadási metaadatokat és bináris csomagokat tartalmazza. A ViVeTech forráskódja, üzleti adatai és hitelesítő adatai a privát tárban maradnak.

A Box a korábban rögzített saját kiadói kulccsal ellenőrzi a katalógust és a csomagokat. A HTTPS-futár önmagában nem ad telepítési jogosultságot. Minden telepítés adminisztrátori jóváhagyáshoz, kompatibilitási próbához és helyi mentéshez kötött.

Letöltési alap: https://galilaci.github.io/vivetech-komponens-kiadasok/
Katalógus: https://galilaci.github.io/vivetech-komponens-kiadasok/catalog.json

Az image-ek 32 MiB-os fájlokban kerülnek a Git-tárba. A Pages építése visszaállítja az eredeti image.tar fájlt, és az aláírt jegyzék szerinti méretet és SHA-256-ot ellenőrzi. A Box egyetlen, átirányítás nélküli HTTPS GET-tel tölti le az eredeti fájlt. Egy már kiadott azonosító/revision nem írható át; új kiadáskor a katalógus sorszáma is nő.

A ViVeTech termék saját, nem nyílt forrású szoftver; a csomagba foglalt harmadik felek licencei érvényesek. Ez a tár nem biztosít forráskód-felhasználási engedélyt.
