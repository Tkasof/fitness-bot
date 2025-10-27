print("🤖 Привет! Я твой фитнес-помощник")

name = input("Как тебя зовут? ")
weight = float(input("Твой вес (кг): "))
height = float(input("Твой рост (см): "))
goal = input("Цель (похудеть/набрать массу/поддерживать): ")

if goal == "похудеть":
    calories = weight * 25
elif goal == "набрать массу":
    calories = weight * 35
else:
    calories = weight * 30

protein = int(weight * 1.8)
fat = int(weight * 0.8)
carbs = int((calories - protein*4 - fat*9) / 4)

days = int(input("Сколько раз в неделю готов заниматься? "))

if days == 1:
    plan = "Плохая идея, которая ничего не даст"
elif days == 2:
    plan = "2 силовые fullbody с перерывом 2-3 дня"
elif days == 3:
    plan = "3 силовые fullbody с перерывом 1-3 дня ИЛИ верх - низ - fullbody ИЛИ 2 силовые fullbody + кардио"
else:
    plan = "день ног - день спины - день груди и рук - кардио ИЛИ это уровень посложнее, лучше обратиться к тренеру"

print(f"🎯 {name}, вот твоя программа:")
print(f"🍽️  ПИТАНИЕ:")
print(f"   Калории: {int(calories)} ккал")
print(f"   Белки: {protein}г")
print(f"   Жиры: {fat}г") 
print(f"   Углеводы: {carbs}г")
print(f"💪 ТРЕНИРОВКИ:")
print(f"   {plan}")