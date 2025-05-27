import random

def generate_geometric_sequence():
    length = random.randint(5, 10)
    first_term = random.randint(1, 5)
    ratio = random.randint(2, 4)
    
    sequence = [first_term * (ratio ** i) for i in range(length)]
    return sequence

def play_geometric_game():
    print("Добро пожаловать в игру 'Геометрическая прогрессия'!")
    print("Вам будет показана последовательность чисел с пропущенным элементом.")
    print("Ваша задача - определить это число.\n")
    
    correct_answers = 0
    total_questions = 0
    
    while True:
        sequence = generate_geometric_sequence()
        hidden_index = random.randint(0, len(sequence) - 1)
        correct_answer = sequence[hidden_index]
        
        displayed_sequence = sequence.copy()
        displayed_sequence[hidden_index] = ".."
        print("Последовательность:", " ".join(map(str, displayed_sequence)))
        
        while True:
            user_input = input("Введите пропущенное число (или 'q' для выхода): ").strip()
            if user_input.lower() == 'q':
                print(f"\nИгра окончена. Ваш результат: {correct_answers} из {total_questions}.")
                return
            
            try:
                user_answer = int(user_input)
                break
            except ValueError:
                print("Ошибка! Введите целое число или 'q' для выхода.")
        
        total_questions += 1
        
        if user_answer == correct_answer:
            print("Правильно! Это действительно", correct_answer, "\n")
            correct_answers += 1
        else:
            print(f"Неправильно. Ваш ответ: {user_answer}. Правильный ответ: {correct_answer}\n")

if __name__ == "__main__":
    play_geometric_game()