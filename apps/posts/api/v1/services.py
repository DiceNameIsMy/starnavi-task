from datetime import date

from django.core.exceptions import ValidationError

from ...models import Post, Like


def get_likes_stats(post_likes) -> dict:
    results = {}

    for like in post_likes:
        date = str(like.date.date())
        if date in results:
            results[date] += 1
        else:
            results[date] = 1

    return results


