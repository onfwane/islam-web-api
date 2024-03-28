import sys
sys.path.append("../")

# Import get_fatwa function
from islam_web import get_fatwa

# A fatwa link from islam web (Get it from search results).
fatwa_link: str = "https://www.islamweb.net/ar/fatwa/99274"
# get_fatwa function result
# NOTE: You can use fatwa number to get it ( 99274 )
response: dict = get_fatwa(fatwa_link=fatwa_link)

# Check if the get fatwa request was done correctly.
if not response.get("ok", False):
    error_message = response.get("error_message", "Unknown error")
    status_code = response.get("status_code", "Status not found")
    print(f"- I got an error: {error_message}\n- Status code: {status_code}")
else:
    # Get fatwa result in result var which is a dictionary.
    fatwa: dict = response["result"]
    """
    {
      "fatwa_title": "وقت قيام الليل",
      "fatwa_num": 99274,
      "fatwa_views": 8125,
      "fatwa_date": "الإثنين 13 رمضان 1428 هـ - 24-9-2007 م",
      "question": "\nفى رمضان أصلي صلاة التراويح فى المسجد, ثم أصلي بمنزلي إحدى عشرة ركعة بمفردي, والمسجد الذي أصلي فيه يمكثون بين أذان العشاء وإقامتها 40 دقيقة تقريبا، فهل يمكنني أن أصلى فى هذا الوقت (بين الأذان والإقامة) ما تيسر لي من الإحدى عشرة ركعة التي أصليهم بمنزلي, وفي هذه الحالة سأكون قد شرعت في القيام قبل صلاة العشاء، فهل يجوز؟\n",
      "answer": "\n\n\nالحمد لله والصلاة والسلام على رسول الله وعلى آله وصحبه، أما بعـد:\nفإن وقت قيام الليل يبدأ بعد صلاة العشاء، والسائل يصليها مع الإمام والحمد لله بل يزيد عليها بصلاته وحده، أما الصلاة قبل العشاء فلا تعتبر من قيام الليل لكن الصلاة بين الأذان والإقامة مرغب فيها، وكذلك التنفل بين المغرب والعشاء فقد قيل إنها هي ناشئة الليل المذكورة في سورة المزمل، وهو قول ابن عمر وأنس بن مالك، وكان علي بن الحسين يصلي بين المغرب والعشاء ويقول: هذا ناشئة الليل؛ كما ذكر القرطبي.\nوعليه، فإن النافلة في هذا الوقت مرغب فيها، والمصلي في هذا الوقت مأجور على صلاته واغتنامه هذا الوقت الذي يغفل عنه الكثير من الناس وهذا هو المطلوب، أما كون المصلي في هذا الوقت يعتبر قد شرع في قيام الليل فإن وقت قيام الليل يبدأ بعد العشاء، وننبه الأخ السائل هنا إلى أنه إن كان يوتر مع الإمام فلا حرج عليه في التنفل بعد ذلك إذا أراد، لكن لا يعيد الوتر، وللفائدة يرجى الاطلاع على الفتوى رقم: 60612، والفتوى رقم: 75477.\nوالله أعلم.\n"
    }
    """
    for key, value in fatwa.items():
        print(
            key.replace("_", " ").title(),
            value, sep=" : "
        )