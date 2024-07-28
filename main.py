def generate_password(n):
    result = ""
    for i in range(1, 21):
        for j in range(i+1, 21):
            if (i + j) % n == 0:
                result += f"{i}{j}"
    return result

# Пример использования:
n = int(input("Введите число от 3 до 20: "))
print(generate_password(n))