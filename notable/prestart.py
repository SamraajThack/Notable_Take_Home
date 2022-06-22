import logging

from notable.db.session import SessionLocal
import notable.db.init

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    try:
        db = SessionLocal()
        # Try to create session to check if DB is awake
        db.execute("SELECT 1")
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info("Initializing service")
    notable.db.init.init_db()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()


