# Railway Deploy


1) New Project → Deploy from GitHub → select this repo.
2) Add variables in Railway → Settings → Variables:
- TELEGRAM_BOT_TOKEN = <your-bot-token>
- TELEGRAM_ADMIN_CHAT = <your-chat-id or leave empty>
- JWT_SECRET = <random-long-secret>
3) (Optional) Add a PostgreSQL plugin and change DATABASE_URL accordingly.
4) Deploy. Open the service URL and test `GET /`
