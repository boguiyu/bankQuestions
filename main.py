from question import Question
from app import API


def print_hi(name):
    print(f'Hi, {name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    api = API("test\\question_bank.json")
    question_1 = Question("where am i?", "NJ", "Bo", 20)
    question_2 = Question("where are you?", "NY", "Pei", 50)
    question_3 = Question("where are you?", "CA", "jiang", 90)
    api.addQuestion("001", question_1.to_dict())
    api.addQuestion("001", question_2.to_dict())
    api.addQuestion("002", question_3.to_dict())
    api.updateQuestion("001", "001_1", "author", "chester")
    api.removeQuestion("001", "001_1")
    api.addQuestion("001", question_1.to_dict())
    print(api.filterSubject("001"))
    print(api.display())


