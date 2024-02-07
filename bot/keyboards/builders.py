from aiogram.utils.keyboard import ReplyKeyboardBuilder


# Фабрика клавиатур
def create_kb(buttons, buttons_in_row):
    builder = ReplyKeyboardBuilder()
    [builder.button(text=button) for button in buttons]
    builder.button(text='Назад')
    builder.adjust(buttons_in_row)
    return builder.as_markup(resize_keyboard=True)
