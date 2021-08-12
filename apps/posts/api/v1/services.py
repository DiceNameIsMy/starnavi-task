from datetime import date

from django.core.exceptions import ValidationError

from ...models import Post, Like


def get_likes_stats(post_likes, start_date: date, end_date: date) -> dict:
    if start_date > end_date:
        raise ValidationError("start_date shouldn't be bigger than the end_date")
    results = {}

    sliced_likes = post_likes.filter(
        date__date__gte=start_date, 
        date__date__lte=end_date
    )

    for like in sliced_likes:
        date = str(like.date.date())
        if date in results:
            results[date] += 1
        else:
            results[date] = 1

    return results


