# Importuje moduł binascii, który dostarcza narzędzia do konwersji 
# między reprezentacjami binarnymi a różnymi formatami kodowania.
import binascii

# Poniżej znajduje się lista identyfikatorów szyfrowania:
# AES_128_DIFFUSER    = 0x0080<br/>
# AES_256_DIFFUSER    = 0x0180<br/>
# AES_128_NO_DIFFUSER = 0x0280<br/>
# AES_256_NO_DIFFUSER = 0x0380<br/>
# AES_XTS_128         = 0x0480<br/>
# AES_XTS_256         = 0x0580<br/><br/>

# Identyfikator trybu szyfrowania (AES_XTS_128)
mode = "0480"

# Klucze szyfrujące
key1 = "cdc6fb36bf30725df6f25b5afb98d30d"
key2 = "923a5da89439af9b15011997c0150ee9"


# Konkatenacja ciągów znaków: mode + key1 + key2. 
# Rezultatem jest pojedynczy ciąg szesnastkowy zawierający identyfikator trybu i oba klucze. 
# Funkcja binascii.unhexlify() - konwertuje ciąg szesnastkowy na odpowiadające mu dane binarne. 
# Każda para znaków szesnastkowych jest przekształcana w jeden bajt.
binary_data = binascii.unhexlify(mode + key1 + key2)

# Zapis do pliku
with open("bitlocker-key.bin", "wb") as output:
    output.write(binary_data)

# Podgląd bajtów
print(binary_data)

