# 라이브러리 불러오기
import random

# 변수 초기화하기
maxNum = 7               # 최대 허용 추측 횟수
maskChar = "_"           # 마스킹 문자
tryCount = 0             # 시도 횟수
guessedLetters = []      # 사용자 추측 문자를 저장할 리스트

# 게임 단어 리스트
WordList = ["anvil", "boutique", "cookie", "fluff", "jazz", "penumonia", "sleigh", "society", "topaz", "tsunami", "yummy", "zombie"]

# 게임에 사용할 단어 고르기
randWord = random.choice(WordList)

# 마스킹한 입력 문자열로 시작하기
userWord = maskChar * len(randWord)

# 게임 시작하기
# 단어를 맞히거나 최대 횟수에 이를 때까지 루프
while randWord != userWord and tryCount < maxNum :
    # 마스킹한 단어 출력
    print("마스킹한 단어 출력: ",userWord)

    # 이미 추측한 문자 표시하기
    if len(guessedLetters) > 0:
        # 입력한 내용이 있다면 빈 문자열로 시작하기
        youTried = ""
        # 추측한 각 문자 더하기
        for i in guessedLetters :
            youTried += i
        print("시도한 문자들 : ", youTried)

    # 남은 시도 횟수 출력하기
    print("남은 시도 횟수: ", maxNum - tryCount )

    # 보기 좋게 빈 줄 출력하기
    print()

    # 추측 문자 입력받기
    userInput = input("추측 문자: ").strip().lower()
    # 1글자만 입력받기
    if len(userInput) > 0:
        userInput = userInput[0]
    # 같은 문자 추측 방지
    if userInput in guessedLetters:
        print("이미 추측한 문자입니다.", userInput)
    else:
        # 새로운 추측 문자를 리스트에 저장하기
        guessedLetters.append(userInput)
        # 리스트 정렬하기
        guessedLetters.sort()

        # 마스킹 업데이트 하기, 빈 문자열로 시작
        userWord = ""
        for i in randWord:
            if i in guessedLetters:
                userWord += i
            else:
                userWord += maskChar
        
        # 확인 물음
        if userInput in randWord:
            print("올바른 추측입니다.")
        else: 
            print("틀렸습니다.")
            tryCount += 1
    print()

if userWord == randWord:
    print("여러분이 이겼습니다. 단어는", randWord, "입니다.")
else:
    print("여러분이 졌습니다. 정답: ", randWord)