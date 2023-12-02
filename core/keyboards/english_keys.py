from aiogram.utils.keyboard import  InlineKeyboardBuilder, InlineKeyboardButton,InlineKeyboardMarkup

button_data = [
    ['Page 1', 'Page 2', 'Page 3', 'Page 4'],
    ['Page 5', 'Page 6', 'Page 7', 'Page 8'],
    ['Page 9', 'Page 10', 'Page 11', 'Page 12'],
    ['Page 13', 'Page 14', 'Page 15', 'Page 16'],
    ['Page 17', 'Page 18', 'Page 19', 'Page 20'],
    # ... add more buttons as needed
]

def english_table():
    builder = InlineKeyboardBuilder()
    for row_index, row in enumerate(button_data):
        for col_index, item in enumerate(row):
            page_number = row_index * 4 + col_index
            builder.button(text=item, callback_data=f"page_{page_number}")
    builder.adjust(4)
    return builder.as_markup()