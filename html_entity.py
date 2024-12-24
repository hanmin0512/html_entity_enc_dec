def encode_to_entities(input_char):
    """
    인코딩: 문자를 HTML 숫자 엔티티(&#숫자;)와 16진수 엔티티(&#x16진수;)로 변환.
    """
    if len(input_char) != 1:
        raise ValueError("단일 문자만 입력하세요.")

    ascii_code = ord(input_char)
    decimal_entity = f"&#{ascii_code};"
    hex_entity = f"&#x{ascii_code:x};"

    return decimal_entity, hex_entity

def decode_from_entities(entity):
    """
    디코딩: HTML 숫자 엔티티(&#숫자;) 또는 16진수 엔티티(&#x16진수;)를 문자로 변환.
    """
    if entity.startswith("&#") and entity.endswith(";"):
        if entity[2] == "x":  # 16진수 엔티티
            char_code = int(entity[3:-1], 16)
        else:  # 10진수 엔티티
            char_code = int(entity[2:-1])

        return chr(char_code)
    else:
        raise ValueError("유효한 HTML 엔티티 형식이 아닙니다.")

def main():
    while True:
        choice = input("선택: 1) 인코딩 2) 디코딩 3) 종료: ").strip()

        if choice == "1":
            char = input("인코딩할 문자를 입력하세요: ").strip()
            try:
                decimal, hex_code = encode_to_entities(char)
                print(f"HTML 숫자 엔티티: {decimal}")
                print(f"HTML 16진수 엔티티: {hex_code}")
            except ValueError as e:
                print(f"오류: {e}")

        elif choice == "2":
            entity = input("디코딩할 HTML 엔티티를 입력하세요: ").strip()
            try:
                decoded_char = decode_from_entities(entity)
                print(f"디코딩된 문자: {decoded_char}")
            except ValueError as e:
                print(f"오류: {e}")

        elif choice == "3":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
