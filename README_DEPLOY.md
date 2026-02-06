Deploying to Render (GitHub + Render)

1) Prepare your local repo

- Ensure you have a GitHub account and `git` installed.
- From the repo root run:

```bash
git init
git add .
git commit -m "Initial commit for Render deploy"
# create a repo on GitHub, then add remote and push
git remote add origin https://github.com/<your-username>/<repo-name>.git
git branch -M main
git push -u origin main
```

2) Recommended repo structure for Render

- Backend lives in `backend/` (already present) and contains `Procfile`, `requirements.txt`, and `runtime.txt`.
- Frontend is static files in root `pages/` and `index.html` (can be served separately).

3) Create a PostgreSQL database on Render (recommended)

- In Render dashboard: New -> PostgreSQL
- Copy the `DATABASE_URL` connection string and set it as an environment variable for your Web Service.

Note: Do NOT rely on SQLite for production on Render — the filesystem is ephemeral and will lose data on deploys.

4) Create a Web Service on Render

- In Render dashboard: New -> Web Service
- Connect your GitHub account and select the repository.
- Branch: usually `main`.
- Root Directory: set to `backend` (because server_v2.py and Procfile are in `backend/`).
- Build Command (optional): `pip install -r requirements.txt`
- Start Command (Procfile will be used) or set: `gunicorn server_v2:app`
- Environment: choose `Python` and the runtime `python-3.11.0` or as in `runtime.txt`.

5) Set required Environment Variables (Render -> Service -> Environment)

- `SECRET_KEY` = a secure random string
- `DATABASE_URL` = from your Render Postgres instance
- `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USERNAME`, `MAIL_PASSWORD`, `MAIL_DEFAULT_SENDER` = for email sending
- `FRONTEND_URL` = public URL where your frontend will be hosted (Render static site or your domain)
- `API_ENV` = production
- `API_DEBUG` = False

6) Initialize the database

- After first deploy, initialize DB either by:
  - Using Render shell (Dashboard -> Shell) and running a small Python script to call `db.create_all()` in `server_v2.py`, or
  - Temporarily enable an endpoint `/api/init-db` (if present) and call it once, or
  - SSH into the instance and run: `python backend/server_v2.py` interactive code to create tables.

7) Verify

- Visit your Render service public URL (e.g. `https://<service>.onrender.com/api/health`)
- Confirm endpoints respond and CORS is configured.
- Update your frontend `FRONTEND_URL` environment variable to the deployed frontend URL so reset links work.

8) Optional: Host frontend

- You can host static frontend on Render as a separate Static Site (connect to same repo, set Root to `/pages`), or use GitHub Pages / Netlify.

9) Notes

- Keep `.env` out of the repo. Use Render environment settings instead.
- Make sure `Procfile` uses `gunicorn server_v2:app` (already present in `backend/Procfile`).
- If you need, I can prepare a small `deploy.sh` to automate local git setup and push, or create a `README` with screenshots.
