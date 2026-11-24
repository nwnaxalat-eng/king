KING — Render setup

The screenshot shows the site still runs on a Netlify domain. Netlify static hosting does not run the Flask/Python API, so /api/tiktok returns an HTML page instead of JSON.

Deploy this complete project as ONE Python Web Service on Render. Do not deploy only the static folder to Netlify.

1. Extract this ZIP.
2. Upload all files and the static folder to a GitHub repository.
3. On Render choose New -> Web Service and connect that repository.
4. Build command: pip install -r requirements.txt
5. Start command: gunicorn app:app
6. Wait for Render to show Live, then open the Render URL, not the old Netlify URL.
7. Check Render URL + /health. It should return JSON showing ok:true and service:KING.

The webpage and /api/tiktok use the same Render domain. The API uses the same Python package as the original uploaded script. Video preview depends on whether TikTok's media host permits playback in the mobile browser; an open-video link is also shown.

If the third-party package no longer supports TikTok, its provider code needs updating. Only download videos you own or have permission to save.
