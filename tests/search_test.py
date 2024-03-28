import sys
sys.path.append("../")

# Import search function
from islam_web import search

query: str = "قيام الليل"
# Get search response
response: dict = search(query) # param={}, headers={}

# Check if the search request was done correctly.
if not response.get("ok", False):
    error_message = response.get("error_message", "Unknown error")
    status_code = response.get("status_code", "Status not found")
    print(f"- I got an error: {error_message}\n- Status code: {status_code}")
else:
    # Get search result in results var which is list of dictionaries.
    results: list[dict] = response["results"]
    
    # The first result
    first_result: dict = results[0]
    """
    {
      "title": "وقت قيام الليل",
      "link": "https://www.islamweb.net/ar/fatwa/99274",
      "description": "فى رمضان أصلي صلاة التراويح فى المسجد ثم أصلي بمنزلي إحدى عشرة ركعة بمفردي والمسجد الذي أصلي فيه يمكثون بين أذان العشاء وإقامتها دقيقة تقريبا، فهل يمكنني أن أصلى فى هذا الوقت بين الأذان والإقامة ما تيسر لي من الإحدى عشرة ركعة التي أصليهم بمنزلي وفي هذه الحالة سأكون قد شرعت في القيام قبل صلاة العشاء، فهل يجوز؟",
      "category": "فقه العبادات > الصلاة > صلاة التطوع > التراويح وقيام الليل"
    }
    """
    for key, value in first_result.items():
        print(key.title(), value, sep=" : ")
