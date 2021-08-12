from django.db.models import QuerySet


def get_likes_stats(post_likes: QuerySet) -> dict:
    results = {}
    
    for like in post_likes:
        date = str(like.date.date())
        if date in results:
            results[date] += 1
        else:
            results[date] = 1

    return results


