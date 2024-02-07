from .builders import create_kb

# Клавиатура для пользователей
START_KB_BUTTONS = [
    'Все мои заявки',
    'Создать новую заявку',
    'Все актвные заявки',
]
start_kb = create_kb(START_KB_BUTTONS, 3)
