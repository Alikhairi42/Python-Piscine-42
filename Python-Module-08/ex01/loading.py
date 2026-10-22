import sys
import importlib


def check_dependencies():
    dependencies = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computing ready",
        "matplotlib": "Visualization ready"
    }

    missing = []

    for name, description in dependencies.items():
        try:
            module = importlib.import_module(name)
            print(f"[OK] {name} ({module.__version__}) - {description}")
        except ImportError:
            print(f"[ERROR] {name} is not installed")
            print(f"Install it with: pip install {name}")
            print(f"Or with: poetry add {name}")
            missing.append(name)

    if missing:
        print("\nMissing dependencies:", ", ".join(missing))
        sys.exit(1)

    print("\nAll dependencies are installed!")


if __name__ == "__main__":
    check_dependencies()