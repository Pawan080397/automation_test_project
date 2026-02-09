import requests

def get_fusion_analysis_data(token, payload):
    """
    🔹 Direct backend validation
    🔹 UI se independent
    """

    url = "https://192.168.1.127:8000"   # ⚠️ real endpoint yaha

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 200, "❌ API response failed"

    return response.json()
