from collections import defaultdict

from django.db.models import QuerySet


def get_likes_stats(post_likes: QuerySet) -> dict:
    results = defaultdict(int)

    for like in post_likes:
        date = str(like.date.date())
        results[date] += 1

    return results


