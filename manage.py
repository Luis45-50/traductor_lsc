
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "traductor_lsc.settings")
    try:
        from django.core.management import execute_from_command_line
    except ModuleNotFoundError as exc:
        if exc.name != "django":
            raise
        raise ImportError(
            "Django no está instalado o no está disponible en el entorno actual."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
