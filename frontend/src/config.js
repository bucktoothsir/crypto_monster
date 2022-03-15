const API = "https://vluiday23m.execute-api.us-west-2.amazonaws.com/production/cipher/";
const configData = {
    "CIPHER_OPTIONS": ["Caesar Cipher", "Linear Cipher", "Vigenère Cipher"],
    "DEFAULT_CIPHER": "Caesar Cipher",
    "CIPHER_KEY": {
    "CAESAR_KEY": ["Shift"],
    "LINEAR_KEY": ["Slope/A", "Slope/B"],
    "VIGENERE_KEY": ["Key", "Key Length"],
    },
    "TITLE": "Encode and Decode Caesar, Linear and Vigenere Ciphers. We support decode without keys.",
    "ENCODE_AREA_TITLE": "Plain Text",
    "DECODE_AREA_TITLE": "Cipher Text",
    "ENCODE_APIS": {
        "Caesar Cipher": API+"caesar/encode",
        "Linear Cipher": API+"linear/encode",
        "Vigenère Cipher": API+"vigenere/encode"
    },
    "DECODE_APIS": {
        "Caesar Cipher": API+"caesar/decode",
        "Linear Cipher": API+"linear/decode",
        "Vigenère Cipher": API+"vigenere/decode"
    }
    
}

export default configData;
