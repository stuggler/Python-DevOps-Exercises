# /// script
# requires-python = ">=3.14"
# dependencies = ["docker", "loguru"]
# ///


import sys
import docker
from docker.errors import DockerException
from loguru import logger
import subprocess


logger.add("watchdog.log", rotation="500 MB", retention="10 Days", level="INFO")


def main() -> None:
    logger.info("Starting Watchdog...")

    try:
        client = docker.from_env()

        client.ping()
        logger.success("Docker engine is responsive.")

        containers = client.containers.list()

        if not containers:
            logger.warning("No containers running currently.")
        else:
            logger.info(f"Detected {len(containers)} running containers.")
            for container in containers:
                logger.info(
                    f"Target identified: {container.name} (Image: {container.image.tags})"  # type: ignore
                )

        command = ["docker", "--version"]

        result = subprocess.run(
            command, shell=False, capture_output=True, text=True, check=False
        )

        logger.info(f"Docker version output: {result.stdout}")

        # if result.stderr:
        #     logger.error(f"Error retrieving Docker version: {result.stderr}")

    except DockerException as e:
        logger.error("Failed to connect to Docker. Is the service running? Error: {e}")
        sys.exit(1)

    except Exception as e:
        logger.critical(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
