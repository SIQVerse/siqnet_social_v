def recommend_content(user_id, history):
    return sorted(history, key=lambda x: x['engagement'], reverse=True)[:5]
