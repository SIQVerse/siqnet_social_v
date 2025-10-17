# SIQNet Social V

**SIQNet Social V** is a global Django-powered social platform built on the **SIQNET DYNAMICS GENERAL DEALING** framework. It fosters sovereign civic engagement, secure digital identity, and decentralized community interaction.

---

## 🚀 Features

- Django backend with PostgreSQL integration  
- Modular apps for user posts, community, authentication, and more  
- Responsive frontend served via Django templates  
- Built-in support for civic tech workflows and social dynamics  
- Docker-ready for containerized deployment  

---

## 🛠️ Tech Stack

- **Backend**: Django + Django REST Framework (Python 3.11+)  
- **Database**: PostgreSQL  
- **Frontend**: HTML, CSS, JavaScript  
- **Auth**: Django Allauth (email, social login)  
- **Deployment**: Railway, Docker  
- **Observability**: Railway Logs & Metrics  
- **Other Tools**: Gunicorn, Render (optional), Cloudflare (recommended)  
- **Time Zone**: Africa/Lusaka  

---

## 📦 Project Structure

- `userauth/` – Authentication and profile management  
- `userposts/` – User-generated content  
- `community/` – Civic groups and engagement  
- `accounts/` – Account settings and permissions  
- `siqposts/` – Sovereign identity posts  
- `versnet/` – Network layer for civic workflows  

---

## 📄 Environment Variables

Set these in Railway or your `.env` file:

```env
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DB_NAME=siqnet
DB_USER=postgres
DB_PASSWORD=your-db-password
DB_HOST=your-db-host
DB_PORT=5432
