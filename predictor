def predict_24h(view_per_min):
    decay_factor = 0.45  # realistic shorts
    predicted_views = view_per_min * 60 * 24 * decay_factor
    if predicted_views > 200000:
        monetization = "HIGH"
    elif predicted_views > 50000:
        monetization = "MEDIUM"
    else:
        monetization = "LOW"
    return int(predicted_views), monetization
