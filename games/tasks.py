from celery import shared_task


@shared_task
def notify_new_game(game_id):
    print(f"🎮 New game created with ID {game_id}")
