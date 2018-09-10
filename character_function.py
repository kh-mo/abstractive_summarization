# Code = 0xAC00 + (Chosung_index * NUM_JOONG * NUM_JONG) + (Joongsung_index * NUM_JONG) + (Jongsung_index)
# ord() 유니코드 코드포인트 반환
CHO = {0:'ㄱ', 1:'ㄲ', 2:'ㄴ', 3:'ㄷ', 4:'ㄸ', 5:'ㄹ', 6:'ㅁ', 7:'ㅂ', 8:'ㅃ', 9:'ㅅ',
       10:'ㅆ', 11:'ㅇ', 12:'ㅈ', 13:'ㅉ', 14:'ㅊ', 15:'ㅋ', 16:'ㅌ', 17:'ㅍ', 18:'ㅎ'}

JOONG = {19:'ㅏ', 20:'ㅐ', 21:'ㅑ', 22:'ㅒ', 23:'ㅓ', 24:'ㅔ', 25:'ㅕ', 26:'ㅖ', 27:'ㅗ', 28:'ㅘ',
         29:'ㅙ', 30:'ㅚ', 31:'ㅛ', 32:'ㅜ', 33:'ㅝ', 34:'ㅞ', 35:'ㅟ', 36:'ㅠ', 37:'ㅡ', 38:'ㅢ', 39:'ㅣ'}

JONG = {40:'', 41:'ㄱ', 42:'ㄲ', 43:'ㄳ', 44:'ㄴ', 45:'ㄵ', 46:'ㄶ', 47:'ㄷ', 48:'ㄹ', 49:'ㄺ',
        50:'ㄻ', 51:'ㄼ', 52:'ㄽ', 53:'ㄾ', 54:'ㄿ', 55:'ㅀ', 56:'ㅁ', 57:'ㅂ', 58:'ㅄ', 59:'ㅅ',
        60:'ㅆ', 61:'ㅇ', 62:'ㅈ', 63:'ㅊ', 64:'ㅋ', 65:'ㅌ', 66:'ㅍ', 67:'ㅎ'}

SPECIAL = {68:'!', 69:'.', 70:" "}
JAMO = list(CHO.values()) + list(JOONG.values()) + list(JONG.values())[1:]

NUM_CHO = 19
NUM_JOONG = 21
NUM_JONG = 28

FIRST_HANGUL_UNICODE = 44032
LAST_HANGUL_UNICODE = 0xD7A3

def is_jamo(letter):
    return letter in JAMO

def is_hangul(letter):
    code = ord(letter)
    if (code >= FIRST_HANGUL_UNICODE and code <= LAST_HANGUL_UNICODE) or is_jamo(letter):
        return True
    return False

def decompose_letter(letter):
    code = ord(letter) - FIRST_HANGUL_UNICODE
    jong = int(code % NUM_JONG)
    code /= NUM_JONG
    joong = int(code % NUM_JOONG)
    code /= NUM_JOONG
    cho = int(code)
    return list(CHO.values())[cho], list(JOONG.values())[joong], list(JONG.values())[jong], list(CHO.keys())[cho], list(JOONG.keys())[joong], list(JONG.keys())[jong]

def decompose_sentence(text):
    result = ""
    result_idx = []
    for char in text:
        # print(char)
        if is_hangul(char):
            cho, jung, jong, cho_idx, jung_idx, jong_idx = decompose_letter(char)
            result = result + cho + jung + jong
            result_idx.append(cho_idx)
            result_idx.append(jung_idx)
            result_idx.append(jong_idx)
        else:
            spec_idx = list(SPECIAL.values()).index(char)
            result += list(SPECIAL.values())[spec_idx]
            result_idx.append(list(SPECIAL.keys())[spec_idx])
    return result, result_idx
decompose_letter("이")

# text = "이것은 테스트 입니다."
# decompose_sentence(text)
char_text, char_text_idx = decompose_sentence(text)
compose_sentence()