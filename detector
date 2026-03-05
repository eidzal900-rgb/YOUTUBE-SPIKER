def calculate_metrics(old, new, minutes=10):
    delta_like = new["like"] - old["like"]
    delta_view = new["view"] - old["view"]
    like_per_min = delta_like / minutes
    view_per_min = delta_view / minutes
    engagement = (new["like"] / new["view"]) * 100 if new["view"] > 0 else 0
    spike = (
        like_per_min > SPIKE_LIKE_PER_MIN and
        view_per_min > SPIKE_VIEW_PER_MIN and
        engagement > SPIKE_ENGAGEMENT
    )
    return like_per_min, view_per_min, engagement, spike
