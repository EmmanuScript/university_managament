
## PostgreSQL Database Configuration

This project is configured to use **PostgreSQL** as the primary database.

### Quick Setup

**Database Credentials:**
- Username: `postgres`
- Password: `newpassword`
- Database: `university_management`
- Host: `localhost`
- Port: `5432`

### Installation Steps

1. **Ensure PostgreSQL is installed:**
   ```bash
   psql --version
   ```

2. **Create the database:**
   ```bash
   psql -U postgres -c "CREATE DATABASE university_management;"
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize database schema:**
   ```bash
   python scripts/init_db.py
   ```

5. **Run the application:**
   ```bash
   uvicorn app.main:app --reload
   ```

### Configuration Files

- **`.env.development`** - Contains PostgreSQL connection string and development settings
- **`app/core/config.py`** - Application configuration with PostgreSQL defaults
- **`app/core/database.py`** - SQLAlchemy database configuration

### Full Setup Guide

See [POSTGRES_SETUP.md](POSTGRES_SETUP.md) for comprehensive PostgreSQL setup instructions, troubleshooting, and advanced configuration.

